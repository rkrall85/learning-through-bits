"""
Purpose: This library will do all the data wrangling we need for various graphs. \n
Created By: Robert Krall \n
Created On: 01/04/2025
"""

import os
import pandas as pd
from openpyxl import load_workbook
import shutil
import datetime


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

        # used for filtering data
        self.current_year = None
        self.previous_year = None
        self.current_quarter = None
        self.year_list = None
        self.self_parm_year = None

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
            # Balances
            balances_sheet = wb['Balances']  # read the sheet from doc
            balance_data = balances_sheet.values  # create dataframe from sheets
            headers = next(balance_data)
            self.balances_df = pd.DataFrame(balance_data, columns=headers)
            self.year_list = self.balances_df['Year'].drop_duplicates().sort_values(ascending=False).to_list()
            # contributions
            contributions_limits_sheet = wb['Contributions Limits']  # read the sheet from doc
            limits_data = contributions_limits_sheet.values  # create dataframe from sheets
            headers = next(limits_data)
            self.contributions_limits_df = pd.DataFrame(limits_data, columns=headers)

        else:
            self.balances_df = pd.read_excel(source_path, sheet_name="Balances")
            self.contributions_limits_df = pd.read_excel(source_path, sheet_name="Contributions Limits")

            self.current_year = self.balances_df['Year'].max()
            self.previous_year = self.current_year - 1

            current_date = datetime.datetime.now()
            self.current_quarter = (current_date.month - 1) // 3 + 1

            self.year_list = self.balances_df['Year'].drop_duplicates().sort_values(ascending=False).to_list()

    def get_end_of_year_total_retirement_balance(self, year: int = None):
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

    def get_yearly_contributions_left(self, type: str = 'HSA', owner: str = None, year: int = None, quarter: int  = None):

        # special logic for if we are looking at person contributions
        if owner is not None:
            contribution_field = 'Contributions - Employee'
        else:
            contribution_field = 'Total Contributions'

        if year is None:
            year = self.current_year
            previous_year = self.previous_year
        else:
            previous_year = year - 1

        if quarter is None:
            quarter = self.current_quarter


        # getting contributions
        yearly_bal_df = self.balances_df[
            (self.balances_df['Type'] == type) &
            ((self.balances_df['Year'] == year) |
             (self.balances_df['Year'] == previous_year))
            ]
        current_ytq_df = self.balances_df[
            (self.balances_df['Type'] == type) &
            (self.balances_df['Year'] == year) &
            (self.balances_df['Quarter'] <= quarter)
        ]
        previous_ytq_df = self.balances_df[
            (self.balances_df['Type'] == type) &
            (self.balances_df['Year'] == previous_year) &
            (self.balances_df['Quarter'] <= quarter)
        ]

        # Apply the dynamic filter for person_Var if it's not None
        if owner is not None:
            yearly_bal_df = yearly_bal_df[yearly_bal_df['Owner'] == owner]
            current_ytq_df = current_ytq_df[current_ytq_df['Owner'] == owner]
            previous_ytq_df = previous_ytq_df[previous_ytq_df['Owner'] == owner]

        # Select the required columns
        yearly_bal_df = yearly_bal_df[['Year', contribution_field]]
        current_ytq_df = current_ytq_df[['Year', contribution_field]]
        previous_ytq_df = previous_ytq_df[['Year', contribution_field]]

        current_year_contributions = yearly_bal_df[yearly_bal_df['Year'] == year][contribution_field].sum()
        current_ytd_contributions = current_ytq_df[current_ytq_df['Year'] == year][contribution_field].sum()
        previous_year_contributions = yearly_bal_df[yearly_bal_df['Year'] == previous_year][contribution_field].sum()
        previous_ytq_contributions = previous_ytq_df[previous_ytq_df['Year'] == previous_year][contribution_field].sum()

        # Getting Limits
        limits_df = self.contributions_limits_df[
            (self.contributions_limits_df['Type'] == type) &
            ((self.contributions_limits_df['Year'] == year) |
             (self.contributions_limits_df['Year'] == previous_year))
            ][['Year', 'Employee Limit']]

        current_limit = limits_df[limits_df['Year'] == year]['Employee Limit'].iloc[0]
        previous_limit = limits_df[limits_df['Year'] == previous_year]['Employee Limit'].iloc[0]

        data = {
            'Year': [year, previous_year, previous_year, year],
            #'year_sort': [self.current_year, self.previous_year, self.previous_year + .1, self.current_year +.1],
            'year_sort': [2, 1, 3, 4],
            'year_label': [f"{year}", f"{previous_year}", f"{previous_year} (Q{quarter})", f"{year} (Q{quarter})"],
            'year_quarter': [None, None, quarter, quarter],
            'current_year_flag': [True, False, False, True],
            'Contributions': [current_year_contributions, previous_year_contributions, previous_ytq_contributions, current_ytd_contributions],
            'Contribution Limit': [current_limit, previous_limit, previous_limit, current_limit],
            'yearly_contributions': [current_limit, previous_limit, previous_limit, current_limit]
        }
        df = pd.DataFrame(data)

        df['Remaining Contribution'] = df['Contribution Limit'] - df['Contributions']

        # Convert 'Year' and 'year_sort' to strings to handle fractional years
        df['Year'] = df['Year'].astype(str)
        df['year_sort'] = df['year_sort'].astype(str)

        # Sort the dataframe by the 'Year' column to change the order
        df = df.sort_values(by='year_sort')

        return df

    def get_fire_balances(self):
        """
        Purpose: This function will return the fire balances and goal dates \n
        Created By: Robert Krall \n
        Created On: 01/10/2025 \n
        :return:
        """

        # current balance
        current_balance_df = self.get_end_of_year_total_retirement_balance(year=self.current_year)
        current_balance = current_balance_df['Balance'].sum()

        # previous balance
        previous_balance_df = self.get_end_of_year_total_retirement_balance(year=self.current_year - 1)
        previous_balance = previous_balance_df['Balance'].sum()

        # goal s
        goal_balances = [1000000, 2000000, 3000000]
        # goal dates
        balances_df = self.get_yearly_retirement_balances()['balances_tr']
        crossed_years = []

        # Initialize a set to keep track of crossed goals
        crossed_goals = set()
        goal_years = set()
        goal_ages = set()

        # Iterate through each row in the dataframe
        for index, row in balances_df.iterrows():
            balance = row['Balance']
            year = row['Year']
            for goal in goal_balances:
                if goal not in crossed_goals and balance >= goal:
                    crossed_years.append((year, goal))
                    crossed_goals.add(goal)
                    birth_date = datetime(1990, 4, 25)
                    age = year - birth_date.year
                    goal_ages.add(age)

        return current_balance, previous_balance, goal_balances, goal_years, goal_ages

    def get_retirement_progress_balances(self,  owner: str = "Robert", year: int = 2024, quarter: int = 1):
        """
        Purpose: Format the values we need for 401k retirement progress bar \n
        Created On: 01/19/2025 \n
        Created By: Robert Krall \n

        :param owner: Robert Or Amanda
        :type owner: str
        :param year: The year you want to look at data for
        :type year: int

        :param quarter: The quarter we want to track for the progress bar
        :type quarter: int

        :return:
        """

        df = self.get_yearly_contributions_left(type='401k', owner=owner, year=year, quarter=quarter)
        df = df[(df['current_year_flag'] == True) & (df['year_quarter'].notnull())]
        df = df.rename(columns={"yearly_contributions": "Yearly Contributions"})
        df['Contributions Tracker'] = (df['Yearly Contributions']/4) * df['year_quarter']
        #df['Contributions Behind'] = df['Contributions Tracker'] - df['Contributions']

        current_contributions = df['Contributions'].iloc[0]
        contributions_goal = df['Contributions Tracker'].iloc[0]
        yearly_contributions = df['Yearly Contributions'].iloc[0]

        # Grabbing Previous Year progress
        df_p = self.get_yearly_contributions_left(type='401k', owner=owner, year=year-1, quarter=quarter)
        df_p = df_p[(df_p['current_year_flag'] == True) & (df_p['year_quarter'].notnull())]
        df_p = df_p.rename(columns={"yearly_contributions": "Yearly Contributions"})

        previous_contributions = df_p['Contributions'].iloc[0]
        previous_yearly_contributions = df_p['Yearly Contributions'].iloc[0]

        '''
        # Sample values
        current_contribution_percentage = 6  # Example: 6% contribution
        yearly_contribution_limit = 22500
        current_contribution_amount = 7000
        annual_salary = 100000
        months_remaining = 6

        # Calculate remaining contribution needed
        remaining_contribution_needed = yearly_contribution_limit - current_contribution_amount

        # Calculate remaining salary for the year
        remaining_salary = (annual_salary / 12) * months_remaining

        # Calculate the new contribution percentage needed
        new_contribution_percentage = (remaining_contribution_needed / remaining_salary) * 100

        print(f"To stay on pace to max out your yearly contributions, you need to increase your 401(k) contribution to {new_contribution_percentage:.2f}% of your salary.")

        
        '''
        return current_contributions, contributions_goal, yearly_contributions, previous_contributions, previous_yearly_contributions
















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