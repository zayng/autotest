import logging
import os

class Logger():
    def __init__(self,name=os.path.join(os.path.abspath('../log'),'log.txt'),clevel=logging.DEBUG,flevel=logging.DEBUG):
        self.logger=logging.getLogger('main')
        self.logger.setLevel(logging.DEBUG)
        fmt=logging.Formatter('[%(asctime)s] %(filename)s[line:%(lineno)d] %(levelname)s %(message)s','%Y-%m-%d %H:%M:%S')
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
        
    def warn(self,msg):
        self.logger.warn(msg)
        
    def error(self,msg):
        self.logger.error(msg)
        
    def critical(self,msg):
        self.logger.critical(msg)
        
def Logger1(name=os.path.join(os.path.abspath('../log'),'log1.txt'),clevel=logging.DEBUG,flevel=logging.DEBUG):
    logger=logging.getLogger('main')
    logger.setLevel(logging.DEBUG)
    fmt=logging.Formatter('[%(asctime)s] %(filename)s[line:%(lineno)d] %(levelname)s %(message)s','%Y-%m-%d %H:%M:%S')
    #日志从控制台输出
    sh=logging.StreamHandler()
    sh.setLevel(clevel)
    sh.setFormatter(fmt)
    #日志输出到文件
    fh=logging.FileHandler(name)
    fh.setLevel(flevel)
    fh.setFormatter(fmt)
    logger.addHandler(sh)
    logger.addHandler(fh)
    return logger
                
log=Logger1()     
if __name__=='__main__':
#     log1=Logger(clevel=logging.ERROR,flevel=logging.DEBUG)
    log1=Logger1()
    log1.error("这是一个error")  
#     log1.info("一个info信息")
#     log1.debug("一个debug信息")
#     log1.warn("一个warning信息")
#     log1.error("一个error信息")
#     log1.critical("一个致命的criticl信息")