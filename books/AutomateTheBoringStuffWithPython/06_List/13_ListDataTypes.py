


spam = ['cat','bat',' rat','elephant']


print(spam[0]) # output 1st item in the list


spam2 = [['cat','bat'], [10,20,30,40,50]]

print(spam2[0][1]) #output the value of bat


# index = single value
# slice = list of values

spam3 = ['cat','bat',' rat','elephant']
print(spam[-1]) #last item in the list (index)

print('The ' + spam[-1] + ' is afread of the ' + spam[-3])

#output slice
print(spam3[1:3])  #Slice

# changing a lis's items via index
spam4 = [10,20,30]
print(spam4)
spam4[1] = 'hello'
print(spam4)

# chagning a lists item via slice
spam4[1:3] = ['cat','dog','mouse']
print(spam4)

# slice short cut
print(spam4[:3])
print(spam4[1:])


# delete items from a lists
spam5 = ['cat','bat',' rat','elephant']
print(spam5)
del spam5[2]
print(spam5)



# string and list similiaers
print(len('Hello'))
print(len([1,2,3]))

# caoncate strings and lists
str1 = 'Hello'
str2 = ' World'
print(str1 + str2)

str3 = [1,2,3]
str4 = [4,5,6]
print(str3 + str4)

str5 = 'Hello' * 3
print(str5)

str6 = [1,2,3] * 3
print(str6)

print(int('32')) #return int
print(str(32)) #return a string
print(list('Hello')) #return a list


# the in and not in operator
print('howdy' in ['hello', 'hi', 'howdy'])
