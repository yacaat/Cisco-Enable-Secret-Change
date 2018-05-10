import paramiko
import time
import pdb
import re
import pyperclip
import logging
import win32com.client as comclt
import subprocess
import sys
import os

def disable_paging(remote_conn):
    '''Disable paging on a Cisco router'''

    remote_conn.send("terminal length 0\n")
    time.sleep(1)

    # Clear the buffer on the screen
    output = remote_conn.recv(1000)
    return output


def send_command(remote_conn, command, screen):
    remote_conn.send(command + '\n')
    rcv_timeout = 0
    output_all = ''
    output = b''
    while rcv_timeout < 5.9 and not ((output.decode('utf-8')).endswith('>') or
                                         (output.decode('utf-8')).endswith('#')):
        if remote_conn.recv_ready():
            output = remote_conn.recv(4096)
            output_all = output_all + output.decode('utf-8')
        else:
            time.sleep(0.1)
            rcv_timeout += 0.1
    if screen:
        # print(output)
        print(output_all)
    return output_all

def myFunc (ip):
    response = os.system('ping {} -w 1 -n 1 > nul'.format(ip))
    if response == 0:
        print('{} is up!'.format(ip))
    else:
        print('{} is dooooooooooooooooooooooown!'.format(ip))
        return


    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    # VARIABLES THAT NEED CHANGED
#    ip = "10.50.1.13"
    username = 'kuhastanesi'
    password = 'PASSWORD'
    mac = ''
    port = ''
    passwords= [['amerikan','PASSWORD'],['amerikan','PASSWORD'],]

    # Create instance of SSHClient object
    for passo in passwords:
        remote_conn_pre = paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print(passo[0], passo[1])
        try:
            remote_conn_pre.connect(ip, username=passo[0], password=passo[1], look_for_keys=False, allow_agent=False)
            remote_conn = remote_conn_pre.invoke_shell()
            break
        except:
            print('Exception geldi')


    output = remote_conn.recv(1000)
    disable_paging(remote_conn)
    logger.info("Connected to {}".format(ip))
    send_command(remote_conn, "en", True)
    send_command(remote_conn, "PASSWORD", True)
    send_command(remote_conn, "wr", True)

    #    mac, port = find_mac(sys.argv[1])
    #    mac, port = find_mac("803f")
    #    found_ip = check_port(remote_conn, port)
    #    if found_ip:
    #        access_sw(found_ip, mac, port)
     #   else:
    #        print('IP: {} Port:{} Mac:{}'.format(ip, port, mac))

    print("\n\n\n\nBy Yalın")


if __name__ == '__main__':
    ip_list = ['10.80.0.' + str(x) for x in range(250)]
    for ip in ip_list:
        myFunc(ip)