import os
import subprocess
import time

proc = subprocess.Popen(["sudo", "./raspberrypi_video"])
time.sleep(2)
print('OK')
# for filename in os.listdir(os.getcwd()):   
#     #print(filename)
#     proc = subprocess.Popen(["a.exe", filename])
#     proc.wait()