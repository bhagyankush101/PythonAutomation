import inspect
import logging


class BaseTestLogger:
    def getLogger(self):
        loggername = inspect.stack()[1][3]
        filehandler = logging.FileHandler('logfile.log')
        logger = logging.getLogger(loggername)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        return logger