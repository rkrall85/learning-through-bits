"""
Purpose: This library will do all the data wrangling we need for various graphs. \n
Created By: Robert Krall \n
Created On: 01/04/2025
"""

import os
import pandas as pd
from openpyxl import load_workbook
import shutil
import yfinance as yf
import datetime
import numpy as np
from datetime import datetime, timedelta
from utility_methods import *


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
        self.stock_prices_df = None
        self.stock_info_df = None

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
            self.stock_prices_df = pd.read_excel(source_path, sheet_name="Stocks")
            self.cpi_df = pd.read_excel(source_path, sheet_name="CPI")

            self.current_year = self.balances_df['Year'].max()
            self.previous_year = self.current_year - 1

            current_date = datetime.today()
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

        if account_type == '401k': sub_type = 'Traditional - 401k'
        elif account_type == 'HSA': sub_type = 'HSA'
        elif account_type == 'Roth IRA': sub_type = 'Roth - IRA'
        else: sub_type = 'Traditional - 401k'

        bal_df = self.balances_df[self.balances_df['Sub Type'] == sub_type]
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

        if type =='401k':
            flag_filter = (self.balances_df['401k Flag'] == True)
        elif type =='HSA':
            flag_filter = (self.balances_df['HSA Flag'] == True)
        else:
            flag_filter = (self.balances_df['401k Flag'] == True) # default to 401k

        # getting contributions
        yearly_bal_filter = flag_filter & ((self.balances_df['Year'] == year) | (self.balances_df['Year'] == previous_year))
        current_ytq_filter = flag_filter & (self.balances_df['Year'] == year) & (self.balances_df['Quarter'] <= quarter)
        previous_ytq_filter = flag_filter & (self.balances_df['Year'] == previous_year) & (self.balances_df['Quarter'] <= quarter)

        yearly_bal_df = self.balances_df[yearly_bal_filter]
        current_ytq_df = self.balances_df[current_ytq_filter]
        previous_ytq_df = self.balances_df[previous_ytq_filter]

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


class StockData(ReportData):
    def __init__(
            self,
            file_name: str = "FIRE_tracker",
            copy_file: bool = False,
            use_copied_file: bool = False,
            get_stock_info: bool = True
    ):
        super().__init__(
            file_name,
            copy_file,
            use_copied_file
        )
        if get_stock_info:
            self.stock_info_df = self._get_investment_stock_info()
        else:
            self.stock_info_df = None

    def _get_investment_stock_info(self):
        """
        Purpose: This function will grab al the current investment info we need  \n
        Created On: 02/10/2025 \n
        Created By: Robert Krall \n
        :return: returns dataframe of random stock info
        """
        stock_info_df = pd.DataFrame()
        current_stocks = sorted(set(self.stock_prices_df['Stock Ticker']))
        for s in current_stocks:
            s_info_df = self.get_stock_ticker_info(s)
            stock_info_df = stock_info_df._append(s_info_df, ignore_index=True)

        return stock_info_df

    def get_stock_ticker_info(self, stock_ticker: str):
        """
        Purpose: This function will return various info about the stock. \n
        Created On: 02/09/2025 \n
        Created By: Robert Krall
        :param stock_ticker: a Stock Ticker such as MMM
        :type stock_ticker: str
        :return: a dictionary of values
        :rtype dict
        """

        ticker = yf.Ticker(stock_ticker)

        long_name = None
        short_name = None
        inception_dt = datetime(year=1900, month=1, day=1)
        category = None
        fund_family = None

        if 'longName' in ticker.info: long_name = ticker.info['longName']
        if 'shortName' in ticker.info: short_name = ticker.info['shortName']
        if 'fundInceptionDate' in ticker.info:
            inception_date = ticker.info['fundInceptionDate']
            inception_date = datetime.utcfromtimestamp(inception_date)
            inception_date = inception_date.date()
            inception_date_str = inception_date.strftime('%Y-%m-%d')
            inception_dt = datetime.fromisoformat(inception_date_str)
        if 'category' in ticker.info: category = ticker.info['category']
        if 'fundFamily' in ticker.info: fund_family = ticker.info['fundFamily']

        # updating category / fund family if its missing
        if fund_family is None:
            if 'Fidelity' in long_name: fund_family = 'Fidelity'
            if 'Vanguard' in long_name: fund_family = 'Vanguard'
        if fund_family == 'Fidelity Investments':
            fund_family = 'Fidelity'
        if category is None:
            if 'Mid Cap' in long_name: category = 'Mid-Cap Blend'
            if 'Small Cap' in long_name: category = 'Small Blend'
            if 'Small Cap' in long_name: category = 'Small Blend'
            if 'International' in long_name: category = 'Foreign Large Blend'
            if '500' in long_name: category = 'Large Blend'
            if stock_ticker == 'FSMAX': category = 'Mid-Cap Blend'
            if stock_ticker == 'VIIIX': category = 'Large Blend'
            if stock_ticker == 'VINIX': category = 'Large Blend'
            if stock_ticker == 'FFOLX': category = 'Target Date Blend'

        # calc the expense ration
        # total_assets = None
        # if 'totalAssets' in ticker.info: total_assets = ticker.info['totalAssets']

        # test = ticker.info.keys()
        current_stock_price, current_reporting_date = self.get_stock_current_price(stock_ticker)
        inception_price = get_stock_inception_price(stock_ticker)
        previous_close_price = ticker.info['previousClose']
        current_reporting_dt_str = current_reporting_date.strftime('%Y-%m-%d')
        current_reporting_dt = datetime.fromisoformat(current_reporting_dt_str)

        if stock_ticker == 'FFOLX': cagr = 0.08 #issue with this stock getting a crazy high CAGR
        else:
            cagr = get_stock_cagr(
                inception_date=inception_dt,
                last_reported_date=current_reporting_dt,
                inception_price=inception_price,
                current_price=previous_close_price
            )

        stats = {
            'Stock': stock_ticker,
            #'Long Name': long_name,
            'Short Name': short_name,
            'Category': category,
            'Fund Family': fund_family,
            'Inception Date': inception_dt,
            'Inception Price': inception_price,
            'Last Reported Date': current_reporting_dt,
            'Previous Close Price': previous_close_price,
            'Current Stock Price': current_stock_price,
            'Compound Annual Growth Rate (CAGR)': cagr
        }
        stats_df = pd.DataFrame([stats])
        return stats_df

    def get_stock_current_price(self, stock_ticker: str, day_period: int = 2):
        """
        Purpose: Returns the current stock price at close \n
        Created By: Robert Krall \n
        Created On: 02/06/2025 \n

        :param stock_ticker: The Stock ticker
        :type stock_ticker: str

        :param day_period:  how many days to look at data. (some stocks are updated in 1 day others are more than 1 day)
        :type day_period: int

        :return: Current Stock Price (close_price) and Last Reported Ddate (current_reporting_date)
        """
        print(f"Looking up {stock_ticker} current price.")
        ticker = yf.Ticker(stock_ticker)
        if ticker is not None:
            hist_data = ticker.history(period=f'{day_period}d')
            if not hist_data.empty:
                close_price = hist_data['Close'].iloc[0]
                current_reporting_date = hist_data.index[-1]
                return close_price, current_reporting_date
            else:
                # Checking for data in the next 5 days and return 0 if there was no data in teh past 5 days
                if day_period == 5:
                    return 0, '1900-01-01'
                else:
                    close_price,current_reporting_date = self.get_stock_current_price(stock_ticker, day_period=day_period + 1)
                    return close_price, current_reporting_date
        else:
            return 0, '1900-01-01'

    def get_future_retirement_balance(self, contributions_df, future_years: int = 20):
        """
        Purpose: This function will predict future value of retirement balance using various methods. \n
        Created By: Robert Krall \n
        Created On: 02/08/2025 \n

        :param contributions_df:
        :param future_years: Number of years in the future
        :type future_years: int

        :return:
        """

        current_year = datetime.today().year
        years = list(range(current_year, current_year + (future_years+1)))
        years_df = pd.DataFrame({'Year': years})

        # get stock info
        ror_df = self.stock_info_df[['Stock', 'Compound Annual Growth Rate (CAGR)','Current Stock Price']].copy()
        ror_df.rename(columns={'Compound Annual Growth Rate (CAGR)':'cagr'},inplace=True)

        # current Stocks per plan
        current_stocks_df = self.stock_prices_df[['Company', 'Employer', 'Owner', 'Type', 'Sub Type', 'Stock Ticker', 'Weighted Average', 'Shares']].copy()
        current_stocks_df.rename(columns={'Stock Ticker': 'Stock'}, inplace=True)

        # for the joining of dataframes (cross join hack)
        ror_df['key'] = 1
        years_df['key'] = 1

        future_pricing = pd.merge(years_df, ror_df, on='key').drop('key', axis=1)
        future_pricing = pd.merge(future_pricing, current_stocks_df, on=['Stock'], how="left")
        future_pricing = pd.merge(future_pricing, contributions_df, on=['Company', 'Employer', 'Owner', 'Type', 'Sub Type'], how="left")
        future_pricing['Yearly Contributions'] = future_pricing['Weighted Average'] * future_pricing['Contributions']
        future_pricing = future_pricing.drop('Contributions', axis=1)

        # figure out future pricing and stocks well buy
        future_pricing['Future Stock Price (CAGR)'] = future_pricing.apply(lambda row: calc_stock_future_price(row, 'cagr'), axis=1)
        future_pricing['Future Stock Price (8%)'] = future_pricing.apply(lambda row: calc_stock_future_price(row, '8%'), axis=1)

        future_pricing['CAGR Shares'] = 0.0
        future_pricing['8% Shares'] = 0.0
        future_pricing['CAGR Value'] = 0.0
        future_pricing['8% Value'] = 0.0

        # Calc how many new shares I will be buying
        future_pricing.loc[~pd.isna(future_pricing['Yearly Contributions']), 'CAGR Shares'] = future_pricing['Yearly Contributions'] / future_pricing['Future Stock Price (CAGR)']
        future_pricing.loc[~pd.isna(future_pricing['Yearly Contributions']), '8% Shares'] = future_pricing['Yearly Contributions'] / future_pricing['Future Stock Price (8%)']

        # removing columns no longer needed
        future_pricing = future_pricing.drop('cagr', axis=1)
        future_pricing = future_pricing.drop('Current Stock Price', axis=1)
        future_pricing = future_pricing.drop('Weighted Average', axis=1)

        buying_shares_df = future_pricing[~pd.isna(future_pricing['Yearly Contributions'])][['Company','Employer','Owner','Type','Sub Type', 'Year', 'Stock', 'Shares', 'CAGR Shares','8% Shares']]
        buying_shares_df['Yearly CAGR Shares'] = 0.0
        buying_shares_df['Yearly 8% Shares'] = 0.0

        # getting the shares over time.
        for index, row in buying_shares_df.iterrows():
            # PK
            company = row['Company']
            employer = row['Employer']
            owner = row['Owner']
            type = row['Type']
            sub_type = row['Sub Type']
            stock_ticker = row['Stock']

            # New Shares
            cagr_shares = row['CAGR Shares']
            eight_percentage_shares = row['8% Shares']

            base_stock_filter = (
                    (buying_shares_df['Company'] == company) &
                    (buying_shares_df['Employer'] == employer) &
                    (buying_shares_df['Owner'] == owner) &
                    (buying_shares_df['Type'] == type) &
                    (buying_shares_df['Sub Type'] == sub_type) &
                    (buying_shares_df['Stock'] == stock_ticker)
            )

            if row['Year'] == current_year:
                stock_filter = base_stock_filter & (buying_shares_df['Year'] == row['Year'])

                cagr_shares += buying_shares_df.loc[stock_filter, 'Shares'].iloc[0]
                eight_percentage_shares += buying_shares_df.loc[stock_filter, 'Shares'].iloc[0]
            else:
                stock_filter = base_stock_filter & (buying_shares_df['Year'] == row['Year'] - 1)  # Grab Last year data to populate
                cagr_shares += buying_shares_df.loc[stock_filter, 'Yearly CAGR Shares'].iloc[0]
                eight_percentage_shares += buying_shares_df.loc[stock_filter, 'Yearly 8% Shares'].iloc[0]
                stock_filter = base_stock_filter & (buying_shares_df['Year'] == row['Year'])  # populate current year data

            # update rows in DF
            buying_shares_df.loc[stock_filter, 'Yearly CAGR Shares'] = cagr_shares
            buying_shares_df.loc[stock_filter, 'Yearly 8% Shares'] = eight_percentage_shares

        # join back to main df
        buying_shares_df = buying_shares_df.drop('Shares', axis=1)
        buying_shares_df = buying_shares_df.drop('CAGR Shares', axis=1)
        buying_shares_df = buying_shares_df.drop('8% Shares', axis=1)
        final_future_pricing = future_pricing.merge(buying_shares_df, on=['Company','Employer','Owner','Type','Sub Type', 'Year', 'Stock'], how='left')
        final_future_pricing.loc[pd.isna(final_future_pricing['Yearly CAGR Shares']), 'Yearly CAGR Shares'] = future_pricing['Shares']
        final_future_pricing.loc[pd.isna(final_future_pricing['Yearly 8% Shares']), 'Yearly 8% Shares'] = future_pricing['Shares']
        # Find the Future Value
        final_future_pricing['Yearly CAGR Value'] = final_future_pricing['Yearly CAGR Shares'] * final_future_pricing['Future Stock Price (CAGR)']
        final_future_pricing['Yearly 8% Value'] = final_future_pricing['Yearly 8% Shares'] * final_future_pricing['Future Stock Price (8%)']
        retirement_balances = final_future_pricing.groupby('Year').agg(
            CAGR_Balance=('Yearly CAGR Value', 'sum'),
            Eight_Percentage_Balance=('Yearly 8% Value', 'sum')
        ).reset_index()
        retirement_balances_final = retirement_balances.copy()
        retirement_balances_final.rename(columns={'CAGR_Balance': 'Yearly CAGR Value'}, inplace=True)
        retirement_balances_final.rename(columns={'Eight_Percentage_Balance': 'Yearly 8% Value'}, inplace=True)
        retirement_balances_final['Yearly CAGR Value (Todays Dollars)'] = retirement_balances_final.apply(lambda row: get_inflation_balance(row, 'cagr'), axis=1)
        retirement_balances_final['Yearly 8% Value (Todays Dollars)'] = retirement_balances_final.apply(lambda row: get_inflation_balance(row, None), axis=1)

        retirement_balances_format = retirement_balances_final.copy()
        retirement_balances_format['Yearly CAGR Value'] = retirement_balances_format['Yearly CAGR Value'].apply(format_money)
        retirement_balances_format['Yearly 8% Value'] = retirement_balances_format['Yearly 8% Value'].apply(format_money)
        retirement_balances_format['Yearly CAGR Value (Todays Dollars)'] = retirement_balances_format['Yearly CAGR Value (Todays Dollars)'].apply(format_money)
        retirement_balances_format['Yearly 8% Value (Todays Dollars)'] = retirement_balances_format['Yearly 8% Value (Todays Dollars)'].apply(format_money)

        return retirement_balances_final, retirement_balances_format
