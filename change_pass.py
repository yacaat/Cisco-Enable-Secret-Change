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
    response = os.system('ping {} -w 1 -n 1'.format(ip))
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
    password = 'KI_IH14mnk!'
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
    send_command(remote_conn, "en", True)
    send_command(remote_conn, "CURRENT_PASSWORD", True)
    send_command(remote_conn, "conf t", True)
    send_command(remote_conn, "enable secret NEW_PASSWORD", True)
    send_command(remote_conn, "username amerikan privilege 15  password NEW_PASSWORD", True)
    time.sleep(1)
    send_command(remote_conn, "no username kuhastanesi\n", True)

#    mac, port = find_mac(sys.argv[1])
#    mac, port = find_mac("803f")
#    found_ip = check_port(remote_conn, port)
#    if found_ip:
#        access_sw(found_ip, mac, port)
 #   else:
#        print('IP: {} Port:{} Mac:{}'.format(ip, port, mac))

    print("\n\n\n\nBy Yalın")


if __name__ == '__main__':
    ip_list = [
        "10.50.0.21",
        "10.50.0.22",
        "10.50.0.23",
        "10.50.0.24",
        "10.50.0.25",
        "10.50.0.26",
        "10.50.0.27",
        "10.50.0.28",
        "10.50.0.29",
        "10.50.0.30",
        "10.50.0.31",
        "10.50.0.32",
        "10.50.0.33",
        "10.50.0.34",
        "10.50.0.35",
        "10.50.0.36",
        "10.50.0.37",
        "10.50.0.38",
        "10.50.0.39",
        "10.50.0.40",
        "10.50.0.41",
        "10.50.0.42",
        "10.50.0.43",
        "10.50.0.44",
        "10.50.0.45",
        "10.50.0.46",
        "10.50.0.47",
        "10.50.0.48",
        "10.50.0.49",
        "10.50.0.50",
        "10.50.0.51",
        "10.50.0.52",
        "10.50.0.53",
        "10.50.0.54",
        "10.50.0.55",
        "10.50.0.56",
        "10.50.0.57",
        "10.50.0.58",
        "10.50.0.59",
        "10.50.0.60",
        "10.50.0.61",
        "10.50.0.62",
        "10.50.0.63",
        "10.50.0.64",
        "10.50.0.65",
        "10.50.0.66",
        "10.50.0.67",
        "10.50.0.68",
        "10.50.0.69",
        "10.50.0.70",
        "10.50.0.71",
        "10.50.0.72",
        "10.50.0.73",
        "10.50.0.74",
        "10.50.0.75",
        "10.50.0.76",
        "10.50.0.77",
        "10.50.0.78",
        "10.50.0.79",
        "10.50.0.80",
        "10.50.0.81",
        "10.50.0.82",
        "10.50.0.83",
        "10.50.0.84",
        "10.50.0.85",
        "10.50.0.86",
        "10.50.0.87",
        "10.50.0.88",
        "10.50.0.89",
        "10.50.0.90",
        "10.50.0.91",
        "10.50.0.92",
        "10.50.0.93",
        "10.50.0.94",
        "10.50.0.95",
        "10.50.0.96",
        "10.50.0.97",
        "10.50.0.98",
        "10.50.0.99",
        "10.50.0.100",
        "10.50.0.101",
        "10.50.0.102",
        "10.50.0.103",
        "10.50.0.104",
        "10.50.0.105",
        "10.50.0.106",
        "10.50.0.107",
        "10.50.0.108",
        "10.50.0.109",
        "10.50.0.110",
        "10.50.0.111",
        "10.50.0.112",
        "10.50.0.113",
        "10.50.0.114",
        "10.50.0.115",
        "10.50.0.116",
        "10.50.0.117",
        "10.50.0.118",
        "10.50.0.119",
        "10.50.0.120",
        "10.50.0.121",
        "10.50.0.122",
        "10.50.0.123",
        "10.50.0.124",
        "10.50.0.125",
        "10.50.0.126",
        "10.50.0.127",
        "10.50.0.128",
        "10.50.0.129",
        "10.50.0.130",
        "10.50.0.131",
        "10.50.0.132",
        "10.50.0.133",
        "10.50.0.134",
        "10.50.0.135",
        "10.50.0.136",
        "10.50.0.137",
        "10.50.0.138",
        "10.50.0.139",
        "10.50.0.140",
        "10.50.0.141",
        "10.50.0.142",
        "10.50.0.143",
        "10.50.0.144",
        "10.50.0.145",
        "10.50.0.146",
        "10.50.0.147",
        "10.50.0.148",
        "10.50.0.149",
        "10.50.0.150",
        "10.50.0.151",
        "10.50.0.152",
        "10.50.0.153",
        "10.50.0.154",
        "10.50.0.155",
        "10.50.0.156",
        "10.50.0.157",
        "10.50.0.158",
        "10.50.0.159",
        "10.50.0.160",
        "10.50.0.161",
        "10.50.0.162",
        "10.50.0.163",
        "10.50.0.164",
        "10.50.0.165",
        "10.50.0.166",
        "10.50.0.167",
        "10.50.0.168",
        "10.50.0.169",
        "10.50.0.170",
        "10.50.0.171",
        "10.50.0.172",
        "10.50.0.173",
        "10.50.0.174",
        "10.50.0.175",
        "10.50.0.176",
        "10.50.0.177",
        "10.50.0.178",
        "10.50.0.179",
        "10.50.0.180",
        "10.50.0.181",
        "10.50.0.182",
        "10.50.0.183",
        "10.50.0.184",
        "10.50.0.185",
        "10.50.0.186",
        "10.50.0.187",
        "10.50.0.188",
        "10.50.0.189",
        "10.50.0.190",
        "10.50.0.191",
        "10.50.0.192",
        "10.50.0.193",
        "10.50.0.194",
        "10.50.0.195",
        "10.50.0.196",
        "10.50.0.197",
        "10.50.0.198",
        "10.50.0.199",
        "10.50.0.200",
        "10.50.0.201",
        "10.50.0.202",
        "10.50.0.203",
        "10.50.0.204",
        "10.50.0.205",
        "10.50.0.206",
        "10.50.0.207",
        "10.50.0.208",
        "10.50.0.209",
        "10.50.0.210",
        "10.50.0.211",
        "10.50.0.212",
        "10.50.0.213",
        "10.50.0.214",
        "10.50.0.215",
        "10.50.0.216",
        "10.50.0.217",
        "10.50.0.218",
        "10.50.0.219",
        "10.50.0.220",
        "10.50.0.221",
        "10.50.0.222",
        "10.50.0.223",
        "10.50.0.224",
        "10.50.0.225",
        "10.50.0.226",
        "10.50.0.227",
        "10.50.0.228",
        "10.50.0.229",
        "10.50.0.230",
        "10.50.0.231",
        "10.50.0.232",
        "10.50.0.233",
        "10.50.0.234",
        "10.50.0.235",
        "10.50.0.236",
        "10.50.0.237",
        "10.50.0.238",
        "10.50.0.239",
        "10.50.0.240",
        "10.50.0.241",
        "10.50.0.242",
        "10.50.0.243",
        "10.50.0.244",
        "10.50.0.245",
        "10.50.0.246",
        "10.50.0.247",
        "10.50.0.248",
        "10.50.0.249",

    ]
    for ip in ip_list:
        myFunc(ip)