

#unordered collections of unique elements


x = set()
x.add(1)
print(x)

x.add(2)
x.add(1) #never got added
print(x)



mylist = [1,1,1,1,1,2,2,2,2,2,24,4,4,44,3,3,3,3,3]
z = set(mylist) #will only grab the unique values
print(z)

myset = {1,2,3}
print(myset)
