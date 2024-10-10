# conda npl environment has these packages

import xarray as xa
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl
import cartopy.crs as ccrs
import numpy as np
from cartopy.util import add_cyclic_point
import cartopy.feature as cfeature
import matplotlib.animation as animation 
from functools import partial

def UpdatePlot(frame, lon, lat, MyNorm, cmap):
    var = data.T[frame,29,:,:].values  # time, lev, lat, lon
    ax.clear()
    ax.set_title(f'Day {frame+1} Surface Temperature')
    mesh = ax.pcolormesh(lon, lat, var, norm=MyNorm, cmap=cmap)
    ax.coastlines()

# import the data
Root = '/glade/derecho/scratch/nforcone/CAM_6_4_025_20240829_bw_wet_ne30_ne30_mg16/run/'
f = 'CAM_6_4_025_20240829_bw_wet_ne30_ne30_mg16.cam.h0i.0001-01-02-00000.nc'
filePath = Root + f
data = xa.open_dataset(filePath)

# plot surface temperature
T_sfc_t0 = data.T[0,29,:,:].values  # time, lev, lat, lon
lon = data.lon.values  # degrees East
lat = data.lat.values
cmap='rainbow'
clevs = np.linspace(T_sfc_t0.min(), T_sfc_t0.max(), 10)

fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()})
normObj = mpl.colors.Normalize(vmin=240,vmax=310)
SM = cm.ScalarMappable(norm=normObj, cmap=cmap)
fig.colorbar(SM, ax=ax, shrink=0.55)

movie = animation.FuncAnimation(fig, 
                                partial(UpdatePlot, 
                                        lon=lon, 
                                        lat=lat,
                                        MyNorm=normObj,
                                        cmap=cmap), 
                                frames = np.arange(0, 10),
                                repeat=True)
plt.show()
# movie.save(filename="/Users/nforcone/Documents/Fall2024/Fall2024Repo/"
#            "CAM_6_4_025_20240829_bw_dry_ne30_ne30_mg16/Figures/"
#            "T_sfc_day1_anim.gif", writer="pillow")
