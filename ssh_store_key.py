import os,sys
import subprocess
import time

# result = subprocess.run('dir', stdout=subprocess.PIPE)
# print(result)

#os.system('echo y | plink 10.80.0.6 -l amerikan -pw Vkv@hSwMng4!')
#os.system('putty 10.80.0.6 -l amerikan -pw Vkv@hSwMng4!')
#os.system('plink 10.80.0.5 -l amerikan -pw Vkv@hSwMng4!')
time.sleep(4)
start = time.time()
for i in range(43,255):
    time_anchor = time.time()
    print("Şu anda {}/255 sw'deyim, {} kaldı.".format(i, 255-i))

    time.sleep(2)
    subprocess.Popen("sw_pass_automation.ahk {}".format(3), shell=True, stdout=subprocess.PIPE)
    time.sleep(3)

    print("{} saniyedir çalışıyor.".format(round(time.time() - start)))
    print("Bu işlem {} saniye sürdü.\n\n\n".format(round(time.time()-time_anchor)))



print("{} saniye sürdü".format(round(time.time() - start)))
print("\n\n\n\n\nBy Yalin")