#!/bin/bash

source "${0%/*}"/../../resources/setup-scripts-base.sh

# Use linux-setup-backup-kde-conf.sh to generate the source

rsync -rl -- "$(linux-setup-get-resources-path.sh)"/kde/my-kde-conf/ ~/
