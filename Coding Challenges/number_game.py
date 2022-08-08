#!/usr/bin/python

import pwn

HOST = "challenges.ringzer0team.com"
PORT = 10130
USER = "number"
PASS = "Z7IwIMRC2dc764L"

def main():
    s = pwn.ssh(user=USER, host=HOST, port=PORT, password=PASS)
    shell = s.shell()

    shell.interactive()



if __name__ == "__main__":
    main()
