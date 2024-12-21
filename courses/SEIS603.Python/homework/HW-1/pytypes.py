#Robert Krall
#pytypes.py

#needed to print out date type
from datetime import date



#print out as many types as possible in python
print(type('45'))                               #string
print(type(45))                                 #int
print(type(45.0))                               #float
print(type(True))                               #bool
print(type([1,2,3,4]))                          #list
print(type([[4,5,6,7],[1,2,3]]))                #list
print(type((1,2,3)))                            #tuple
print(type({'John': 12345, 'James':54321}))     #dict (dictionary)
print(type(date.today()))                       #datetime.date
print(type(None))                               #None type
