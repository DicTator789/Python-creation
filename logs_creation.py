import logging
import logging
import psutil
import time
import os
import asyncio
from logs_colors_class import CustomFormatter



# logger = logging.basicConfig(
#     filename='app.log',
#     level=logging.DEBUG,
#     format=CustomFormatter()
# )

logger = logging.getLogger("app.log")
logger.setLevel(logging.DEBUG)


# create file handler with a higher log level
fh = logging.FileHandler('app.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(CustomFormatter())
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

ch.setFormatter(CustomFormatter())

logger.addHandler(ch)
logger.addHandler(fh)



# logging.basicConfig(level=logging.DEBUG)


async def check(usage):
    if(usage>70 and usage<80):
        logger.warning("System usage is high")  
    elif(usage>90):
        logger.critical("System usage is critical")
    else:
        logger.info("System usage is OK")

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

# time.sleep(3)
# os.system('cls' if os.name=='nt' else 'clear')




