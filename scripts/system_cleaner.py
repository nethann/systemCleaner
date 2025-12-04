import os
import ctypes
import shutil

# Folder targets
folderTargets = {
    "Temp": "%TEMP%",
    "SystemTemp": r"C:\Windows\Temp",
    "LocalAppTemp": "%LOCALAPPDATA%\Temp",
    "BrowserCaches": r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache",
}

class SystemCleaner:
    def __init__(self):
        self.shell32 = ctypes.windll.shell32

    def list_temp_files(self):
        logs = []
        for name, path in folderTargets.items():
            full_path = os.path.expandvars(path)
            logs.append(f"\nContents of {name} ({full_path}):")
            try:
                for item in os.listdir(full_path):
                    logs.append(f" - {item}")
            except PermissionError:
                logs.append(f"Skipped locked folder: {full_path}")
            except FileNotFoundError:
                logs.append(f"Folder not found: {full_path}")
        return logs

    def clean_temp_files(self):
        logs = []
        for name, path in folderTargets.items():
            full_path = os.path.expandvars(path)
            logs.append(f"\nDeleting contents of {name} ({full_path}):")
            try:
                for item in os.listdir(full_path):
                    item_path = os.path.join(full_path, item)
                    try:
                        if os.path.isfile(item_path):
                            os.remove(item_path)
                            logs.append(f"Removed file: {item_path}")
                        elif os.path.isdir(item_path):
                            shutil.rmtree(item_path)
                            logs.append(f"Removed directory: {item_path}")
                    except PermissionError:
                        logs.append(f"Skipped locked item: {item_path}")
            except PermissionError:
                logs.append(f"Skipped locked folder: {full_path}")
            except FileNotFoundError:
                logs.append(f"Folder not found: {full_path}")
        return logs

    def clean_recycle_bin(self):
        SHERB_NOCONFIRMATION = 0x00000001
        SHERB_NOPROGRESSUI   = 0x00000002
        SHERB_NOSOUND        = 0x00000004
        flags = SHERB_NOCONFIRMATION | SHERB_NOPROGRESSUI | SHERB_NOSOUND

        result = self.shell32.SHEmptyRecycleBinW(None, None, flags)
        if result != 0:
            return [f"Failed to empty Recycle Bin. Error {hex(result)}"]
        else:
            return ["Emptied Recycle Bin!"]
