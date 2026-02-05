# import psutil
# import time
# import os

# pid = os.getpid()
# python_process = psutil.Process(pid)

# print('Memory used by this python script: ',python_process.memory_info()[0]/2**30)
# cpu_usage = psutil.cpu_percent(interval=1)
# print(os.name)
# time.sleep(1)
# os.system('cls' if os.name=='nt' else 'clear')
# # print('physical memory useD:',psutil.virtual_memory()[2])
# # print('physical memory useD:',psutil.virtual_memory().percent)
# # print(cpu_usage)

# Source - https://stackoverflow.com/a/69511430
# Posted by Karol Zlot, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-05, License - CC BY-SA 4.0

from tqdm import tqdm
from time import sleep
import psutil

with tqdm(total=100, desc='cpu%', position=0) as cpubar, tqdm(total=100, desc='ram%', position=1) as rambar:
    while True:
        rambar.n = psutil.virtual_memory().percent
        cpubar.n = psutil.cpu_percent()
        rambar.refresh()
        cpubar.refresh()
        sleep(0.5)
        break
