import requests
import sys
import os
from time import sleep
from subprocess import Popen, PIPE, CREATE_NEW_CONSOLE
import subprocess
from termcolor import colored
import ctypes
from os import getcwd


ctypes.windll.kernel32.SetConsoleTitleW("Web Crawler - Verification")

while(True):
    hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
    print ("\nDevice ID :",hwid)
    print("\nInput Your Account to Access Web Crawler")
    print("---------")
    hwid_confirm = hwid

    username_input = input("Username: ")
    password_input = input("Password: ")
    with open('data\init.txt', 'w+') as f:
        f.write(username_input)
        f.close()

    server = requests.get("https://raw.githubusercontent.com/unskilleddegree/path/main/server.txt")
    server_url = server.text.strip("\n")
    target_hwid = requests.get(server_url + username_input + "/hwid_" + username_input + ".txt")
    target_username = requests.get(server_url + username_input+"/username_" + username_input + ".txt")
    target_password = requests.get(server_url + username_input+"/password_" + username_input + ".txt")
    validation = requests.get(server_url + username_input + "/validation.txt")
    data1 = target_username.text
    data2 = target_password.text

    os.system('cls' if os.name == 'nt' else 'clear')
    if hwid_confirm in target_hwid.text:
        pass
    else:
        print(colored("Your Device ID is not registered to the system!", 'red'))
        print(colored("Contact support to get access.", 'red'))
        notValid = " "
        for x in notValid:
            print(x, end='')
            sys.stdout.flush()
            sleep(10)
        break
    if username_input == data1:
        pass
    if password_input == data2:
        copyright = "Web Crawler by Unskilleddegree"
        for x in copyright:
            print(x, end='')
            sys.stdout.flush()
            sleep(0.1)
        print("\n\nWelcome back",username_input)
        member = colored(validation.text,'green')
        for x in member:
            print(x, end='')
            sys.stdout.flush()
            sleep(0.1)
        os.startfile("init.exe")
        sys.exit()
    else:
        print("Either your account has been Expired or you put a wrong account! \nPlease contact support to renew or try again.")
