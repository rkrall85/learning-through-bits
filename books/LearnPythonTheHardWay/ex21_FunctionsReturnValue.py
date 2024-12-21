



# ex21: Functions can return something
def add(a, b):
    print("adding %d - %d" %(a, b))
    return a + b

def substract(a, b):
    print("SUBTRACTING %d - %d " % (a, b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b

print("Let's do some math with just fucntions")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))


#A puzzle for the extra credit, type it in anyway
print("Here is a puzzle.")

what = add(age, substract(height, divide(weight, multiply(iq, 2))))

print("That becomes: ", what, "Cane you do it by hand?")
