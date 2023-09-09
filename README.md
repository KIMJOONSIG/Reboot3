# 🌈 Team Reboot Third Project
- ☁ 구름(goorm) 정보 보호 전문가 양성 마스터 클래스 과정 1기의 goorm Team Project: 포렌식 아티팩트 수집 시스템 개발
<br>

## 📂 프로젝트 개요

- **과제 주제:** 포렌식 아티팩트 수집 시스템 개발
- **과제 기간:** 2023.08.28 ~ 2023.09.08
- **과제 설명:** 파이썬 코드와 오픈소스를 활용한 포렌식 아티팩트 수집 시스템 개발
<br>

## 🛠️ Technical Skills

### 📒 Languages
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> 

### 📗 Tools
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white"/> <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>

### 📙 Communication
<img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white"/> <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white"/> 

<br>

## 💻 조원 소개

<table>
  <tr>
    <th align="center">이름</th>
    <th align="center">역할</th>
    <th align="center">맡은 부분</th>
  </tr>
  <tr>
    <td align="center">박서경</td>
    <td align="center">조장</td>
    <th align="center">Mac OS</th>
  </tr>
    <tr>
    <td align="center">김준식</td>
    <td align="center">조원</td>
    <th align="center">Mac OS</th>
  </tr>
      <tr>
    <td align="center">김기연</td>
    <td align="center">조원</td>
    <th align="center">Windows</th>
  </tr>
  <tr>
    <td align="center">조인철</td>
    <td align="center">조원</td>
    <th align="center">Windows</th>
  </tr>
  <tr>
    <td align="center">김문정</td>
    <td align="center">조원</td>
    <th align="center">Linux</th>
  </tr>
    <tr>
    <td align="center">이근희</td>
    <td align="center">조원</td>
    <th align="center">Linux</th>
  </tr>
</table>

<br>

## 🗂️ 전체 Repository 구조

```bash
code
  └─── Reboot_all.py # 통합 포렌식 아티팩트 수집 툴
       ├── MAC_ALL.py # Mac OS 포렌식 아티팩트 툴
       ├── LINUX_ALL.py # Linux 포렌식 아티팩트 툴 
       └── reboot3.py # Windows 포렌식 아티팩트 툴
```

<br>

## 기능 구현
<table>
    <tr>
      <th>Reboot_all.py</th>
    </tr>
    <tr>
      <td valign="top"><img src="https://github.com/KIMJOONSIG/Reboot2/assets/129662947/0f02f3a9-4cc5-4497-96b3-ba41ef604f20"></td>
    </tr>
  </table> 

## 🖥️ [Mac OS](https://github.com/KIMJOONSIG/Reboot3/tree/main/Mac)
- Mac OS의 포렌식 아티팩트 수집 툴
- 주요 기능
  - Eventlog
  - Disk dump
  - Memory dump
  - System information
  - Running process
  - APFS file system
  - Recyclebin
  - Port, IP, ARP
  - Open handle
  - System log
  - Patch list
  - Enviornment
  - Documents
  - bash log
  - Propery list
  - Web history
  - launchctl list
- Mac OS Repository 구조

```bash
MAC
└─── MAC_ALL.py
     ├── Apple_APFS.py
     ├── Eventlog.py
     ├── bash_zsh_log.py
     ├── cron.py
     ├── disk_dump.py
     ├── documents.py
     ├── environment.py
     ├── launch_list.py
     ├── memory_dump.py
     ├── open_handle.py
     ├── patch_list.py
     ├── port_ip_list.py
     ├── process.py
     ├── program_cache_data.py
     ├── property_list.py
     ├── recyclebin.py
     ├── service_demon.py
     ├── system_infor.py
     └── web_history.py
  
```
- 기능 사진
  <table>
    <tr>
      <th>Mac OS</th>
    </tr>
    <tr>
      <td valign="top"><img src="https://github.com/KIMJOONSIG/Reboot2/assets/129662947/5de1544f-4f77-438a-a020-2387cb080895"></td>
    </tr>
  </table> 

## 🪟 [Windows](https://github.com/KIMJOONSIG/Reboot3/tree/main/Windows)
- Windows의 포렌식 아티팩트 수집 툴
- 주요 기능
  - Memory dump
  - Registry Hive
  - System info
  - System Group Policy
  - Event log
  - Services log
  - Hosts data
  - SRUM
  - Environment Variables
  - Patch list
  - Process List
  - Port, IP, ARP, BIOS
  - Open handle
  - System logon info
  - UserAssist
  - AutoRun
  - Registry User
  - Web History
  - Recycle Bin
  - LNK
  - PowerShell log
  - Recent Activity
  - Prefetch
  - NTFS

- Windows Repository 구조

```bash
Windows
└─── reboot3.py
  
```
- 기능 사진
  <table>
    <tr>
      <th>Windows</th>
    </tr>
    <tr>
      <td>추후 추가 예정</td>
    </tr>
  </table> 

## 🐧 [Linux](https://github.com/KIMJOONSIG/Reboot3/blob/main/Linux/LINUX_ALL.py)
- Linux의 포렌식 아티팩트 수집 툴
- 주요 기능
  -   

- Linux Repository 구조

```bash
Linux
└─── LINUX_ALL.py
  
```
- 기능 사진
  <table>
    <tr>
      <th>LINUX_ALL.py</th>
    </tr>
    <tr>
      <td>추후 추가 예정</td>
    </tr>
  </table> 
