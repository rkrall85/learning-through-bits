

#range function
for num in range(0,11,2): #start, end, step
    print(num)

#output range into a list
print(list(range(0,10)))

index = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index, letter))
    index += 1
print("*"*100)

#better then above
for index, letter in enumerate('abcde'):
    print('At index {} the letter is {}'.format(index, letter))

print("*"*100)
print(list(enumerate('abcde')))

print("*"*100)
#Zip two lists (only goes to shorter list)
mylist1 = [1,2,3,4,5,6,7]
mylist2 = ['a','b','c','d','e']
for item in zip(mylist1, mylist2):
    print(item)

print("*"*100)
print(list(zip(mylist1, mylist2)))

print('x' in [1,2,3])

mylist = [10,20,30,40,100]
print(min(mylist)) #min value in list
print(max(mylist)) #max value in list

from random import shuffle
print(mylist)
shuffle(mylist)
print(mylist) #put in random order

from random import randint
print(randint(0,100))
