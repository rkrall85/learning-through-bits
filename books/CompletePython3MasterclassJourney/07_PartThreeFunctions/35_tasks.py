


#task 1
def check_ten(n1,n2):
    '''
    Create a function that takes in two integers
        and returns True if their sum is 10,
        False if their sum is something else.
    '''
    '''
    if n1+n2 ==10: return True
    else: return False
    '''
    #book solution
    return (n1+n2 == 10)


print("task 1")
print(check_ten(10,0))
print(check_ten(5,5))
print(check_ten(2,7))
print("*"*100)

#task 2
def check_ten_sum(n1,n2):
    '''
    Create a function that takes in two integers
        and returns True if their sum is 10,
        otherwise, return the actual sum value.
    '''
    if n1+n2 ==10:
        return True
    else:
        return n1+n2

print("task 2")
print(check_ten_sum(10,0))
print(check_ten_sum(2,7))
print("*"*100)

#task 3
def first_upper(mystring):
    '''
    Create a function that takes in a string
        and returns back the first character of that string in upper case.
    '''
    #return mystring[:1].upper()
    #book solution
    return mystring[0].upper()

print("task 3")
print(first_upper('hello'))
print(first_upper('agent'))
print("*"*100)

#task 4
def last_two(mystring):
    '''
    Create a function that takes in a string
        and returns the last two characters.
        If there are less than two chracters, return the string: "Error"
    '''
    if len(mystring) < 2:
        return 'Error'
    else:
        return mystring[-2:]

print("task 4")
print(last_two('hello'))
print(last_two('hi'))
print(last_two('a'))
print("*"*100)

#task 5
def seq_check(nums):
    '''
    Given a list of integers,
        return True if the sequence [1,2,3] is somewhere in the list.
        Hint: Use slicing and a for loop.
    '''
    #if set([1,2,3]).issubset(set(nums)): return True
    #else: return False
    #book solution
    for i in range(len(nums)-2):
        #chck for sets of three for 1,2,3
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False

print("task 5")
print(seq_check([1,2,3]))
print(seq_check([7,7,7,1,2,3,7,7,7]))
print(seq_check([3,2,1,3,2,1,1,1,2,2,3,3,3]))
print("*"*100)


#task 6
def compare_lens(s1, s2):
    '''
    Given a 2 strings,
        create a function that returns the difference in length between them.
        This difference in length should always be a positive number (or just 0).
        Hint: Absolute Value.
    '''
    return abs(len(s1)-len(s2))

print("task 6")
print(compare_lens('aa','aa'))
print(compare_lens('a','bb'))
print(compare_lens('bb','a'))
print("*"*100)

#task 7
def sum_or_max(mylist):
    '''
    Given a list of integers,
        if the length of the list is an even number,
            return the sum of the list.
        If the length of the list is odd,
            return the max value in that list.
    '''
    if len(mylist)%2 ==0:   return sum(mylist)
    else:                   return max(mylist)

print("task 7")
print(sum_or_max([1,2,3]))
print(sum_or_max([0,1,2,3]))
print("*"*100)

#task 8
def replace_and_switch(name):
    '''
    Agents in the field sometimes need to speak in code.
        Create a function that takes in a string name (e.g. "James", "Cindy", etc...)
            and replaces all vowels with the letter x.

            For our purposes, consider these letters as vowels: [a,e,i,o,u]).
            Then switch the position of the first and last letters.

    This task is challenging,
    break it down into multiple pieces.
    '''
    '''
    output = list(name)

    for i,letter in enumerate(name):
        for vowel in ['a','e','i','o','u']:
            if letter.lower() == vowel:
                output[i] = 'x'

    output = ''.join(output)
    output = output[-1:] + output[1:-1] + output[:1]
    return output
    '''
    #book solution
    output = list(range(len(name)))

    for i, letter in enumerate(name):
        if letter.lower() in ['a','e','i','o','u']:
            output[i] = 'x'
        else:
            output[i] = letter
    #now swtich first and last letters
    last = output[-1]
    first = output[0]
    output[0] = last
    output[-1] = first

    #join back togther into a string
    return ''.join(output)


print("Task 8")
print(replace_and_switch("James"))
print(replace_and_switch("Cindy"))
print(replace_and_switch("Alfred"))
print("*"*100)
