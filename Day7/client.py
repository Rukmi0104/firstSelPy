# approach 1

# import module1
# import module2
#
# module1.func1()
# module1.func2()
#
# module2.func3()
# module2.func4()


# approach 2
# from module1 import *   # using * wildcard all functions inside module1 can be accessed
# from module2 import *   # using * wildcard all functions inside module2 can be accessed
#
# func1()
# func3()
# func4()
# func2()


# approach 3
# from module1 import func1, func2, func   # explicitly mention function name which need to access
# from module2 import func3, func4, func  # explicitly mention function name which need to access
#
# func1()
# func3()
# func4()
# func2()
# func()      # this common function will be used from latest import file. In this example it will take from module2

# approach 4
# if we want to access common functions from both files then use module name. Example below

# import module2
# import module1
# module2.func()
# module1.func()


####################################################################
# modules with class
####################################################################
# approach1

import module1
import module2

# access instance method
# obj1 = module1.A()
# obj2 = module2.B()
#
# obj1.method()
# obj1.method1()
# obj2.method2()
# obj2.method()
# obj1.staticMethod()
# obj1.classMethod()

####################################################################
# approach2
# from module1 import A
# from module2 import B
#
# obj1 = A()
# obj2 = B()
#
# obj1.method()
# obj1.method1()
# obj2.method2()
# obj2.method()
# obj1.staticMethod()
# obj1.classMethod()
# # OR
# A.classMethod()
# A.staticMethod()
####################################################################
# approach 3

from module1 import *
from module2 import *

# module1.func()
# module1.func2()


####################################################################
# if same class name is present in both modules
# import module1
# import module2
#
# obj1 = module1.C()
# obj2 = module2.C()
# obj1.method1()
# obj2.method1()

####################################################################
# if same class name is present in both modules
# approach 1
# import module1
# import module2
#
# obj1 = module1.C()
# obj2 = module2.C()
# obj1.method1()
# obj2.method1()


####################################################################
# if same class name is present in both modules
# approach 2

# from module1 import C, A
# from module2 import C, B
#
# obj1 = C()
# obj1.method1()


####################################################################
# Packages -> package collection of modules
####################################################################

from package1.module2 import *
from package1.module1 import *

module2.C()
module1.A()

