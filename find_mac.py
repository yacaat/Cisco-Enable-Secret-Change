import paramiko
import time
import pdb
import re
import pyperclip
import logging
import win32com.client as comclt
import subprocess
import sys


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


def find_mac(partial_mac):
    mac_address_table = send_command(remote_conn, "sh mac add", True)
    # macs = re.findall(r'\S*' + partial_mac, mac_address_table)
    macs = re.findall(r'(\w{4}\.\w{4}\.\w{4}).*?(\S+)\r\n', mac_address_table)
    possible_macs = list()
    print('Choose the mac address: \n')
    for mac in macs:
        if partial_mac in mac[0]:
            possible_macs.append(mac)
    for i, mac in enumerate(possible_macs):
        print("{} - {} - {}\n".format(i, mac[0], mac[1]))
    if len(possible_macs) != 1:
        input()
        return possible_macs[i]
    else:
        return possible_macs[0]


def check_port(remote_conn, port):
    temp = send_command(remote_conn, '\nsh cdp ne ' + port + ' de', False)
    ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', temp)
    if ip:
        return ip[0]
    else:
        # print('This port not connected to switch')
        return False


def access_sw(ip, mac, port):
    remote_conn_pre.connect(ip, username='amerikan', password='PASSWORD', look_for_keys=False, allow_agent=False)
    remote_conn = remote_conn_pre.invoke_shell()
    output = remote_conn.recv(1000)
    disable_paging(remote_conn)
    logger.info("Connected to {}".format(ip))
    send_command(remote_conn, "en", False)
    send_command(remote_conn, "PASSWORD", False)
    mac_address_table = send_command(remote_conn, "sh mac add", False)
    macs = re.findall(r'(\w{4}\.\w{4}\.\w{4}).*\s(\S+)', mac_address_table)
    for temp_mac in macs:
        if mac in temp_mac[0]:
            port = temp_mac[1]
            break
    found_ip = check_port(remote_conn, port)
    if found_ip:
        access_sw(found_ip, mac)
    else:
        print('IP: {} Port:{} Mac:{}'.format(ip, port, mac))
        wsh = comclt.Dispatch("WScript.Shell")

        subprocess.Popen("putty {} -l amerikan -pw {}".format(ip, 'PASSWORD'), shell=True, stdout=subprocess.PIPE)
        time.sleep(2)
        wsh.AppActivate("Putty")  # select another application
        wsh.SendKeys("en\n")  # saend the keys you wanta
        time.sleep(1)
        wsh.SendKeys("PASSWORD\n")

#        time.sleep(1)
#        subprocess.Popen("meyer.ahk {} {}".format(port,sys.argv[2]), shell=True, stdout=subprocess.PIPE)


        # pdb.set_trace()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    # VARIABLES THAT NEED CHANGED
    ip = '10.80.0.254'
    username = 'amerikan'
    password = 'PASSWORD'
    mac = ''
    port = ''

    # Create instance of SSHClient object
    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
    remote_conn = remote_conn_pre.invoke_shell()

    output = remote_conn.recv(1000)
    disable_paging(remote_conn)
    logger.info("Connected to {}".format(ip))
    send_command(remote_conn, "en", False)
    send_command(remote_conn, "PASSWORD", False)
    mac, port = find_mac(sys.argv[1])
#    mac, port = find_mac("803f")
    found_ip = check_port(remote_conn, port)
    if found_ip:
        access_sw(found_ip, mac, port)
    else:
        print('IP: {} Port:{} Mac:{}'.format(ip, port, mac))

    print("\n\n\n\nBy Yalın")


