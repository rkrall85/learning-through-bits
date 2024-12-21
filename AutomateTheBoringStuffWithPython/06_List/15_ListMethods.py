


# method same as function but called on a value

spam = ['hello', 'hi','howdy','heyas']

print(spam.index('hello')) # return 0
print(spam.index('heyas')) # return 3
#print(spam.index('heyas12')) # expection error
print('-' * 100 )

spam = ['Zophie','Pooka','Fat-tail','Pooka']
print(spam.index('Pooka')) #return first match
print('-' * 100 )

# append and insert list methods
# append = end of list
spam = ['cat','dog', 'bat']
print(spam)
spam.append('moose')
print(spam)
print('-' * 100 )

# insert = insert at any point in list
spam = ['cat','dog', 'bat']
print(spam)
spam.insert(1,'chicken')
print(spam)

print('-' * 100 )

# remove methods
spam = ['cat','dog', 'bat']
print(spam)
spam.remove('bat') #will error out if not in the list; will remove only first match
print(spam)
print('-' * 100 )

# del statement
spam = ['cat','dog', 'bat']
print(spam)
del spam[0]
print(spam)
print('-' * 100 )

# sort list methods
spam = [2,5,3.14,-7]
print(spam)
spam.sort()
print(spam)
print('-' * 100 )

spam = ['ants','dogs','cats','elephants','bats']
print(spam)
spam.sort() #upper case then lower case
print(spam)
print('-' * 100 )

spam.sort(reverse=True) #reverse sorting
print(spam)
print('-' * 100 )



spam = ['a','z','A','Z']
spam.sort()
print(spam)
spam.sort(key=str.lower) #want to sort it in betical no matter the case.
print(spam)
