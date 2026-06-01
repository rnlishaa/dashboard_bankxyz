import geopandas as gpd

gdf = gpd.read_file('app/static/shp/gadm41_IDN_1.shp')
print("Kolom:", gdf.columns.tolist())
print("Contoh nilai NAME_1:", gdf['NAME_1'].head(10).tolist())
gdf.to_file('app/static/indonesia.geojson', driver='GeoJSON')
print("Done!")