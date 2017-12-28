

spam = 1
while spam < 5:
    print('Hello world!')
    spam = spam + 1



name = ''
while True:
    print('please type your name')
    name = input()
    if name == 'your name':
        break
print('Thank you')



spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3: #skip the print of spam of 3
        continue
    print ('spam is ' + str(spam))
