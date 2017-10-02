#!/usr/bin/env bash

set -oux pipefail

yum -y reinstall ca-certificates
yum -y install ansible
