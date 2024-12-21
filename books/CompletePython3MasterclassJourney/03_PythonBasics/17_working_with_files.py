

import os
os.chdir('C:\\Users\\rkrall\\github\\CompletePython3MasterclassJourney\\03_PythonBasics')
file_name = 'test_file.txt'

myfile = open(file_name)
lines = myfile.read()
print(lines)
#print(myfile.readlines())
#myfile.seek(0) #resets the cursor in the file
#print(myfile.read())
myfile.close()


#lets you not worry about closing a file
#there is different modes for writing and opening
with open(file_name) as myfile:
    lines = myfile.read()

print(lines)

f = open('second_file.txt', mode='r')
print(f.read())
f.close()

f = open('second_file.txt', 'w') #over write the current file if its exsist.
f.write('new lines2')
f.close()

with open('second_file.txt') as f: print(f.read())
#create new file

with open('second_file2.txt','w') as f:
    f.write('new file made')

with open('second_file2.txt') as f: print(f.read())

#append or a mode will continue writting in the correct file.
with open('second_file2.txt','a') as f:
    f.write('\nanother line')

with open('second_file2.txt','r') as f: print(f.read())
