

#Question 1:Open the exam.txt file with Python and with only read permission and store the contents in a list called exam_lines

import os
os.chdir('C:\\Users\\rkrall\\github\\CompletePython3MasterclassJourney\\FieldReadinessExams')
file_name = 'exam.txt'

with open(file_name) as f:
    exam_lines = f.readlines()
print(exam_lines)

print("*"*100)
#Question 2: HOw many lines does this file have?
print(len(exam_lines)) #7

print("*"*100)
#Question 3: Print out te 5th line of the text file
print(exam_lines[5:6])

print("*"*100)
#Question 4: Grab the last line of hte text file and saev it to a variable called last
last = exam_lines[-1]
print(last)

print("*"*100)
#Question 5: Use Indexing to grab the letter from the last line of the file
print(last[5])


print("*"*100)
#Question 6: HOw could you use python count how many words there are in the last line?
l = []
for word in last.split(): l.append(word)
print(len(l))

print("*"*100)
#Question 7: What data types are returned by the following lines?
print(type(2/3))        #float
print(type(2+2.0))      #flaot
print(type(1+1))        #int
print(type("2"+"2"))    #string
print(type(1>2))        #bool

print("*"*100)
#Question 8:  Your task is to retrieve the string "get me please" from the dictionary with stacked index and key calls.
d = {"levelone":[1,2,{'leveltwo':[5,6,[1,['get me please']]]}]}
print(d['levelone'])
print(d['levelone'][2])
print(d['levelone'][2]['leveltwo'])
print(d['levelone'][2]['leveltwo'][2])
print(d['levelone'][2]['leveltwo'][2][1])
print(d['levelone'][2]['leveltwo'][2][1][0])
print("*"*100)
#bonus task
#how many uniquie ints are in this list?

mylist = [1,2,3,4,5,6,4,3,2,1,2,3,4,5,6,6,7,8,5,6,7,8,9,8,9,8,9,7,10,123,1,2,2,3,1,3,2,4,1,4,4,1,2,2,22,3,4,1,4,1]
mysets = set(mylist)
print(len(mysets)) #12
