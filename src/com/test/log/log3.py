import logging
import os
#logging.basicConfig(filename=os.path.join(os.getcwd(),'log.txt'),\
#                    level=logging.DEBUG,filemode='w',format='%(asctime)s-%(levelname)s:%(message)s')
logger=logging.getLogger("simple_exaple.txt")
logger.setLevel(logging.DEBUG)
#建立一个filename记入日志到文件，级别为debug以上
fh=logging.FileHandler("spam.log")
fh.setLevel(logging.DEBUG)
#将日志输出到cmd控制台上，级别error以上
ch=logging.StreamHandler()
ch.setLevel(logging.ERROR)

#设置日志格式
fmt=logging.Formatter("%(asctime)s : %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(fmt)
fh.setFormatter(fmt)
logger.addHandler(ch)
logger.addHandler(fh)
#开始打印日志
logger.debug("debug message1111111111中文")
logger.info("info message22222222222中文")
logger.warn("warn message 23sdjflsdjfl")
logger.error("error message e39098209348u-234up2o34j")
logger.critical("critical message")







