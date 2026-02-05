import logging
import psutil
import time
import os
import asyncio


logging.basicConfig(level=logging.INFO)


async def check(usage):
    if(usage>80 and usage<90):
        logging.warning("System is OK")  
    elif(usage>90):
        logging.critical("System is critical")
    else:
        logging.info("System is OK")

async def main():
    #Memory used by this python script
    pid = os.getpid()
    python_process = round(psutil.Process(pid).memory_info()[0]/2**30,2)
    print('Memory used by this python script in GB : ',python_process,'GB')
    await check(python_process)

    #CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print('CPU usage : ',cpu_usage)
    await check(cpu_usage)

    #Ram usage
    ram_usage = psutil.virtual_memory().percent
    print('RAM usage : ',ram_usage)
    await check(ram_usage)

    #Disk usage for current drive
    disk_usage = psutil.disk_usage('/')
    print('Disk usage current drive : ',disk_usage.percent)

    #all the disk usage
    print('Disk usage All drives : ')
    disk_partition = psutil.disk_partitions()
    for part in disk_partition:
        try:
            usage = psutil.disk_usage(part.mountpoint)
            print(part.device, usage.percent)
            await check(usage.percent)
        except PermissionError:
            pass

asyncio.run(main())

time.sleep(3)
os.system('cls' if os.name=='nt' else 'clear')
print('physical memory useD:',)




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
