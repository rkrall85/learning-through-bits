
import os
os.chdir('C:\\Users\\rkrall\\github\\randomscripts\padcolumns')

f2 = open('PadTestOutput.txt', 'w')   # write mode

#open file and put contents in a list
with open('PadTest.txt')  as fileopen: lines = fileopen.read().splitlines()

#pad items in list with 100 and output to new file.
for x in lines:f2.write(x.ljust(99)+'\n')

#closing files
f.close()
f2.close()
