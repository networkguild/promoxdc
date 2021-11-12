import os
import datetime
from utils import proxmox_connection
from log import setup_logger

logger = setup_logger(__name__)

PASSWORD = os.environ.get("PASSWORD", "admin")
USERNAME = os.environ.get("USERNAME", "admin")
PROCESS_COUNT = int(os.environ.get("PROCESS_COUNT", "5"))

newcontainer = {
    "vmid": "",
    "ostemplate": "local:vztmpl/alpine-ssh.tar.gz",
    "hostname": "",
    "storage": "local",
    "memory": 512,
    "swap": 512,
    "cores": 1,
    "password": "lab123",
    "net0": "name=eth0,bridge=vmbr0,ip=192.168.163.102/24,gw=192.168.163.1",
}


async def get_containers(host: str, stats: bool):
    proxmox = proxmox_connection(host=host, user=USERNAME, password=PASSWORD)
    containers = []
    for node in proxmox.nodes.get():
        for lxc in proxmox.nodes(node["node"]).lxc.get():
            if stats:
                containers.append(lxc)
            else:
                config = proxmox.nodes(node["node"]).lxc(lxc["vmid"]).config.get()
                containers.append(config)

    return containers


async def get(arguments):
    with open(arguments.inventory) as f:
        hosts = f.read().splitlines()
        for ip in hosts:
            logger.info(f"Getting containers from node {ip}")

            vms = await get_containers(ip, False)
            for vm in vms:
                logger.info(
                    f"Container name: {vm['hostname']}, arch: {vm['arch']}\n"
                    + f"Net: {vm['net0']}\n"
                    + f"Digest: {vm['digest']}\n"
                    + f"Os: {vm['ostype']}, swap: {vm['swap']}M, memory: {vm['memory']}M"
                )


async def get_stats(arguments):
    with open(arguments.inventory) as f:
        hosts = f.read().splitlines()
        for ip in hosts:
            logger.info(f"Getting container stats from node {ip}")

            vms = await get_containers(ip, True)
            for vm in vms:
                logger.info(
                    f"Container name: {vm['name']}, id: {vm['vmid']}, "
                    f"status: {vm['status']}, uptime: {str(datetime.timedelta(seconds = vm['uptime']))}"
                )


async def create(arguments):
    pass
