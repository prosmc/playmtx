# playmtx-010

playmtx-010 is a simple ansible playbook template (recipe) that can be used to run against a virtual machine. For that purpose a Vagrantfile <br> 
is shipped with this project.

###### PREREQUISITES
---
For running the playmtx-010 you need the following software components on your host system

Name                | Reference    
------------------- | --------------- 
VirtualBox >=5.2.42 | [https://www.virtualbox.org/wiki/VBoxInstallAndRun](https://www.virtualbox.org/wiki/VBoxInstallAndRun)
Vagrant >=2.2.1     | [https://www.vagrantup.com/docs/installation](https://www.vagrantup.com/docs/installation)
Ansible >=2.8.1     | [https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

###### REPOSITORY CONTENT
---

Recipe Categories         | Main Focus             | Components
--------------------------|------------------------|-----------------------------------------------------------------------
playmtx-010               | Basic Template         | Simple Ansible Playbook & Vagrant File (centos8)


SETUP
---

1. Clone the playmtx repo

        $ cd ~
        $ mkdir playmtx-ws01
        $ cd playmtx-ws01
        $ git clone https://github.com/schneidermatic/playmtx.git

2. Start the Virtual Machine

        $ cd ./playmtx-ws01/playmtx-010/vagrant
        $ . ./.envrc
        $ x_setup

        After a successful run of 'x_setup' the virtual machine should be started.

        $ ps -ef | grep playmtx

        schneid+  6476 12518  0 15:05 pts/3    00:00:00 grep --color=auto playmtx <br>
        schneid+ 32272 31280  5 14:28 ?        00:02:04 /usr/lib/virtualbox/VBoxHeadless --comment playmtx --startvm <br> c4aaf69-491f-4a2d-adf3-0b47c453e595--vrde config

    **NOTE:** In .envrc there are some short hands defined and one of it is 'x_setup'. So if your are <br>
              interested which additional short cuts you can use or how it works than take a closer look <br>
              at the .envrc file.
      
3. Run the Ansible Playbook

        $ cd ./playmtx-ws01/playmtx-010/ansible-playbook
        $ . ./.envrc
        $ x_started staging

    **NOTE:** In .envrc there are some short hands defined for running the ansible playbook. So it's sufficient
              to call the short cut 'x_started' + <environment> to run the playbook. Take a look at '.envrc' 
              to get to know how the basic ansible command looks like.

4. In addition to 'x_started' there a two further short cuts:

        $ x_stopped # -- which simulates a stop of the Python Application
        $ x_remove  # -- which removes the Python Application from the Virtual Machine


5. Stop the Virtual Machine

        $ cd ./playmtx-ws01/playmtx-010/vagrant
        $ vagrant halt

   **NOTE:** For more Vagrant commands take a look here: [https://www.vagrantup.com/docs/cli](https://www.vagrantup.com/docs/cli)

CONTRIBUTING
---
If you find some bugs or have any requests/suggestions don't hesitate to open an issue or make a pull request.
