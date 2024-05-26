# class is a template or blueprint. It is a logical entity. No memory allocation will happen
# attributes of class are variables and methods/function.
# we call method when defined inside class
# we call function when defined independently.

class resume_template:  # No round bracket needed. it has some purpose to use
    name = "xyz"

    def func1(self, edu):
        print("education: ", edu)


print(resume_template)
# o/p <class '__main__.resume_template'>. Meaning, class without parenthesis gives the class name
print(resume_template())
# o/p <__main__.resume_template object at 0x0000022112D2EA80>. Meaning, class with parenthesis gives object reference.

# objects are real time entity where actual memory allocation will happen.
obj1 = resume_template()  # object assignment1 or creating an instance. We can create n number of object independent
# of each other
print(obj1.name)
obj1.func1("BE")
obj1.name = "pooja"
print(obj1.name)

obj2 = resume_template()  # object assignment2.
print(obj2.name)
obj2.func1("B-TECH")
obj2.name = "Ruk"
print(obj2.name)
