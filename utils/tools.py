import logging
import datetime
import os


def create_logger(log_path, log_level=logging.DEBUG):
    logger = logging.getLogger()
    logger.setLevel(log_level)

    path = os.path.normpath(log_path + "/Log/")
    if not os.path.isdir(path):
        os.mkdir(path)

    file_handler = logging.FileHandler(os.path.normpath(path + f"/{datetime.datetime.today().date()}.log"))

    formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
