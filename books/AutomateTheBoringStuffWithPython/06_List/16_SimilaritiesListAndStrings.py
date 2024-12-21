


# simliarites between lists and strings


print(list('hello'))
name = 'Zophie'
print(name[0])

print('XXX' in name)

for letter in name:
    print(letter)

print('-' * 10)

name = 'Zohpie the cat'
print(name[7])
#name[7] = 'X' #error
print('-' * 10)

name = 'Zophie the cat'
newname = name[0:7] + 'the' + name[8:12]
print(newname)
print('-' * 10)


#changing values
#strings example
spam = 42
cheese = spam
print(cheese)
spam = 100
print(spam)
print('-'*10)
#list example
spam = [0,1,2,3,4,5]
cheese = spam #this is a reference; hence why both values get changed
cheese[1] = 'Hello'
print(cheese)
print(spam)
print('-' * 10)
