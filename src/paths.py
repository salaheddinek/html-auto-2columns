import sys
import os


def get_working_dir():
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the PyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.
        folder_path = os.path.dirname(sys.executable)
    else:
        folder_path = os.path.dirname(os.path.abspath(__file__))
    if os.path.isfile(folder_path):
        folder_path = os.path.dirname(folder_path)
    return folder_path


def get_logs_path(package_name):
    parent_path = get_working_dir()
    return os.path.join(parent_path, package_name + ".log")


def get_save_file_path():
    parent_path = get_working_dir()
    return os.path.join(parent_path, "original_html_texts.txt")
