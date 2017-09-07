import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#create subplot
m = Basemap(projection='mill', llcrnrlat=-20, urcrnrlat=50,llcrnrlon=-130, urcrnrlon=-60, resolution='c')
m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.fillcontinents(color='#04BAE3', lake_color='#FFFFFE')
m.drawmapboundary(fill_color = '#FFFFFE')

plt.title('first map')
plt.show()