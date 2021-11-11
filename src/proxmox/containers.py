import os
import asyncio
from utils import proxmox_connection
from log import setup_logger

logger = setup_logger(__name__)

PASSWORD = os.environ.get("PASSWORD", "admin")
USERNAME = os.environ.get("USERNAME", "admin")
PROCESS_COUNT = int(os.environ.get("PROCESS_COUNT", "5"))


async def get_containers(host: str):
    proxmox = proxmox_connection(host=host, user=USERNAME, password=PASSWORD)
    containers = []
    for node in proxmox.nodes.get():
        for lxc in proxmox.nodes(node["node"]).lxc.get():
            config = proxmox.nodes(node["node"]).lxc(lxc["vmid"]).config.get()
            logger.info(config)
            logger.info(lxc)
            containers.append(config)

    return containers


def get(arguments):
    with open(arguments.inventory) as f:
        hosts = f.read().splitlines()
        for ip in hosts:
            logger.info(f"Getting virtual machines from node {ip}")

            vms = asyncio.run(get_containers(ip))
            for vm in vms:
                pass


#                logger.info(
#                    f"""
# Container name: {vm['hostname']}, vmid: {vm['vmid']}, status: {vm['status']}
# Os: {vm['ostype']}, mac: {vm['hwaddr']}, swap: {vm['swap']}M, memory: {vm['memory']}M
#        """
#                 )
