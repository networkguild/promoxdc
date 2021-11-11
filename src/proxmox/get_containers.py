import os

from src.utils import proxmox_connection
from src.log import setup_logger

logger = setup_logger(__name__)

PASSWORD = os.environ.get('PASSWORD', 'admin')


def get_containers(host: str, username: str):
    proxmox = proxmox_connection(host=host, user=username, password=PASSWORD)
    vms = []
    for node in proxmox.nodes.get():
        for lxc in proxmox.nodes(node['node']).lxc.get():
            config = proxmox.nodes(node['node']).lxc(lxc["vmid"]).config.get()
            vms.append(lxc)
            logger.info(config)

    return vms
