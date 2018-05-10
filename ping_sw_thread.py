import os
import openpyxl
import re
import threading
from queue import Queue
import time
lock = threading.Lock()
wb = openpyxl.load_workbook('ping_sw_thread.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

start = time.time()
sw_up = list()
def ping(ip):
    print('Pinging {}'.format(ip))
    # response = os.system('ping 10.80.0.{} -w 1 -n 1'.format(ip))
    # if response == 0:
    #     print('{} is up!'.format(ip))
    #     sw_up.append(ip)
    mac_address_table = os.popen('ping 10.80.0.{} -w 1 -n 1'.format(ip)).read()
    if r'Received = 1' in mac_address_table:
        print('=======')
        #sw_up.append(re.search(r'[0-9]+(?:\.[0-9]+){3}', mac_address_table).group())
        sw_up.append(ip)
        print(ip)
        print('=======')



def worker():
    while True:
        ip = q.get()
        ping(ip)
        q.task_done()

q = Queue()
for i in range(64):
     t = threading.Thread(target=worker)
     t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
     t.start()

for ip in range(1,255):
    q.put(ip)

q.join()
print('{} saniye surdu'.format(time.time()-start))
for ip in sw_up:
    sheet.cell(row=int(ip), column=1).value = '10.80.0.{}'.format(ip)

wb.save('ping_sw_thread.xlsx')

