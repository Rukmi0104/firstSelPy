# function is s set of statement
# def is a keyword and return

# def myFunc():
#     print("this is my function")


# invoke the function. Ex1
# myFunc()  # Function is invoked with parenthesis. o/p: this is my function

# invoke the function. Ex2
# func = myFunc
# func()  # function is invoked after creating object reference with parenthesis.

# Ex1 for getting reference of a function
# print(myFunc)  # When function is called without parenthesis then, it gives object reference of a function
# o/p: <function myFunc at 0x000002090BC3A2A0>
# Ex2 for getting reference of a function    # namespace
# var = myFunc  # function is invoked after creating object reference without parenthesis.
# print(var)


##################################################
# with parameter and without return
# without parameter and without return
# with parameter and with return
# without parameter and with return

#########################################3
# without parameter and without return
# def myfunc1():
#     print("this is my function")
#
#
# myfunc1()
# # or
# print(myfunc1())

############################################
# empty function or do nothing
# def myfunc2():
#     pass
#
#
# myfunc2()

###########################################
# without parameter and with return
# def addition():
#     a=3
#     b=4
#     c = 3+4
#     return a, b, c
#
#
# print(addition())       # prints values in tuple form
# print(addition()[0])
#
# # or
# tup = addition()
# print(tup[0])
# print(tup[1])
# print(tup[2])

########################################
# function with positional argument
# def addition1(a, b, c, d):
#     print(f"a is {a}, b is {b}, c is {c}, d is {d} and sum of all parameters is {a + b + c + d}")
#
#
# addition1(1, 2, 3, 4)
# addition1(1, 2, 13, 4)
# addition1(1, 2, 4, 3)
# addition1(1, 2, 3)  # TypeError: addition1() missing 1 required positional argument: 'd'
# addition1(2)    # TypeError: addition1() missing 3 required positional arguments: 'b', 'c', and 'd'

##############################################
# function with default argument
# def addition2(a, b, c=0, d=0):  # c and d are default argument
#     print(f"a is {a}, b is {b}, c is {c}, d is {d} and sum of all parameters is {a + b + c + d}")
#
#
# addition2(2, 4) # no type error for c and d as default arguments are passed in function
# addition2(2,4,3,5) # o/p a is 2, b is 4, c is 3, d is 5 and sum of all parameters is 14

# rule 1
# SyntaxError: parameter without a default follows parameter with a default #
# function with default argument in the beginning throw error
# def addition3(a=0, b=0, c, d):
#     print("this function definition is not correct")


# addition3(2,4)

###############################################
# function with keyword
# def addition(a=1, b=2, c=3, d=4):
#     print(f"addition of all parameters is {a + b + c + d}")


# addition()  # o/p addition of all parameters is 10
# OR
# addition(2, 4, c=4, d=9) # addition of all parameters is 19
# OR addition(a=4, b=4, 5, 6)    #yntaxError: positional argument follows keyword argument. Meaning, positional
# argument should be passed first and then keyword argument should be passed.

# addition(a=2, c= 4) # addition of all parameters is 12. c and d is taken from function definition.
# addition(1, a = 2, c= 5) # TypeError: addition() got multiple values for argument 'a'


################################################
################################################
# variable scope
# global and local variable at function level

# ex 1
# x = "global var"
#
# def myfunc():
#     y = "local var"
#     print(f"global variable is 'x : {x}' and local variable is 'y : {y}'")

# print(f"global variable is x : {x} and local variable is x : {y} before calling function")  # NameError: name 'y' is not defined. meaning local variable is not accessible outside the function. Its scope is limited to that function only.
# myfunc()
# print(f"global variable is x : {x} and local variable is x : {y} after calling function")  # NameError: name 'y' is not defined. meaning local variable is not accessible outside the function. Its scope is limited to that function only.

# ###################
# # ex 2
# a = "global var"
#
#
# def myfunc1():
#     a = "local var"
#     print(f"global variable is 'a : {a}' and local variable is 'a : {a}'")  # if same variable name is used inside and
#     # outside the function then, within function only local variable value is used.
#
#
# print(f"global variable is a with value : {a} and local variable is again a and value is : {a} before calling function")
# # if same variable name is used inside and # outside the function then, outside function only global variable value
# # is used before or after calling the function.
# myfunc1()
# print(f"global variable is a with value : {a} and local variable is again a and value is : {a} after calling function")
# # if same variable name is used inside and # outside the function then, outside the function only global variable
# # value is used before or after calling the function.


###################
# ex 3
# a = "global var"
#
#
# def myfunc1():
#     global a    # local variable 'a' is declared as global variable so that i can be accessed outside the function but
#     # only after calling the function
#     a = "local var"
#     print(f"global variable is 'a : {a}' and local variable is 'a : {a}'")  # if same variable name is used inside and
#     # outside the function then, within function only local variable value is used.
#
#
# print(f"global variable is a with value : {a} and local variable is again a and value is : {a} before calling function")
# # if same variable name is used inside and outside the function , but local variable is declared as global then,
# # outside function global variable value is used before calling the function and local var is used after calling the
# # function.
# myfunc1()
# print(f"global variable is a with value : {a} and local variable is again a and value is : {a} after calling function")
# # if same variable name is used inside and outside the function , but local variable is declared as global (ex.
# # global a) then, outside function global variable value is used before calling the function and local var is used
# # after calling the function.


################################
# ex 4
# a = "global var"
#
# def myfunc():
#     a = "local var"
#     global a    # "SyntaxError: name 'a' is assigned to before global declaration". Meaning declaration of global
#     # variable should be done before assigning value to variable
#     print(f"global variable is 'a : {a}' and local variable is 'a : {a}'")
#
# print(f"global variable is a : {a} and local variable is x : {a} before calling function")  # NameError: name 'y' is not defined. meaning local variable is not accessible outside the function. Its scope is limited to that function only.
# myfunc()
# print(f"global variable is a : {a} and local variable is x : {a} after calling function")  # NameError: name 'y' is not defined. meaning local variable is not accessible outside the function. Its scope is limited to that function only.


################################
# ex 5
# x = "global var"
#
# def myfunc():
#     global y
#     y = "local var"
#     print(f"global variable is 'x : {x}' outside function and global variable is 'y : {y}' within function")
#
# print(f"global variable is x : {x} outside function and global variable is y : {y} inside the function before calling function")
# # NameError: name 'y' is not defined. meaning global varibale y which is declared inside the function can be used
# # outside the function but only after calling the function.
# myfunc()
# print(f"global variable is x : {x} outside function and global variable is y : {y} inside the function after calling function")


################################
# ex 6
# x = "global var"
#
# def myfunc(y,z):
#     # global y #SyntaxError: name 'y' is parameter and global. Meaning, positional parameters defined inside function can not be declared as global.
#     a = "local var"
#     print(f"global variable is 'x : {x}' outside function and local variable is 'a : {a}' within function")
#
#
# myfunc(11,12)


##############################
# *args and **kwargs
# Ex1 of *args

# def myFunc2(*args):
#     print(args)
#
#
# myFunc2(30, 20, 40)
# o/p (30, 20, 40). Meaning we can pass n number of positional parameter values while calling a function.
# Output is in tuple form.

# Ex2. use in sum
def myfunc3(*args):
    print(args)
    sum = 0
    for i in args:
        sum = sum + i
    print(sum)
    return args

obj1 = myfunc3(5, 8, 7)
myfunc3(5, 4, 3, 6, 8, 9, 0)
print(obj1[0])

############################
# Ex1. use in sum
# def myfunc4(**kwargs):
#     print(kwargs)
#     sum1 = 0
#     for i in kwargs.values():
#         sum1 = sum1 + i
#     print(sum1)
#
#
# myfunc4(a=5, b=8)
# myfunc4(a=1, c=4, d=3, b=6)

# output is in dict form.
