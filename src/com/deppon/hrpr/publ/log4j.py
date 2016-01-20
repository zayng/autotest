"""
Created on 2015年11月2日

@author: 119937
"""
import logging
import os


class Logger(object):
    """自定义日志类，用于记录自动化测试运行日志"""

    def __init__(self, name='main', file=os.path.join(os.path.abspath('../log'), 'log.txt'), clevel=logging.DEBUG,
                 flevel=logging.DEBUG):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                                '%Y-%m-%d %H:%M:%S')
        # 日志从控制台输出
        sh = logging.StreamHandler()
        sh.setLevel(clevel)
        sh.setFormatter(fmt)
        # 日志输出到文件
        fh = logging.FileHandler(file)
        fh.setLevel(flevel)
        fh.setFormatter(fmt)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def get_log(self):
        return self.logger

logger = Logger()
log4 = logger.get_log()

def logger1():
    return log4
