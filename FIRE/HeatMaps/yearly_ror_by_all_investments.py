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
        file_name = "../FIRE_tracker.xlsx"
        cwd = os.getcwd()
        home_dir = os.path.expanduser('~')
        one_drive_relative_path = f'OneDrive\\Documents\\finance\\{file_name}'
        source_path = os.path.join(home_dir, one_drive_relative_path)
        destination_path = os.path.join(cwd, file_name);
        if copy_file: shutil.copy(source_path, destination_path);
        return {"balances": pd.read_excel(destination_path, sheet_name="Balances")}
    else:
        return {"balances": pd.DataFrame(xl("Balances"))}


copy_file = False
current_date = datetime.now()
tab_data = get_env_vars(copy_file)
balances_df = tab_data['balances']\
# column Names
columns_names = get_column_names()
balance_columns_names = columns_names['balance_columns_names']
pk = columns_names['pk_all_investment_types']
balances_columns = columns_names['balances']
# Data Frames
balances_df = balances_df.rename(columns=balance_columns_names)
balances_df = balances_df[(balances_df['Type'] != 'Traditional IRA')] # figure out how to fix Amandas ROR and tradtional IRA
balances_df = balances_df[(balances_df['Type'] != 'HSA') & (balances_df['Employer'] != 'Farm Credit')] # figure out how to fix Amandas ROR and tradtional IRA
balances = balances_df[balances_df['Total Retirement Flag'] == True]
balances.replace([np.inf, -np.inf, np.nan], 0, inplace=True)

aggregated_df = get_balances_group_by(balances, pk)

# Setting up the Heat Map
yearly_summary = aggregated_df.copy()
# Getting unique IDs for investment names
yearly_summary = yearly_summary.assign(
    full_investment_name=yearly_summary.Owner.astype(str) + ' - '
                         + yearly_summary.Type.astype(str)
                         + ' (' + yearly_summary.Employer.astype(str)
                         + ' | ' + yearly_summary.Company.astype(str) + ')'
)
create_heat_map(yearly_summary, 'All Investment RoR and Gains')
