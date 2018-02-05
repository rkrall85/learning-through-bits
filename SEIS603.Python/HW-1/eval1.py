#Robert Krall
#eval1.py

'''
    #order of operators#
        ()              paranthese
        **              exponentiation
        -x              nagation
        *, /, //, %	    multiplication, real and integer division, remainder
        +,-             addition,subtraction
'''

python_answer = 2 + (3 - 1) * 10 / 5 * (2 + 3) #math formula from htt


#vars for paranthese
robert_par1 = (3-1) #2
robert_par2 = (2+3) #5

#excuting based on order of operator rules
robert_answer = robert_par1 * 10                #20
robert_answer = float(robert_answer / 5)        #4.0
robert_answer  = robert_answer * robert_par2    #20.0
robert_answer = 2 + robert_answer               #22.0

#output both result sets
print('Python solution: ' , python_answer) #22.0
print('Robert solution: ' , robert_answer) #22.0
