# # variable in python are reference to the object in the memory. variables are container
# x = 5
# y = "john"
#
# # x and y are variables references to the objects in the memory. the integer object 5 and string object "john" is
# # stored in some memory location 0x20bfa819cc8 and x and y are the only reference to the object
# print(x)
# print(y)



# ================================ keywords in python========================
# keywords in python are the reserved words which can not be used as variable names

import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))
print(dir(keyword.kwlist))

print(dir(__builtins__))
