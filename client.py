import time
import paramiko
import logging
import sys
from msvcrt import getch
from multiprocessing.dummy import Pool as ThreadPool
import signal
import signal
import os
import threading
class ExitCommand(Exception):
    pass

def disable_paging(remote_conn):
    '''Disable paging on a Cisco router'''

    remote_conn.send("terminal length 0\n")
    time.sleep(1)

    # Clear the buffer on the screen
    output = remote_conn.recv(1000)
    print(output.decode('utf-8'), end='')
    return output


def send_command(remote_conn, command, screen):
    remote_conn.send(command + '\n')
    rcv_timeout = 0
    output_all = ''
    output = b''
    while rcv_timeout < 0.9 and not ((output.decode('utf-8')).endswith('>') or
                                     (output.decode('utf-8')).endswith('#') or
                                     (output.decode('utf-8')).endswith(':')):
        if remote_conn.recv_ready():
            output = remote_conn.recv(4096)
            output_all = output_all + output.decode('utf-8')
        else:
            time.sleep(0.1)
            rcv_timeout += 0.1
    if screen:
        # print(output)
        print(output_all, end='')
    return output_all



def client(rw):

    command = ''
    while True:
        global count
        if count > 5:
            sys.exit()
        print('Buyuk yarakbasi')
        if rw == 'write':
            key = getch()

            if ord(key) == 27:  # ESC
                remote_conn_pre.close()
                break
            if ord(key) == 224:  # ESC
                key = getch()
                if ord(key) == 72:
                    print('Yukari basildi')
            remote_conn.send(key.decode('ASCII'))
#            time.sleep(0.13)
            rcv_timeout = 0

        # while (rcv_timeout < 0.2 and not ((output.decode('utf-8')).endswith('>') or
        #                                       (output.decode('utf-8')).endswith('#') or
        #                                       (output.decode('utf-8')).endswith(':'))) and output == b'':
        if rw == 'read':
            output = ''
            print('yarak basi')
            while True:
                #if remote_conn.recv_ready():
                output = remote_conn.recv(4096).decode('utf-8')
                print('****'+output+'****',end='')
                sys.stdout.flush()
                time.sleep(0.1)
                if output == '':
                    count += 1
                    print(count)
                    if count > 5:
                        print('Ciktim')
                        raise ExitCommand()
                        sys.exit()


                # if output.endswith(">") or len(output) != 4096: #1 or len(output) == 3 or len(output) == 22:#len(output) != 4096 or output.endswith():
                #     break
                # else :
                #     time.sleep(0.1)

if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        # VARIABLES THAT NEED CHANGED
        ip = '10.80.0.' + sys.argv[1]
        username = 'amerikan'
        password = 'Vkv@hSwMng4!'
        mac = ''
        port = ''

        # Create instance of SSHClient object
        remote_conn_pre = paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
        remote_conn = remote_conn_pre.invoke_shell()
        logger.info("Connected to {}".format(ip))
        output = remote_conn.recv(1000)
        disable_paging(remote_conn)
        send_command(remote_conn, "enable", True)
        send_command(remote_conn, "brcd1920", True)
        global count
        count = 0
        urls = [
            'write',
            'read',
        ]

        # make the Pool of workers
        pool = ThreadPool(2)

        # open the urls in their own threads
        # and return the results
        results = pool.map(client, urls)

        # close the pool and wait for the work to finish
        pool.close()
        pool.join()
    except ExitCommand:
        pass
    finally:
        print('finally will still run')