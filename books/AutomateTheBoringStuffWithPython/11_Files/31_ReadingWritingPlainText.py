


import os

os.chdir('C:\\Users\\rkrall\\github\\AutomateTheBoringStuffWithPython\\11_Files')

f = open('31_zSampleFile.txt')          # read only mode
f2 = open('31_zSampleFile2.txt', 'w')   # write mode


content = f.read()
#print(f.readlines())

#f2.write('Hello')



f.close()
f2.close()
