#!/usr/bin/env bash

set -oux pipefail

yum -y reinstall --disablerepo=epel ca-certificates
yum -y install epel-release
yum -y install ansible
