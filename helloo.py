import psutil
import time
import os


#Memory used by this python script
pid = os.getpid()
python_process = psutil.Process(pid)
print('Memory used by this python script in MB : ',round(python_process.memory_info()[0]/2**20,2),'MB')


#CPU usage
cpu_usage = psutil.cpu_percent(interval=1)
print('CPU usage : ',cpu_usage)


#Ram usage
ram_usage = psutil.virtual_memory().percent
print('RAM usage : ',ram_usage)

disk_usage = psutil.disk_usage('/')
print('Disk usage current drive : ',disk_usage.percent)

disk_partition = psutil.disk_partitions()

#all the disk usage
for part in disk_partition:

    usage = psutil.disk_usage(part.mountpoint)
    print(part.device, usage.percent)




time.sleep(1)
# os.system('cls' if os.name=='nt' else 'clear')
# print('physical memory useD:',)




#graphiocal bar of the cpu and ram usage

# from tqdm import tqdm
# from time import sleep
# import psutil

# with tqdm(total=100, desc='cpu%', position=0) as cpubar, tqdm(total=100, desc='ram%', position=1) as rambar:
#     while True:
#         rambar.n = psutil.virtual_memory().percent
#         cpubar.n = psutil.cpu_percent()
#         rambar.refresh()
#         cpubar.refresh()
#         sleep(0.5)
#         break
