import json
import pandas as pd
import numpy as np
import vincent

vincent.core.initialize_notebook()
from IPython.core.display import display, HTML


country_data_tmp = pd.DataFrame({'country_names' : np.array(['Argentina', 'Armenia', 'Australia', 'Austria']),
                                 'country_alpha3' : np.array(['ARG','ARM','AUS','AUT']),
                                 'my_rate' : np.array([0.254, 0.3456, 0.26, 0.357])})
country_data_tmp.head()

#map drawing bit Input[2] from your notebook
#Note the changes in variable names

world_topo = r'C:\Users\rkrall\github\vincent_map_data\vincent_map_data\world-countries.topo.json'

geo_data = [{'name': 'countries',
             'url': world_topo,
             'feature': 'world-countries'}]

vis = vincent.Map(data=country_data_tmp,
                  geo_data=geo_data,
                  scale=1100,
                  data_bind='my_rate',
                  data_key='country_alpha3',
                  map_key={'countries': 'id'})

#vis.display()

display(vis.display())
