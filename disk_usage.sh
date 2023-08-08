#!/bin/bash

for user in $(awk -F':' '{ print $1}' /etc/passwd); do
    home_dir="/home/$user"
    if [ -d "$home_dir" ]; then
        disk_usage=$(sudo du -sh "$home_dir" 2>/dev/null | cut -f1)
        echo "$user - $disk_usage"
    fi
done
