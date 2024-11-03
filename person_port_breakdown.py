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
        0: 'Booking #', 1: 'Year', 2: 'Month', 3: 'YM', 4: 'Brand', 5: 'Ship', 6: 'Itinerary', 7: 'Itinerary Category',
        8: 'Home Port', 9: 'Class', 10: 'Days', 11: 'Category', 12: 'Category Rank', 13: 'Room Type', 14: 'Cruise Amount',
        15: 'Gratuities', 16: 'Room Price',17: 'Room Price Per Day', 18: 'Cruise Amount Per Day', 19: 'Airfare',
        20: 'Drink Package', 21: 'Total Cruise Amount', 22: 'Costco Rebate', 23: 'Shareholder', 24: 'OBC',
        25: 'AARP Rebate', 26: 'Total Savings', 27: 'Final Cruise Price', 28: 'Ports', 29: 'Room #', 30: 'Floor',
        31: 'Excursions', 32: 'Notes', 33: 'Who Went', 34: "Room Classification"
    }
    output_dict = {
        "tab_cruise_data_column_names": tab_cruise_data_column_names,
    }

    return output_dict

copy_file = False
current_date = datetime.now()
tab_data = get_env_vars(copy_file)
cruise_data = tab_data['cruise_data']
# Column names
columns_names = get_column_names()
tab_cruise_data_column_names = columns_names['tab_cruise_data_column_names']
# Data Frames
cruise_data_df = cruise_data.rename(columns=tab_cruise_data_column_names)

cruise_data_df = cruise_data_df[['Who Went', 'Ports', 'Year']]

# Create lists
cruise_data_df['Who Went'] = cruise_data_df['Who Went'] .apply(lambda x: x.split(', '))
cruise_data_df['Ports'] = cruise_data_df['Ports'] .apply(lambda x: x.split(', '))
# explode the lists
cruise_data_df = cruise_data_df.explode('Who Went')
cruise_data_df = cruise_data_df.explode('Ports')
# Re Name column
cruise_data_df.rename(columns={'Who Went': 'Person'}, inplace=True)
cruise_data_df.rename(columns={'Ports': 'Port'}, inplace=True)

# Pivot the data
pivot_df = cruise_data_df.pivot_table(index='Port', columns='Person', aggfunc='size', fill_value=0)

# Adding Total Visit Column
#pivot_df['Total Visits'] = cruise_data_df.groupby('Port')['Person'].transform('count').drop_duplicates().sort_index()
pivot_df['Total Visits'] = cruise_data_df.groupby('Port')['Year'].nunique()

# Reorder the columns: Move 'Total Visits' after 'Port'
cols = pivot_df.columns.to_list()
cols.insert(0, cols.pop(cols.index('Total Visits')))
pivot_df = pivot_df[cols]

# Reset index
pivot_df.reset_index(inplace=True)
pivot_df.columns.name = None  # Remove the axis name

# Sort by 'Total Visits'
pivot_df.sort_values(by='Total Visits', ascending=False, inplace=True)
# Sort within each port by the number of visits for each person
sorted_cols = ['Port', 'Total Visits'] + sorted(pivot_df.columns[2:], key=lambda col: pivot_df[col].sum(), reverse=True)
pivot_df = pivot_df[sorted_cols]
pivot_df.sort_values(by=sorted_cols[1:], ascending=False, inplace=True)

# Remove index
pivot_df.reset_index(inplace=True)
pivot_df = pivot_df.drop('index', axis=1)

pivot_df