import pandas as pd
import numpy as np
import vincent as v

world_topo = r'vincent_map_data/world-countries.topo.json'

country_data_tmp = pd.DataFrame({'country_names' : np.array(['Argentina', 'Armenia', 'Australia', 'Austria']),
                                 'country_FIPS' : np.array(['032', '051', '036', '040']),
                                 'my_rate' : np.array([0.254, 0.3456, 0.26, 0.357])})
country_data_tmp.head()

geo_data = [{'name': 'countries',
             'url': world_topo,
             'feature': 'world-countries'}]

vis = v.Map(data=country_data_tmp,
                  geo_data=geo_data,
                  scale=1100,
                  data_bind='my_rate',
                  data_key='country_FIPS',
                  map_key={'counties': 'properties.FIPS'})

vis.display()
