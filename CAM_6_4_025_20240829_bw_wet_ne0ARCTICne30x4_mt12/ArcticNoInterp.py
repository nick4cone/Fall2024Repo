import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

data_path = '/glade/derecho/scratch/nforcone/CAM_6_4_025_20240829_bw_wet_ne0ARCTICne30x4_mt12/run/CAM_6_4_025_20240829_bw_wet_ne0ARCTICne30x4_mt12.cam.h1i.0001-01-02-00000.nc'

data = xr.open_dataset(data_path)

fig, ax = plt.subplots(
    1,
    1,
    figsize=(10, 10),
    constrained_layout=True,
    subplot_kw={"projection": ccrs.PlateCarree()},
)

print(data.variables)
print(data.lev)
print(data.Q)

cf = ax.contourf(data.lon, data.lat, data.RELHUM[9,23,:,:])  # time: 10, lev: 30, lat: 900, lon: 1800
cb = plt.colorbar(cf, ax=ax, shrink=0.54)
cb.set_label('Specific Humidity Kg/Kg', size=14) 
ax.gridlines(draw_labels=True, linestyle='--', color='black')
ax.set_global()
ax.set_title("Wet Baroclinic Wave Test Case\nArctic 1/4 Degree Resolution, 1 Degree Elsewhere\n"
             "Interpolated to Lat/Lon Grid", size=14)
plt.show()
