import json
import pandas as pd
import os
import datetime
from utils.tools import create_logger


global log
# TODO File Setup


# TODO Robot Initializer
def robot_initializer():
    global log
    log = create_logger(os.getcwd())


# TODO Robot Finisher
def robot_finisher(success: bool):
    pass


if __name__ == "__main__":
    robot_initializer()

    robot_finisher(True)
