import subprocess
import getpass
import time
import os

def encryptpassword():
    if not os.path.exists(".sshpasswd.gpg"):
        subprocess.run(["./password.sh"])

def osiris():
    subprocess.run(["./osiris.sh", user + host])

user = input("Username: ")
host = "@thoth.cs.pitt.edu"

encryptpassword()
osiris()
while True:
    command = input("Press o to revive, exit to exit: ")
    if command == "o":
        osiris()
    if command == "exit":
        exit()
