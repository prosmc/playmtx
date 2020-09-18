# playmtx-005

playmtx-005 is a simple ansible playbook template (recipe) that can be used to run against a virtual machine. For that purpose a Vagrantfile <br> 
is shipped with this project.

###### PREREQUISITES
---
For running the playmtx-005 you need the following software components on your host system

Name                | Reference    
------------------- | --------------- 
VirtualBox >=5.2.42 | [https://www.virtualbox.org/wiki/VBoxInstallAndRun](https://www.virtualbox.org/wiki/VBoxInstallAndRun)
Vagrant >=2.2.1     | [https://www.vagrantup.com/docs/installation](https://www.vagrantup.com/docs/installation)
Ansible >=2.8.1     | [https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

###### REPOSITORY CONTENT
---

Recipe Categories         | Main Focus             | Components
--------------------------|------------------------|-----------------------------------------------------------------------
playmtx-005               | Basic Template         | Simple Ansible Playbook & Vagrant File (centos8)


SETUP
---

1. Clone the playmtx repo

        $ cd ~
        $ mkdir playmtx-ws01
        $ cd playmtx-ws01
        $ git clone https://github.com/schneidermatic/playmtx.git

2. Start the Virtual Machine

        $ cd ./playmtx-ws01/playmtx-005/vagrant
        $ . ./.envrc
        $ x_setup

        After a successful run of 'x_setup' the virtual machine should be started.

        $ ps -ef | grep playmtx

        schneid+  6476 12518  0 15:05 pts/3    00:00:00 grep --color=auto playmtx <br>
        schneid+ 32272 31280  5 14:28 ?        00:02:04 /usr/lib/virtualbox/VBoxHeadless --comment playmtx --startvm <br> c4aaf69-491f-4a2d-adf3-0b47c453e595--vrde config

    **NOTE:** In .envrc there are some short cuts defined and one of it is 'x_setup'. So if your are <br>
              interested which additional short cuts you can use or how it works than take a closer look <br>
              at the .envrc file.
      
3. Run the Ansible Playbook

        $ cd ./playmtx-ws01/playmtx-005/ansible-playbook
        $ . ./.envrc
        $ x_started staging

        PLAY [playmtx-005] ******************************************************************************************************************************

        TASK [Gathering Facts] **************************************************************************************************************************
        Friday 18 September 2020  17:33:28 +0200 (0:00:00.084)       0:00:00.084 ****** 
        ok: [127.0.0.1]

        TASK [simple-role : include_tasks] **************************************************************************************************************
        Friday 18 September 2020  17:33:29 +0200 (0:00:01.241)       0:00:01.326 ****** 
        included: /home/schneidermatic/workspace-01/python-ws01/playmtx/playmtx-005/ansible-playbook/roles/simple-role/tasks/present.yml for 127.0.0.1

        TASK [simple-role : create a directory] *********************************************************************************************************
        Friday 18 September 2020  17:33:29 +0200 (0:00:00.065)       0:00:01.392 ****** 
        ok: [127.0.0.1]

        TASK [simple-role : Copy Python file] ***********************************************************************************************************
        Friday 18 September 2020  17:33:30 +0200 (0:00:00.651)       0:00:02.043 ****** 
        ok: [127.0.0.1] => (item=/home/schneidermatic/workspace-01/python-ws01/playmtx/playmtx-005/ansible-playbook/roles/simple-role/files/myapp.py)

        TASK [simple-role : Run the Python script] ******************************************************************************************************
        Friday 18 September 2020  17:33:31 +0200 (0:00:00.982)       0:00:03.026 ****** 
        changed: [127.0.0.1]

        TASK [simple-role : debug] **********************************************************************************************************************
        Friday 18 September 2020  17:33:32 +0200 (0:00:00.702)       0:00:03.728 ****** 
        ok: [127.0.0.1] => {
                "msg": "===> /tmp/app/myapp.py is STARTED!"
        }

        TASK [simple-role : include_tasks] **************************************************************************************************************
        Friday 18 September 2020  17:33:32 +0200 (0:00:00.041)       0:00:03.769 ****** 
        skipping: [127.0.0.1]

        TASK [debug] ************************************************************************************************************************************
        Friday 18 September 2020  17:33:32 +0200 (0:00:00.047)       0:00:03.817 ****** 
        ok: [127.0.0.1] => {
        "msg": "playmtx-005 is successfully executed!"
        }

        PLAY RECAP **************************************************************************************************************************************
        127.0.0.1                  : ok=7    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   

        Friday 18 September 2020  17:33:32 +0200 (0:00:00.016)       0:00:03.834 ****** 
        =============================================================================== 
        simple-role ------------------------------------------------------------- 2.49s
        gather_facts ------------------------------------------------------------ 1.24s
        debug ------------------------------------------------------------------- 0.02s
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
        total ------------------------------------------------------------------- 3.75s

    **NOTE:** In .envrc there are some short cuts defined for running the ansible playbook. So it's sufficient
              to call the short cut 'x_started' + <environment> to run the playbook. Take a look at '.envrc' 
              to get to know how the basic ansible command looks like.

4. In addition to 'x_started' there a two further short cuts:

        $ x_stopped # -- which simulates a stop of the Python Application
        $ x_remove  # -- which removes the Python Application from the Virtual Machine


5. Stop the Virtual Machine

        $ cd ./playmtx-ws01/playmtx-005/vagrant
        $ vagrant halt

   **NOTE:** For more Vagrant commands take a look here: [https://www.vagrantup.com/docs/cli](https://www.vagrantup.com/docs/cli)

CONTRIBUTING
---
If you find some bugs or have any requests/suggestions don't hesitate to open an issue or make a pull request.
