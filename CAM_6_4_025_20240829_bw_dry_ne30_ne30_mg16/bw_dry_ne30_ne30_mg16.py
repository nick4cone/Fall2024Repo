import xarray as xa
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# %%
# import the data
Root = '/Users/nforcone/Documents/Fall2024/data/'
f = 'CAM_6_4_025_20240829_bw_dry_ne30_ne30_mg16.cam.h0i.0001-01-02-00000.nc'
filePath = Root + f
data = xa.open_dataset(filePath)

# %%
# plot the data
T_sfc = data.T[:,29,:,:].values
lon = data.lon.values  # degrees East
lat = data.lat.values
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()})