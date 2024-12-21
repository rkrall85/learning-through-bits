import pandas as pd
import os;import shutil
from datetime import datetime

if os.name == "nt":
    from travel.common_functions import *


def get_env_vars(copy_file=False):
    if os.name == "nt":
        file_name = "Cruise Life.xlsx"
        cwd = os.getcwd()
        home_dir = os.path.expanduser('~')
        one_drive_relative_path = f'OneDrive\\Documents\\life_events\\{file_name}'
        source_path = os.path.join(home_dir, one_drive_relative_path)
        destination_path = os.path.join(cwd,file_name);
        if copy_file: shutil.copy(source_path, destination_path);
        return {"cruise_data": pd.read_excel(destination_path, sheet_name="cruise_data")}
    else:
        return {"cruise_data": pd.DataFrame(xl("cruise_data"))}


copy_file = False
current_date = datetime.now()
tab_data = get_env_vars(copy_file)
cruise_data = tab_data['cruise_data']
# Column names
columns_names = get_column_names()
tab_cruise_data_column_names = columns_names['tab_cruise_data_column_names']
# Data Frames
cruise_data_df = cruise_data.rename(columns=tab_cruise_data_column_names)
cruise_data_df = cruise_data_df[['Who Went', 'Ports', 'Booking #', 'Days']]

# Create lists
cruise_data_df['Who Went'] = cruise_data_df['Who Went'].apply(lambda x: x.split(', '))
# explode the lists
cruise_data_df = cruise_data_df.explode('Who Went')
# Re Name column
cruise_data_df.rename(columns={'Who Went': 'Person'}, inplace=True)
cruise_data_df.rename(columns={'Booking #': 'Cruises'}, inplace=True)

group_df = cruise_data_df.groupby(['Person']).agg({
    'Cruises': 'count',
    'Days': 'sum'
}).reset_index()

# Define day levels
day_levels = [1,        2,     25,    75,          200]
level_names = ['Blue', 'Red', 'Gold', 'Platinum', 'Diamond']

# Apply the function to each row
group_df['Current VIFP'], group_df['Days Next VIFP'], group_df['Next VIFP Level'] = zip(*group_df['Days'].apply(lambda x: get_level_info(x, day_levels, level_names)))

# Pivot The Data
pivot_df = group_df.pivot_table(index='Person', values=['Cruises', 'Days', 'Current VIFP', 'Days Next VIFP', 'Next VIFP Level'], aggfunc='first')


# Order by 'Booking #' in descending order
sorted_pivot_df = pivot_df.sort_values(by='Cruises', ascending=False)
sorted_pivot_df.reset_index(inplace=True)

# re order the columns
sorted_pivot_df = sorted_pivot_df[['Person', 'Cruises', 'Days', 'Current VIFP', 'Days Next VIFP', 'Next VIFP Level']]
sorted_pivot_df
