# instance method
# class method
# static method

###################################
# instance method
class myClass:
    def func1(self, a, b):
        print(self) # o/p <__main__.myClass object at 0x000001958B63E420>. Meaning, 'self' gives object of class
        print("this is an instance method func1", a, b)


obj1 = myClass()    # class instantiation
print(obj1)
obj1.func1(20, 40)
# # self is a default parameter which should not be passed here. object as a first parameter is passed with self
myClass.func1(5,7, 7)  # if function is directly called with class then all 3 parameter should be passed.
myClass.func1(5, 7) # o/p TypeError: myClass.func1() missing 1 required positional argument: 'b'

obj2 = myClass  # class assigning
print(obj2)     # o/p <class '__main__.myClass'>. Meaning, it gives class name
obj2.func1(30, 50, 70)
myClass.func1(3, 6,8)
# # value 30 is assigned to 'self', 50 to 'a' and 70 to 'b'
#
# obj2.func1(30, 40)
#     # o/p TypeError: myClass.func1() missing 1 required positional argument: 'b'


############################################
# class method
############################################
# class myClass1:
#     @classmethod
#     def func1(cls, c, d):
#         print(cls)  # o/p <class '__main__.myClass1'>  . Meaning, it gives class name
#         print("this is class method func1", c, d)
#
#
# # obj3 = myClass1()
# # print(obj3) # <__main__.myClass1 object at 0x000001C7E2ECDDC0>. Meaning, 'cls' gives object of class
# # obj3.func1(4, 6)    # passes class name as first parameter
#
# obj4 = myClass1
# print(obj4) # o/p <class '__main__.myClass1'>. meaning, this gives class name
# obj4.func1(2, 4)    # passes class name as first parameter
# # OR
# myClass1.func1(3,6)
#
# # obj4.func1(3,5, 6)
# # TypeError: myClass1.func1() takes 3 positional arguments but 4 were given

