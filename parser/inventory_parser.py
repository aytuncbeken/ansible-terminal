from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager


def get_inventory(inventory_path):
    loader = DataLoader()
    return InventoryManager(loader, sources=inventory_path)


def get_groups_from_inventory(inventory):
    return inventory.groups


def get_hosts_from_group(group):
    return group['hosts']