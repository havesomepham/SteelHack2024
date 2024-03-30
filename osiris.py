import subprocess
import getpass
import time
import os

def encryptpassword():
    if not os.path.exists(".sshpasswd.gpg"):
        subprocess.run(["./password.sh"])

def osiris(user, host):
    # subprocess.run(["./osiris.sh", user + host])
    process = subprocess.Popen(["./osiris.sh", user + host])
    time.sleep(10)

def main():
    user = input("Username: ")
    host = "@thoth.cs.pitt.edu"

    encryptpassword()
    osiris(user, host)
    while True:
        command = input("Press o to revive, exit to exit: ")
        if command == "o":
            osiris(user, host)
        if command == "exit":
            exit()

if __name__ == "__main__":
    main()