#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:32:23 2024

@author: nforcone
"""
import xarray as xa
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
from cartopy.util import add_cyclic_point
import cartopy.feature as cfeature
import matplotlib.animation as animation 
from functools import partial

def UpdatePlot(frame, lon, lat, cmap):
    var = data.T[frame,29,:,:].values  # time, lev, lat, lon
    ax.clear()
    ax.set_title(f'Day {frame+1} Surface Temperature')
    ax.pcolormesh(lon, lat, var, cmap=cmap)
    ax.coastlines()

# import the data
Root = '/Users/nforcone/Documents/Fall2024/data/'
f = 'CAM_6_4_025_20240829_bw_dry_ne30_ne30_mg16.cam.h0i.0001-01-02-00000.nc'
filePath = Root + f
data = xa.open_dataset(filePath)

# plot surface temperature
T_sfc_t0 = data.T[0,29,:,:].values  # time, lev, lat, lon
lon = data.lon.values  # degrees East
lat = data.lat.values
cmap='plasma'
clevs = np.linspace(T_sfc_t0.min(), T_sfc_t0.max(), 10)

fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()})

movie = animation.FuncAnimation(fig, 
                                partial(UpdatePlot, 
                                        lon=lon, 
                                        lat=lat,
                                        cmap=cmap), 
                                frames = np.arange(0, 10),
                                repeat=True)
# movie.save(filename="/Users/nforcone/Documents/Fall2024/Fall2024Repo/"
#            "CAM_6_4_025_20240829_bw_dry_ne30_ne30_mg16/Figures/"
#            "T_sfc_day1_anim.gif", writer="pillow")
