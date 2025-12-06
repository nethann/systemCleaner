# SIMPLE SYSTEM CLEANER

## Current folders being managed
1. Temp
2. SystemTemp
3. LocalAppTemp

## Listing Temp Files
Iterates through all files and directories in the above folders and logs their contents to a scrollable UI area, handling locked or missing folders gracefully.

## Cleaning Temp Files
Iterates through the folders above and deletes all files and subdirectories, skipping locked or inaccessible items. Logs each removed file or folder in the UI.

## Cleaning Recycle Bin
Empties the Windows Recycle Bin using a system call, suppressing confirmation dialogs, progress UI, and sounds. Handles errors and logs whether the operation was successful.

## UI Features
- Built with Tkinter for a simple graphical interface.
- Buttons for:
  - Listing temp files
  - Cleaning temp files and folders
  - Cleaning the Recycle Bin
  - Quitting the application
- Scrollable log area to display operations in real-time.
- Customizable icon support for the application window.
- Packaged with PyInstaller for one-file standalone execution.
