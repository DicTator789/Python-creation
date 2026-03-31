

from log_analyzer import log_analyzer  #refers to the class now
import asyncio
import psutil


class server:
    def __init__(self, log_file):
        self.log_analyzer = log_analyzer(log_file)

    def check_health(self):
        print("CPU:", psutil.cpu_percent(),"%")
        print("Memory",psutil.virtual_memory().percent,"%")

    def generate_report(self):
        print("generating report")
        log_data = self.log_analyzer.process_logs()

        report ={
            "CPU": psutil.cpu_percent(),
            "RAM": psutil.virtual_memory().percent,
            "logs":log_data
        }

        return report



a = server("D:\\Moltbot\\app.log")
a.check_health()
print(a.generate_report())