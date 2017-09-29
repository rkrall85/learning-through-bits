
import numpy as np
#Read a file and output the count per each word in the file.
f = open('PythonExercises/2.SampleFile.txt','r')
#print(f.read()) #outputing the file to console.


#Putting words in doc in a list
list_of_words = []
with open('PythonExercises/2.SampleFile.txt') as f2:
    for line in f2:
        word_list = [elt.strip() for elt in line.split(' ')]
        list_of_words.append(word_list)

#Making Matrix of words with number of times word shows up in doc.
name_count =  {}
word_count = len(word_list)
wc = 1
word_maxtrix = []
word_maxtrix.append([1,word_list[0]])

while wc < word_count:
    #print(word_list[wc])
    #grabbing current row in Matrix
    Current_word = word_list[wc]
    martrix_count = len(word_maxtrix)
    ms = 0
    while ms < martrix_count:
        current_maxtrix = word_maxtrix[ms][1]
        if current_maxtrix == Current_word: #found match
            word_maxtrix[ms][0] = word_maxtrix[ms][0] + 1
            ms = ms + 1
            found_flag = "yes"
        else:
            found_flag = "no"
            ms = ms + 1
    if found_flag ==  "no": word_maxtrix.append([1,Current_word])
    wc =  wc + 1


print(word_maxtrix)
