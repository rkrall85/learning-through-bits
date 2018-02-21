


try:
    1 + '2'
except TypeError:
    print('You are not adding the correct things together')
else:
    print("everything ran smoothly")




try:
    f = open('testfile','r')
    f.write('Test write this')
except:
    print("hey an error happened!")
else:
    print("everything worked")



try:
    f = open('testfile','r')
    f.write('Test write this')
except:
    print("hey an error happened!")
finally:
    print("this code will always run")
