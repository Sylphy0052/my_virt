import os
import shlex
import sqlite3
import subprocess
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("python start.py vm_ip vm_port")
    else:
    	args = sys.argv
    	vm_ip = args[1]
    	vm_port = args[2]

	command = '/home/pi/raspi/sh/start {0} {1}'.format(vm_ip, vm_port)

	p = _exec_process(command)
    p.wait()
