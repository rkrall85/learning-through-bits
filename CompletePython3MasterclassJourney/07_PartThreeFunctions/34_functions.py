


def add_function(num1=0, num2=0):
    return num1+num2


results = add_function(1,2)
print(results)


def report_agent():
    print('Report Agent')

report_agent()


def report(name='missing'):
    print("Reporting {}".format(name))

report('bond')


def add(n1,n2):
    print(n1+n2)

add(2,3) #can't assign answer to variable since its only print

def add(n1,n2):
    return(n1+n2)

results = add(2,3)
print(results)


def secret_check(mystring):
    return 'secret' in mystring.lower()

print(secret_check('hello'))
print(secret_check('this is a Secret'))


def code_maker(mystring):
    '''
    INPUT: is a string
    OUTPUT: same string, but all vowels are converted to an x
    '''
    output = list(mystring)

    for i,letter in enumerate(mystring):
        for vowel in ['a','e','i','o','u']:
            if letter.lower() == vowel:
                output[i] = 'x'

    output = ''.join(output)

    return output

result = code_maker('hello') #hxllx
print(result)
