import os
import logging
import time
import paramiko

# logging.basicConfig(filename='example.log', filemode='w', level=logging.INFO)
logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


def disable_paging(remote_conn):
    remote_conn.send("terminal length 0\n")
    time.sleep(1)
    output = remote_conn.recv(1000)
    return output


def send_command(remote_conn, command, screen):
    remote_conn.send(command + '\n')
    rcv_timeout = 0
    output_all = ''
    output = b''
    while rcv_timeout < 5.9 and not ((output.decode('utf-8')).endswith('>') or (output.decode('utf-8')).endswith('#')):
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


def ping(ip, re=4):
    for i in range(re):
        response = os.system('ping {} -w 1 -n 1 > nul '.format(ip))
        if response == 0:
            logger.info("{} is up".format(ip))
            return True
        #time.sleep(0.5)
    else:
        logger.info("{} is down".format(ip))
        return False


def connect(ip):
    if not ping(ip):
        return

    passwords = [['a', 'PASSWORD'], ['a', 'PASSWORD'],]  # ['ku','PASSWORD'],]
    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for password in passwords:
        try:
            remote_conn_pre.connect(ip, username=password[0], password=password[1],
                                    look_for_keys=False, allow_agent=False)
            break
        except paramiko.ssh_exception.AuthenticationException:
            pass
    try:
        remote_conn = remote_conn_pre.invoke_shell()
        disable_paging(remote_conn)
        logger.info("Connected to {}".format(ip))
        send_command(remote_conn, "en", False)
        send_command(remote_conn, "PASSWORD", False)
        output = send_command(remote_conn, "wr", False)
        if 'OK' in output:
            print('SW{} configuration is saved.'.format(ip))
        else:
            print('SW{} configuration is not saved!!!!!!!!!!!'.format(ip))
    except paramiko.ssh_exception.SSHException:
        logger.error('{} Wrong User Credentials!'.format(ip))
