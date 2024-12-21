

#index order of values that can be orded and added or removed values


my_list = [1,2,3]
print(my_list)

my_list = ['a','b','c']
print(my_list)

my_list = [1,'a',2.3]
print(my_list)


my_list = ['a','b','c','d']
print(my_list[0])
print(my_list[0:3]) #up and not including 3

print(len('hello'))
print(len(my_list))

my_list = [1,2,3]
my_list.append(4)
print(my_list)

print(my_list.pop()) #remove last one (index of -1)
print(my_list)
my_list.append(4)

my_list.pop(0) #remove first
print(my_list)


my_list = [1,2,3,4]
my_first_item = my_list.pop(0)
print(my_list)
print(my_first_item)


my_list = [1,2,3,4,5]
my_list.reverse()
print(my_list)

my_list = [4,6,2,9]
my_list.sort() #sorting the list
print(my_list)

my_list = [1,2,3]
my_list.insert(2,'new') #insert at any location based on index
print(my_list)


new_list = [1,2,['a','b','c']]
print(type(new_list))

print(new_list[2][0]) #calling a value in a nested listed
