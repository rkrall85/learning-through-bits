import os
import shutil
from datetime import datetime
import pandas as pd
import numpy as np
import seaborn as sns


import calendar
import plotly
#import skimage
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.colors as colors


if os.name == "nt":
    from FIRE.common_functions import *




def get_env_vars(copy_file: bool =False):
    if os.name == "nt":
        file_name = "FIRE_tracker.xlsx"
        cwd = os.getcwd()
        home_dir = os.path.expanduser('~')
        one_drive_relative_path = f'OneDrive\\Documents\\finance\\{file_name}'
        source_path = os.path.join(home_dir, one_drive_relative_path)
        destination_path = os.path.join(cwd,file_name);
        if copy_file: shutil.copy(source_path, destination_path);
        return {
            "yearly_contributions": pd.read_excel(destination_path, sheet_name="Contributions - Yearly"),
            "yearly_balances": pd.read_excel(destination_path, sheet_name="Balances - Yearly")
        }
    else:
        return {
            "yearly_contributions": pd.DataFrame(xl("Contributions - Yearly")),
            "yearly_balances": pd.DataFrame(xl("Balances - Yearly"))
        }


def calculate_ror(row):
    """
    Purpose: This function will calc the ror per row \n
    Created On: 12/24/2024 \n
    Created By: Robert Krall \n
    """
    if row['Previous Balance'] == 0:
        return 0
    else:
        return ((row['Balance'] - (
                    row['Previous Balance'] + row['Total Contributions'] + row['Roll Over'])) /
                (row['Previous Balance'] + row['Total Contributions'] + row['Roll Over']))


copy_file = False
current_date = datetime.now()
tab_data = get_env_vars(copy_file)
yearly_contributions_data = tab_data['yearly_contributions']
yearly_balances_data = tab_data['yearly_balances']
today = pd.Timestamp(datetime.today())
# column Names
columns_names = get_column_names()
tab_yearly_contributions_column_names = columns_names['tab_yearly_contributions']
tab_yearly_balances_column_names = columns_names['tab_yearly_balances']
yearly_by_company_by_type = columns_names['yearly_by_company_by_type']
yearly_balance = columns_names['yearly_balance']
pk_by_type = columns_names['pk_by_type']

# Data Frames
contributions_df = yearly_contributions_data.rename(columns=tab_yearly_contributions_column_names)
balances_df = yearly_balances_data.rename(columns=tab_yearly_balances_column_names)
contributions_by_type = contributions_df[yearly_by_company_by_type]
# Remove .1 and .2 in column names
contributions_by_type.rename(columns=lambda x: x.replace('.1', ''), inplace=True)
contributions_by_type.rename(columns=lambda x: x.replace('.2', ''), inplace=True)
balances = balances_df[balances_df['Total Retirement Flag'] == True][yearly_balance]
#balances['Previous Balance'] = balances['Balance'].shift(1)
balances['Previous Balance'] = balances.groupby(['Company', 'Employer', 'Owner', 'Type'])['Balance'].shift(1)
balances.replace([np.inf, -np.inf, np.nan], 0, inplace=True)
#balances['Balance Diff'] = balances['Balance'] - balances['Previous Balance'] # Need to bring in roll Over values and contributions

# index dfs to join them
#contributions_by_type.set_index(pk_by_type, inplace=True)
#balances.set_index(pk_by_type, inplace=True)
merged_dataset = pd.merge(balances, contributions_by_type, on=pk_by_type, how='left')
merged_dataset['Gains'] = (merged_dataset['Balance'] - merged_dataset['Previous Balance']
                           - merged_dataset['Total Contributions'] - merged_dataset['Roll Over'])
merged_dataset['ROR'] = merged_dataset.apply(calculate_ror, axis=1)


# Create Heat Map
i_df = merged_dataset[['Company', 'Employer', 'Owner', 'Type', 'Year', 'ROR', 'Gains']]
#i_df = i_df.reset_index()
#i_df['investment_name'] = f"{i_df['Company']} - {i_df['Employer']} - {i_df['Type']} ({i_df['Owner']})"
i_df = i_df.assign(investment_name=i_df.Company.astype(str) + ' - ' + i_df.Employer.astype(str) + ' - ' + i_df.Type.astype(str) + '(' + i_df.Owner.astype(str) + ')')
# Investment ID
i_names_df = pd.DataFrame(i_df.investment_name.unique(), columns=['investment_name'])
i_names_df['investment_id'] = i_names_df.index
# joining both dfs to get index ids
merged_i_df = pd.merge(i_df, i_names_df, on='investment_name', how='left')

# get variables
year_num = merged_i_df.Year.unique()
year_name = merged_i_df.Year.unique()
year_num.sort(axis=0)
year_name.sort(axis=0)
column = int(len(year_num))
xlabels = year_name

investment_num = merged_i_df.investment_id.unique()
investment_names = merged_i_df.investment_name.unique()

# Row and columns of arrays
row = int(max(investment_num))

#making a Blank array
heat_map_array = np.zeros([row+1, column], dtype="float64")

# Loop through data to ROR in the array to figure out row level coloring
for x in range(row, -1,-1):
    c_investment = investment_num[x]
    for y in range(0,column):
        c_year = year_num[y]
        ror_values = merged_i_df[(merged_i_df.investment_id == c_investment) & (merged_i_df.Year == c_year)].ROR

        if not(ror_values.empty):
            ror_values = np.round(ror_values.item(), decimals=3)
        else:
            ror_values = np.round(0.000, decimals=3)
        heat_map_array[x, y] = ror_values


# move array to df to do row level coloring
heat_map_df = pd.DataFrame(heat_map_array)
row_color_df = heat_map_df.div(heat_map_df.max(axis=1).where(heat_map_df.max(axis=1) != 0, abs(heat_map_df.min(axis=1))), axis=0)
# making the size of boxes
#plt.figure(figsize=(18, 5))

# Create heat map
sns.heatmap(row_color_df, fmt='', linewidth=0.2, robust=True, square=False, xticklabels=xlabels,
                 yticklabels=investment_names, cmap="RdYlGn")
#plt.set_title('Investments Yearly Rate of Return')


plt.show()
print(1)





#pivot_df = merged_dataset.pivot_table(index=['Company', 'Employer', 'Owner', 'Type'], columns='Year', values='ROR')#, aggfunc='sum')


# Sort the columns in descending order
#pivot_df = pivot_df.reindex(sorted(pivot_df.columns, reverse=True), axis=1)
#pivot_df.fillna(0, inplace=True)
#pivot_df['Sum'] = pivot_df.sum(axis=1)
#pivot_df.sort_values(by='Sum', ascending=False, inplace=True)
#pivot_df.drop(columns='Sum', inplace=True)

#sorted_cols = sorted(pivot_df.columns, reverse=True)
#pivot_df.fillna(0, inplace=True)
#pivot_df = pivot_df[sorted_cols]

#pivot_df.sort_values(by=sorted_cols[1:], ascending=False, inplace=True)

#pivot_df.fillna(0, inplace=True)
#years = sorted([col for col in pivot_df.columns if col.isdigit()], reverse=True)
#years = sorted(pivot_df.columns, reverse=True)
#pivot_df_2 = pivot_df.sort_values(by=years, ascending=False, inplace=True)
#pivot_df_2.reset_index(drop=True, inplace=True)

# Reset the index to convert multi-index into columns
#pivot_df_reset = pivot_df.reset_index()
print(1)