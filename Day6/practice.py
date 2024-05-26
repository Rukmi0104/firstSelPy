# public, private, protected-pseudo protected
var=""
class myclass:
    var="public var"
    __var1="private var"
    _var2="Protected var"

    def mymethod(self):
        print("this is public method")
        print("accessing private attribute",self.__var1)
        self.__mymethod1()

    def __mymethod1(self):
        print("this is private method")

    def _mymethod2(self):
        print("this is protected method")


class myclass2:

    def mymethod(self):
        print("from my class 2")
        print(myclass.var)
        print(myclass._var2)

obj=myclass()
obj1=myclass2()
print(obj.var)
obj.mymethod()
print(obj._var2)
obj._mymethod2()

obj1.mymethod()


# print(obj.__var1)
# obj.__mymethod1()