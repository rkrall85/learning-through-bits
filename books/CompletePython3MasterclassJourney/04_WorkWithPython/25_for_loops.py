


mylist = [1,2,3,4]
for num in mylist:
    print(num,end=' ' ) #print on all same line

print("*"*10)
print('\n')
for num in mylist:
    print('hello')

print("*"*10)
print('\n')
for letter in 'this is a string':
    print(letter)

print("*"*10)
print('\n')
tup = (1,2,3,4)
for n in tup:
    print(n)

print("*"*10)
print('\n')
list_of_tups = [(1,2),(3,4),(5,6),(7,8),(9,10)]
for (item1, item2) in list_of_tups:
    print(item1)
    print(item2)
    print('\n')

print("*"*10)

for n1,n2 in list_of_tups:
    print(n1)

print("*"*10)
d = {'a':1, 'b':2, 'c':3}
for key, value in d.items():
    print(key)
    print(value)
    print('\n')


print("*"*10)
for k in d:
    print(d[k])


print("*"*10)
for letter in 'code':
    if letter == 'd':
        continue
    print(letter)
