# taking more than one form is polymorphysm
# overload and override
#

#Overload
###########################################
# operator overload

# example 1    # + operator performs addition as well as concatenation as below
print(10+10)    #o/p 20 . meaning adds 2 numbers
print("string" + "string")  # o/p stringstring . Meaning concatenate 2 strings

# example 2     * operation performing multiplication and concatenation as below
print(10 * "string")    #o/p stringstringstringstringstringstringstringstringstringstring
print(10 * 10)           # o/p 100

###########################################
# method overload

# method overload can be done using *args parameter. with *args we can pass n number of parameters during function
# call as below


def method1(*args):
    print(args)


method1(22)         # why comma in output (22,) ??
method1(22, 44)
method1(45, 66, 5, 3)


#Override
###########################################
# method override-> when multiple methods with the same method name and variable are available then, latest method is called.
# example 1
def methodOver1(a):
    print("this is first method", a)


def methodOver1(a):
    print("this is 2nd method", a)


def methodOver1(a):
    print("this is 3rd method", a)

methodOver1(3)      #o/p this is 3rd method 3


# ########################################## example 2 method override-> when multiple methods with the same method
# name and different variable are available then, latest method is called.

def methodOver1(a):
    print("this is first method", a)


def methodOver1(b):
    print("this is 2nd method", b)


def methodOver1(c):
    print("this is 3rd method", c)


methodOver1(5)      # o/p this is 3rd method 5

