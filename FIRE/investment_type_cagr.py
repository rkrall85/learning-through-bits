import os
import shutil
from datetime import datetime
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy_financial as npf

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


def calculate_iir(row):
    return np.irr(row['Updated Ending Balance'])


# Function to calculate cash flow list for each row
def calculate_year_cash_flow(row):
    #return [- (row['Initial Balance'] + row['Total Contributions'] + row['Roll Over']), row['Ending Balance']]
    #return [- (row['Total Contributions'] + row['Roll Over']), row['Ending Balance']]
    #return [-(row['Total Contributions'] + row['Roll Over']) + row['Ending Balance']]
    return (row['Ending Balance'] - row['Starting Balance']) - (row['Total Contributions'] + row['Roll Over'])


copy_file = False
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
balances_df = balances_df[(balances_df['Owner'] == 'Robert') & (balances_df['Type'] == 'Roth IRA')] # Testing out a subset of data
balances = balances_df[balances_df['Total Retirement Flag'] == True]
balances.replace([np.inf, -np.inf, np.nan], 0, inplace=True)
yearly_balances = balances[balances['End of Year Flag'] == True][balances_columns]

#yearly_balances['Previous Balance'] = yearly_balances.groupby(pk)['Balance'].shift(1)

# Initial  Balance
balances_initial = balances.groupby(['Owner', 'Type']).agg(
    Date=('Date', 'min')
).reset_index()
balances_initial = pd.merge(balances_initial, balances,
                                    on=['Owner', 'Type', 'Date'],
                                    how='inner').groupby(['Owner', 'Type']).agg(
    Starting_Balance=('Balance', 'sum'),
    Year=('Year', 'min')
).reset_index()


#  Initial Roll Over
roll_over_initial = balances.groupby(['Owner', 'Type']).agg(
    Year=('Year', 'min')
).reset_index()
roll_over_initial = pd.merge(roll_over_initial, balances,
                                    on=['Owner', 'Type', 'Year'],
                                    how='inner').groupby(['Owner', 'Type']).agg(
    Roll_Over=('Roll Over', 'sum'),
    Year=('Year', 'min')
).reset_index()


# Starting Balance
'''
balances_yearly_start = balances.groupby(['Owner', 'Type', 'Year']).agg(
    Date=('Date', 'min')
).reset_index()
balances_yearly_start = pd.merge(balances_yearly_start, balances,
                                    on=['Owner', 'Type', 'Year', 'Date'],
                                    how='inner').groupby(['Owner', 'Type', 'Year', 'Date']).agg(
    Starting_Balance=('Balance', 'sum')
).reset_index()
'''

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
#balances_yearly_final_dataset = pd.merge(balances_yearly_contributions, balances_yearly_start, on=['Owner', 'Type', 'Year'], how='left')
balances_yearly_final_dataset = pd.merge(balances_yearly_contributions, balances_yearly_end, on=['Owner', 'Type', 'Year'], how='left')
balances_yearly_final_dataset.replace([np.inf, -np.inf, np.nan], 1, inplace=True)
# re-name columns
balances_yearly_final_dataset.rename(columns={'Starting_Balance': 'Starting Balance'}, inplace=True)
balances_yearly_final_dataset.rename(columns={'Ending_Balance': 'Ending Balance'}, inplace=True)
# re order columns
balances_yearly_final_dataset = balances_yearly_final_dataset[['Owner', 'Type', 'Year', 'Starting Balance', 'Total Contributions', 'Roll Over', 'Ending Balance']]
# Apply the function to each row and accumulate the cash flows
balances_yearly_final_dataset['Cash Flow'] = balances_yearly_final_dataset.apply(calculate_year_cash_flow, axis=1)

print(1)

# CAlc the very m
irr_results = []
for owner in balances_yearly_final_dataset['Owner'].unique():
    for acc_type in balances_yearly_final_dataset['Type'].unique():
        filtered_df = balances_yearly_final_dataset[(balances_yearly_final_dataset['Owner'] == owner) & (balances_yearly_final_dataset['Type'] == acc_type)]

        #initial_balance_df = balances_initial[(balances_initial['Owner'] == owner) & (balances_initial['Type'] == acc_type)]
        #initial_balance_value = -(initial_balance_df['Starting_Balance'].iloc[0])

        initial_roll_over_df = roll_over_initial[(roll_over_initial['Owner'] == owner) & (roll_over_initial['Type'] == acc_type)]
        if not initial_roll_over_df.empty:
            initial_roll_over_value = initial_roll_over_df['Roll_Over'].iloc[0]

        if not filtered_df.empty:
            for year in filtered_df['Year'].unique():

                # yearly CAGR
                current_year_df = filtered_df[filtered_df['Year'] == year]#['Cash Flow'].iloc[0]
                cy_starting_balance = current_year_df['Starting Balance'].iloc[0]
                cy_ending_balance = current_year_df['Ending Balance'].iloc[-1]

                cy_contributions = current_year_df['Total Contributions'].sum()
                cy_roll_over = current_year_df['Roll Over'].sum()

                cash_flow = current_year_df['Cash Flow'].sum()

                #cy_adjusted_starting_balance = cy_starting_balance + cy_roll_over
                #cy_adjusted_ending_balance = cy_ending_balance - cy_roll_over


                # if year is initial year then we add initial roll over to starting balance
                row_values = {'Owner': owner, 'Type': acc_type, 'Year': year}
                row_exists_roll_over = not initial_roll_over_df[
                    (initial_roll_over_df['Owner'] == row_values['Owner']) &
                    (initial_roll_over_df['Type'] == row_values['Type']) &
                    (initial_roll_over_df['Year'] == row_values['Year'])
                ].empty

                cy_adjusted_starting_balance = cy_starting_balance
                if row_exists_roll_over:
                    cy_adjusted_starting_balance += initial_roll_over_value

                cy_adjusted_ending_balance = cy_ending_balance - cy_contributions

                yearly_cagr = (cy_adjusted_ending_balance / cy_adjusted_starting_balance) ** (1/1) - 1


                irr_results.append({
                    'Owner': owner,
                    'Type': acc_type,
                    'Year': year,
                    'Yearly CARG': yearly_cagr, # * 100,
                    'Yearly Cash Flow': cy_adjusted_ending_balance
                    #'Yearly Cash Flow': yearly_cash_flows,

                })

irr_df = pd.DataFrame(irr_results)

print(irr_df.to_string())


print(1)