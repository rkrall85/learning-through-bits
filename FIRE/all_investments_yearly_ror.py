import os
import shutil
from datetime import datetime
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

if os.name == "nt":
    from FIRE.common_functions import *


def get_env_vars(copy_file: bool = False):
    if os.name == "nt":
        file_name = "FIRE_tracker.xlsx"
        cwd = os.getcwd()
        home_dir = os.path.expanduser('~')
        one_drive_relative_path = f'OneDrive\\Documents\\finance\\{file_name}'
        source_path = os.path.join(home_dir, one_drive_relative_path)
        destination_path = os.path.join(cwd, file_name);
        if copy_file: shutil.copy(source_path, destination_path);
        return {"balances": pd.read_excel(destination_path, sheet_name="Balances")}
    else:
        return {"balances": pd.DataFrame(xl("Balances"))}


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


def get_pivoted_data(yearly_summary, heat_map_ordering):
    """
    Purpose: This will pivot the dataframe data to get data setup for heat map \n
    Created By: Robert Krall \n
    Created On: 12/26/2024 \n
    :param yearly_summary: dataframe of yearly summary
    :type yearly_summary: dataframe
    :return:
    """
    pivot_ror = yearly_summary.pivot(index='full_investment_name', columns='Year', values='ROR')
    pivot_gains = yearly_summary.pivot(index='full_investment_name', columns='Year', values='Gains')
    years_list = sorted(yearly_summary['Year'].unique(), reverse=True)

    update_ror = order_pivot_data(pivot_ror, heat_map_ordering, years_list)
    updated_gains = order_pivot_data(pivot_gains, heat_map_ordering, years_list)

    return update_ror, updated_gains


def order_pivot_data(pivot_df, heat_map_ordering, years_list):
    """
    Purpose: Re-order the datafame so its columns are years desc and rows are investment based on those years \n
    Created By: Robert Krall \n
    Created On: 12/26/2024 \n
    :param pivot_df:
    :return:
    """
    # heat map columns
    distinct_years = ['full_investment_name'] + sorted(years_list, reverse=True)
    # Remove years from heat map df
    # join the 2 dataframes to oder the set
    pivot_df = pd.merge(pivot_df, heat_map_ordering, on=['full_investment_name'], how='left')
    # Sort based on the created 'rank' column
    pivot_df.sort_values(by='heat_map_order', ascending=True, inplace=True)
    # re order columns
    pivot_df = pivot_df[distinct_years]
    pivot_df.set_index('full_investment_name', inplace=True)

    return pivot_df

copy_file = True
current_date = datetime.now()
tab_data = get_env_vars(copy_file)
balances_df = tab_data['balances']
today = pd.Timestamp(datetime.today())
# column Names
columns_names = get_column_names()
balance_columns_names = columns_names['balance_columns_names']
pk = columns_names['pk']
balances_columns = columns_names['balances']
# Data Frames
balances_df = balances_df.rename(columns=balance_columns_names)
balances = balances_df[balances_df['Total Retirement Flag'] == True]
balances.replace([np.inf, -np.inf, np.nan], 0, inplace=True)
# Yearly balances
yearly_balances = balances[balances['End of Year Flag'] == True][balances_columns]
yearly_balances['Previous Balance'] = yearly_balances.groupby(pk)['Balance'].shift(1)
#yearly_balances['Previous Balance'] = yearly_balances['Previous Balance'].fillna(1)
yearly_balances.replace([np.inf, -np.inf, np.nan], 0, inplace=True)
# yearly contributions
group_by = pk + ['Year']
yearly_contributions = balances.groupby(group_by).agg({
    'Total Contributions': 'sum',
    'Roll Over': 'sum'
}).reset_index()
# yearly summary
yearly_summary = pd.merge(yearly_balances, yearly_contributions, on=pk+['Year'], how='left')
#yearly_summary = yearly_summary[yearly_summary['Year'] == 2024]
yearly_summary = yearly_summary[yearly_summary['Owner'] != 'Amanda'] # temp fix until I get the loan issue figured out

yearly_summary['Gains'] = (yearly_summary['Balance'] - yearly_summary['Previous Balance']
                           - yearly_summary['Total Contributions'] - yearly_summary['Roll Over'])
yearly_summary['ROR'] = yearly_summary.apply(calculate_ror, axis=1)
# Getting unique IDs for investment names
yearly_summary = yearly_summary.assign(
    full_investment_name=yearly_summary.Owner.astype(str) + ' - '
                         + yearly_summary.Type.astype(str)
                         + ' (' + yearly_summary.Employer.astype(str)
                         + ' | ' + yearly_summary.Company.astype(str) + ')'
)
# Getting Years Count
investment_years = yearly_summary.groupby(['full_investment_name']).agg(
    year_count=('Year', 'count'),
    max_year=('Year', 'max')
).reset_index()
# Determine the most recent year and create a mapping
most_recent_year = investment_years['max_year'].max()
year_mapping = {most_recent_year - i: chr(65 + i) for i in range(most_recent_year - investment_years['max_year'].min() + 1)}
investment_years['Year_Letter'] = investment_years['max_year'].map(year_mapping)
investment_years['heat_map_order'] = investment_years['Year_Letter'] + investment_years['year_count'].astype(str)
heat_map_ordering = investment_years[['full_investment_name', 'heat_map_order']]

pivot_ror, pivot_gains = get_pivoted_data(yearly_summary, heat_map_ordering)

# Set a mask for NaN values
mask = pivot_ror.isnull()

# Custom annotation to display both ROR and Gains
annot = pivot_ror.copy().astype(str)
for i in range(pivot_ror.shape[0]):
    for j in range(pivot_ror.shape[1]):
        ror = pivot_ror.iloc[i, j]
        gains = pivot_gains.iloc[i, j]
        annot.iloc[i, j] = f'{ror:.2%}\n${gains:,.2f}'

# Create the heatmap
cmap = LinearSegmentedColormap.from_list('custom_cmap', ['red', 'yellow', 'green'])
cmap.set_bad(color='#ECEABC') # Set the color for NaN values

# larger figure size and square =True makes sure the heat box is big enough
plt.figure(figsize=(30, 20))

ax = sns.heatmap(pivot_ror, annot=annot, cmap=cmap, linewidths=.5, fmt='', center=0, square=True, mask=mask)

# Remove x and y labels
ax.set_xlabel('')
ax.set_ylabel('')

# Set the title
plt.title('Heatmap with ROR and Gains')
# Display the plot
plt.show()