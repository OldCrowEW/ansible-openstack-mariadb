# Ansible Role: OpenStack Mariadb

[![Build Status](https://travis-ci.org/OldCrowEW/ansible-openstack-mariadb.svg?branch=master)](https://travis-ci.org/OldCrowEW/ansible-openstack-mariadb)

Ansible role to install and configure OpenStack mariadb * associated packages. This follows the install guide for
better or worse :D

*Note:* mysql_secure_installation is not run as part of this initial role

## Requirements

None

## Role Variables

None

## Dependencies

    oldcrowew.ansible_openstack_common

## Example Playbook

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: "oldcrowew.ansible_openstack_common" }
         - { role: "ansible-openstack-mariadb" }

## License

BSD

## Author Information

John Favorite