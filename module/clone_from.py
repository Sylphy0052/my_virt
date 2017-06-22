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

def clone(to_ip):
	_time_start()

	# print('clone run... from {0} on {1} to {2}'.format(vm_ip, from_ip, to_ip))

	command = """
	sshpass -p {0}
	scp -o StrictHostKeyChecking=no
	/home/pi/diff.qcow2 {2}@{3}:~
	""".format(_pass, _usr, to_ip)

	p = _exec_process(command)
	p.wait()

	print('clone complete.')
	_time_end()

if __name__ == '__main__':
    if(len(argv) != 2):
        print('python clone to_ip')
    else:
        to_ip = sys.argv[1]
        clone(to_ip)
