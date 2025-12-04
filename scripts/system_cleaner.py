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
    "BrowserCaches": r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache",
    "RecycleBin": ""
}

class SystemCleaner: 
    def __init__(self):
        pass

    #LISTING FOLDERS
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

    #DELETING TEMP 
    def delete_temp(self, folder_dict): 
        for name, path in folder_dict.items(): 

            if not path: 
                continue

            else: 
                full_path = os.path.expandvars(path)
                print(f"\nDeleting contents of {name} ({full_path}):")

                try: 
                    for item in os.listdir(full_path): 
                        item_path = os.path.join(full_path, item)
                        try: 
                            if os.path.isfile(item_path): 
                                os.remove(item_path)
                                print(f"Removed file: {item_path}")
                            elif os.path.isdir(item_path): 
                                shutil.rmtree(item_path)
                                print(f"Removed directory: {item_path}")
                        except PermissionError:
                            print(f"Skipped locked items: {item_path}")
                except PermissionError:
                    print(f"Skipped locked folder: {full_path}")
                except FileNotFoundError:
                    print(f"Folder not found: {full_path}")

cleaner = SystemCleaner() 
# cleaner.list_temp(folderTargets)
cleaner.delete_temp(folderTargets)
