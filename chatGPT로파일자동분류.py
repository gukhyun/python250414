import os
import shutil

# 다운로드 폴더 경로
DOWNLOADS_DIR = r"c:\Users\student\Downloads"

# 이동할 폴더 경로 (다운로드 폴더 하위에 생성)
DEST_DIRS = {
    "images": [".jpg", ".jpeg"],
    "data": [".csv", ".xlsx"],
    "docs": [".txt", ".doc", ".pdf"],
    "archive": [".zip"]
}

def get_destination_folder(extension):
    extension = extension.lower()
    for folder, ext_list in DEST_DIRS.items():
        if extension in ext_list:
            return os.path.join(DOWNLOADS_DIR, folder)
    return None

def organize_downloads():
    for filename in os.listdir(DOWNLOADS_DIR):
        file_path = os.path.join(DOWNLOADS_DIR, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            dest_folder = get_destination_folder(ext)
            if dest_folder:
                os.makedirs(dest_folder, exist_ok=True)
                dest_path = os.path.join(dest_folder, filename)
                # 파일명이 중복될 경우 덮어쓰지 않고 이름 변경
                counter = 1
                base, extension = os.path.splitext(filename)
                while os.path.exists(dest_path):
                    dest_path = os.path.join(dest_folder, f"{base}_{counter}{extension}")
                    counter += 1
                shutil.move(file_path, dest_path)

if __name__ == "__main__":
    organize_downloads()