import os
import shutil
import time

def remove():
    deleted_folders = 0
    deleted_files = 0

    path = "/Recycle Bin"
    days = 30

    seconds = time.time() - (days * 24 * 60 * 60)

    if os.path.exists(path):
        for folders,subfolders,files in os.walk(path):
            if seconds >= get_file_or_folder_age(subfolder):
                remove_folder(subfolder)
                deleted_folders = deleted_folders+1
                break
            else:
                for folder in folders:
                    folder_path = os.path.join(subfolder,folder)
                    if seconds >= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deleted_folders = deleted_folders+1 
                
                for file in files:
                    file_path = os.path.join(subfolder,file)
                    if seconds >= get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deleted_files = deleted_files+1
        else:
            if seconds >= get_file_or_folder_age(path):
                remove_file(path)
                deleted_files = deleted_files+1
    else:
        print(f'"{path}"is not found')
        deleted_files = deleted_files+1
    
    print(f"total deleted folders: {deleted_folders}")
    print(f"total deleted files: {deleted_files}")

def remove_folder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed successfully")
    else:
        print("Unable to delete the" +path)

def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime