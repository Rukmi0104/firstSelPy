# Modules are collection of functions and classes

def func1():
    print("this is func1 inside module1")


def func2():
    print("this is func2 inside module1")


def func():
    print("this is common function func from module1")


class A:
    def method1(self):
        print("this is method1 from class A")

    def method(self):
        print("this is method from class A")

    @classmethod
    def classMethod(cls):
        print("this is classMethod from class A")

    @staticmethod
    def staticMethod():
        print("this is staticMethod from class A")


class C:
    def method1(self):
        print("this is method1 from class C module1")
