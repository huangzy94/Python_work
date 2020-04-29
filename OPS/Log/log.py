import os
import time
from logging.handlers import RotatingFileHandler
import logging
import inspect


path = os.path.join(r'D:\Python_work\OPS\Log', 'log')               # 拼接路径（r进行反斜杠转义）
print("log存放路径：", path)


handlers = {logging.DEBUG: os.path.join(path, 'debug.log'),

            logging.INFO: os.path.join(path, 'info.log'),

            logging.WARNING: os.path.join(path, 'warning.log'),

            logging.ERROR: os.path.join(path, 'error.log'),
            }


def createHandlers():
    log_levels = handlers.keys()

    for level in log_levels:
        to_path = os.path.abspath(handlers[level])
        handlers[level] = RotatingFileHandler(to_path, maxBytes=10000, backupCount=2, encoding='utf-8')


# 加载模块时创建全局变量
createHandlers()

# 将日志输出到控制台
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter()
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


class PrintLog:

    def printfNow(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    def __init__(self):
        self.__loggers = {}

        log_levels = handlers.keys()

        for level in log_levels:
            logger = logging.getLogger(str(level))

            logger.addHandler(handlers[level])

            logger.setLevel(level)

            self.__loggers.update({level: logger})

    def getLogMessage(self, level, message):
        frame, filename, lineNo, functionName, code, unknowField = inspect.stack()[2]

        '''日志格式：[时间] [类型] [记录代码] 信息'''

        return "[%s] [%s] [%s - %s - %s] %s" % (self.printfNow(), level, filename, lineNo, functionName, message)

    def info(self, message):
        message = self.getLogMessage("info", message)

        self.__loggers[logging.INFO].info(message)

    def error(self, message):
        message = self.getLogMessage("error", message)

        self.__loggers[logging.ERROR].error(message)

    def warning(self, message):
        message = self.getLogMessage("warning", message)

        self.__loggers[logging.WARNING].warning(message)

    def debug(self, message):
        message = self.getLogMessage("debug", message)

        self.__loggers[logging.DEBUG].debug(message)

    def critical(self, message):
        message = self.getLogMessage("critical", message)

        self.__loggers[logging.CRITICAL].critical(message)


if __name__ == "__main__":
    logger = PrintLog()
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
