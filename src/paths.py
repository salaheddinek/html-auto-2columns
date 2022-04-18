import os


def get_working_dir():
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
