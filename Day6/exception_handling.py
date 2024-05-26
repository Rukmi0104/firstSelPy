# error -> syntax error, indentation error
# exception -> type error, name, value error

################################
# simple program 1

# print("program 1")
# print("program 2")
# print(aa)   # NameError: name 'aa' is not defined
# here we are trying to print unknown variable which throws name error and execution is stopped. Line 9 and 10
# are not executed. To avoid such situation we can catch these exception and continue with execution.
# print("program 3")
# print("program 4")

################################
# program 2 -> catch exception with try and except block

# print("program 1")
# print("program 2")
# try:
#     print(aa)
# except Exception as msg:
#     print("exception occurred", msg)
#
# print("program 3")
# print("program 4")

################################
# Python defined error -> some error/ exceptions are predefined in python as below. these exception can be handled.

list1 = [1, 2, 3, 4]
# print(1/0) # ZeroDivisionError: division by zero
# print(10 + "string")    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(list[5])  # IndexError: list index out of range

# example 1
# try:
#     print(1/0)
#     print(10 + 'string')
#     print(list1[5])
# except ZeroDivisionError as msg:
#     print('exception occurred', msg)
# except TypeError as msg:
#     print('exception occurred', msg)
# except IndexError as msg:
#     print('exception occurred', msg)
# here first print statement is throwing error, so first except block will execute.

##########################################
# example 2

# try:
#     # print(1/0)
#     print(10 + 'string')
#     # print(list1[5])
# except ZeroDivisionError as msg:
#     print('exception occurred', msg)
#     print("type is: ", format(type(msg)))   # get type of error o/p -> type is:  <class 'TypeError'>
# except TypeError as msg:
#     print('exception occurred', msg)
#     print("type is: ", (type(msg)))   # get type of error
# except IndexError as msg:
#     print('exception occurred', msg)
#     print("type is: ", format(type(msg)))   # get type of error. o/p -> type is:  <class 'IndexError'>
# here third print statement is throwing error, so third except block for index out of bound exception will execute.
# we can get type of error by using type() or using format with type


##########################################
# example 3 -> else and finally block.
# else and finally blocks are optional.
# else block will be executed if the is no error in except block. 'finally' will always execute if given

# try:
#     print(1/0)
#     # print(10 + 'string')
#     # print(list1[5])
# except ZeroDivisionError as msg:
#     print('exception occurred', msg)
#     print("type is: ", format(type(msg)))  # get type of error o/p -> type is:  <class 'TypeError'>
# except TypeError as msg:
#     print('exception occurred', msg)
#     print("type is: ", (type(msg)))  # get type of error
# except IndexError as msg:
#     print('exception occurred', msg)
#     print("type is: ", format(type(msg)))
#
# else:
#     print("no exception occurred")
# finally:
#     print("finally block executed")


##########################################
# example 4 -> else and finally block

try:
    # print(1/0)
    # print(10 + 'string')
    # print(list1[5])
    print("this is try block")
except ZeroDivisionError as msg:
    print('exception occurred', msg)
    print("type is: ", format(type(msg)))  # get type of error o/p -> type is:  <class 'TypeError'>
except TypeError as msg:
    print('exception occurred', msg)
    print("type is: ", (type(msg)))  # get type of error
except IndexError as msg:
    print('exception occurred', msg)
    print("type is: ", format(type(msg)))

else:
    print("no exception occurred")
finally:
    print("finally block executed")

