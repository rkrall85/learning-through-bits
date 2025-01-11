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

        self.balances_df = None
        self.contributions_limits_df = None

        self.get_excel_data()
        self.balance_core_fields = ['Company', 'Employer', 'Owner', 'Year', 'Balance']

    def get_excel_data(self):
        """
        Purpose: This function will grab all the sheets of data we need \n
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

        # issue with copy; its not copying the values in the doc. (remove calcs in sheet and od it in python or find a better wya to copy)
        if self.use_copied_file:
            wb = load_workbook(filename=destination_path, read_only=True)  # load the workbook
            balances_sheet = wb['Balances']  # read the sheet from doc
            balance_data = balances_sheet.values  # create dataframe from sheets
            headers = next(balance_data)
            self.balances_df = pd.DataFrame(balance_data, columns=headers)

        else:
            self.balances_df = pd.read_excel(source_path, sheet_name="Balances")
            self.contributions_limits_df = pd.read_excel(source_path, sheet_name="Contributions Limits")
            # evnets? goals?

    def get_end_of_year_total_retirement_balance(self, year: int= None):
        """
        Purpose: Get the 401k, HSA, end of year balances\n
        Created By: Robert Krall \n
        Created On: 01/04/2025
        Updated On  | Purpose \n
        01/10/2025 | Added Year Parm

        :param year: The year you want to filter on
        :type year: int
        :return:
        """
        df = self.balances_df
        if year is None:
            filter_df = df[(df['End of Year Flag'] == True) & (df['Total Retirement Flag'] == True)]
        else:
            filter_df = df[(df['End of Year Flag'] == True) & (df['Total Retirement Flag'] == True) & (df['Year'] == year)]
        return filter_df

    def get_yearly_retirement_balances(self, group_by=None, return_hsa: bool = False, return_401k: bool = False):
        """
        Purpose: This function will create the bar graphs for all three retirement yearly balances reports (total retirement, 401k, HSA) \n
        Created By: Robert Krall \n
        Created Ono: 01/04/2025 \n
        """
        if group_by is None:
            group_by = ['Year']
        if 'Year' not in group_by:
            group_by.insert(0, 'Year')

        end_of_year_df = self.get_end_of_year_total_retirement_balance()

        # Filter Data
        retirement_filter_df = end_of_year_df.loc[end_of_year_df['401k Flag'] == True]
        hsa_filter_df = end_of_year_df.loc[end_of_year_df['HSA Flag'] == True]

        # Balances
        balances_tr = end_of_year_df.groupby(group_by).agg(Balance=('Balance', 'sum')).reset_index()

        df_return = {'balances_tr': balances_tr}

        if return_401k:
            balances_401k = retirement_filter_df.groupby(group_by).agg(Balance=('Balance', 'sum')).reset_index()
            df_return['balances_401k'] = balances_401k
        if return_hsa:
            balances_hsa = hsa_filter_df.groupby(group_by).agg(Balance=('Balance', 'sum')).reset_index()
            df_return['balances_hsa'] = balances_hsa

        return df_return

    def get_yearly_contributions_per_person(self, account_type: str = '401k'):
        """
        Purpose: This function will return the yearly contributions broken down by employee, and employer with yearly employee limit. \n
        Created By: Robert Krall \n
        Created On: 01/05/2025 \n
        :param account_type: 401k HSA, Roth IRA, etc
        :type account_type: str
        :return: dataframe of values
        """

        bal_df = self.balances_df[self.balances_df['Type'] == account_type]
        con_df = self.contributions_limits_df[self.contributions_limits_df['Type'] == account_type][['Year','Employee Limit']]

        yearly_contributions = bal_df.groupby(['Year', 'Owner']).agg(
            Employee=('Contributions - Employee', 'sum'),
            Employer=('Contributions - Employer', 'sum')
        ).reset_index()

        yearly_contributions = pd.merge(yearly_contributions, con_df, on='Year', how='left')

        return yearly_contributions

    def get_yearly_retirement_contributions(self, agg_by=None):
        """
        Purpose: This function will return the yearly contributions broken down by employee, and employer with yearly employee limit. \n
        Created By: Robert Krall \n
        Created On: 01/08/2025 \n
        :return: dataframe of values
        """
        group_by = ['Year']
        group_by.insert(1, agg_by)
        bal_df = self.balances_df[(self.balances_df['Total Retirement Flag'] == True) & (self.balances_df['Total Contributions'] != 0)]

        yearly_contributions = bal_df.groupby(group_by).agg(
            Contributions=('Total Contributions', 'sum')
        ).reset_index()

        return yearly_contributions

    def get_fire_balances(self):
        """
        Purpose: This function will return the fire balances and goal dates \n
        Created By: Robert Krall \n
        Created On: 01/10/2025 \n
        :return:
        """

        # current year
        year = self.balances_df['Year'].max()

        # current balance
        current_balance_df = self.get_end_of_year_total_retirement_balance(year=year)
        current_balance = current_balance_df['Balance'].sum()

        # previous balance
        previous_balance_df = self.get_end_of_year_total_retirement_balance(year=year-1)
        previous_balance = previous_balance_df['Balance'].sum()

        # goal s
        goal_balances = [1000000, 2000000, 3000000, 4000000, 5000000]
        # goal dates
        balances_df = self.get_yearly_retirement_balances()['balances_tr']
        crossed_years = []

        # Initialize a set to keep track of crossed goals
        crossed_goals = set()
        goal_years = set()

        # Iterate through each row in the dataframe
        for index, row in balances_df.iterrows():
            balance = row['Balance']
            year = row['Year']
            for goal in goal_balances:
                if goal not in crossed_goals and balance >= goal:
                    crossed_years.append((year, goal))
                    crossed_goals.add(goal)
                    goal_years.add(year)

        return current_balance, previous_balance, goal_balances, goal_years















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