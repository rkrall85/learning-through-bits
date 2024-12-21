





print('hello')
print("hello")
#\t = tab, \n = return
print("I want this in 2 lines \njust like this") # \n is a new line break

word = 'hello'
print(word)
print(word[0])
print(word[-1])

alpha = 'abcdef'
print(alpha[0:3]) #up to 3 but not including 3
print(alpha[:3])


basic = "hello world"
print(basic.upper())
print(basic.lower())
print(basic.split()) #by default based on spaces
print(basic.split('o')) #split on o's.

user_name = "Recruit"
action = 'run'
print('The {} needs to {}'.format(user_name,action))
print('The {a} needs to {b}'.format(a=user_name,b=action))


num = 123.6789
print('the code is {:.1f}'.format(num)) #round 1 place after decimal
print('the code is {:.0f}'.format(num)) #round to whole number
