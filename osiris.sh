#!/bin/sh

# echo "##### RUNNING OSIRIS ######"
echo "##### LOGGING IN #####"
gpg -d -q .sshpasswd.gpg | sshpass ssh -T $1