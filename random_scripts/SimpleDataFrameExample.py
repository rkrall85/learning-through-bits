import pandas as pd
import numpy as np
from datetime import date


InterestRate = 0.04
Years = 30
#PaymentsYear = 12
Principal = 200000
AddlPrincipal = 50
StartDate = (date(2016,1,1))
Frequency = 'monthly'

'''
figure out how many payments and frequency to calc payment amount
example:
    freq = 2w (every 2 weeks), MS (monthly)
    per = 240 periods to calculate (20 years or 240 months)
'''
if Frequency == 'monthly':
    Freq            = 'MS' #month start
    PaymentsPerYear = 12
    Periods         = PaymentsPerYear*Years
elif Frequency == 'bi-monthly':
    Freq            = '2ws'
    PaymentsPerYear = 12*2
    Periods         = PaymentsPerYear*Years
else:
    Freq            = 'AS' #year start freq
    PaymentsPerYear = 12
    Periods         = PaymentsPerYear*Years

#print(Periods)
#cal payment
#pmt = np.pmt(InterestRate/PaymentsPerYear, Periods, Principal)

# Calculate the interest
#ipmt = np.ipmt(InterestRate/12, 1, Periods, Principal)
#ipmt2 = np.ipmt(InterestRate/12, 1, 30*12, Principal)


# Calculate the principal
#ppmt = np.ppmt(InterestRate/PaymentsPerYear, PaymentsPerYear, Periods, Principal)


#building the calendar of payments
rng = pd.date_range(
                    start   = StartDate,
                    periods = Periods,
                    freq    = Freq,
                    name    = "Payment_Date"
                    )
#print (rng)

#Create a data fram fro the payments, princ, interest (dateframe is like a db table)
df = pd.DataFrame(index=rng,columns=['Payment', 'Principal', 'Interest', 'Addl_Principal', 'Balance','Curr_Balance', 'Cumulative_Principal'], dtype='float')
df.reset_index(inplace=True)
df.index += 1
df.index.name = "Period"

#calc each column in data frame
df["Payment"] = np.pmt(
                       rate = InterestRate/PaymentsPerYear, #Rate of interest (per period)
                       nper = Periods,                      #Number of compounding periods
                       pv = Principal                       #Present value
                       )
df["Principal"] = np.ppmt(
                          rate  = InterestRate/PaymentsPerYear,
                          per   = df.index,
                          nper  = Periods,
                          pv    = Principal
                          )
df["Interest"] = np.ipmt(
                         rate   = InterestRate/PaymentsPerYear,
                         per    = df.index,
                         nper   = Periods,
                         pv     = Principal
                         )
df["Addl_Principal"] = -AddlPrincipal
df = df.round(2)


df["Cumulative_Principal"] = df["Cumulative_Principal"].clip(lower=-Principal)
df["Curr_Balance"] = Principal + df["Cumulative_Principal"]
print(df)
