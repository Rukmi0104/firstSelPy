# constructor __init__ is an instance method. No value will return.
# this is invoked at the time of object creation

class myClass:
    def __init__(self, a, b):
        print("constructor got executed", a, b)


obj1 = myClass(20, 40)
obj1.__init__(20, 30)   # this will work but not an ideal way to execute init method

# obj1 = myClass() # TypeError: myClass.__init__() missing 2 required positional arguments: 'a' and 'b'. Meaning init
# method is invoked at the time of object creation. It doesn't need to invoke separately like other user defined
# methods. So arguments should be passed during class object creation
