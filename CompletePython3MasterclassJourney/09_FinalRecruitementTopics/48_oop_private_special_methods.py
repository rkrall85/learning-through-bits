

class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def report(self):
        print("I am {} {}".format(self.first_name, self.last_name))

    def hello(self):
        print("Hello!")

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
    #guide user from not using thism metho but they still could.
    #not shown in auto complete unless you type in _
    def _private_method(self):
        print("private method")

a = Agent(first_name='Alan', last_name='Turing', code_name='Hero')
#print(a.report())
print(a.first_name)
print(a._private_method())


class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    #special methods
    def __str__(self):
        return 'Title is {} and Author is {}'.format(self.title, self.author)
    def __len__(self):
        return self.pages
    def __del__(self):
        print('a book has been deleted')

b = Book('Python Rocks', 'James Bond', 200)
print(b) #calls  __str__
print(len(b)) #calls __len__
del b #calls __del__ and removes the book

print(b)
