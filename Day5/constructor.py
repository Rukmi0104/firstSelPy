# __init__ is a instance method. no value will get return.
# init constructor get invoked at the time of object creation.


#########################################################
# # init with instance method
# ######################################
# class myClass:
#     def __init__(self, a, b):     # a and b are the instance variable which are bounded to constructor only
#         self.classA = a
#         self.classB = b
#         print("init constructor got executed and instance variables are", a, b)
#         print("init constructor got executed and class variables are", self.classA, self.classB)
#
#     def func1(self):
#         print(self.classA, self.classB)
#
#     def func2(self):
#         print(self.classA, self.classB)
#
#
# obj1 = myClass(2, 5)
# obj1.func1()
# obj1.func2()
#
# obj2 = myClass(44, 55)
# obj2.func1()
# obj2.func2()


# init with class and static methods
######################################
class myClass:
    def __init__(self, a, b):
        # self.classA = a   # in class and static method class variables can not be access with self keyword. it gives "AttributeError: type object 'myClass' has no attribute 'classA'" error as in line 42
        # self.classB = b    # in class and static method class variables can not be access with self keyword. it gives "AttributeError: type object 'myClass' has no attribute 'classA'" error as in line 42
        myClass.a = a  # in class and static method class variables can be access with class name only.
        myClass.b = b  # in class and static method class variables can be access with class name only.

        print("init constructor got executed and instance variables are", a, b)
        print("init constructor got executed and class variables are", self.a, self.b)

    @classmethod
    def func1(cls):
        # print(cls.a, cls.b)   # AttributeError: type object 'myClass' has no attribute 'a'
        print(cls.a, cls.b)
        print(myClass.a, myClass.b)

    @staticmethod
    def func2():
        print(myClass.a, myClass.b)


obj1 = myClass(2, 5)
obj1.func1()
obj1.func2()

