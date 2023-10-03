import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        # logger.debug("A debug statement is executed")
        # logger.info("Information statement")
        # logger.debug("A debug statement is executed")
        # logger.warning("Something is in warning mode")
        # logger.error("A Major error has happened")
        # logger.critical("Critical issue")
        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until((By.LINK_TEXT, text))
