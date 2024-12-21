import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#create subplot
#m = Basemap(projection='mill', llcrnrlat=-20, urcrnrlat=50,llcrnrlon=-130, urcrnrlon=-60, resolution='c') #Entire USA
#m = Basemap(projection='mill', llcrnrlat=30, urcrnrlat=40,llcrnrlon=-100, urcrnrlon=-80, resolution='c')
#m = Basemap(projection='mill', llcrnrlat=30, llcrnrlon=--100, urcrnrlat=40, urcrnrlon=-80, resolution='c')
m = Basemap(llcrnrlon=-103,llcrnrlat=30,urcrnrlon=-79,urcrnrlat=48,
        projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
#m = Basemap(projection='mill', llcrnrlon=-180,llcrnrlat=-90, urcrnrlon=180 , urcrnrlat=90, resolution='c')

m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.fillcontinents(color='#04BAE3', lake_color='#FFFFFF')
m.drawmapboundary(fill_color = '#FFFFFf')


'''
#Houston TX
lat, lon = 29.67, -95.36
x,y = m(lon, lat)
m.plot(x,y,'ro', markersize=20)

#Minneapolis MN
lat, long = 44.8848, -93.2223
x,y = m(lon, lat)
m.plot(x,y,'ro', markersize=20, alpha=.5)

#St Paul MN
lat, long = 44.93, -93.06
x,y = m(lon, lat)
m.plot(x,y,'go', markersize=15, alpha=.5)
'''


plt.title('Geo Plotting')
plt.show()