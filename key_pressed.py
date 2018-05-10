from msvcrt import getch
import sys

while True:
    key = getch()
    #print('',end=key.decode('utf-8'))
    sys.stdout.flush()

    print(ord(key))
    #print(key.decode('ASCII'))
    if ord(key) == 97: #ESC
        break
    if ord(key) == 224:  # ESC
        print('Function key')
        key = getch()
        print(str(ord(key))+'******')
