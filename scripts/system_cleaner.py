
import os 
import ctypes 
import shutil
import psutil

#Clearing recycle bin, Temp Folders, Browser Cache
folderTargets = {
    "Temp" : "%TEMP%", 
    "SystemTemp": r"C:\Windows\Temp",
    "LocalAppTemp": "%LOCALAPPDATA%\Temp",
    "BrowserCaches": r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache",
}

class SystemCleaner: 
    def __init__(self):
        self.shell32 = ctypes.windll.shell32  

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

    def clean_recyclew(self): 
        SHERB_NOCONFIRMATION = 0x00000001
        SHERB_NOPROGRESSUI   = 0x00000002
        SHERB_NOSOUND        = 0x00000004

        flags = SHERB_NOCONFIRMATION | SHERB_NOPROGRESSUI | SHERB_NOSOUND

        result = self.shell32.SHEmptyRecycleBinW(
            None,
            None,
            flags
        )

        if result != 0: 
            print(f"Failed to empty Bin. Error {hex(result)}")
        else: 
            print("Emptied Bin!")


cleaner = SystemCleaner() 
# cleaner.list_temp(folderTargets)
# cleaner.delete_temp(folderTargets)
# cleaner.clean_recyclew()