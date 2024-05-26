# constuctor --- __init__---instance method---no value will get return
# invoked at the time of object craetion

# class myclass:
#     def __init__(self,a,b):# instance variable a b
#         self.a=a
#         self.b=b
#         print("constuctor got executed", a, b)
#
#
#     def func1(self):
#         print(self.a,self.b)
#
#     def func2(self):
#         print(self.a, self.b)
#
#
# obj1=myclass(1,2)
# obj1.func1()
# obj1.func2()
#
# #
# obj2=myclass(20,33)
# obj2.func1()
# obj2.func2()
# obj3=myclass(44,33)

################################################diff ways

class myclass:
    def __init__(self,a,b):# instance variable a b
        myclass.a=a
        myclass.b=b
        print("constuctor got executed", a, b)

    @classmethod
    def func1(cls):
        # print(cls.a,cls.b)#AttributeError: type object 'myclass' has no attribute 'a'
        print(cls.a,cls.b)
    @staticmethod
    def func2():
        # print(myclass.a, myclass.b)#AttributeError: type object 'myclass' has no attribute 'a'
        print(myclass.a, myclass.b)


obj1=myclass(1,2)
obj1.func1()
obj1.func2()