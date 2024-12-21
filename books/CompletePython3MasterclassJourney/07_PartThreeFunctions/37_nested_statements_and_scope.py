


x = 'outside'
def report():
    x = 'inside'
    return x

print(report())

print(x)

# local
# enclosing
# global
# built in



#local scope example
def report():
    x = 'local scope'
    print(x)

report()

x = 'this is global level'
def enclosing():
    #x = 'enclosing level'
    def inside():
        print(x)

    inside()

enclosing()
