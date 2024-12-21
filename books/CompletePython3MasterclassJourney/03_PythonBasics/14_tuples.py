
#use when data never chagnes such as dates of the year

mytuple = (1,2,3)
print(type(mytuple))


t = ('a',1,3.4)
print(t[0])

mylist = [1,2,3]
mylist[0] = 'new'
print(mylist)

#mytuple[0] ='new' #error! You can't replace items in a tuple

t = ('a','b','c','a')
print(t)
print(t.index('b'))

print(t.count('a'))


d = {'a':1,'b':2}
print(d.items())
