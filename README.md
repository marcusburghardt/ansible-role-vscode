ansible-role-vscode
=========

This role will ensure the Visual Studio Code is properly installed and configured.  
We can manage extensions and workspaces through variables, using the existing  
standards defined in "defaults/main.yml" or overridden them in a playbook, for example.  

This role will:  
- Ensure the Official Repository for VSCODE;
- Ensure VSCODE is installed and updated from the repository;
- Ensure the desired state for the defined extensions;

To install this role:  
$ ansible-galaxy role install marcusburghardt.ansible_role_vscode

Requirements
------------

- python3

Role Variables
--------------

You can customize your environment in a very simple and centralized way editing some variables in:
- defaults/main.yml

In some rare cases, you may change some configuration to reflect your local environment in:
- vars/*.yml

Observe that the above variables could be set in your playbook too, which, IMO is much more elegant. ;)  
Take a look in the Example Playbook section.

Dependencies
------------

None

Example Playbook
----------------

This playbook will prepare everything with the right variables.  
For this example, lets call this playbook file as "ansible_vscode.yml":  

---
- hosts: linux
  vars:
    - available_tasks:
      - { enabled: True,  name: 'configure_vscode' }
  roles:
    - marcusburghardt.ansible_role_vscode

Considering the inventory file is in the same folder and is called "hosts_vscode",  
you can run this command to see the magic happen:  
$ ansible-playbook -K -i hosts_vscode ansible_vscode.yml  

Maybe you would like to set some ansible configurations for this environment.  
For instance, define a local folder to hold downloads roles.  
You can find an example of ansible.cfg file in "files" folder.

License
-------

This Source Code Form is subject to the terms of the Mozilla Public  
License, v. 2.0. If a copy of the MPL was not distributed with this  
file, You can obtain one at http://mozilla.org/MPL/2.0/.

Author Information
------------------

Marcus Burghardt
- https://github.com/marcusburghardt/
- https://www.linkedin.com/in/marcusburghardt/
