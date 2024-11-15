import pandas as pd;
import os;
import shutil;
from datetime import datetime;
import math;
import numpy as np

if os.name == "nt":
    from common_functions import *


def get_env_vars(copy_file=False):
    if os.name == "nt":
        source_path = "C:\\Users\\rober\\OneDrive\\Documents\\life_events\\Cruise Life.xlsx";
        destination_path = "/Cruise Life.xlsx";
        if copy_file: shutil.copy(source_path, destination_path);
        dict_1 = {
            "cruise_data": pd.read_excel(destination_path, sheet_name="cruise_data")
        }
    else:
        dict_1 = {
            "cruise_data": pd.DataFrame(xl("cruise_data"))
        }
    return dict_1


copy_file = False
current_date = datetime.now()
tab_data = get_env_vars(copy_file)
cruise_data = tab_data['cruise_data']
# Column names
columns_names = get_column_names()
tab_cruise_data_column_names = columns_names['tab_cruise_data_column_names']
# Data Frames
cruise_data_df = cruise_data.rename(columns=tab_cruise_data_column_names)
# Filter out future cruises
cruise_data_df['Cruise Date'] = pd.to_datetime(cruise_data_df['Cruise Date'])
today = pd.Timestamp(datetime.today())

future_cruise = cruise_data_df[cruise_data_df['Cruise Date'] > today].iloc[:1]['Days']
future_cruise_days = int(future_cruise.iloc[0])
current_cruises_df = cruise_data_df[cruise_data_df['Cruise Date'] < today]

current_cruises_df = current_cruises_df[['Who Went', 'Booking #', 'Days']]

# Create lists
current_cruises_df['Who Went'] = current_cruises_df['Who Went'].apply(lambda x: x.split(', '))
# explode the lists
current_cruises_df = current_cruises_df.explode('Who Went')
# Re Name column
current_cruises_df.rename(columns={'Who Went': 'Person'}, inplace=True)
current_cruises_df.rename(columns={'Booking #': 'Cruises'}, inplace=True)

drop_dups_df = current_cruises_df.drop_duplicates(subset=['Person', 'Cruises'])

group_df = drop_dups_df.groupby(['Person']).agg({
    'Cruises': 'count',
    'Days': 'sum'
}).reset_index()

# Define day levels
day_levels = [1, 2, 25, 75, 200]
level_names = ['Blue', 'Red', 'Gold', 'Platinum', 'Diamond']

# Apply the function to each row
group_df['Current VIFP'], group_df['Days Next VIFP'], group_df['Next VIFP Level'] = zip(
    *group_df['Days'].apply(lambda x: get_level_info(x, day_levels, level_names)))

# Pivot The Data
pivot_df = group_df.pivot_table(index='Person',
                                values=['Cruises', 'Days', 'Current VIFP', 'Days Next VIFP', 'Next VIFP Level'],
                                aggfunc='first')

# Order by 'Booking #' in descending order
sorted_pivot_df = pivot_df.sort_values(by='Cruises', ascending=False)
sorted_pivot_df.reset_index(inplace=True)

sorted_pivot_df['Next Cruise Upgraded'] = (future_cruise_days >= sorted_pivot_df['Days Next VIFP']).astype(int)

# re-order the columns
sorted_pivot_df = sorted_pivot_df[[
    'Person', 'Cruises', 'Days', 'Current VIFP', 'Days Next VIFP', 'Next VIFP Level', 'Next Cruise Upgraded'
]]
sorted_pivot_df
