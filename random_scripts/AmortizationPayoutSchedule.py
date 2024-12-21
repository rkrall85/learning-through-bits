import pandas as pd
from datetime import date
import numpy as np
from collections import OrderedDict
from dateutil.relativedelta import *
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize

'''
********************************************************************************
The following functions where taken from the following website. I have tweaked
them for my needs and made some enhancements.

https://github.com/chris1610/pbpython/blob/master/notebooks/Amortization-Corrected-Final.ipynb
********************************************************************************
'''
def amortize(principal, interest_rate, years, pmt, addl_principal, start_date, annual_payments,frequency):
    """
    Calculate the amortization schedule given the loan details.

    :param principal: Amount borrowed
    :param interest_rate: The annual interest rate for this loan
    :param years: Number of years for the loan
    :param pmt: Payment amount per period
    :param addl_principal: Additional payments to be made each period.
    :param start_date: Start date for the loan.
    :param annual_payments: Number of payments in a year.

    :return:
        schedule: Amortization schedule as an Ortdered Dictionary
    """

    # initialize the variables to keep track of the periods and running balances
    p = 1
    beg_balance = principal
    end_balance = principal

    while end_balance > 0:

        # Recalculate the interest based on the current balance
        if frequency == 'bi-monthly': annual_payments=26

        interest = round(((interest_rate/annual_payments) * beg_balance), 2)
        # Determine payment based on whether or not this period will pay off the loan
        pmt = min(pmt, beg_balance + interest)
        principal = pmt - interest

        # Ensure additional payment gets adjusted if the loan is being paid off
        addl_principal = min(addl_principal, beg_balance - principal)
        end_balance = beg_balance - (principal + addl_principal)

        yield OrderedDict([('Month',start_date),
                           ('Period', p),
                           ('Begin Balance', beg_balance),
                           ('Payment', pmt),
                           ('Principal', principal),
                           ('Interest', interest),
                           ('Additional_Payment', addl_principal),
                           ('End Balance', end_balance)])

        # Increment the counter, balance and date
        p += 1
        if frequency =='bi-monthly':
            start_date += relativedelta(weeks=2)
        else:#need to add more payment options such as quartley and weekly
            start_date += relativedelta(months=1)
        beg_balance = end_balance

def amortization_table(principal, interest_rate, years,
                       addl_principal=0,
                       annual_payments=12,
                       start_date=date.today(),
                       frequency='monhtly'):
    """
    Calculate the amortization schedule given the loan details as well as summary stats for the loan

    :param principal: Amount borrowed
    :param interest_rate: The annual interest rate for this loan
    :param years: Number of years for the loan

    :param annual_payments (optional): Number of payments in a year. DEfault 12.
    :param addl_principal (optional): Additional payments to be made each period. Default 0.
    :param start_date (optional): Start date. Default first of next month if none provided

    :return:
        schedule: Amortization schedule as a pandas dataframe
        summary: Pandas dataframe that summarizes the payoff information
    """

    # Payment stays constant based on the original terms of the loan
    payment = -round(np.pmt(interest_rate/annual_payments, years*annual_payments, principal), 2)
    if frequency == 'bi-monthly': payment=payment/2

    #print(annual_payments, principal)

    # Generate the schedule and order the resulting columns for convenience
    schedule = pd.DataFrame(amortize(principal, interest_rate, years, payment,
                                     addl_principal, start_date, annual_payments,frequency))
    schedule = schedule[["Period", "Month", "Begin Balance", "Payment", "Interest",
                         "Principal", "Additional_Payment", "End Balance"]]

    # Convert to a datetime object to make subsequent calcs easier
    schedule["Month"] = pd.to_datetime(schedule["Month"])
   
    #print(pd.to_datetime(schedule['Week'])[:75])

    #Create a summary statistics table
    payoff_date = schedule["Month"].iloc[-1]
    stats = pd.Series([payoff_date, schedule["Period"].count(), interest_rate,
                       years, principal, payment, addl_principal,
                       schedule["Interest"].sum()],
                       index=["Payoff Date", "Num Payments", "Interest Rate", "Years", "Principal",
                             "Payment", "Additional Payment", "Total Interest"])

    return schedule, stats
'''
********************************************************************************
********************************************************************************
********************************************************************************
'''
'''
Static variables
'''
principal       = 500 #$250,000
interest_rate   = .02 #3%
start_date      = date(2018,1,1)
'''
Scenario 1: 15 year monthly payment with $50 extra princ payments.
'''
frequency       = 'monthly'
years           = 2
addl_principal  = 0
schedule1, stats1 = amortization_table(
                                        principal       = principal,
                                        interest_rate   = interest_rate,
                                        years           = years,
                                        addl_principal  = addl_principal,
                                        annual_payments = 12,
                                        start_date      = start_date,#date(2017,8,29),
                                        frequency       = frequency
                                        )
#print(pd.DataFrame([stats1]))
'''
Scenario 2: 30 year monthly payment with $50 extra princ payments.
'''
frequency       = 'bi-monthly'
years           = 2
addl_principal  = 0
schedule2, stats2 = amortization_table(
                                        principal       = principal,
                                        interest_rate   = interest_rate,
                                        years           = years,
                                        addl_principal  = addl_principal,
                                        annual_payments = 12,
                                        start_date      = start_date,#date(2017,8,29),
                                        frequency       = frequency
                                        )
#print (schedule1.tail())

#print (schedule2)

print (schedule1.head())
print (schedule2.head())

#just out total interest spent.
#print (schedule1[['Interest']].sum())
#print (schedule2[['Interest']].sum())


#print(pd.DataFrame([stats1, stats2]))

#ScenariosVariables('bi-monthly',25)
#print (freq,payments_per_year,periods)


#creating a graph
plt.style.use('ggplot')
fig, ax = plt.subplots(1, 1)
schedule1.plot(x='Month', y='End Balance', label="30 year monthly w/o addlt payment", ax=ax)
schedule2.plot(x='Month', y='End Balance', label="30 year bi-mothly w/o addlt payment", ax=ax)
#schedule3.plot(x='Month', y='End Balance', label="15 year mothly w/o addlt payment", ax=ax)
plt.title("Pay Off Timelines");

plt.show()


'''
def make_plot_data(schedule, stats, freq):
    """Create a dataframe with annual interest totals, and a descriptive label"""
    y = schedule.set_index('Month')['Interest'].resample("A").sum().reset_index()
    y["Year"] = y["Month"].dt.year
    y.set_index('Year', inplace=True)
    y.drop('Month', 1, inplace=True)

    label="{} years at {}% with additional payment of ${} with {} payments".format(stats['Years'], stats['Interest Rate']*100, stats['Additional Payment'],freq)
    return y, label

y1, label1 = make_plot_data(schedule1, stats1,'monthly')
y2, label2 = make_plot_data(schedule2, stats2, 'bi-monthly')
#y3, label3 = make_plot_data(schedule3, stats3)

y = pd.concat([y1, y2], axis=1)


figsize(7,5)
fig, ax = plt.subplots(1, 1)
y.plot(kind="bar", ax=ax)

plt.legend([label1, label2], loc=1, prop={'size':10})
plt.title("Interest Payments");

plt.show()
'''
'''
#df, stats = amortization_table(700000, .04, 30, addl_principal=200, start_date=date(2016, 1,1))

#print (stats)

#print (df.head())

#print (df.tail())
'''
#schedule1, stats1 = amortization_table(100000, .04, 30, addl_principal=50, start_date=date(2016,1,1))
#schedule2, stats2 = amortization_table(100000, .05, 30, addl_principal=200, start_date=date(2016,1,1))
#schedule3, stats3 = amortization_table(100000, .04, 15, addl_principal=0, start_date=date(2016,1,1))
