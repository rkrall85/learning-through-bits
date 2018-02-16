

#Map()

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

my_new_nums = list(map(square,my_nums))


print(my_nums)
print('')
print(my_new_nums)

print("*"*100)

def splicer(mystring):
    if len(mystring)%2 == 0:
            return 'even'
    else:
        return mystring[0]


my_names = ['A','BB','CC','DDDD']

print(my_names)
print(list(map(splicer, my_names))) #pass function and list; map will call function

print("*"*100)


#Filter()
def check_even(num):
    return num%2 == 0

print(check_even(10))
print(check_even(9))

nums = [1,2,3,4,5,6]
print(list(filter(check_even,nums))) #only return true

print("*"*100)

#lambda expression
#def square(num): return num**2
#print(square(4))

#lambda num: num**2 #this is format of lambda

print(list(map(lambda x:x**2, [1,2,3])))

print(list(filter(lambda n:n%2==0, [1,2,3,4,5])))
