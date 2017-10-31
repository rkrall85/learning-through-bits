import numpy as np
#f = open('PythonExercises/2.SampleFile.txt','r') #this will not close the file

line_number = 0
list_of_words = []
#Read a file and output the count per each word in the file.
with open('PythonExercises/2.SampleFile.txt','r') as f: #will auto close file
    for a_line in f:
        line_number += 1
        word_list = [elt.strip() for elt in a_line.split(' ')]
        list_of_words.append(word_list)

num_of_lines = len(list_of_words) #number if lines in the txt file
#combining all the lines into 1 list of words
all_words = []
for i in range(num_of_lines): all_words = all_words + list_of_words[i]

all_words = sorted(all_words)#sorting list
word_set = set(all_words) #getting a distinct list of words

#create an 2 dim arrary with 0s for count for each dist word
#m = []
#for i in enumerate(word_set): m.append((0,i[1]))


m = {}
for i in enumerate(word_set):
        m.update({i:0})

print(m)
dict2 = {'Smith': 9}
m.update(dict2)
print(m)
##print(type(m))



dict = {'Name': 'Zara', 'Age': 7}
print(dict)
x = 'Name'
dict2 = {x: 'female' }

dict.update(dict2)
print(dict)

#for i in enumerate(all_words):
#for i in all_words:
#for x in enumerate(m):
    #print(m[0],[1])
    #print(i[1],[1])
#    print(i)


'''
print (m)

for idx, item in enumerate(m):
    print(idx)
    m[1,0] = 4
   #if 123 in item:
       #alist[idx] = 2014

print (m)

'''


'''
#working so far but the update
for i in enumerate(all_words):
        #print(i[1])
        current_word = i[1]
        for x in enumerate(m):
            current_matrix = x[1][1]
            #print(x[1][1])
            if current_word == current_matrix:
                current_count = x[1][0] + 1
                #Update row in matrix
                x[1][0] = current_count



print (m)
'''
#m = np.ones((len(word_set),2))
#m[0:] = m[0:].astype('str') #convert 0s to stringZ
#m3[0][1] = m[0][1].astype('str') #convert 0s to stringZ

#m = str(m)[1:-1]

#m[0,0] = '5'
#m[0,1] = '6'


'''
for i in enumerate(word_set):
        print(i[1])
        m[i,0] = 1
        m[i,1] = i[1]
'''

#for x in range(w):m2 = [[0 for x in range(w)] for y in range(h)] #Create blank matrix
#for i in range(word_set): counts = counts + ', 1'

#m3 = np.matrix([m1,m2])

#print(m3[0])




#Creating the matrix for cound and words
#word_count_matrix[]
#word_count_matrix[0][0] = 1, all_words[0]

#print(all_words[0])
#print(word_count_matrix)








#print (all_words)
#
'''
for index, word in enumerate(word_list):
    print("word:" + word + " is in position:" + str(index))

#looping through all the lines
for i in range(num_of_lines):
    num_of_words = len(list_of_words[i])
    for x in range(num_of_words):
        print(x)


'''
