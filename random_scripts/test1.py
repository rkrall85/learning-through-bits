import pandas as pd
from datetime import date
import numpy as np
from collections import OrderedDict
from dateutil.relativedelta import *


def amortize(principal, interest_rate, years, addl_principal=0, annual_payments=12, start_date=date.today()):

    pmt = -round(np.pmt(interest_rate/annual_payments, years*annual_payments, principal), 2)
    pmt = pmt/2
    print (pmt)
    
    
    # initialize the variables to keep track of the periods and running balances
    p = 1
    beg_balance = principal
    end_balance = principal

    while end_balance > 0:

        # Recalculate the interest based on the current balance
        #interest = round(((interest_rate/annual_payments) * beg_balance), 2)
        interest = round(((interest_rate/26) * beg_balance), 2)


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
        #start_date += relativedelta(months=1)
        start_date += relativedelta(weeks=2)
        beg_balance = end_balance

schedule = pd.DataFrame(amortize(500, .02, 2, addl_principal=0, annual_payments=12,start_date=date(2016, 1,1)))
print(schedule)#[:75])

#total_interest = schedule.['interest'].sum()

print (schedule[['Interest']].sum())


#print(schedule)

#schedule1, stats1 = amortization_table(100000, .04, 30, addl_principal=50, start_date=date(2016,1,1))
#print ([stats1])