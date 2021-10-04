from proxmoxer import ProxmoxAPI
import logging
import sys

LOG_FORMAT = '[%(levelname)s %(asctime)s %(filename)s:%(lineno)d]: %(message)s'
DATE_FORMAT = '%d/%b/%Y %H:%M'


def proxmox_connection(host, user, password):

    return ProxmoxAPI(
        host=host,
        user=user,
        password=password,
        verify_ssl=False,
        service='PVE'
    )


def get_logger():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)
    logger = logging.getLogger(__name__)
    return logger
