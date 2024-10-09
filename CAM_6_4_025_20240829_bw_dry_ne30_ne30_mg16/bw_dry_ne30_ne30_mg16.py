import xarray as xa
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
from cartopy.util import add_cyclic_point
import cartopy.feature as cfeature

# %%
def GetColorLevs(var, numLevels):
    return np.linspace(var.min(), var.max(), numLevels)

# %%
def SpatialPlot(lon, lat, var, numLevels=10, cmap='plasma', 
                titleStr='Add Title', cbarStr='Color Variable'):
    var_cyclic, lon = add_cyclic_point(var, coord=lon)
    fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()})
    clevs = GetColorLevs(var_cyclic, numLevels)
    cf = ax.contourf(lon, lat, var_cyclic, levels=clevs, cmap=cmap)
    ax.coastlines()
    ax.gridlines(linestyle = '--', color = 'black', draw_labels=True)
    ax.add_feature(cfeature.STATES)
    cbar = fig.colorbar(cf, ax=ax, shrink=0.55, pad=0.1)
    cbar.set_label(cbarStr, size=14)
    fig.suptitle(titleStr, size=14, y=0.79)

# %%
# import the data
Root = '/Users/nforcone/Documents/Fall2024/data/'
f = 'CAM_6_4_025_20240829_bw_dry_ne30_ne30_mg16.cam.h0i.0001-01-02-00000.nc'
filePath = Root + f
data = xa.open_dataset(filePath)

# %%
# plot surface temperature
T_sfc_t0 = data.T[0,29,:,:].values  # time, lev, lat, lon
lon = data.lon.values  # degrees East
lat = data.lat.values

Tparams = {'titleStr': 'Day 1 Surface Temperature',
          'cbarStr': 'Temperature Kelvin'}
SpatialPlot(lon, lat, T_sfc_t0, **Tparams)
