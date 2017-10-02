#!/usr/bin/env bash
#
# Guest Additions will be installed for the kernel packaged with the base ISO -
# when the kernel is updated via yum update this reference is no longer valid
# so we must install Guest Additions

set -oux pipefail

kernel=$(uname -r)
yum reinstall -y ca-certificates
yum install -y gcc kernel-devel-${kernel} bzip2 perl
mount -o loop /home/vagrant/VBoxGuestAdditions.iso /mnt
REMOVE_INSTALLATION_DIR=0 /mnt/VBoxLinuxAdditions.run
umount /mnt
