from proxmoxer import ProxmoxAPI


def proxmox_connection(host, user, password):

    return ProxmoxAPI(
        host=host, user=user, password=password, verify_ssl=False, service="PVE"
    )
