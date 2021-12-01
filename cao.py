import os
import urllib
import pandas as pd
import numpy as np
import netCDF4 as nc
import folium
from folium.plugins import HeatMap

path = 'focos_abertos_mensal_202111.csv'
df = pd.read_csv(path)

m = folium.Map(location=[-3.10361111, -60.01555555], zoom_start= 10)

mask = ((df['data'] > '2021-11-01 00:00:00')& (df['satelite'] == 'NOAA-20' ) & (df['lat'] > -8.2617 ) & (df['lat'] < 1.2893) & (df['lon'] > -69.2102 ) & (df['lon'] < -56.987 ))
df2 = df.loc[mask]

locais = df2.iloc[:,:2].values.tolist()

HeatMap(locais, radius = 20).add_to(m)

m.save('heatmap.html')
