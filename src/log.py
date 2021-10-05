import sys
import logging
import logging.handlers
from multiprocessing import Queue

log_msg_queue = Queue()
LOG_FORMAT = '%(levelname)s: %(message)s'
DATE_FORMAT = '%d/%b/%Y %H:%M'


def setup_logger(name: str):
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)
    logger = logging.getLogger(name)
    return logger
