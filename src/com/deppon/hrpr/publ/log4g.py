"""
Created on 2015年11月2日

@author: 119937
"""
import logging
import os


def logger(name='master', file=os.path.join(os.path.abspath('../log'), 'log1.txt'),
            clevel=logging.DEBUG, flevel=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
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
    logger.addHandler(sh)
    logger.addHandler(fh)
    return logger

log4g = logger()

def logger1():
    return log4g
