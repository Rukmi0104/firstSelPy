import logging
import datetime


## logging with append
def log_logger_as_append():
    log_file_path = r"D:\SeleniumPython\Projects\FITA\pythonProject1_FITA\hybrid_framework\logs\log.txt"
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s::%(levelname)s-->%(message)s",
                        handlers=[logging.StreamHandler(), logging.FileHandler(filename=log_file_path, mode="a")],
                        force=True)
    return logging


# logging with write


# def log_logger_as_write():
#     dt = datetime.datetime.now()
#     formatted_dt = dt.strftime('%d-%m-%Y-%H-%M-%S')
#     log_file_path = fr"D:\SeleniumPython\Projects\FITA\pythonProject1_FITA\hybrid_framework\logs\log_{formatted_dt}.txt"
#     logging.basicConfig(level=logging.INFO,
#                         format="%(asctime)s::%(levelname)s-->%(message)s",
#                         handlers=[logging.StreamHandler(), logging.FileHandler(filename=log_file_path, mode="w")],
#                         force=True)
#     return logging
