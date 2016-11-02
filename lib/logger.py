import logging
import os

__author__ = "H.D. 'Chip' McCullough IV"


class Logger:
    """
    Logging class that implements a simple logger to make life easier.
    """
    def __init__(self, name, out, formatting, level=logging.DEBUG):
        """
        Initialize Logger.
        :param name: getLogger
        :param out: filename
        :param formatting: Formatting string for Logger
        :param level: Level for base logger, set to DEBUG as default
        """
        self.__delLog(out)
        self.__logger = logging.getLogger(name)
        self.__logger.setLevel(level)

        fh = logging.FileHandler(os.path.join(".", "logs", out + ".log"))
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        fmt = logging.Formatter(formatting)
        fh.setFormatter(fmt)
        ch.setFormatter(fmt)
        self.__logger.addHandler(fh)
        self.__logger.addHandler(ch)

    @property
    def logger(self):
        return self.__logger

    def __delLog(self, logName):
        logPath = os.path.join(".", "logs", logName + ".log")
        if os.path.exists(logPath):
            os.remove(os.path.join(logPath))
