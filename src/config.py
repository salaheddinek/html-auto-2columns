import sys
import os
import logging


HELP_TEXT = """
Modify Shopify page code to add 2 columns sections. This is done by
replacing <h6> elements that contain the following texts:
###start### (or ###start_inv### to inverse columns), ###next###, ###end###.
"""


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


def setup_logging(logger_name, logging_lvl, save_logs_to_file):
    init_logger = logging.getLogger(logger_name)
    init_logger.setLevel(logging_lvl)
    i_formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] - %(message)s', "%Y-%m-%d %H:%M:%S")
    ch = logging.StreamHandler()
    ch.setFormatter(i_formatter)
    init_logger.addHandler(ch)
    if save_logs_to_file:
        log_file_path = get_logs_path(logger_name)
        if os.path.exists(log_file_path):
            os.remove(log_file_path)
        handler = logging.FileHandler(log_file_path, encoding='utf8')
        n_formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] - %(message)s', "%Y-%m-%d %H:%M:%S")
        handler.setFormatter(n_formatter)
        handler.setLevel(logging_lvl)
        init_logger.addHandler(handler)
