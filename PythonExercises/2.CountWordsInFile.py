
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
word_count =  (len(word_list))
word_maxtrix = []
word_maxtrix.append([1,word_list[0]])
















w, h = 2, word_count #making the width and height of Matrix
Matrix = [[0 for x in range(w)] for y in range(h)] #Create blank matrix
#Matrix[0][0] = 1,  word_list[0] #update row 1 with first word in file


#j =  np.random.randint(1, size=(3, 3)) #prob a better way to make the matrix
j = np.ones((len(word_list),2))
j[0:] = j[0:].astype('str') #convert 0s to stringZ
j[0][1] = j[0][1].astype('str') #convert 0s to stringZ

#print(word_maxtrix[0][1])
#j[0,0] = '5' #col 1 row 1 #count
#j[0,1] = 6 #col 2 row 1 #word
#j[0][1] = 'John'
#j[0][0] = 'John'
#j[0,1] = 'John'
#print(j)

word_count = word_count - 1
found_flag = "no"
#Put the words in the array
for list in list_of_words:
    for x in list:
        wc = 1
        max_row_number = len(word_maxtrix)+1
        row_number = len(word_maxtrix)
        while row_number < max_row_number: #wc < word_count and
            current_word = word_maxtrix[0][wc]
            if x == current_word:
                row_number = row_number -1
                current_count = word_maxtrix[row_number][0]
                word_maxtrix[row_number][0] = current_count + 1
                found_flag = "yes"
                row_number = row_number + 2 #find a better way
            else:
                found_flag = "no"
                missing_word = x
                #wc = wc + 1
                row_number = len(word_maxtrix) + 1
        if found_flag == "no":
            row_number = len(word_maxtrix) + 1
            word_maxtrix.append([1,missing_word])


print(word_maxtrix)
        #j[c:0] = x
        #j[c:0] = x
        #word_maxtrix.append([1,x])



#aa = np.asmatrix(list_of_words)


#print("end")
#print (word_list[0])
#for x  in enumerate(word_list):
#for x in range(len(word_list)):
#for x in range(0,len(word_list)):
#for x in list_of_words:
    #for y in x:
    #    print(y)


#j[0,0] = 5
#j[0,1] = 6
#o = j[3,0]
#print(0)
#print(j)

''''


for list in list_of_words:
    c = 0
    for x in list:
        wc = 0
        print (x)
        while wc < word_count:
            current_word = j[wc,0]
            print (current_word)
            if x == current_word:
                print("yes")
            else:
                #print("no")
                #print(wc)
                #print(current_word)
                #j[wc,1] = x
                #j[wc,0] = 1
                wc = word_count
            wc = wc + 1

        if x == current_word:
                current_count = j[wc,0]
                j[wc,o] = current_count+ 1
                pint("insert")
            else:
                j[wc,1] = current_word
                print("update")

'''

        #is_valid = np.equal(j, c)
        #print(is_valid)
        #ix = np.isin(j, c)
        #print(ix)
        #print(np.where(ix))



        #g = j.item(0,0)
        #print(g)
        #print(c)
#        c = c+1


        #if is_valid.any() == 1:#'True'
        #    print ("yes")
    #        g = j.item(0,x)
            #g = Matrix.([0][x])
#            print(g)
        #Matrix[0][x] = 1,[x]
        #print(Matrix[0][x])
        #current_count = Matrix[0:]
        #print(current_count)


#        else:#
            #print("no")

        #x= x+1

x,y = 0 , h+ 1
#print(Matrix[0][0])

#print(Matrix[0][0])
#print(Matrix[1][0])
#print(Matrix[2][0])
#print(Matrix[3][0])
#print(Matrix[0][0])
#print(Matrix)
