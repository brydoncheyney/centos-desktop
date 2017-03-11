# Centos 7 Desktop

Provisioning a Centos 7 Desktop using [Packer](https://www.packer.io/),
[Vagrant](https://www.vagrantup.com/),
[Virtualbox](https://www.virtualbox.org/) and
[Ansible](https://www.ansible.com/)

# Usage

Build and package the centos-7-desktop box

    ./build

Install the box

    vagrant box add --force --name centos-7-desktop builds/virtualbox-centos-7-desktop.box

Start the box (without running the ansible provisioner)

    vagrant up --no-provision

Modifications to the ansible roles can be tested by provisioning the vagrant machine

    vagrant provision
