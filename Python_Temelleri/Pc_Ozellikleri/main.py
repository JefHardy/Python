import platform
import psutil

def get_cpu_info():
    cpu_info = {}
    cpu_info['processor'] = platform.processor()
    cpu_info['architecture'] = platform.machine()
    cpu_info['cpu_count'] = psutil.cpu_count(logical=False)
    cpu_info['cpu_threads'] = psutil.cpu_count(logical=True)
    return cpu_info

def get_memory_info():
    memory_info = {}
    memory = psutil.virtual_memory()
    memory_info['total'] = round(memory.total / (1024**3), 2)  # Convert to GB
    memory_info['available'] = round(memory.available / (1024**3), 2)  # Convert to GB
    memory_info['used'] = round(memory.used / (1024**3), 2)  # Convert to GB
    memory_info['percent'] = memory.percent
    return memory_info

def get_disk_info():
    disk_info = {}
    disk = psutil.disk_usage('/')
    disk_info['total'] = round(disk.total / (1024**3), 2)  # Convert to GB
    disk_info['used'] = round(disk.used / (1024**3), 2)  # Convert to GB
    disk_info['free'] = round(disk.free / (1024**3), 2)  # Convert to GB
    disk_info['percent'] = disk.percent
    return disk_info

def get_general_info():
    general_info = {}
    general_info['system'] = platform.system()
    general_info['release'] = platform.release()
    general_info['version'] = platform.version()
    return general_info

cpu_info = get_cpu_info()
memory_info = get_memory_info()
disk_info = get_disk_info()
general_info = get_general_info()

print("----- Genel Bilgiler -----")
print(f"İşletim Sistemi: {general_info['system']} {general_info['release']} {general_info['version']}")
print("\n----- CPU Bilgileri -----")
print(f"İşlemci: {cpu_info['processor']}")
print(f"Mimari: {cpu_info['architecture']}")
print(f"Çekirdek Sayısı: {cpu_info['cpu_count']}")
print(f"Thread Sayısı: {cpu_info['cpu_threads']}")
print("\n----- Bellek Bilgileri -----")
print(f"Toplam Bellek: {memory_info['total']} GB")
print(f"Kullanılabilir Bellek: {memory_info['available']} GB")
print(f"Kullanılan Bellek: {memory_info['used']} GB")
print(f"Bellek Kullanım Yüzdesi: {memory_info['percent']}%")
print("\n----- Disk Bilgileri -----")
print(f"Toplam Disk Alanı: {disk_info['total']} GB")
print(f"Kullanılan Disk Alanı: {disk_info['used']} GB")
print(f"Boş Disk Alanı: {disk_info['free']} GB")
print(f"Disk Doluluk Yüzdesi: {disk_info['percent']}%")

