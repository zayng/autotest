import logging
import ctypes
from _winapi import STD_OUTPUT_HANDLE

FOREGROUND_WHITE=0x0007
FOREGROUND_BLUE=0x01
FOREGROUND_GREEN=0x02
FOREGROUND_RED=0x04
FOREGROUND_YELLOW=FOREGROUND_RED | FOREGROUND_GREEN

STD_OUTPUT_HANDLE=-11
std_out_handle=ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_color(color,handle=std_out_handle):
    bool=ctypes.windll.kernel32.SetConsoleTextAttribute(handle,color)
    return bool


class Logger():
    def __init__(self,name,clevel=logging.DEBUG,flevel=logging.DEBUG):
        self.logger=logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        fmt=logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s','%Y-%m-%d %H:%M:%S')
        #日志从控制台输出
        sh=logging.StreamHandler()
        sh.setLevel(clevel)
        sh.setFormatter(fmt)
        #日志输出到文件
        fh=logging.FileHandler(name)
        fh.setLevel(flevel)
        fh.setFormatter(fmt)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)
        
    def debug(self,msg):
        self.logger.debug(msg)
    
    def info(self,msg):
        self.logger.info(msg)
        
    def warn(self,msg,color=FOREGROUND_YELLOW):
        set_color(color)
        self.logger.warn(msg)
        set_color(FOREGROUND_WHITE)
        
    def error(self,msg,color=FOREGROUND_RED):
        set_color(color)
        self.logger.error(msg)
        set_color(color)
        
    def critical(self,msg):
        self.logger.critical(msg)
        
if __name__=='__main__':
    log=Logger('yx1.txt',logging.ERROR,logging.DEBUG)
    log.info("一个info信息")
    log.debug("一个debug信息")
    log.warn("一个warning信息")
    log.error("一个error信息")
    log.critical("一个致命的criticl信息")