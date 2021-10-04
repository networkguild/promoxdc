import os
import logging
import sys
from multiprocessing import Pool
from functools import partial
import argparse
from proxmox import get_containers
from utils import get_logger

PROCESS_COUNT = int(os.environ.get('PROCESS_COUNT', '5'))
_HERE = os.path.dirname(__file__)
custom_logger = get_logger()


def get_vms(argument):
    custom_logger.info(f'Getting virtual machines from node {argument.host}')
    vms = get_containers.get_containers(argument.host, argument.user)
    for vm in vms:
        custom_logger.info(f"{vm['vmid']}, {vm['name']}, {vm['status']}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--ssh-config', help='Path to SSH -config')

    action = parser.add_mutually_exclusive_group()
    action.add_argument('-c', '--create', action='store_true', help='Create new container', default=False)
    action.add_argument('-g', '--get', action='store_true' ,help='Get container by vdi', default=False)

    edit_args = parser.add_argument_group()
    edit_args.add_argument('-f', '--file', help='Config xml', required=False)
    edit_args.add_argument('-i', '--inventory', help='Inventory file', required=False)

    get_args = parser.add_argument_group()
    get_args.add_argument('--host', help='Host hostname:[port]')
    get_args.add_argument('--user', default='admin', help='Proxmox node username')

    args = parser.parse_args()

    if args.get:
        if not(args.host and args.user):
            custom_logger.warning('Host not defined!')
            exit()
        get_vms(args)

