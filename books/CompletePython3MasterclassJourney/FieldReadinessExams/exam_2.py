
#question 1. Use a for loop and indexing to print out only the words that start with an s in this sentence:
mystring = "Secret agents are super good at staying hidden."
mystring = mystring.lower()
mylist = mystring.split(' ') #split up words in a list
i=0
while i in range(len(mylist)):
    if mylist[i][0:1] == 's':
        print(mylist[i])
    i += 1

print("*"*100)


#question 2: Use a for loop to only print out the words with an even number of characters/letters.
for word in mystring.split():
    if len(word) % 2 ==0:
        print(word)

print('*'*100)

#Question 3:Use a list comprehension to create a list of every first letter in this string:
i=0
l = list()
for word in mystring.split():
    l.append(word[:1])
print(l)
l = list()
#OR
[l.append(word[0]) for word in mystring.split()]
print(l)

print("*"*100)

#question 4:Use list comprehension to create a list of all the even numbers from 0 to 10.
l = list()
i = 0
while i in range(11):
    if i % 2 == 0:
        l.append(i)
    i +=1
print(l)

print("*"*100)

#Question 5: Use the range function to create a list of all the even numbers from 0 to 10.
print(list(range(0,11,2)))
print("*"*100)

#Question 6:Create a for loop that uses the random library to create a list of 10 random numbers.
import random
l = []
for x in range(0,11):
    l.append(random.randrange(0,100))
    i += 1
print(l)

print("*"*100)

#Question 7:Use list comprehension and the random library to create a list of 10 random numbers
l = []
[l.append(random.randint(0,100)) for n in range(0,11)]
print(l)

#Question 8:
num1 = int(input ("Enter a even number: "))
while num1 % 2 != 0:
    print("Please provide an even number: " + str(num1))
    num1 = int(input ("Enter a even number: "))
else:
    print("Thank you")
    num1 = 2
