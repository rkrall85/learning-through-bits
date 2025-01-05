import os
import shutil
from datetime import datetime
import pandas as pd
import numpy as np


if os.name == "nt":
    from FIRE.common_functions.common_functions import *
    from FIRE.common_functions.dataframe_cleanup import *


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


copy_file = False
current_date = datetime.now()
tab_data = get_env_vars(copy_file)
balances_df = tab_data['balances']
events_df = tab_data['events']
# column Names
columns_names = get_column_names()
balance_columns_names = columns_names['balance_columns_names']
events_column_names = columns_names['events_column_names']
pk = columns_names['pk_investment_types']
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
aggregated_df = get_balances_group_by(balances, pk)

# grabbing label for investment
events_df.rename(columns={'HeatMapLabel':'Label'},inplace=True)
balances_yearly_final_dataset = pd.merge(aggregated_df, events_df, on=pk+['Year'], how='left')
# Setting up the Heat Map
yearly_summary = balances_yearly_final_dataset.copy()
# Getting unique IDs for investment names
yearly_summary = yearly_summary.assign(
    full_investment_name=yearly_summary.Owner.astype(str) + ' (' + yearly_summary.Type.astype(str) + ')'
)
create_heat_map(yearly_summary,include_labels=True)

