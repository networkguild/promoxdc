import os

from utils import proxmox_connection

PASSWORD = os.environ.get('PASSWORD', 'admin')


def get_containers(host: str, username: str):
    proxmox = proxmox_connection(host=host, user=username, password=PASSWORD)
    vms = []
    for node in proxmox.nodes.get():
        for vm in proxmox.get('nodes/%s/openvz' % node['node']):
            vms.append(vm)

    return vms
