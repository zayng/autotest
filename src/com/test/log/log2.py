import logging
import os
logging.basicConfig(filename=os.path.join(os.getcwd(),'log.txt'),\
                    level=logging.DEBUG,filemode='w',format='%(asctime)s-%(levelname)s:%(message)s')
