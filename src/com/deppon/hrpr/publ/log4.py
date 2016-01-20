"""
Created on 2015年11月2日

@author: 119937
"""
import logging
import os


class Logger(object):
    """自定义日志类，用于记录自动化测试运行日志"""

    def __init__(self, name=os.path.join(os.path.abspath('../log'), 'log.txt'), clevel=logging.DEBUG,
                 flevel=logging.DEBUG):
        self.logger = logging.getLogger('main')
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                                '%Y-%m-%d %H:%M:%S')
        # 日志从控制台输出
        sh = logging.StreamHandler()
        sh.setLevel(clevel)
        sh.setFormatter(fmt)
        # 日志输出到文件
        fh = logging.FileHandler(name)
        fh.setLevel(flevel)
        fh.setFormatter(fmt)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warn(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

    def get_log(self):
        return self.logger


def logger1(name=os.path.join(os.path.abspath('../log'), 'log1.txt'), clevel=logging.DEBUG, flevel=logging.DEBUG):
    logger = logging.getLogger('brunch')
    logger.setLevel(logging.DEBUG)
    fmt = logging.Formatter('[%(asctime)s] %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            '%Y-%m-%d %H:%M:%S')
    # 日志从控制台输出
    sh = logging.StreamHandler()
    sh.setLevel(clevel)
    sh.setFormatter(fmt)

    # 日志输出到文件
    fh = logging.FileHandler(name)
    fh.setLevel(flevel)
    fh.setFormatter(fmt)
    logger.addHandler(sh)
    logger.addHandler(fh)
    return logger


logger = Logger()
log4 = logger.get_log()

if __name__ == '__main__':
    log2 = Logger().get_log()
    log2.info("一个info信息")
    log2.debug("一个debug信息")
    log2.warn("一个warning信息")
    log2.error("一个error信息")
    log2.critical("一个致命的criticl信息")

    log1 = logger1()
    log1.debug("一个debug信息")
    log1.info("一个info信息")
    log1.warn("一个warning信息")
    log1.error("一个error信息")
    log1.critical("一个致命的criticl信息")
