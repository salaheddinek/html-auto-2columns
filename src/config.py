import sys
import os
import logging


HELP_TEXT = """
Modify HTML page code to add 2 columns sections. Examples can be found in our GitHub page:
<a href="https://github.com/salaheddinek/html-auto-2columns">https://github.com/salaheddinek/html-auto-2columns</a>


Following these steps will get the desired <b>results</b>: 

1. Copy the CSS code to your website, this need to be done only once.

2. Insert <h6> titles with the according tags in order to wrap the sections that need to be formatted:

    <u>* For direct 2 columns section insert:</u>
        - <h6> ... ###start### ... </h6>
        - Followed by the content of the first columns.
        - Followed by <h6> ... ###next### ... </h6>.
        - Followed by the content of the second column
        - Followed  by <h6> ... ###end### ... </h6>.

   <u>* For opposite sides 2 columns:</u>
        - <h6> ... ###start_inv### ... </h6>
        - Followed by the content of the second columns.
        - Followed by <h6> ... ###next### ... </h6>.
        - Followed by the content of the first column
        - Followed  by <h6> ... ###end### ... </h6>.

3. Copy the source HTML code and paste it in the application Original HTML text entry.

4. Click on <b>PROCESS</b> button.

5. Copy the result HTML code and replace the original one on the website
"""

USE_WORKING_DIR = False


def get_working_dir(use_current_working_dir=USE_WORKING_DIR):
    if use_current_working_dir:
        return os.getcwd()
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


def get_config_file_path(package_name):
    exe_dir = get_working_dir()
    return os.path.join(exe_dir, package_name + "_config.json")


def get_logs_path(package_name):
    parent_path = get_working_dir()
    return os.path.join(parent_path, package_name + ".log")


def get_save_file_path():
    parent_path = get_working_dir()
    return os.path.join(parent_path, "original_html_texts.txt")


def get_default_settings():
    default_settings = {
            "clear_elements": True,
            "save_origins_to_file": False,
            "save_file_path": get_save_file_path(),
            "indent_length": 4,
            "pre_proc_clear_shopify_tags": False,
            "pre_proc_unwrap_without_class": False,
            "pre_proc_unwrap_without_class_affected": ["div", "span"],
            "pre_proc_remove_attributes": False,
            "pre_proc_remove_attributes_affected": ["p", "span", "strong", "b", "div", "u", "em", "h1", "h2", "br"],
            "pre_proc_unwrap_no_content": False,
            "pre_proc_unwrap_no_content_affected": ["strong", "em", "u", "i", "span", "div"],
            "pre_proc_group_consecutive": False,
            "pre_proc_group_consecutive_affected": ["span", "strong", "em", "u", "i", "b"],
        }
    return default_settings


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
