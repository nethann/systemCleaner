import psutil #checks disk usage before/after cleanup
import os #nvaigate folders
import tempfile #find Windows temp directory
from ctypes import * #empty Recycle Bin 
import pathlib  #clean,safe path handling
import shutil

#Clearing recycle bin, Temp Folders, Browser Cache

folderTargets = {
    "Temp" : "%TEMP%", 
    "SystemTemp": r"C:\Windows\Temp",
    "LocalAppTemp": "%LOCALAPPDATA%\Temp",
    "BrowserCaches": r"%LOCALAPPDATA%\Google\Chrome\User",
    "RecycleBin": ""
}

class SystemCleaner: 
    def __init__(self):
        pass

    #TEMP FOLDERS
    def list_temp(self, folder_dict): 
        for name, path in folder_dict.items(): 
            if not path: 
                continue 

            else: 
                full_path = os.path.expandvars(path)
                print(f"\nContents of {name} ({full_path}):")

                try: 
                    for item in os.listdir(full_path): 
                        item_path = os.path.join(full_path, item) 
                        print(f" - {item}")
                except PermissionError: 
                    print(f" Skipped locked folder: {full_path}")

                except FileNotFoundError: 
                    print(f" Folder not found: {full_path}")

    def delete_temp(self, path): 
        for i in os.listdir(self.path): 
            file_path = os.path.join(self.path, i)
            
            try: 
                if os.path.isfile(file_path): 
                    os.remove(file_path)
                    print(f'Removed file {file_path}')
                elif os.path.isdir(file_path): 
                    shutil.rmtree(file_path)
                    print(f'Removed directory {file_path}')

            except PermissionError: 
                print(f'Skipped locked file or folder: {file_path}')


cleaner = SystemCleaner() 
# cleaner.list_temp()
cleaner.list_temp(folderTargets)
# cleaner.delete_temp()