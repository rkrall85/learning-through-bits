



mylist = [1,2,3]
mylist.append(4) #methods on the list
print(mylist.count(2))
print(mylist)


class Sample():
    pass

x = Sample()
print(type(x))

class Agent():
    #class object attribute
    planet = 'Earth'
    def __init__(self, f_name, l_name, eye_color, height):
        self.first_name = f_name
        self.last_name  = l_name
        self.eye_color  = eye_color
        self.height     = height


x = Agent('James','Bond','green', 175)
y = Agent('Sally','Johnson','blue', 180)
print(x.first_name)
print(x.last_name)
print(x.eye_color)
print(x.height)
print(x.planet)
print("*"*100)
print(y.first_name)
print(y.last_name)
print(y.eye_color)
print(y.height)
print(y.planet)
