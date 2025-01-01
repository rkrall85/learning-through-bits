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
        return {
            "balances": pd.read_excel(destination_path, sheet_name="Balances"),
            "events": pd.read_excel(destination_path, sheet_name="Events")
        }
    else:
        return {
            "balances": pd.DataFrame(xl("Balances")),
            "events": pd.DataFrame(xl("Events"))
        }

def calculate_yearly_mark_gains(row):
    # Function to calculate cash flow list for each row
   return row['Ending Balance'] - row['Total Contributions'] - row['Initial_Balance'] - row['Initial_Roll_Over'] - row['Starting Balance']

def calculate_yearly_ror(row):
    return row['Yearly Market Gains'] / row['Ending Balance']


copy_file = False
current_date = datetime.now()
tab_data = get_env_vars(copy_file)
balances_df = tab_data['balances']
events_df = tab_data['events']
today = pd.Timestamp(datetime.today())
# column Names
columns_names = get_column_names()
balance_columns_names = columns_names['balance_columns_names']
events_column_names = columns_names['events_column_names']
pk = columns_names['pk']
balances_columns = columns_names['balances']
# Data Frames
balances_df = balances_df.rename(columns=balance_columns_names)
events_df = events_df.rename(columns=events_column_names)
events_df = events_df[['Owner', 'Type', 'Year', 'HeatMapLabel']]
#balances_df = balances_df[(balances_df['Owner'] == 'Robert') & (balances_df['Type'] == 'HSA')] # Testing out a subset of data
balances_df = balances_df[(balances_df['Owner'] != 'Amanda')] # figure out how to fix Amandas ROR and tradtional IRA
balances_df = balances_df[(balances_df['Type'] != 'Traditional IRA')] # figure out how to fix Amandas ROR and tradtional IRA
balances = balances_df[balances_df['Total Retirement Flag'] == True]
balances.replace([np.inf, -np.inf, np.nan], 0, inplace=True)
yearly_balances = balances[balances['End of Year Flag'] == True][balances_columns]

# Initial  Balance
balances_initial = balances.groupby(['Owner', 'Type']).agg(
    Date=('Date', 'min')
).reset_index()
balances_initial = pd.merge(balances_initial, balances,
                                    on=['Owner', 'Type', 'Date'],
                                    how='inner').groupby(['Owner', 'Type']).agg(
    Initial_Balance=('Balance', 'sum'),
    Year=('Year', 'min')
).reset_index()


#  Initial Roll Over
roll_over_initial = balances.groupby(['Owner', 'Type']).agg(
    Year=('Year', 'min')
).reset_index()
roll_over_initial = pd.merge(roll_over_initial, balances,
                                    on=['Owner', 'Type', 'Year'],
                                    how='inner').groupby(['Owner', 'Type']).agg(
    Initial_Roll_Over=('Roll Over', 'sum'),
    Year=('Year', 'min')
).reset_index()


# Ending Balance
balances_yearly_end = balances_df[balances_df['End of Year Flag'] == True]
balances_yearly_end = balances_yearly_end.groupby(['Owner', 'Type', 'Year']).agg(
    Ending_Balance=('Balance', 'sum')
).reset_index()

# Starting Balance (previous ending balance)
balances_yearly_end['Starting Balance'] = balances_yearly_end.groupby(['Owner', 'Type'])['Ending_Balance'].shift(1)

# Contributions and Roll Over
balances_yearly_contributions = balances.groupby(['Owner', 'Type', 'Year']).agg({
    'Total Contributions': 'sum',
    'Roll Over': 'sum'
}).reset_index()

# Start to build the balance final data set
balances_yearly_final_dataset = pd.merge(balances_yearly_contributions, balances_yearly_end, on=['Owner', 'Type', 'Year'], how='left')
balances_yearly_final_dataset.replace([np.inf, -np.inf, np.nan], 1, inplace=True)
# re-name columns
balances_yearly_final_dataset.rename(columns={'Starting_Balance': 'Starting Balance'}, inplace=True)
balances_yearly_final_dataset.rename(columns={'Ending_Balance': 'Ending Balance'}, inplace=True)
# re order columns
balances_yearly_final_dataset = balances_yearly_final_dataset[['Owner', 'Type', 'Year', 'Starting Balance', 'Total Contributions', 'Roll Over', 'Ending Balance']]
# Apply the function to each row and accumulate market gains and the ROR
balances_yearly_final_dataset = pd.merge(balances_yearly_final_dataset, balances_initial, on=['Owner', 'Type', 'Year'],how='left')
balances_yearly_final_dataset['Initial_Balance'].fillna(0, inplace=True)

balances_yearly_final_dataset = pd.merge(balances_yearly_final_dataset, roll_over_initial, on=['Owner', 'Type', 'Year'],how='left')
balances_yearly_final_dataset['Initial_Roll_Over'].fillna(0, inplace=True)

balances_yearly_final_dataset['Yearly Market Gains'] = balances_yearly_final_dataset.apply(calculate_yearly_mark_gains, axis=1)
balances_yearly_final_dataset['Rate of Return'] = balances_yearly_final_dataset.apply(calculate_yearly_ror, axis=1)
#print(balances_yearly_final_dataset.to_string())
# grabbing label for investment
events_df.rename(columns={'HeatMapLabel':'Label'},inplace=True)
balances_yearly_final_dataset = pd.merge(balances_yearly_final_dataset, events_df, on=['Owner', 'Type', 'Year'], how='left')
# Setting up the Heat Map
yearly_summary = balances_yearly_final_dataset.copy()
# Getting unique IDs for investment names
yearly_summary = yearly_summary.assign(
    full_investment_name=yearly_summary.Owner.astype(str) + ' (' + yearly_summary.Type.astype(str) + ')'
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

pivot_ror, pivot_gains, pivot_labels = get_pivoted_data(yearly_summary, heat_map_ordering, include_labels=True)

# Set a mask for NaN values
mask = pivot_ror.isnull()

# Custom annotation to display both ROR and Gains
annot = pivot_ror.copy().astype(str)
for i in range(pivot_ror.shape[0]):
    for j in range(pivot_ror.shape[1]):
        ror = pivot_ror.iloc[i, j]
        gains = pivot_gains.iloc[i, j]
        labels = pivot_labels.iloc[i,j]

        annot_string = f'{ror:.2%}\n${gains:,.2f}'
        if pd.notna(labels):
            annot_string += f'\n\n{labels}'
        else:
            annot_string += f'\n\n'
        annot.iloc[i, j] = annot_string

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
plt.title('Heatmap with Investment Type ROR and Gains')
# Display the plot
plt.show()
