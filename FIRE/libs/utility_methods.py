import yfinance as yf
from datetime import datetime, timedelta


def get_stock_cagr(inception_date, last_reported_date, inception_price, current_price):
    """

    :param inception_date:
    :param last_reported_date:
    :param inception_price:
    :param current_price:
    :return:
    """

    if inception_price == 0: inception_price = 1

    n = (last_reported_date - inception_date).days / 365.25
    cagr = ((current_price / inception_price) ** (1 / n)) - 1

    return cagr


def get_stock_inception_price(stock_ticker: str):
    """

    :param stock_ticker:
    :return:
    """
    ticker = yf.Ticker(stock_ticker)
    hist_data = ticker.history(period='max')
    open_price = hist_data['Open'].iloc[0]
    return open_price


def calc_stock_future_price(row, percentage_flag):

    if percentage_flag == 'cagr':
        rate = row['cagr']
    else:
        rate = 0.08

    current_year = datetime.today().year
    years = row['Year'] - current_year

    principal = row['Current Stock Price']

    # Calculate the compound interest
    amount = principal * (1 + rate) ** (1 * years)

    # Calculate the interest earned
    #interest = amount - principal

    return amount


def get_inflation_balance(row, flag ='cagr'):
    current_year = datetime.today().year
    years = row['Year'] - current_year

    if flag =='cagr':
        principal = row['Yearly CAGR Value']
    else:
        principal = row['Yearly 8% Value']

    # Calculate the compound interest
    amount = 1/ (1 + 0.03) ** years
    future_value = principal * amount

    return future_value
