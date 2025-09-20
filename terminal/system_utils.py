import psutil

def cpu(*args):
    print(f"CPU Usage: {psutil.cpu_percent()}%")

def mem(*args):
    mem = psutil.virtual_memory()
    print(f"Memory Usage: {mem.percent}%")

def ps(*args):
    for proc in psutil.process_iter(['pid', 'name']):
        print(f"{proc.info['pid']} - {proc.info['name']}")

system_command_map = {
    "cpu": cpu,
    "mem": mem,
    "ps": ps,
}
