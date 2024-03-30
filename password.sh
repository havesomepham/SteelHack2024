#!/bin/sh

echo "##### ENCRYPTING PASSWORD #####"
read -sp 'Password: ' passvar
echo $passvar > .sshpasswd
gpg -c .sshpasswd
rm .sshpasswd