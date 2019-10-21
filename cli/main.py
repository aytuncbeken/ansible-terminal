#!/usr/bin/python

import argparse
from parser import inventory_parser
import logging
from distutils.spawn import find_executable
import subprocess
import pkg_resources
import os

# Set argument parser
connection_types = ['ssh', 'sftp']
connection_type = connection_types[0]
argument_parser = argparse.ArgumentParser(
    description="Open SSH/SFTP session to hosts defined in Ansible Inventory"
)

argument_parser.add_argument('--ansible-inventory-path', dest='inventory_path', action='store', required=True,
                             help="Path for Ansible Inventory file or directory. If directory is given, all Ansible "
                                  "Inventory files will be parsed recurively")
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
    logger.debug("Parsing Inventory %s", cli_args.inventory_path)
    inventory = inventory_parser.get_inventory(cli_args.inventory_path)
    main_interaction(inventory)


def check_pre_reqs():
    pre_reqs = ['ssh', 'sftp']
    for pre_req in pre_reqs:
        if find_executable(pre_req) is None:
            logger.error('Missing dependency. %s command line utility is missing.', pre_req)
            quit(1)


def main_interaction(inventory):
    while True:
        print_header()
        for index, type in enumerate(connection_types):
            print("[{}] {}".format(index, type))
        index = raw_input("Select connection type [default=ssh]:")
        if index and int(index) in range(0, len(connection_types)):
            connection_type = connection_types[int(index)]
            group_interaction(inventory)
        elif not index:
            group_interaction(inventory)
        else:
            continue


def group_interaction(inventory):
    groups = inventory_parser.get_groups_from_inventory(inventory)
    while True:
        print_header()
        for index, group in enumerate(groups):
            host_num = len(groups[group].hosts)
            if host_num > 0:
                print("[{}] {}({})".format(index, group, host_num))
        index = raw_input("Select group []: ")
        if index and int(index) in range(0, len(groups)):
            host_interaction(groups.values()[int(index)])
            break
        else:
            continue


def host_interaction(group):
    hosts = group.hosts
    while True:
        print_header()
        for index, host in enumerate(hosts):
            print("[{}] {}".format(index, host))
        index = raw_input("Select host []: ")
        if index and int(index) in range(0, len(hosts)):
            host_connection(hosts[int(index)])
            break
        else:
            continue


def host_connection(host):
    command = connection_type
    ansible_ssh_user = "root"
    ansible_host = str(host)
    ansible_ssh_private_key_file = None
    if 'ansible_ssh_user' in host.vars:
        ansible_ssh_user = host.vars.get('ansible_ssh_user')
    command = command + " " + ansible_ssh_user
    if 'ansible_host' in host.vars:
        ansible_host = host.vars.get('ansible_host')
    command = command + '@' + ansible_host
    if 'ansible_ssh_private_key_file' in host.vars:
        ansible_ssh_private_key_file = host.vars.get('ansible_ssh_private_key_file')
        command = command + " -i " + ansible_ssh_private_key_file
    subprocess.call(command, shell=True)


def print_header():
    os.system('clear')
    print "Ansible SSH Command Line Utility -", pkg_resources.require("ansible-terminal")[0].version


if __name__ == "__main__":
    main()
