import os
import subprocess
import sqlite3
import shutil
import sys
import psutil
from datetime import datetime
import pyfiglet

results_folder = '/mnt/c/Users/USER/Desktop/구름프로젝트3-2/Reboot3/Linux/Linux_results'
if not os.path.exists(results_folder):
    os.makedirs(results_folder)

log_file_path = os.path.join(results_folder, "authorization_log.txt")


user_input = input("이 명령어는 sudo 권한이 필요합니다. 계속하시겠습니까? (y/n): ")

if user_input.lower() == 'y':
    authorized_user = input("권한을 허용한 사용자의 이름을 입력해주세요: ")
    inspector_name = input("검사자의 이름을 입력해주세요: ")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = f"{current_time}, 검사자: {inspector_name}, 권한을 허용한 사용자: {authorized_user}\n"
    
    with open(log_file_path, "a") as log_file:
        log_file.write(log_entry)

    print(f"{authorized_user} 님이 권한을 허용했습니다.")

def execute_and_save(command, label):
    if isinstance(command, list):
        result = subprocess.run(command, stdout=subprocess.PIPE)
    else:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    
    with open(os.path.join(results_folder, f"{label.replace(' ', '_').replace('=', '')}.txt"), "w") as f:
        f.write(output)


commands_labels = {
        "Linux System Info": ['uname', '-a'],
        "Linux System Date Info": ['date'],
        "Linux Hard Clock Info": ['hwclock', '--verbose'],
        "Linux CPU Info": ['lscpu'],
        "Linux Block Device Info": ['lsblk'],
        "Linux Memory Using Info": ['free', '-h'],
        "Linux Environment Variables": ['env'],
        "Linux User Info": ['cat', '/etc/passwd', 'cat', '/etc/shadow', 'cat', '/etc/group'],
        "Linux SSH Access History Info": ['cat', '/var/log/auth.log'],
        "Linux Bash History": ['cat', '~/.bash_history'],
        "Linux Network Info": ['ip', 'addr'],
        "Linux Network Active Connections": ['netstat', '-tuln'],
        "Linux ARP Table Info": ['ip', 'neigh'],
        "Linux Iptables Rules": ['sudo', 'iptables', '-L'],
        "Linux Process Info": ['ps', 'aux'],
        "Linux Activated Services Info": ['systemctl', 'list-units', '--type=service'],
        "Linux System Startup Programs": ['systemctl', 'list-unit-files'],
        "Linux Disk Using Info": ['df', '-h'],
        "Linux Mount Files Info": ['mount'],
        "Linux PCI Connecting Device Info": ['lspci'],
        "Linux Trash Info": ['ls', '~/.local/share/Trash/files/'],
        "Linux System Logs": ['cat', '/var/log/syslog'],
        "Linux Kernel Logs": ['cat', '/var/log/kern.log'],
        "Linux Boot Logs": ['cat', '/var/log/boot.log'],
        "Linux Daemon Logs": ['cat', '/var/log/daemon.log'],
        "Linux Cron Jobs": ['cat', '/etc/crontab', 'ls', '/var/spool/cron/'],
        "Linux SELinux Logs": ['cat', '/var/log/audit/audit.log'],
        "Linux Web Server Logs": ['cat', '/var/log/apache2/access.log', 'cat', '/var/log/apache2/error.log'],
        "Linux Mail Server Logs": ['cat', '/var/log/mail.log'],
        "Linux USB Logs": ['dmesg', '|', 'grep', 'usb']
}
    
for label, command in commands_labels.items():
    execute_and_save(command, label)    
 
def gather_all_info():
    print("Gathering all Linux system info...")
    for label, command in commands_labels.items():
        execute_and_save(command, label)

def is_browser_running(browser_name=None):
    if browser_name is None:
        browser_name = input("Enter browser name to check if it's running: ").lower()
    print(f"Checking if {browser_name} is running...")
   
    for process in psutil.process_iter():
        try:
            if browser_name in process.name().lower():
                print(f"{browser_name} is running.")
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    print(f"{browser_name} is not running.")
    return False

def tcpdump_collection():
    print("Collecting TCPDump data...")
    
    if os.geteuid() != 0:
        print("이 스크립트는 루트 권한으로 실행되어야 합니다.")
        return

def tcpdump_collection():
    print("Collecting TCPDump data...")
    
    if os.geteuid() != 0:
        print("이 스크립트는 루트 권한으로 실행되어야 합니다.")
        return

    tcpdump_cmd = ["tcpdump", "-c", "50"]  
    try:
        packet_data = subprocess.run(tcpdump_cmd, stdout=subprocess.PIPE, text=True).stdout
    except Exception as e:
        packet_data = str(e)

    file_path = os.path.join(results_folder, "TCPDump_Collection.txt")
    with open(file_path, "w") as file:
        file.write(packet_data)

def collect_antivirus_logs():
    print("Collecting antivirus logs...")    
    logs_to_collect = {
        "ClamAV": "/var/log/clamav/clamav.log",
        "Sophos": "/var/log/sophos.log",
        "ESET": "/var/log/eset.log",
        "Bitdefender": "/var/log/bitdefender.log",
        "Avira": "/var/log/avira.log",
        "F-Prot": "/var/log/f-prot.log",
        "chkrootkit": "/var/log/chkrootkit.log",
    }

    collected_logs = {}
    
    for antivirus, log_path in logs_to_collect.items():
        try:
            with open(log_path, 'r') as log_file:
                collected_logs[antivirus] = log_file.read()
            print(f"{antivirus} logs collected successfully.")
        except FileNotFoundError:
            print(f"{antivirus} log file not found.")
        except Exception as e:
            print(f"An error occurred while collecting {antivirus} logs: {str(e)}")
    
    file_path = os.path.join(results_folder, "Antivirus_Logs.txt")
    with open(file_path, "w") as file:
        for antivirus, log in collected_logs.items():
            file.write(f"{antivirus} logs:\n{log}\n")

def linux_main():
    while True:
        print("1. Linux Various Info")
        print("2. Browser Running Check")
        print("3. TCPDump Collection")
        print("4. Antivirus Logs")
        print("0. Exit")

        choice = input("Enter the number of the feature you want to execute: ")

        if choice == '1':
            gather_all_info()
        elif choice == '2':
            is_browser_running()
        elif choice == '3':
            tcpdump_collection()
        elif choice == '4':
            collect_antivirus_logs()
        elif choice == '0':
            print("Exiting LINUX_ALL.py and returning to main menu...")
            break
        else:
            print("Invalid choice. Please enter a valid number.")

if __name__ == "__main__":
    if user_input.lower() == 'y':
        linux_main()
    else:
        print("사용자가 권한 부여를 거부했습니다. 스크립트를 종료합니다.")
        exit(1)
