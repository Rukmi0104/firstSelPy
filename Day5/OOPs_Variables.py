# global/local/class/instance variables

############################################
# instance method
############################################
# var1 = "global var"
#
#
# class myClass:
#     var2 = "class var"
#
#     def func1(self):  # this is instance method
#         var3 = "local var"
#         self.var4 = "local var converted to class var"
#         print(f"global variable accessed inside function is '{var1}'")
#         print(f"class variable accessed inside function using self keyword is '{self.var2}'")
#         print(f"class variable accessed inside function using class name is '{myClass.var2}'")
#         print(f"local variable is '{var3}'")
#         print(f"local variable converted to class variable is '{self.var4}'")
#         return var3
#
#     def func2(self):
#         var5 = "local var in func2"
#         print(self.var4)
#         # local variable inside one function which is converted to class variable using self keyword can be used in
#         # other methods also.
#
#         print(var5)
#
#
# print("print statement before object creation and outside class")
# obj1 = myClass()
# obj1.func1()
#
# print("print statement after object creation and outside class")
# print(obj1.var4)  # class variable can be accessed using object
# print(obj1.var2)  # class variable can be accessed using object
# print(myClass.var2)  # class variable can be accessed using class name
# obj1.var2 = "class var changed" # class variable can be changed using object
# myClass.var2 = "class var changes 123"  # class var can be changed using class name
# print(myClass.var2)     # class variable changed using object and using class name are independent.
# print(obj1.var2)    # class variable changed using object and using class name are independent.
#
# print(obj1.func1())   # this statement is printing as None.. why?????
#
# # print(obj1.var1)
# # AttributeError: 'myClass' object has no attribute 'var1'. Did you mean: 'var2'?. Meaning,
# # global variable can not be accessed using class object.
#
# obj1.func2()


############################################
# var = "global var"
#
#
# class myClass:
#     var = "class var"
#
#     def func1(self):  # this is instance method
#         var = "local var"
#         # print(f"global variable accessed inside function is ", globals()['var'])
#         # print(f"class variable accessed inside function using self keyword is '{self.var}'")
#         # print(f"class variable accessed inside function using class name is '{myClass.var}'")
#         # print(f"local variable is '{var}'")
#
#
# print("print statement before object creation and outside class")
# obj1 = myClass()
# obj1.func1()
#
# print("print statement after object creation and outside class")
# print(obj1.var)  # this gives class variable
# print(myClass.var)  # this gives class variable
# obj1.var = "class var changed" # class var will be changed
# myClass.var = "class var changes 123"  # class var is changed
# print(myClass.var)     # class variable changed using object and using class name are independent.
# print(obj1.var)    # class variable changed using object and using class name are independent.


############################################
# class method
# ############################################
# var1 = "global var"
#
#
# class myClass:
#     var2 = "class var"
#
#     @classmethod
#     def func1(cls):  # this is instance method
#         var3 = "local var"
#         cls.var4 = "local var converted to class var"
#         print(f"global variable accessed inside function is '{var1}'")
#         print(f"class variable accessed inside function using cls keyword is '{cls.var2}'")
#         print(f"class variable accessed inside function using class name is '{myClass.var2}'")
#         print(f"local variable is '{var3}'")
#         print(f"local variable converted to class variable is '{cls.var4}'")
#         return var3
#
#
# print("print statement before object creation and outside class")
# obj1 = myClass()
# obj1.func1()
# print("print statement after object creation and outside class")
# obj1.var2 = "class var changed using object"
# myClass.var2 = "class var changed using class name"
# print(obj1.var2)
# print(myClass.var2)


# local_var1 = obj1.func1()
# print(local_var1)   # output will be 'None' if method 'func1()' does not return anything


############################################
# var = "global var"
#
#
# class myClass:
#     var = "class var"
#
#     @classmethod
#     def func1(cls):  # this is instance method
#         var = "local var"
#         print(f"global variable accessed inside function is", globals()['var'])
#         print(f"class variable accessed inside function using cls keyword is '{cls.var}'")
#         print(f"class variable accessed inside function using class name is '{myClass.var}'")
#         print(f"local variable is '{var}'")
#         return var
#
#
# # print("print statement before object creation and outside class")
# obj1 = myClass()
# obj1.func1()
# # print("print statement after object creation and outside class")
# obj1.var = "class var changed using object"
# myClass.var = "class var changed using class name"
# print(obj1.var)
# print(myClass.var)
#
# local_meth = obj1.func1()
# print(local_meth)


############################################
# static method
# ############################################
# var1 = "global var"
#
#
# class myClass:
#     var2 = "class var"
#
#     @staticmethod
#     def func1():  # this is instance method
#         var3 = "local var"
#         print(f"global variable accessed inside function is '{var1}'")
#         print(f"class variable accessed inside function using class name is '{myClass.var2}'")
#         print(f"local variable is '{var3}'")
#         return var3
#
#
# # print("print statement before object creation and outside class")
# obj1 = myClass()
# obj1.func1()
# # print("print statement after object creation and outside class")
# obj1.var2 = "class var changed using object"
# myClass.var2 = "class var changed using class name"
# print(obj1.var2)
# print(myClass.var2)
#
# obj1.func1()


# ############################################
var = "global var"


class myClass:
    var = "class var"

    @staticmethod
    def func1():  # this is instance method
        var = "local var"
        print(f"global variable accessed inside function is", globals()['var'])
        print(f"class variable accessed inside function using class name is '{myClass.var}'")
        print(f"local variable is '{var}'")
        return var


# print("print statement before object creation and outside class")
obj1 = myClass()
obj1.func1()
# # print("print statement after object creation and outside class")
obj1.var = "class var changed using object"
myClass.var = "class var changed using class name"
print(obj1.var)
print(myClass.var)

obj1.func1()