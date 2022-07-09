#!/usr/bin/python3
__version__ = '3.2.1'
__author__ = 'Salah Eddine Kabbour'
__package__ = "html-auto-2columns"

import tree_processing
from ui_mainwindow import Ui_MainWindow
from ui_settings_widget import Ui_stg_form
import PySide6.QtGui as Qg
import PySide6.QtCore as Qc
import PySide6.QtWidgets as Qw
from datetime import datetime
import config
import logging
import formatter
import qt_icons
import argparse
import sys
import styling
import json
import os


class MainWindow(Qw.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.i = qt_icons.qt_icon_from_text_image(qt_icons.APP_ICON)
        self.setWindowIcon(self.i)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_settings = Ui_stg_form()
        self.ui_settings.setupUi(self.ui.wid_settings)
        self.setWindowTitle(__package__)
        self.thread = None
        self.downloader = None
        self.show_logs = True
        self.show_settings = True
        self.line_wrap_mode = True
        self.saved_settings = config.get_default_settings()
        stg_file_path = config.get_config_file_path(__package__)
        if os.path.isfile(stg_file_path):
            with open(stg_file_path, 'r') as fp:
                self.saved_settings = json.load(fp)
                self.log(f"Loaded Settings from file {stg_file_path}", logging.DEBUG, 5000)
        self.restore_settings_info()
        self.update_settings_window()
        self._style_app()
        self._connect_signals()
        self.show_hide_logs()
        self.show_hide_settings()

    def process_html(self):
        html_processor = formatter.HtmlFormatter(self)
        html_processor.log.connect(self.log)
        html_processor.w_msg.connect(self.window_message)
        out = html_processor.process(self.ui.plain_text_html.toPlainText(), self.saved_settings)
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
        affected_tags = []
        for txt_holder in [self.ui_settings.ledit_no_content_tags, self.ui_settings.ledit_r_class_tags,
                           self.ui_settings.ledit_r_attributes_tags, self.ui_settings.ledit_group_consecutive]:

            txt = txt_holder.text()
            for c in txt:
                if not c.isalnum() and c != " " and c != ",":
                    self.log("ERROR: affected tags should contain HTML tags separated by ','", logging.ERROR, 5000)
                    return
            cur_tags = txt.lower().split(",")
            affected_tags += [[]]
            for cur_tag in cur_tags:
                cur_tag = cur_tag.strip()
                if cur_tag != "":
                    affected_tags[-1].append(cur_tag)

        self.saved_settings["pre_proc_clear_shopify_tags"] = self.ui_settings.cbox_clear_shopify_tags.isChecked()

        self.saved_settings["pre_proc_unwrap_no_content"] = self.ui_settings.cbox_unwrap_no_content.isChecked()
        self.saved_settings["pre_proc_unwrap_no_content_affected"] = affected_tags[0]

        self.saved_settings["pre_proc_unwrap_without_class"] = self.ui_settings.cbox_unwrap_without_class.isChecked()
        self.saved_settings["pre_proc_unwrap_without_class_affected"] = affected_tags[1]

        self.saved_settings["pre_proc_remove_attributes"] = self.ui_settings.cbox_remove_attributes.isChecked()
        self.saved_settings["pre_proc_remove_attributes_affected"] = affected_tags[2]

        self.saved_settings["pre_proc_group_consecutive"] = self.ui_settings.cbox_group_consecutive.isChecked()
        self.saved_settings["pre_proc_group_consecutive_affected"] = affected_tags[3]

        self.saved_settings["indent_length"] = int(self.ui_settings.sbox_indent_length.text())

        self.saved_settings["clear_elements"] = self.ui_settings.cbox_clear_elements.isChecked()
        self.saved_settings["save_origins_to_file"] = self.ui_settings.cbox_save_origins.isChecked()
        self.saved_settings["save_file_path"] = self.ui_settings.ledit_save_path.text()
        self.restore_settings_info()
        self.update_settings_window()
        self.show_hide_settings()
        self.log("Saved new Settings")
        if self.ui_settings.cbox_save_stg.isChecked():
            settings_path = config.get_config_file_path(__package__)
            with open(settings_path, 'w') as fp:
                json.dump(self.saved_settings, fp, indent=4)
                self.log(f"Saved Settings to file {settings_path}", logging.DEBUG, 5000)

    def restore_settings_info(self):
        self.ui_settings.cbox_clear_elements.setChecked(self.saved_settings["clear_elements"])
        self.ui_settings.cbox_save_origins.setChecked(self.saved_settings["save_origins_to_file"])
        self.ui_settings.ledit_save_path.setText(self.saved_settings["save_file_path"])

        self.ui_settings.cbox_clear_shopify_tags.setChecked(self.saved_settings["pre_proc_clear_shopify_tags"])

        self.ui_settings.cbox_unwrap_no_content.setChecked(self.saved_settings["pre_proc_unwrap_no_content"])
        self.ui_settings.ledit_no_content_tags.setText(
            ", ".join(self.saved_settings["pre_proc_unwrap_no_content_affected"]))

        self.ui_settings.cbox_unwrap_without_class.setChecked(self.saved_settings["pre_proc_unwrap_without_class"])
        self.ui_settings.ledit_r_class_tags.setText(
            ", ".join(self.saved_settings["pre_proc_unwrap_without_class_affected"]))

        self.ui_settings.cbox_remove_attributes.setChecked(self.saved_settings["pre_proc_remove_attributes"])
        self.ui_settings.ledit_r_attributes_tags.setText(
            ", ".join(self.saved_settings["pre_proc_remove_attributes_affected"]))

        self.ui_settings.cbox_group_consecutive.setChecked(self.saved_settings["pre_proc_group_consecutive"])
        self.ui_settings.ledit_group_consecutive.setText(
            ", ".join(self.saved_settings["pre_proc_group_consecutive_affected"]))

        self.ui_settings.sbox_indent_length.setValue(self.saved_settings["indent_length"])

    def cancel_settings(self):
        self.restore_settings_info()
        self.update_settings_window()
        self.show_hide_settings()
        self.log("Cancel all changes to Settings")

    def update_settings_window(self):
        if self.ui_settings.cbox_save_origins.isChecked():
            self.ui_settings.wid_save_path.setDisabled(False)
        else:
            self.ui_settings.wid_save_path.setDisabled(True)

        if self.ui_settings.cbox_unwrap_without_class.isChecked():
            self.ui_settings.ledit_r_class_tags.setDisabled(False)
        else:
            self.ui_settings.ledit_r_class_tags.setDisabled(True)

        if self.ui_settings.cbox_remove_attributes.isChecked():
            self.ui_settings.ledit_r_attributes_tags.setDisabled(False)
        else:
            self.ui_settings.ledit_r_attributes_tags.setDisabled(True)

        if self.ui_settings.cbox_unwrap_no_content.isChecked():
            self.ui_settings.ledit_no_content_tags.setDisabled(False)
        else:
            self.ui_settings.ledit_no_content_tags.setDisabled(True)

        if self.ui_settings.cbox_group_consecutive.isChecked():
            self.ui_settings.ledit_group_consecutive.setDisabled(False)
        else:
            self.ui_settings.ledit_group_consecutive.setDisabled(True)

    def show_hide_settings(self):
        if self.show_settings:
            self.show_settings = False
            self.ui.btn_settings.setDisabled(False)
            self.ui.wid_settings.hide()
            self.ui.btn_indent.show()
            self.ui.btn_compact.show()
            self.ui.wid_html.show()
        else:
            self.show_settings = True
            self.ui.btn_settings.setDisabled(True)
            self.ui.btn_indent.hide()
            self.ui.btn_compact.hide()
            self.ui.wid_html.hide()
            self.ui.wid_settings.show()

    def change_save_path(self):
        name = Qw.QFileDialog.getSaveFileName(self, 'Save File', dir=config.get_save_file_path())
        name = name[0]
        if name != "":
            self.ui_settings.ledit_save_path.setText(name)

    def copy_to_clipboard(self):
        clipboard = Qg.QClipboard()
        processed_html = self.ui.plain_text_processed.toPlainText()
        clipboard.setText(tree_processing.clear_spaces(processed_html))
        self.log("Copied processed HTML text to clipboard")

    def compact_html_text(self):
        processed_html = self.ui.plain_text_processed.toPlainText()
        self.ui.plain_text_processed.setPlainText(tree_processing.clear_spaces(processed_html))

        plain_text_html = self.ui.plain_text_html.toPlainText()
        self.ui.plain_text_html.setPlainText(tree_processing.clear_spaces(plain_text_html))

    def indent_html_text(self):
        processed_html = tree_processing.clear_spaces(self.ui.plain_text_processed.toPlainText())
        self.ui.plain_text_processed.setPlainText(tree_processing.prettify2(processed_html,
                                                                            self.saved_settings["indent_length"]))

        plain_text_html = tree_processing.clear_spaces(self.ui.plain_text_html.toPlainText())
        self.ui.plain_text_html.setPlainText(tree_processing.prettify2(plain_text_html,
                                                                       self.saved_settings["indent_length"]))

    def _connect_signals(self):
        self.ui.btn_process.clicked.connect(self.process_html)
        self.ui.btn_clear.clicked.connect(self.clear_entries)
        self.ui.btn_settings.clicked.connect(self.show_hide_settings)
        self.ui.btn_quit.clicked.connect(self.close_app)
        self.ui.btn_logs.clicked.connect(self.show_hide_logs)
        self.ui.btn_help.clicked.connect(self.display_about_page)
        self.ui.btn_copy.clicked.connect(self.copy_to_clipboard)

        self.ui.btn_compact.clicked.connect(self.compact_html_text)
        self.ui.btn_indent.clicked.connect(self.indent_html_text)
        self.ui.btn_wrap.clicked.connect(self.toggle_line_wrap_mode)

        self.ui_settings.cbox_save_origins.clicked.connect(self.update_settings_window)
        self.ui_settings.cbox_unwrap_no_content.clicked.connect(self.update_settings_window)
        self.ui_settings.cbox_remove_attributes.clicked.connect(self.update_settings_window)
        self.ui_settings.cbox_unwrap_without_class.clicked.connect(self.update_settings_window)
        self.ui_settings.cbox_group_consecutive.clicked.connect(self.update_settings_window)

        self.ui_settings.btn_ok.clicked.connect(self.save_settings)
        self.ui_settings.btn_cancel.clicked.connect(self.cancel_settings)
        self.ui_settings.btn_change.clicked.connect(self.change_save_path)

    def toggle_line_wrap_mode(self):
        if self.line_wrap_mode:
            self.line_wrap_mode = False
            self.ui.btn_wrap.setIcon(self.i_wn)
            self.ui.plain_text_html.setLineWrapMode(Qw.QPlainTextEdit.LineWrapMode.NoWrap)
            self.ui.plain_text_processed.setLineWrapMode(Qw.QPlainTextEdit.LineWrapMode.NoWrap)
        else:
            self.line_wrap_mode = True
            self.ui.btn_wrap.setIcon(self.i_w)
            self.ui.plain_text_html.setLineWrapMode(Qw.QPlainTextEdit.LineWrapMode.WidgetWidth)
            self.ui.plain_text_processed.setLineWrapMode(Qw.QPlainTextEdit.LineWrapMode.WidgetWidth)

    def _style_app(self):
        self.Buttons_list = [self.ui.btn_process, self.ui.btn_quit, self.ui.btn_clear, self.ui.btn_help,
                             self.ui.btn_logs, self.ui.btn_settings, self.ui.btn_copy, self.ui_settings.btn_change,
                             self.ui_settings.btn_ok, self.ui_settings.btn_cancel, self.ui.btn_compact,
                             self.ui.btn_indent]
        for button in self.Buttons_list:
            btn_color = button.palette().color(Qg.QPalette.Button).name()
            button.setStyleSheet(styling.generate_button_stylesheet(btn_color))

        self.Tool_Buttons_list = [self.ui.btn_help, self.ui.btn_logs, self.ui.btn_settings, self.ui.btn_wrap]
        for button in self.Tool_Buttons_list:
            btn_color = button.palette().color(Qg.QPalette.Button).name()
            button.setStyleSheet(styling.generate_tool_button_stylesheet(btn_color))

        frames = [self.ui.plain_text_logs, self.ui.plain_text_html, self.ui.plain_text_processed]
        for frame in frames:
            frame.setStyleSheet(styling.generate_frame_stylesheet(styling.COLORS["entry_bg"]))

        line_edits = [self.ui_settings.ledit_save_path, self.ui_settings.ledit_r_class_tags,
                      self.ui_settings.ledit_r_attributes_tags, self.ui_settings.ledit_no_content_tags,
                      self.ui_settings.ledit_group_consecutive, ]
        for line_edit in line_edits:
            line_edit.setStyleSheet(styling.generate_line_edit_stylesheet(styling.COLORS["entry_bg"]))

        self.ui.frame.setStyleSheet(styling.generate_frame_stylesheet())

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

        self.i_cp = qt_icons.qt_icon_from_text_image(qt_icons.COPY_ICON)
        self.ui.btn_copy.setIcon(self.i_cp)

        self.i_c = qt_icons.qt_icon_from_text_image(qt_icons.CLEAR_ICON)
        self.ui.btn_clear.setIcon(self.i_c)
        self.ui_settings.btn_cancel.setIcon(self.i_c)
        #
        self.i_h = qt_icons.qt_icon_from_text_image(qt_icons.INFO_ICON)
        self.ui.btn_help.setIcon(self.i_h)

        self.i_sv = qt_icons.qt_icon_from_text_image(qt_icons.SAVE_ICON)
        self.ui_settings.btn_ok.setIcon(self.i_sv)

        self.i_ch = qt_icons.qt_icon_from_text_image(qt_icons.CHANGE_ICON)
        self.ui_settings.btn_change.setIcon(self.i_ch)

        self.i_t = qt_icons.qt_icon_from_text_image(qt_icons.TREE_ICON)
        self.ui.btn_indent.setIcon(self.i_t)

        self.i_f = qt_icons.qt_icon_from_text_image(qt_icons.FLOW_ICON)
        self.ui.btn_compact.setIcon(self.i_f)

        self.i_w = qt_icons.qt_icon_from_text_image(qt_icons.LINE_WRAP_ICON)
        self.ui.btn_wrap.setIcon(self.i_w)

        self.i_wn = qt_icons.qt_icon_from_text_image(qt_icons.LINE_WRAP_OFF_ICON)

    def display_about_page(self):
        text = f'<div style="text-align:center"><h1>{__package__}</h1><small>v{__version__}</small></div>'
        text += config.HELP_TEXT
        self.window_message(text, "About page")

    @Qc.Slot()
    def window_message(self, msg, title="Info", minimum_width=800, minimum_height=900):
        txt = msg.replace("<h6>", "&lt;h6&gt;")
        txt = txt.replace("</h6>", "&lt;/h6&gt;")
        txt = txt.replace("\n", "<br/>")

        used_font = self.font().__copy__()
        used_size = used_font.pointSize()
        if used_size > 2:
            used_font.setPointSize(used_size - 2)

        qd = Qw.QDialog(self)
        qd.setModal(True)
        qd.setPalette(self.palette())
        qd.setWindowTitle(title)

        scroll = Qw.QScrollArea()
        layout = Qw.QVBoxLayout()
        label = Qw.QLabel(txt, scroll)
        label.setTextFormat(Qc.Qt.RichText)
        label.setWordWrap(True)
        label.setPalette(self.palette())
        label.setFont(used_font)
        scroll.setWidget(label)
        scroll.setFrameShape(Qw.QFrame.StyledPanel);
        scroll.setStyleSheet(styling.generate_scrollable_area_stylesheet())
        scroll.setWidgetResizable(True)
        layout.addWidget(scroll)
        # scroll.setFixedHeight(200)
        mini_layout = Qw.QHBoxLayout()
        h_spacer = Qw.QSpacerItem(40, 20, Qw.QSizePolicy.Policy.Expanding, Qw.QSizePolicy.Policy.Minimum)
        mini_layout.addSpacerItem(h_spacer)
        btn = Qw.QPushButton(qd)
        btn_color = btn.palette().color(Qg.QPalette.Button).name()
        btn.setStyleSheet(styling.generate_button_stylesheet(btn_color))
        btn.setFont(used_font)
        btn.setMinimumWidth(btn.minimumWidth())
        btn.clicked.connect(qd.accept)
        btn.setText("   OK   ")
        mini_layout.addWidget(btn)
        mini_layout.addSpacerItem(h_spacer)
        layout.addLayout(mini_layout)
        qd.setMinimumWidth(minimum_width)
        qd.setMinimumHeight(minimum_height)

        qd.setLayout(layout)
        qd.show()
        qd.exec()

    @Qc.Slot()
    def log(self, msg, log_lvl=logging.INFO, time=5000):
        logger = logging.getLogger(__package__)
        logger.log(log_lvl, msg)
        if log_lvl == logging.INFO or log_lvl == logging.WARNING or log_lvl == logging.ERROR:
            bar_msg = " " + msg.capitalize()
            now = datetime.now()
            ui_log = "<span>[<span style='color: {};'>{}</span>] [{}] - {}</span>"
            keys = {logging.INFO: "INFO", logging.WARNING: "WARN", logging.ERROR: "ERROR"}
            self.ui.plain_text_logs.appendHtml(ui_log.format(styling.LOGS_COLORS[log_lvl],
                                                             keys[log_lvl],
                                                             now.strftime("%H:%M:%S"),
                                                             msg.capitalize()))
            s_font = self.ui.statusbar.font()
            self.ui.statusbar.setStyleSheet(f"color: {styling.LOGS_COLORS[log_lvl]}")
            self.ui.statusbar.setFont(s_font)
            self.ui.statusbar.showMessage(bar_msg, time)


def boolean_string(s):
    if s not in {'False', 'True'}:
        raise ValueError('Not a valid boolean string')
    return s == 'True'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description='Modify Shopify page code to add 2 columns sections. This is done by '
                                                 'replacing <h6> elements that contain the following texts: '
                                                 '###start### (or ###start_inv### to inverse columns), ###next###, '
                                                 '###end###.')
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
    config.setup_logging(__package__, args.log_level, args.logs_file)

    # initiate App
    app = Qw.QApplication(sys.argv)
    app.setStyle(args.style)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())
