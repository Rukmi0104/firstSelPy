# errors can be defined by user

###########
# Using Raise
##########################################
# Ex.1 simple
# n = 2003
# if n % 4 == 0:
#     print(n, " is a leap year")
# else:
#    raise ImportError(n, " is not a leap year")

# o/p -> ImportError: (2003, ' is not a leap year'). In above example once exception occured execution is stopped.
# so we can use try except to continue with execution as below

#######################
# Ex.2 with try except block
# try:
#     n = 2003
#     if n % 4 == 0:
#         print(n, " is a leap year")
#     else:
#         raise ImportError(n, " is not a leap year") # -> this is user defined error message
# except Exception as msg:
#     print("exception handled ", msg)


###########
# Using assert
##########################################
# Ex.1 simple
# n = 2003
# assert n % 4 == 0, "Not a Leap Year"    # -> this is user defined error message
# print(n, " leap year")
# o/p -> AssertionError: Not a Leap Year.

##########################################
# Ex.2 with try except block

try:
    n = 2003
    assert n % 4 == 0, "not a leap year"
    print(n, " is a leap year")
except Exception as msg:
    print("Exception handled, ", msg)

