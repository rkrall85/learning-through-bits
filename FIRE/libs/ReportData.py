"""
Purpose: This library will do all the data wrangling we need for various graphs. \n
Created By: Robert Krall \n
Created On: 01/04/2025
"""

import os
import pandas as pd
from openpyxl import load_workbook
import shutil


class ReportData:
    def __init__(
            self,
            file_name: str = "FIRE_tracker",
            copy_file: bool = False,
            use_copied_file: bool = False
    ):
        self.file_name = file_name
        self.copy_file = copy_file
        self.use_copied_file = use_copied_file
        self.balance_df = self.get_balance_data() # only grab the data once then re use the cache.
        self.balance_core_fields = ['Company', 'Employer', 'Owner', 'Year', 'Balance']

    def get_balance_data(self):
        """
        Purpose: This function will grab all the balance data \n
        Created By: Robert Krall \n
        Created On: 01/04/2025 \n
        :return: dataframe of data
        :rtype: dataframe
        """
        cwd = os.getcwd()
        home_dir = os.path.expanduser('~')
        one_drive_relative_path = f'OneDrive\\Documents\\finance\\{self.file_name}.xlsx'
        source_path = os.path.join(home_dir, one_drive_relative_path)
        destination_path = os.path.join(cwd, f'{self.file_name}.xlsx');
        if self.copy_file: shutil.copy(source_path, destination_path);

        if self.use_copied_file:
            wb = load_workbook(filename=destination_path, read_only=True)  # load the workbook
            balances_sheet = wb['Balances']  # read the sheet from doc
            balance_data = balances_sheet.values  # create dataframe from sheets
            headers = next(balance_data)
            balances_df = pd.DataFrame(balance_data, columns=headers)
        else:
            balances_df = pd.read_excel(source_path, sheet_name="Balances")

        return balances_df

    def get_end_of_year_total_retirement_balance(self):
        """
        Purpose: Get the 401k, HSA, end of year balances\n
        Created By: Robert Krall \n
        Created On: 01/04/2025
        :return:
        """
        df = self.balance_df
        filter_df = df[(df['End of Year Flag'] == True) & df['Total Retirement Flag'] == True]
        return filter_df

    def get_yearly_retirement_balances(self):
        """
        Purpose: This function will create the bar graphs for all three retirement yearly balances reports (total retirement, 401k, HSA) \n
        Created By: Robert Krall \n
        Created Ono: 01/04/2025 \n
        """
        end_of_year_df = self.get_end_of_year_total_retirement_balance()

        # Filter Data
        retirement_filter_df = end_of_year_df.loc[end_of_year_df['401k Flag'] == True]
        hsa_filter_df = end_of_year_df.loc[end_of_year_df['HSA Flag'] == True]

        # Balances
        balances_tr = end_of_year_df.groupby(['Year']).agg(Balance=('Balance', 'sum')).reset_index()
        balances_401k = retirement_filter_df.groupby(['Year']).agg(Balance=('Balance', 'sum')).reset_index()
        balances_hsa = hsa_filter_df.groupby(['Year']).agg(Balance=('Balance', 'sum')).reset_index()

        return balances_tr, balances_401k, balances_hsa



'''
class Reports(ReportData):
    def __init__(
            self,
            file_name: str = "FIRE_tracker",
            copy_file: bool = False,
            use_copied_file: bool = False
    ):
         super().__init__(
             file_name,
             copy_file,
             use_copied_file
         )
'''