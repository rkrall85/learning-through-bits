
'''
Found this example here:
https://sushanthukeri.wordpress.com/2017/03/14/data-analysis-with-amortisation-schedules/
'''

import pandas as pd
import numpy as np
from datetime import date
import matplotlib.pyplot as plt
#%matplotlib inline

interest_rate       = 0.02183
mortgage_term       = 30
num_payments_per_yr = 26
mortgage            = 800000
first_payment_date  = date(2017, 3, 16)
adj_interest_rate   = interest_rate/num_payments_per_yr
num_periods         = mortgage_term * num_payments_per_yr
#rng                 = pd.date_range(first_payment_date, periods = num_periods, freq='14d')
rng                 = pd.date_range(first_payment_date, periods = num_periods, freq='10B')
#rng                 = pd.date_range(first_payment_date, periods = num_periods, freq='m')

rng.name            = 'Payment Date'
#print(rng[:5])

#cal the bi-weekly payment
pmt = round(np.pmt(adj_interest_rate, num_periods, mortgage), 2)
print(pmt)
#pmt2 = pmt/2
#print(pmt2)


