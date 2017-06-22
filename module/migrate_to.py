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

def migrate(vm_port):
	_time_start()

	# print('migrate run... from {0} on {1} to {2}'.format(vm_ip, from_ip, to_ip))

	command = '''
	python /mnt/py/migrate_start.py {0}
	'''.format(vm_port)
	p = _exec_process(command)
	p.wait()

    print('migrate complete.')
	_time_end()

if __name__ == '__main__':
    if(len(argv) != 2):
        print('python migrate.py vm_port')
    else:
        vm_port = sys.argv[1]
        clone(vm_port)
