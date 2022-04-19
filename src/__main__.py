#!/usr/bin/python3
__version__ = '2.0'
__author__ = 'Salah Eddine Kabbour'
__package__ = " html-auto-2columns"

from ui_mainwindow import Ui_MainWindow
from ui_settings_widget import Ui_stg_form
import PySide6.QtGui as Qg
import PySide6.QtCore as Qc
import PySide6.QtWidgets as Qw
from datetime import datetime
import paths
import logging
import formatter
import qt_icons
import argparse
import sys
import os
import colorsys


LOGS_COLORS = {logging.INFO: "#206040", logging.WARNING: "#996633", logging.ERROR: "#ad1f1f"}

HELP_TEXT = """
Modify Shopify page code to add 2 columns sections. This is done by
replacing <h6> elements that contain the following texts:
###start### (or ###start_inv### to inverse columns), ###next###, ###end###.
"""


def change_lightness(in_hex_color, in_added_lightness):
    c_hex = in_hex_color.lstrip('#')
    lv = len(c_hex)
    r, g, b = tuple(int(c_hex[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    h, l, s = colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
    n_l = l + in_added_lightness
    n_l = max(0, min(1, n_l))
    r, g, b = colorsys.hls_to_rgb(h, n_l, s)
    return '#%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255))


def setup_logging(logging_lvl, save_logs_to_file):
    init_logger = logging.getLogger(__package__)
    init_logger.setLevel(logging_lvl)
    i_formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] - %(message)s', "%Y-%m-%d %H:%M:%S")
    ch = logging.StreamHandler()
    ch.setFormatter(i_formatter)
    init_logger.addHandler(ch)
    if save_logs_to_file:
        log_file_path = paths.get_logs_path(__package__)
        if os.path.exists(log_file_path):
            os.remove(log_file_path)
        handler = logging.FileHandler(log_file_path, encoding='utf8')
        n_formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] - %(message)s', "%H:%M:%S")
        handler.setFormatter(n_formatter)
        handler.setLevel(logging_lvl)
        init_logger.addHandler(handler)


class MainWindow(Qw.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.i = qt_icons.qt_icon_from_text_image(qt_icons.APP_ICON)
        self.setWindowIcon(self.i)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_settings = Ui_stg_form()
        self.ui_settings.setupUi(self.ui.wid_settings)
        self.help_msg = Qw.QMessageBox(self)
        self.setWindowTitle(__package__)
        self.thread = None
        self.downloader = None
        self.show_logs = True
        self.show_settings = True
        self.saved_settings = {
            "clear_elements": True,
            "save_origins_to_file": False,
            "save_file_path": paths.get_save_file_path(),
        }
        self.ui_settings.ledit_save_path.setText(self.saved_settings["save_file_path"])
        self.enable_disable_save_path_line_edit()
        self._style_app()
        self._connect_signals()
        self.show_hide_logs()
        self.show_hide_settings()

    def process_html(self):
        html_processor = formatter.HtmlFormatter(self)
        html_processor.log.connect(self.log)
        path = self.saved_settings["save_file_path"]
        if not self.saved_settings["save_origins_to_file"]:
            path = ""
        out = html_processor.process(self.ui.plain_text_html.toPlainText(), self.saved_settings["clear_elements"], path)
        self.ui.plain_text_processed.setPlainText(out)

    def clear_entries(self):
        self.log("Entries cleared")
        self.ui.plain_text_html.clear()
        self.ui.plain_text_processed.clear()

    def close_app(self):
        self.log("Closing app", logging.DEBUG, 5000)
        self.close()

    def show_hide_logs(self):
        if self.show_logs:
            self.show_logs = False
            self.ui.plain_text_logs.hide()
            self.ui.btn_logs.setIcon(self.i_h_logs)
        else:
            self.show_logs = True
            self.ui.plain_text_logs.show()
            self.ui.btn_logs.setIcon(self.i_s_logs)

    def save_settings(self):
        self.saved_settings["clear_elements"] = self.ui_settings.cbox_clear_elements.isChecked()
        self.saved_settings["save_origins_to_file"] = self.ui_settings.cbox_save_origins.isChecked()
        self.saved_settings["save_file_path"] = self.ui_settings.ledit_save_path.text()
        self.enable_disable_save_path_line_edit()
        self.show_hide_settings()
        self.log("Saved new Settings")

    def cancel_settings(self):
        self.ui_settings.cbox_clear_elements.setChecked(self.saved_settings["clear_elements"])
        self.ui_settings.cbox_save_origins.setChecked(self.saved_settings["save_origins_to_file"])
        self.ui_settings.ledit_save_path.setText(self.saved_settings["save_file_path"])
        self.enable_disable_save_path_line_edit()
        self.show_hide_settings()
        self.log("Cancel all changes to Settings")

    def enable_disable_save_path_line_edit(self):
        if self.ui_settings.cbox_save_origins.isChecked():
            self.ui_settings.wid_save_path.setDisabled(False)
        else:
            self.ui_settings.wid_save_path.setDisabled(True)

    def show_hide_settings(self):
        if self.show_settings:
            self.show_settings = False
            self.ui.btn_settings.setDisabled(False)
            self.ui.btn_settings.setDown(False)
            self.ui.wid_settings.hide()
            self.ui.wid_html.show()
        else:
            self.show_settings = True
            self.ui.btn_settings.setDisabled(True)
            self.ui.btn_settings.setDown(True)
            self.ui.wid_settings.show()
            self.ui.wid_html.hide()

    def _connect_signals(self):
        self.ui.btn_process.clicked.connect(self.process_html)
        self.ui.btn_clear.clicked.connect(self.clear_entries)
        self.ui.btn_settings.clicked.connect(self.show_hide_settings)
        self.ui.btn_quit.clicked.connect(self.close_app)
        self.ui.btn_logs.clicked.connect(self.show_hide_logs)
        self.ui.btn_help.clicked.connect(self.help_msg.exec)

        self.ui_settings.cbox_save_origins.clicked.connect(self.enable_disable_save_path_line_edit)
        self.ui_settings.btn_ok.clicked.connect(self.save_settings)
        self.ui_settings.btn_cancel.clicked.connect(self.cancel_settings)
        # Qc.QObject.connect(self.ui.btn_process, Qc.SIGNAL("clicked()"), self.process_link())

    def _style_app(self):
        self.Buttons_list = [self.ui.btn_process, self.ui.btn_quit, self.ui.btn_clear, self.ui.btn_help,
                             self.ui.btn_logs, self.ui.btn_settings,
                             self.ui_settings.btn_ok, self.ui_settings.btn_cancel]
        for button in self.Buttons_list:
            btn_color = button.palette().color(Qg.QPalette.Button).name()
            button.setStyleSheet(self._generate_button_stylesheet(change_lightness(btn_color, -0.05)))

        self.i_stg = qt_icons.qt_icon_from_text_image(qt_icons.SETTINGS_ICON)
        self.ui.btn_settings.setIcon(self.i_stg)

        self.i_s_logs = qt_icons.qt_icon_from_text_image(qt_icons.SHOW_LOGS_ICON)
        self.i_h_logs = qt_icons.qt_icon_from_text_image(qt_icons.CLOSE_LOGS_ICON)
        self.ui.btn_logs.setIcon(self.i_s_logs)

        self.i_pro = qt_icons.qt_icon_from_text_image(qt_icons.PROCESS_ICON)
        self.ui.btn_process.setIcon(self.i_pro)
        #
        self.i_q = qt_icons.qt_icon_from_text_image(qt_icons.EXIT_ICON)
        self.ui.btn_quit.setIcon(self.i_q)

        self.i_c = qt_icons.qt_icon_from_text_image(qt_icons.CLEAR_ICON)
        self.ui.btn_clear.setIcon(self.i_c)
        self.ui_settings.btn_cancel.setIcon(self.i_c)
        #
        self.i_h = qt_icons.qt_icon_from_text_image(qt_icons.INFO_ICON)
        self.ui.btn_help.setIcon(self.i_h)

        self.i_sv = qt_icons.qt_icon_from_text_image(qt_icons.SAVE_ICON)
        self.ui_settings.btn_ok.setIcon(self.i_sv)

        # message box
        # self.help_msg.setStyleSheet("color: red; background-color: green;")
        self.help_msg.setWindowTitle("About page")
        self.help_msg.setText(HELP_TEXT)

    @Qc.Slot()
    def log(self, msg, log_lvl=logging.INFO, time=5000):
        logger = logging.getLogger(__package__)
        logger.log(log_lvl, msg)
        if log_lvl == logging.INFO or log_lvl == logging.WARNING or log_lvl == logging.ERROR:

            bar_msg = " " + msg.capitalize()
            now = datetime.now()
            ui_log = "<span>[<span style='color: {};'>{}</span>] [{}] - {}</span>"
            keys = {logging.INFO: "INFO", logging.WARNING: "WARN", logging.ERROR: "ERROR"}
            self.ui.plain_text_logs.appendHtml(ui_log.format(LOGS_COLORS[log_lvl],
                                                             keys[log_lvl],
                                                             now.strftime("%H:%M:%S"),
                                                             msg.capitalize()))
            s_font = self.ui.statusbar.font()
            self.ui.statusbar.setStyleSheet(f"color: {LOGS_COLORS[log_lvl]}")
            self.ui.statusbar.setFont(s_font)
            self.ui.statusbar.showMessage(bar_msg, time)

    @staticmethod
    def _generate_button_stylesheet(hex_color):
        c = hex_color
        lighter_c = change_lightness(c, 0.1)
        light_c = change_lightness(c, 0.05)
        dark_c = change_lightness(c, -0.05)
        darker_c = change_lightness(c, -0.15)

        ss = ""
        ss += "QPushButton {"
        ss += f"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 {light_c}, stop:1 {c});"
        ss += f"border-radius:3px; border: solid {darker_c}; "
        ss += "border-width: 1px 2px 2px 1px;"
        ss += "padding: 10px 15px 10px 15px;"
        ss += "}"
        ss += "QPushButton:hover {"
        ss += f"background-color: qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 {lighter_c}, stop:1 {light_c});"
        ss += "}"
        ss += f"QPushButton:pressed {{background-color: {dark_c};}}"
        ss_tb = ss.replace("QPushButton", "QToolButton")
        ss_tb = ss_tb.replace("padding: 10px 15px 10px 15px;", "padding: 7px 7px 7px 7px;")
        # print(ss_tb)
        return ss + ss_tb


def boolean_string(s):
    if s not in {'False', 'True'}:
        raise ValueError('Not a valid boolean string')
    return s == 'True'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description='Download links from a specific website')
    parser.add_argument('-s', '--style', help='Qt application style', type=str,
                        default="Fusion", metavar='\b')
    parser.add_argument('-l', '--log_level', help='FATAL = 50, ERROR = 40, WARNING = 30, INFO = 20, DEBUG = 10, '
                                                  'NOTSET = 0', type=int, default=20, metavar='\b')
    parser.add_argument('-k', '--style_keys', help='Show available styles for Qt application', type=boolean_string,
                        default=False, metavar='\b')
    parser.add_argument('-f', '--logs_file', help='Output logs to file', type=boolean_string,
                        default=False, metavar='\b')
    args = parser.parse_args()

    if args.style_keys:
        print(Qw.QStyleFactory.keys())
        exit(0)

    # Initiate logger
    setup_logging(args.log_level, args.logs_file)

    # initiate App
    app = Qw.QApplication(sys.argv)
    app.setStyle(args.style)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())
