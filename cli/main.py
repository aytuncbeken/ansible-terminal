#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    This includes necessary functions for CLI and Main.
"""
__author__ = "Aytunc Beken"
__copyright__ = "Copyright (C) 2019 Aytunc Beken"
__license__ = "MIT"
__maintainer__ = "Aytunc Beken"
__email__ = "aytuncbeken.ab@gmail.com"

import argparse
from ansible_parser import inventory_parser
import logging
from distutils.spawn import find_executable
import subprocess
import pkg_resources
import os
import sys

# Global definitions
exit_char = '='

# Set argument ansible_parser
connection_types = ['ssh', 'sftp']
connection_type = connection_types[0]
argument_parser = argparse.ArgumentParser(
    description="Open SSH/SFTP session to hosts defined in Ansible Inventory"
)

argument_parser.add_argument('-a', '--ansible-inventory-path', dest='inventory_path', action='store', required=True,
                             help="Path for Ansible Inventory file or directory. If directory is given, all Ansible "
                                  "Inventory files will be parsed recursively")
argument_parser.add_argument('-p', '--protocol', dest='protocol', action='store', required=True,
                             choices=connection_types, help='Protocol type for connection to Hosts')
argument_parser.add_argument('--debug', dest="debug", action="store_const", required=False, help="Enable debug logs",
                             const="debug")
argument_parser.add_argument('-v', '--version', action='version',
                             version='%(prog)s ' + pkg_resources.require("ansible-terminal")[0].version)
cli_args = argument_parser.parse_args()

# Logging Configuration
logging.basicConfig()
logger = logging.getLogger()
if cli_args.debug is None:
    logger.setLevel(logging.ERROR)
else:
    logger.setLevel(logging.DEBUG)


def main():
    """
    Main function of the script
    :return: void
    """
    global connection_type
    connection_type = cli_args.protocol
    logger.debug("Parsing Inventory %s", cli_args.inventory_path)
    inventory = inventory_parser.get_inventory(cli_args.inventory_path)
    main_interaction(inventory)


def check_pre_reqs():
    """
    Checks dependencies
    :return: void
    """
    pre_reqs = ['ssh', 'sftp']
    for pre_req in pre_reqs:
        if find_executable(pre_req) is None:
            logger.error('Missing dependency. %s command line utility is missing.', pre_req)
            quit(1)


def main_interaction(inventory):
    """
    Main CLI Integration for Ansible Inventory Groups
    :param inventory: Inventory
    :return: void
    """
    groups = inventory_parser.get_groups_from_inventory(inventory)
    while True:
        print_header()
        for index, group in enumerate(groups):
            host_num = len(groups[group].hosts)
            if host_num > 0:
                print("[{}] {}({})".format(index, group, host_num))
        print("[{}] back/exit".format(exit_char))
        user_input = raw_input("Select group or type a string []: ")
        if check_is_integer(user_input):
            index = int(user_input)
            if index in range(0, len(groups)):
                host_interaction(groups.values()[int(index)])
        elif not check_is_integer(user_input):
            if user_input == exit_char:
                exit(0)
            if user_input and len(user_input) >= 1:
                host_interaction(None, inventory_parser.search_for_host(inventory, user_input))
        else:
            continue


def host_interaction(group, host_list=None):
    """
    Host CLI Integration for Ansible Hosts in given Ansible Inventory Group
    :param host_list:  lost of filtered hosts
    :param group: Group Name
    :return: void
    """
    if host_list is None:
        hosts = group.hosts
    else:
        hosts = host_list
    if len(hosts) == 1:
        host_connection(hosts[0])
        return
    while True:
        print_header()
        for index, host in enumerate(hosts):
            print("[{}] {}".format(index, host))
        print("[{}] back/exit".format(exit_char))
        user_input = raw_input("Select host []: ")
        if check_is_integer(user_input):
            index = int(user_input)
            host_connection(hosts[int(index)])
            break
        if not check_is_integer(user_input):
            if user_input == exit_char:
                break
        else:
            continue


def host_connection(host):
    """
    Open SSH/SFTP connection to selected host
    :param host: Ansible Inventory Host
    :return: void
    """
    global connection_type
    command = connection_type
    ansible_ssh_user = "root"
    ansible_host = str(host)
    ansible_ssh_private_key_file = None
    if 'ansible_ssh_private_key_file' in host.vars:
        ansible_ssh_private_key_file = host.vars.get('ansible_ssh_private_key_file')
        command = command + " -i " + ansible_ssh_private_key_file
    if 'ansible_ssh_user' in host.vars:
        ansible_ssh_user = host.vars.get('ansible_ssh_user')
    command = command + " " + ansible_ssh_user
    if 'ansible_host' in host.vars:
        ansible_host = host.vars.get('ansible_host')
    command = command + '@' + ansible_host
    subprocess.call(command, shell=True)


def print_header():
    """
    Print CLI header and clean screen
    :return: void
    """
    os.system('clear')
    print("Ansible SSH Command Line Utility -", pkg_resources.require("ansible-terminal")[0].version)


def check_is_integer(value):
    try:
        int(value)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    main()
