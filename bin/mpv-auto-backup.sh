#!/bin/bash

while true; do
    [ -e /tmp/mpv-save ] && mpv-backup.sh
    sleep 2
done
