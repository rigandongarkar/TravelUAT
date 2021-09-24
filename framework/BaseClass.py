import inspect
import logging

import pytest


@pytest.mark.usefixtures("setup")
class Base_Class:

    def getlogger(self):

        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler("C:\\Users\\rigan\\PycharmProjects\\travelTest\\Misc\\logs.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger