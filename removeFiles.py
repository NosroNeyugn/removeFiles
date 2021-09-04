import time
import os
import shutil
def main():
    path="/PATH_TO_DELETE"
    days=30
    deleted_folders_count=0
    deleted_files_count=0
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            if seconds>=get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deleted_folders_count=deleted_folders_count+1
                break
            else:
                for folder in folders:
                    folder_path=os.path.join(root_folder,folder)
                    if seconds>=get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deleted_folders_count=deleted_folders_count+1
                for file in files:
                    file_path=os.path.join(root_folder,file)
                    if seconds>=get_file_or_folder_age(file_path):
                        remove_folder(file_path)
                        deleted_file_count=deleted_file_count+1
    else:
        print(f'"{path}"is not found')
        deleted_files_count=deleted_files_count+1

    print(f"Total Folders Deleted: {deleted_folders_count}")
    print(f"Total Files Deleted: {deleted_files_count}")
    
def remove_folder(path):
    if not shutil.rmtree(path):
        print(f"{path} was removed successfully")
    else:
        print(f"Unable to delete {path}")

def remove_file(path):
    if not os.remove(path):
        print(f"{path} was removed successfully")
    else:
        print(f"Unable to delete {path}")

def get_file_or_folder_age(path):
    ctime=os.stat(path).st_ctime
    return ctime

if __name__=='_main_':
    main()