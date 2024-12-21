#Robert Krall
#eval2.py

'''
    #order of operators#
        ()              paranthese
        **              exponentiation
        -x              nagation
        *, /, //, %	    multiplication, real and integer division, remainder
        +,-             addition,subtraction
'''

python_answer = 1.0+2.0*5**6**2%3-4//47 #math formula from htt

#excuting based on order of operator rules
robert_answer  = 5**6                           #15625
robert_answer = robert_answer ** 2              #244140625
robert_answer = 2.0 * robert_answer             #488281250.0
robert_answer = robert_answer % 3               #2.0
robert_answere = 4 // 47                        #2.0
robert_answer = 1.0 + robert_answer             #3.0
robert_answer = robert_answer - robert_answere  #3.0

#output both result sets
print('Python solution: ' , python_answer) #3.0
print('Robert solution: ' , robert_answer) #3.0
