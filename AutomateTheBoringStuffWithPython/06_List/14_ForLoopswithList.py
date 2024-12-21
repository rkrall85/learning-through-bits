




for i in range(4):
    print(i)


#print(range(4))    # same as list[0,1,2,3]
#print(list(range(4)))

#print(list(range(0, 100, 2))) #list from 0-100 and incrase by 2

#spam = list(range(0, 100, 2))
#print(spam)

# print out index and value ina  list.
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' +str(i)  + ' in supplies is: ' + supplies[i])


# multi assigments
cat = ['fat', 'orange', 'loud']
# old way (bad way)
size = cat[0]
color = cat[1]
disposition = cat[2]
#new way
size, color, disposition = cat
#print (size)
size, color, disposition = 'skinny', 'black', 'quiet'
#print (size)


a = 'AAA'
b = 'BBB'
print(a + ' ' + b)
a,b = b,a
print(a + ' ' + b)


# augmented assignment operators
# works for +, -, *, /, %
spam  = 42
spam = spam + 1 # old way
spam += 1 # new way
