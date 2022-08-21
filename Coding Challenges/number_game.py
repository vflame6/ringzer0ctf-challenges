#!/usr/bin/python

from pwn import *

HOST = "challenges.ringzer0team.com"
PORT = 10130
USER = "number"
PASS = "Z7IwIMRC2dc764L"

def main():
    # idk this is not working for me, googled for a solution and nothing, the script just  after connection
    s = ssh(USER, HOST, PORT, PASS)
    


    
if __name__ == "__main__":
    main()
