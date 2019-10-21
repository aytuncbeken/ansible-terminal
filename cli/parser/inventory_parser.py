#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    This includes necessary functions for getting groups/hosts from Ansible Inventory
"""
__author__ = "Aytunc Beken"
__copyright__ = "Copyright (C) 2019 Aytunc Beken"
__license__ = "MIT"
__maintainer__ = "Aytunc Beken"
__email__ = "aytuncbeken.ab@gmail.com"

from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager


def get_inventory(inventory_path):
    """
    Loads Ansible Inventory from given path
    :param inventory_path: Full path of the inventory directory or file
    :return: Inventory
    """
    loader = DataLoader()
    return InventoryManager(loader, sources=inventory_path)


def get_groups_from_inventory(inventory):
    """
    Return groups from Ansible Inventory
    :param inventory: Inventory
    :return: Groups
    """
    return inventory.groups


def get_hosts_from_group(group):
    """
    Return hosts from Inventory by given group
    :param group: Name of the group
    :return: Hosts
    """
    return group['hosts']
