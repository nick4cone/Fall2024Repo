# conda npl environment has these packages

import xarray as xa
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl
import metpy
import cartopy.crs as ccrs
import numpy as np
from cartopy.util import add_cyclic_point
from cartopy.mpl.ticker import LatitudeFormatter, LongitudeFormatter
import cartopy.feature as cfeature
import matplotlib.animation as animation 
from functools import partial

# import the data
Root = '/glade/derecho/scratch/nforcone/CAM_6_4_025_20240829_bw_wet_ne30_ne30_mg16/run/'
f = 'CAM_6_4_025_20240829_bw_wet_ne30_ne30_mg16.cam.h0i.0001-01-02-00000.nc'
filePath = Root + f
data = xa.open_dataset(filePath)

lon = data.lon.values  # degrees East
lat = data.lat.values
lev = data.lev.values

myLon = lon[150]
var = data.U[9,:,:,50].values

labelSize = 13
fig, ax = plt.subplots()
ax.invert_yaxis()
ax.set_ylabel('Pressure hPa', size=labelSize)
ax.set_xlabel('Latitude', size=labelSize)
ax.set_title(f'Day 10 Zonal Wind at Longitude {myLon:.2f} E', size=labelSize)
mesh = ax.contourf(lat, lev, var)
cbar = plt.colorbar(mesh, ax=ax)
cbar.set_label('Zonal Wind m/s', size=labelSize)
plt.show()

plt.savefig("/glade/u/home/nforcone/Fall2024Repo/"
            "CAM_6_4_025_20240829_bw_wet_ne30_ne30_mg16/"
            "run_on_derecho/Figures/Cross_Section_bw_wet_new_ic.png", dpi=300)
