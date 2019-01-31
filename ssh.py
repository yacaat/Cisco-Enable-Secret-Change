import subprocess, sys, pyautogui, time
from pyperclip import copy, paste


ip = "10.80.0." + sys.argv[1]
print(len(sys.argv))
password = "Vkv@hSwMng4!"

switch_passwords = {
                    '10.80.0.254': {'ssh' : 'Vkv@h91detk0c!', 'enable' : 'Eyo76re69//'},
                    '10.80.0.*': {'ssh' : 'Vkv@hSwMng4!', 'enable' : 'brcd1920'},
                    }


if ip != "10.80.0.254":
    subprocess.Popen("putty {} -l amerikan -pw {}".format(ip,'Vkv@hSwMng4!'), shell=True, stdout=subprocess.PIPE)
    time.sleep(2)
    if len(sys.argv) == 3:
        subprocess.Popen("sw_pass_automation.ahk {}".format(sys.argv[2]), shell=True, stdout=subprocess.PIPE)
    elif len(sys.argv) == 2:
        subprocess.Popen("sw_pass_automation.ahk", shell=True, stdout=subprocess.PIPE)
else:
    subprocess.Popen("putty {} -l amerikan -pw {}".format(ip, 'Vkv@h91detk0c!'), shell=True, stdout=subprocess.PIPE)
    time.sleep(2)
    if len(sys.argv) == 3:
        pass
    elif len(sys.argv) == 2:
        subprocess.Popen("bb_pass_automation.ahk", shell=True, stdout=subprocess.PIPE)

