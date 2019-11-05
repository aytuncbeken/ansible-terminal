# Ansible SSH
This script list hosts which are defined in Ansible Inventory and open SSH/SFTP connection to host which is selected.

## Usage
Print usage:

```ansible-ssh ```

Print version:

```ansible-ssh -v```

Work with Ansible Inventory

```ansible-ssh --ansible-inventory-path <Full Path To Inventory Directory or File> --protocol {sftp, ssh}``` 

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