'''
Robert Krall
SEIS763
Assignment 1
'''

#import these libraries
import pandas as pd
input_file  = open('FisherIris_MDL.csv','r')  #read mode

#1.Read in the CSV file “FisherIris_MDL.csv” into a matrix named as “Iris”.
#print(str('*'*10) +'Question 1' + str('*'*10))
Irish = pd.read_csv(input_file, sep="|", header=None)
Irish.columns = ["a","b","c","d","f","e"]#leave out if there is a header
#print(Irish)

#2.Display the number of row and number of columns of the matrix “Iris”.
print(str('*'*10) +'Question 2' +str('*'*10))
print("(row,columns)")
print(Irish.shape)

#3.Display all the row numbers that have the 5th column less than 0.
print(str('*'*10) +'Question 3' +str('*'*10))
print(Irish[Irish.f<0])

#4.Remove the rows with the 5th column less than 0 from the “Iris” matrix.
Irish = Irish[Irish.f<0]

#5.Display the number of row and number of columns of the “Iris” matrix again.
print(str('*'*10) +'Question 5' + str('*'*10))
print("(row,columns)")
print(Irish.shape)

#6.Copy the first 4 columns in the new “Iris” matrix into a new matrix “X”.
print(str('*'*10) +'Question 6' + str('*'*10))
x = Irish.iloc[:,0:4]
print(x)

#7.Copy the 5th columns in the new “Iris” matrix into a new variable (or matrix) “Y”.
#print(str('*'*10) +'Question 7' + str('*'*10))
y = Irish.f

#8.Display the maximum value and the minimum value of each column in “X”.
print(str('*'*10) +'Question 8' + str('*'*10))
#axis = 0 is column base, 1 is row based
min = x.min(axis=0)
max = x.max(axis=0)
print("Min:", min.values)
print("Max:", max.values)

#9.Display the number of elements in the third column of the matrix “X” that is greater than 36.
print(str('*'*10) +'Question 9' + str('*'*10))
print(x[x.c>36])

#make sure to close both files
input_file.close()
