import os
import shutil


####운영체제 버전 정보 저장



source_path = "/System/Library/CoreServices/SystemVersion.plist"
destination_path = "./Mac/mac_result/SystemVersion.plist"

# 파일이 이미 존재하면 삭제
if os.path.exists(destination_path):
    os.remove(destination_path)
    print(f"Existing file '{destination_path}' removed.")

# 파일 복사
shutil.copy(source_path, destination_path)
print(f"/System/Library/CoreServices/SystemVersion.plist이 복사되었습니다.")




source_path = "/Library/Receipts/InstallHistory.plist"
destination_path= "./Mac/mac_result/InstallHistory.plist"

# 소스 디렉토리가 존재하는지 확인합니다.
if os.path.exists(destination_path):
    os.remove(destination_path)
    print(f"Existing file '{destination_path}' removed.")
try:
    shutil.copy(source_path, destination_path)
    print("Library/Receipts/InstallHistory.plist 파일이 성공적으로 복사되었습니다.")

except:
    print("에러")





source_path = "/Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist"
destination_path = "./Mac/mac_result/com.apple.airport.preferences.plist"

# 이미 존재하는 파일 삭제
if os.path.exists(destination_path):
    os.remove(destination_path)
    print(f"Existing file '{destination_path}' removed.")

# 파일 복사
shutil.copy(source_path, destination_path)
print(f"/System/Library/CoreServices/SystemVersion.plist이 복사되었습니다.")
print(f"com.apple.airport.preferences.plist이 복사되었습니다.")