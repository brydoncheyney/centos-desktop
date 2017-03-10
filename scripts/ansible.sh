#!/usr/bin/env bash

# epel
rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

# ansible
yum -y install ansible
