
import csv
import pandas as pd
import os
os.chdir('C:\\Users\\rkrall\\github\\randomscripts\padmulticolumns')

df = pd.read_csv('padmultitest.csv', delimiter='|')
df2 = open('padmultiout.txt', 'w')   # write mode

tuples = [tuple(x) for x in df.values] #making a tuple of the data
#dicts = df.to_dict().values #making a dictonary of the data

for i in range(len(tuples)): #row loop
    #print('row: '+ str(i)  + ' value: ' + str(tuples[i]))
    for x in range(len(tuples[i])): #column loop
        if x == 0:# column 1 is 40 char
            z = str(tuples[i][x])
            df2.write(z.ljust(39))
        elif x == 1: # column 2 is 100 chars
            df2.write(z.ljust(99))
        else: # else just 10 chars
            df2.write(z.ljust(9))
        df2.write('|')
    df2.write('\n')

#df.close()
df2.close()
