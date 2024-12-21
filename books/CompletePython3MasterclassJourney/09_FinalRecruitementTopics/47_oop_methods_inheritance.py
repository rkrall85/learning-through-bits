

class Circle():
    pi = 3.14 #class object attribute
    def __init__(self, radius=1):
        self.radius = radius

    #area methd
    def area(self):
        return self.radius * self.radius * Circle.pi

    def perimater(self):
        return 2* self.radius * Circle.pi

    def report_something(self, name):
        return 'Report {}'.format(name)

my_circle = Circle(3)
print(my_circle.radius)
print(my_circle.area())
print(my_circle.perimater())
print(my_circle.report_something('John'))


class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def report(self):
        print("I am {} {}".format(self.first_name, self.last_name))

    def hello(self):
        print("Hello!")

p = Person('James', 'Bond')
print(p.report())
print(p.hello())

#inhertiate Person class
class Agent(Person):
    def __init__(self, first_name, last_name, code_name):
        Person.__init__(self, first_name, last_name)
        self.code_name = code_name

    #over rite report methd from person class
    def report(self):
        print('Sorry I can not tell you my real name')
        print("But you can call me {}".format(self.code_name))

    def true_name(self, passcode=0):
        if passcode == 123:
            print("Correct Passcode")
            print("I am {} {}".format(self.first_name, self.last_name))
        else:
            self.report()

x = Agent(first_name='Allen', last_name='Turing', code_name='Hero')
print(x.hello())
print(x.true_name(123))
