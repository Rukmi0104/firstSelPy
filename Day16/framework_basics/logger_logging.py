# logging shows documentation of status of test cases passed or failed
# there are many types of logging file we can use ex. html, xml, text file logs

'''
there are 5 levels of logging
NOTSET          0
DEBUG           10
INFO            20
WARNING         30
ERROR           40
CRITICAL        50

if we dont set any of the level then by default WARNING type will print
'''

import logging

# print(logging.getLogger())#<RootLogger root (WARNING)>
###### set level

# l = logging.getLogger()
# l.setLevel(logging.DEBUG)


# ## ============ print logger in text file ==============##
# txt_location = r"D:\SeleniumPython\Projects\FITA\pythonProject1_FITA\Day16\framework_basics\auto_logger.txt"
# logging.basicConfig(filename=txt_location,
#                     filemode="a",
#                     level=logging.DEBUG,
#                     format="%(asctime)s::%(levelname)s::%(message)s")


## ============ print logger in text file and on console ==============##
# to get data on console we have to use streamHandler
# to get data in log file we have to use fileHandler

txt_path = r"D:\SeleniumPython\Projects\FITA\pythonProject1_FITA\Day16\framework_basics\auto_logger1.txt"
# stream_handler = logging.StreamHandler()
# file_handler = logging.FileHandler(filename=txt_path, mode="a",)

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s::%(levelname)s-->%(message)s",
                    handlers=[logging.StreamHandler(), logging.FileHandler(filename=txt_path, mode="a",)])
logging.debug("this is debug log message")
logging.info("this is info log message")
logging.warning("this is warning log message")
logging.critical("this is critical log message")





