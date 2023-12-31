#sudo 사용
#Mac os 시스템 정보(운영체제 버전, 시스템 아키텍처, 사용자 이름, 호스트 이름, 네트워크 정보, 디스크 사용량, 로그인된 사용자)
import os
import platform
import socket
import subprocess

def get_os_version():
    return platform.mac_ver()[0]

def get_architecture():
    return platform.architecture()[0]

def get_username():
    return os.getlogin()

def get_hostname():
    return socket.gethostname()

def get_network_info():
    return subprocess.check_output(['ifconfig']).decode()

def get_disk_usage():
    return subprocess.check_output(['df', '-h']).decode()

def get_logged_in_users():
    return subprocess.check_output(['who']).decode()

def main():
    # 'mac_result' 폴더 생성 혹은 확인
    results_folder = 'mac_result'
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    # 결과값 저장 경로를 'mac_result' 폴더 내로 지정
    result_file_path = os.path.join(results_folder, "system_information.txt")
    
    with open(result_file_path, 'w') as file:
        file.write("OS Version: " + get_os_version() + '\n')
        file.write("Architecture: " + get_architecture() + '\n')
        file.write("Username: " + get_username() + '\n')
        file.write("Hostname: " + get_hostname() + '\n\n')
        file.write("Network Info:\n" + get_network_info() + '\n')
        file.write("Disk Usage:\n" + get_disk_usage() + '\n')
        file.write("Logged-in Users:\n" + get_logged_in_users() + '\n')

    print(f"System information saved to {result_file_path}.")

if __name__ == '__main__':
    main()
