

import yfinance as yf
import pandas as pd
import numpy as np

# Define the stock ticker and the time period
#ticker = 'AAPL'  # Example: Apple Inc.
ticker = 'VO'
start_date = '2004-01-01'
end_date = '2025-02-02'

# Fetch historical data
stock_data = yf.download(ticker, start=start_date, end=end_date,multi_level_index=False,  actions=True)

# Check for stock splits
stock_splits = stock_data[stock_data['Stock Splits'] != 0]


# Group by year and get the last entry per year
stock_data['Year'] = stock_data.index.year

# the close amount per year
yearly_amounts = stock_data.groupby('Year').last()['Close'].reset_index()
yearly_amounts['Open'] = yearly_amounts['Close'].shift(1)
yearly_amounts.at[0, 'Open'] = stock_data.iloc[0]['Open']

# calc the number of days in trading year
first_date_per_year = stock_data.groupby('Year').apply(lambda df: df.index.min()).reset_index(name='First Date')
last_date_per_year = stock_data.groupby('Year').apply(lambda df: df.index.max()).reset_index(name='Last Date')
yearly_dates = pd.merge(first_date_per_year, last_date_per_year, on=['Year'], how='inner')
yearly_dates['days_in_year'] = (yearly_dates['Last Date'] - yearly_dates['First Date']).dt.days + 1

# yearly dataset
yearly_dataset = pd.merge(yearly_amounts[['Year','Open', 'Close']], yearly_dates[['Year','days_in_year']], on='Year', how='inner')
# Rate of Return Dataframe
yearly_dataset['Yearly Rate of Return'] = (yearly_dataset['Close'] / yearly_dataset['Open']) ** (365 / yearly_dataset['days_in_year']) - 1


print(yearly_dataset)

# Calculate the average yearly rate of return
average_rate_of_return = yearly_dataset['Yearly Rate of Return'].mean()
