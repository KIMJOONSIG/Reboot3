import os
import shutil
# 검색을 시작할 디렉토리 설정 (루트 디렉토리부터 검색하려면 'C:\\' 또는 다른 드라이브 경로로 설정)
search_directory = 'C:\\'
# 검색 대상 파일 이름
file_to_find = 'MEMORY.DMP'
# 검색 및 복사 작업
found = False  # 파일을 찾았는지 여부를 나타내는 플래그
# 사용자의 바탕화면 경로
desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
# 복사될 Memory.dmp 파일 경로
destination_path = os.path.join(desktop_path, 'Memory.dmp')
for foldername, subfolders, filenames in os.walk(search_directory):
    if file_to_find in filenames:
        found = True
        source_path = os.path.join(foldername, file_to_find)
        try:
            shutil.copy(source_path, destination_path)
            print(f"{file_to_find}를 {destination_path}로 복사 완료.")
        except PermissionError:
            print("관리자 권한이 필요합니다.")
        except Exception as e:
            print(f"파일 복사 중 오류 발생: {e}")
if not found:
    print(f"{file_to_find} 파일을 찾을 수 없습니다.")
