from tkinter import *
from tkinter import ttk, scrolledtext
import system_cleaner

cleaner = system_cleaner.SystemCleaner()

root = Tk()
root.geometry("800x800")
root.resizable(False, False)

style = ttk.Style()
style.configure("Big.TButton", font=("Arial", 13), padding=10)

frm = ttk.Frame(root, padding=10)
frm.pack(expand=True)

ttk.Label(frm, text="Windows Machine Cleaner", font=("Arial", 24)).pack(pady=10)

button_width = 30

log_area = scrolledtext.ScrolledText(frm, width=80, height=20, font=("Arial", 12), state='disabled', bg='white')
log_area.pack(pady=10)

def log(messages):
    log_area.configure(state='normal')
    log_area.delete('1.0', END)  
    for message in messages:
        log_area.insert(END, message + "\n")
    log_area.see(END)
    log_area.configure(state='disabled')

def list_temp_files():
    logs = cleaner.list_temp_files()
    log(logs)

def clean_temp_files():
    logs = cleaner.clean_temp_files()
    log(logs)

def clean_recycle_bin():
    logs = cleaner.clean_recycle_bin()
    log(logs)

ttk.Button(frm, text="List Temp Files", width=button_width, style="Big.TButton", command=list_temp_files).pack(pady=5)
ttk.Button(frm, text="Clean Temp Files & Folders", width=button_width, style="Big.TButton", command=clean_temp_files).pack(pady=5)
ttk.Button(frm, text="Clean Recycle Bin", width=button_width, style="Big.TButton", command=clean_recycle_bin).pack(pady=5)
ttk.Button(frm, text="Quit", width=button_width, style="Big.TButton", command=root.destroy).pack(pady=5)

root.mainloop()
