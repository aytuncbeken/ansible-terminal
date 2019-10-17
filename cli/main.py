#!/usr/bin/python

import argparse
import logging
from shutil import which

# Set argument parser
actions = ['ssh', 'sftp']
argument_parser = argparse.ArgumentParser(
    description="Open SSH/SFTP session to hosts defined in Ansible Inventory"
)

argument_parser.add_argument('--ansible-inventory-path', dest='inventory-path', action='store', required=True,
                             help="Path for Ansible Inventory file or directory. If directory is given, all Ansible "
                                  "Inventory files will be parsed recurively")
argument_parser.add_argument('--ansible-ssh-connection-property', dest='ssh-connection-property', action='append',
                             required=False,
                             help="(Optional) Use for overwriting Ansible SSH Connection Properties which are defined "
                                  "in inventory files. Properties defined in here will be applied to all hosts in "
                                  "inventory")
argument_parser.add_argument('--debug', dest="debug", action="store_const", required=False, help="Enable debug logs",
                             const="debug")
cli_args = argument_parser.parse_args()

# Logging Configuration
logger = logging.getLogger()
if cli_args.debug is None:
    logging.setLoggerClass(logging.ERROR)
else:
    logging.setLoggerClass(logging.DEBUG)


def main():
    logger.debug("Command Line Utility Started")


def check_pre_reqs():
    pre_reqs = ['ssh', 'sftp']
    for pre_req in pre_reqs:
        if which(pre_req) is None:
            logger.error('Missing dependency. %s command line utility is missing.', pre_req)
            quit(1)


if __name__ == "__main__":
    main()
