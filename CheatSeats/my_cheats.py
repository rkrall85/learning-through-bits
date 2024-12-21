
#list of random examples to do various stuff in python

#examples: https://ehmatthes.github.io/pcc/cheatsheets/README.html


'''
import these libraries for examples
'''
import pandas as pd
import numpy as np






#####################Pandas Examples###########################

# Read example file_name
#mdf =  pd.read_excel(open(file_name,'rb'), sheetname=0) #tab 0 in spreadsheet

#passing dataframe to function
a = pd.DataFrame({'a':[1,2], 'b':[3,4]})
def letgo(df):
    df = df.drop('b', axis=1)
    return(df)

print(a)
a = letgo(a)
print(a)






################################################################
