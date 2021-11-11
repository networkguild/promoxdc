import os
import argparse
from proxmox import get_containers
from log import setup_logger
import pyfiglet

VERSION = os.environ.get('VERSION_NUMBER', '1.0-SNAPSHOT')

figlet = pyfiglet.figlet_format('LXC Proxy', font='slant')
banner = f'{figlet}Version: {VERSION}\n'
print(banner)

PROCESS_COUNT = int(os.environ.get('PROCESS_COUNT', '5'))
_HERE = os.path.dirname(__file__)
logger = setup_logger(__name__)


def get_vms(argument):
    logger.info(f'Getting virtual machines from node {argument.host}')
    vms = get_containers.get_containers(argument.host, argument.user)
    for vm in vms:
        logger.info(f"{vm['vmid']}, {vm['name']}, {vm['status']}")


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
            logger.warning('Host not defined!')
            exit()
        get_vms(args)

