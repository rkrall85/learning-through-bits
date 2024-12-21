




import pandas as pd

df1 = pd.read_csv('randomscripts\comparefiles\comparefile1.csv',
                    names=['UID', 'FirstName'],
                    sep='|',
                    skiprows=[0]
)

df2 = pd.read_csv('randomscripts\comparefiles\comparefile2.csv',
                    names=['UID', 'FirstName'],
                    sep='|',
                    skiprows=[0]
)

print(df1) #output file 1
print(df2) #output file 2

print('-' *10 )

common_cols = df1.columns.tolist()                         #generate list of column names
df12 = pd.merge(df1, df2, on=common_cols, how='inner')     #extract common rows with merge
df22 = df2[~df2['UID'].isin(df12['UID'])]

print(df22)
