

def func():
    print("func() in one.py")

print("top level print statement in one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being in another module")
