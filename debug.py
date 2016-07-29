# from stackoverflow
import logging
logger = logging.getLogger('root')
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] \n %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)
