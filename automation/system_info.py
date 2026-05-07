import psutil

def get_system_stats():
    try:
        # CPU usage
        cpu = psutil.cpu_percent(interval=1)

        # RAM usage
        memory = psutil.virtual_memory()
        ram_percent = memory.percent
        total_ram = round(memory.total / (1024 ** 3), 2)  # GB
        used_ram = round(memory.used / (1024 ** 3), 2)

        # Disk usage (C drive or main drive)
        disk = psutil.disk_usage('/')
        disk_percent = disk.percent
        total_disk = round(disk.total / (1024 ** 3), 2)
        used_disk = round(disk.used / (1024 ** 3), 2)
        free_disk = round(disk.free / (1024 ** 3), 2)

        return (
            f"CPU usage is {cpu} percent. "
            f"RAM usage is {ram_percent} percent. "
            f"{used_ram} GB used out of {total_ram} GB RAM. "
            f"Disk usage is {disk_percent} percent. "
            f"{used_disk} GB used, {free_disk} GB free out of {total_disk} GB."
        )

    except Exception as e:
        print("System Stats Error:", e)
        return "Unable to fetch system stats"
    
