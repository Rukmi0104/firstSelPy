# # Numbers
# # there are 3 numeric data types in python. int, float, complex
#
# a = 10
# b = 20.4
# c = 5 + 3j
#
# print(type(a))  # <class 'int'>
# print(type(b))  # <class 'float'>
# print(type(c))  # <class 'complex'>
#
# # integer
# x = 11
# y = 333333333333333343546456
# z = -24234345
# print(type(x))  # <class 'int'>
# print(type(y))  # <class 'int'>
# print(type(z))  # <class 'int'>
#
# # float
# d = 22.2
# e = 333336456456.56756757
# f = -34.65
# g = 3e456
# h = 45E677
# i = -56.9e9809
# print(type(d))  # <class 'float'>
# print(type(e))  # <class 'float'>
# print(type(f))  # <class 'float'>
# print(type(g))  # <class 'float'>
# print(type(h))  # <class 'float'>
# print(type(i))  # <class 'float'>
# print(g)
# print(h)
# print(i)
#
# # type casting
# # cast to an integer
#
# j = int(2.4)
# k = int(2.9)
# l = int("55")
# print("float is converted to int and value is ", j)  # 2
# print("float is converted to int and value is ", k)  # 2
# print("string is converted to int and value is ", l)  # 55
#
# # casting to float
# m = float(33)
# n = float("3")
# o = float("4.6")
# print("int is converted into float and value is ", m)  # 33.0
# print("string is converted into float and value is ", n)  # 3.0
# print("string is converted into float and value is ", o)  # 4.6
#
# # casting to string
# p = str(3)
# q = str(333.5444)
# r = str("s1")
# print("int is converted into string and value is ", p)  # 3
# print("float is converted into string and value is ", q)  # 333.5444
# print("string is converted into string and value is ", r)  # s1
# print(type(p))
#
# # string to number
#
# s = "10"
# t = "22.44"
# u = "hello"
# print(type(s))
# print(type(t))
# print(type(u))
# num1 = int(s)
# print(num1)
# print(type(num1))
#
# num2 = int(22.44)
# print(num2)
# print(type(num2))
#
# num3 = int(u)  # ValueError: invalid literal for int() with base 10: 'hello'
# print(type(num3))

# ord() and chr()
# ord() is use to convert char to ascii value
# this is applicable only for char data. For string datatype it will not work.

# ascii_value = ord("a")
# print(ascii_value)
# print(type(ascii_value))
#
# # OR
# b = "string"
# # print(ord(b))       # TypeError: ord() expected a character, but string of length 6 found
# print(type(b))
#
# print(chr(97))  # a is a chr for ascii value 97


