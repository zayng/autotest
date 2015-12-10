import logging

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
        
    def warn(self,msg):
        self.logger.warn(msg)
        
    def error(self,msg):
        self.logger.error(msg)
        
    def critical(self,msg):
        self.logger.critical(msg)
        
if __name__=='__main__':
    log=Logger('yx.txt',logging.ERROR,logging.DEBUG)
    log.info("一个info信息")
    log.debug("一个debug信息")
    log.warn("一个warning信息")
    log.error("一个error信息")
    log.critical("一个致命的criticl信息")