# public , private and protected or pseudo protected methods and variable

class myClass:
    var1 = "public var"
    __var2 = "private var"
    _var3 = "protected var"

    def myMethod1(self):
        print("this is public method")
        print("accessing public variable: ", self.var1)
        print("accessing private variable: ", self.__var2)
        print("accessing protected variable: ", self._var3)
        myClass.__myMethod2(self)

    def __myMethod2(self):
        print("this is private method")
        print("accessing public variable: ", self.var1)
        print("accessing private variable: ", self.__var2)
        print("accessing protected variable: ", self._var3)

    def _myMethod3(self):
        print("this is protected method")
        print("accessing public variable: ", self.var1)
        print("accessing private variable: ", self.__var2)
        print("accessing protected variable: ", self._var3)


class myClass1:
    def myMethod1(self):
        print("this is function inside myClass1")


obj1 = myClass()
obj2 = myClass1()
# accessing public method outside class
obj1.myMethod1()
obj2.myMethod1()

# accessing private method outside class
# obj1.__myMethod2()
# o/p -> AttributeError: 'myClass' object has no attribute '__myMethod2'. Did you mean: 'myMethod1'?.
# meaning private method (__myMethod2) can not be called individually outside the class. if you want to use it then,
# we can call it inside another public method (myMethod1) within same class and use that function.

# accessing protected method outside class
obj1._myMethod3()

# accessing public variable
print(obj1.var1)  # o/p -> public var

# accessing protected var
print(obj1._var3)  # o/p -> protected var

# accessing private variable
# print(obj1.__var2)
# print(myClass.__var2)
# AttributeError: 'myClass' object has no attribute '__var2'. Did you mean: '_var3'?
# meaning private variables can not access outside the class.


