import ipaddress
import netifaces
import os
import sqlite3
import shlex
import subprocess
from subprocess import TimeoutExpired, PIPE
from time import time
import threading
import sys

_usr = 'pi'
_pass = 'raspberry'

def _time_start():
	global _start_time
	_start_time = time()

def _time_end():
	elapsed_time = time() - _start_time
	print('time: {0:.2f}[sec]'.format(elapsed_time))

def clone(to_vm_ip, to_vm_port):
	_time_start()
	command = """
	python /home/pi/raspi/py/clone_start.py {0} {1}
	""".format(to_vm_ip, to_vm_port)

	print(command)

	p = _exec_process(command)
	try:
		p.wait(timeout = 60)
	except TimeoutExpired:
		print('clone error')

	_add_ssh(vm_ip)
	_update_vm_info(vm_ip)
	print('clone complete.')
	_time_end()

if __name__ == '__main__':
    if(len(argv) != 3):
        print('python clone to_vm_ip to_vm_port')
    else:
        to_vm_ip = sys.argv[1]
        to_vm_port = sys.argv[2]
        clone(to_vm_ip, to_vm_port)
