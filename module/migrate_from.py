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

def _time_start():
	global _start_time
	_start_time = time()

def _time_end():
	elapsed_time = time() - _start_time
	print('time: {0:.2f}[sec]'.format(elapsed_time))

def migrate(to_ip, vm_port):
	_time_start()

	# print('migrate run... from {0} to {2}'.format(to_ip))

	command = '''
	sshpass -p {3}
	scp -o StrictHostKeyChecking=no
	/home/pi/diff.qcow2 {5}@{6}:~
	'''.format(_pass, _usr, to_ip)

	p = _exec_process(command)
	p.wait()

	print('telnet')
	command = '''
	python /home/pi/raspi/py/telnet.py {0} {1}
	'''.format(to_ip, vm_port)
	p = _exec_process(command)
	p.wait(timeout = 90)

	command = 'rm /home/pi/diff.qcow2'
	p = _exec_process(command)
	p.wait()

    print('migrate complete.')
	_time_end()

if __name__ == '__main__':
    if(len(argv) != 5):
        print('python migrate.py to_ip vm_port')
    else:
        to_ip = sys.argv[1]
        vm_port = sys.argv[2]
        clone(to_ip, vm_port)
