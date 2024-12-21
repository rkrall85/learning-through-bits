

# pythontutor.com/visualize.html

name = 'Alice'
if name == 'Alice':
    print('Hello Alice')
print('Done')



name = 'Bob'
age = 30000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, kiddo')
elif age > 2000:
    print('Unlikc you, Alice is not an undead, imortal vampire')
elif age > 100:
    print('You are not Alice, grannie')



print('Enter a name.')
name = input()
if name: #can use truthy and falsey values
    print('Thank you for entering a name.')
else:
    print('You did not enter a name.')
