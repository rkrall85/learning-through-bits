import pandas as pd;import os;import shutil;
from datetime import datetime;import math;import numpy as np

def get_env_vars(copy_file=False):
    if os.name == "nt":
        source_path = "C:\\Users\\rober\\OneDrive\\Documents\\life_events\\Cruise Life.xlsx";
        destination_path = "C:\\dev\\data_learning\\travel\\Cruise Life.xlsx";
        if copy_file: shutil.copy(source_path, destination_path);
        return {
            "cruise_data": pd.read_excel(destination_path, sheet_name="cruise_data")
        }
    else:
        return {
            "cruise_data": pd.DataFrame(xl("cruise_data"))
        }


def get_column_names():
    tab_cruise_data_column_names = {
        0: 'Booking #', 1: 'Cruise Date', 2: 'Year', 3: 'Month', 4: 'Brand', 5: 'Ship', 6: 'Itinerary',
        7: 'Itinerary Category',
        8: 'Home Port', 9: 'Class', 10: 'Days', 11: 'Category', 12: 'Category Rank', 13: 'Room Type',
        14: 'Cruise Amount',
        15: 'Gratuities', 16: 'Room Price', 17: 'Room Price Per Day', 18: 'Cruise Amount Per Day', 19: 'Airfare',
        20: 'Drink Package', 21: 'Total Cruise Amount', 22: 'Costco Rebate', 23: 'Shareholder', 24: 'OBC',
        25: 'AARP Rebate', 26: 'Total Savings', 27: 'Final Cruise Price', 28: 'Ports', 29: 'Room #', 30: 'Floor',
        31: 'Excursions', 32: 'Notes', 33: 'Who Went', 34: "Room Classification"
    }
    output_dict = {
        "tab_cruise_data_column_names": tab_cruise_data_column_names,
    }

    return output_dict


# Function to determine the current level, days until the next level, and the next level
def get_level_info(days, levels, names):
    for i in range(len(levels) - 1):
        if levels[i] <= days < levels[i + 1]:
            current_level = names[i]
            days_to_next = levels[i + 1] - days
            next_level = names[i + 1] if i < len(names) else None
            return current_level, days_to_next, next_level
    # If days are beyond the last threshold
    return names[-1], 0


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
cruise_data_df['Who Went'] = cruise_data_df['Who Went'] .apply(lambda x: x.split(', '))
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
