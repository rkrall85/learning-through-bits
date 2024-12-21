


mylist = []
s = 'somestring'
for letter in s: mylist.append(letter)
print(mylist)

#better way
mynewlist = [letter for letter in s]
print(mynewlist)


squares = [x**2 for x in range(0,11)]
print(squares)

evens = [x for x in range(0,10) if x%2 == 0]
print(evens)

mylist = [x if x%2 == 0 else 'not even' for x in range(0,10)]
print(mylist)
