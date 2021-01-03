# Ansible SSH
This script list hosts which are defined in Ansible Inventory and open SSH/SFTP connection to host which is selected.

## Usage
Print usage:

```ansible-terminal ```

Print version:

```ansible-terminal -v```

Work with Ansible Inventory by different options

```
usage: ansible-terminal [-h] -a [INVENTORY_PATH [INVENTORY_PATH ...]] -p
                        {ssh,sftp} [--debug] [-v] [-n NAME] [-u SSH_USER]
                        [-k SSH_KEY]

Open SSH/SFTP session to hosts defined in Ansible Inventory

optional arguments:
  -h, --help            show this help message and exit
  -a [INVENTORY_PATH [INVENTORY_PATH ...]]
                        Path for Ansible Inventory file or directory. Multiple
                        definitions can be done.If directory is given, all
                        Ansible Inventory files will be parsed recursively
  -p {ssh,sftp}         Protocol type for connection to Hosts. ssh / sftp
  --debug               Enable debug logs
  -v                    show program's version number and exit
  -n NAME               Name of host to search. If one host matches, will
                        connect automaically
  -u SSH_USER           SSH Username for ssh connection type. This will
                        override ansible_ssh_user for all connections
  -k SSH_KEY            SSH Key File path for ssh connection type. This will
                        override ansible_ssh_private_key_file for all
                        connections
``` 

PyPI - https://pypi.org/project/ansible-terminal/

## Notes
For default, Below parameters are used for SSH/SFTP connection.
```
user: root
ssh-key: ~/.ssh/
target machine: host
```
You can overwrite these values by defining related [Ansible Behavioral Inventory Properties](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#connecting-to-hosts-behavioral-inventory-parameters) in the inventory.
Parameters:
```
ansible_ssh_user
ansible_host
ansible_ssh_private_key_file
```
  
### Thanks
Please do not forget to star when you are using : ) 
