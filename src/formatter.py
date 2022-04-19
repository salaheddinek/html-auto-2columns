from enum import Enum
import re
import PySide6.QtCore as Qc
import logging
from datetime import datetime


class Types(Enum):
    START = 1
    START_INV = 2
    NEXT = 3
    END = 4


class Header6:
    def __init__(self):
        self.idx_start = 0
        self.idx_end = 0
        self.text = ""
        self.type = None

    def detect_type(self):
        if "###start###" in self.text.lower():
            self.type = Types.START
        if "###start_inv###" in self.text.lower():
            self.type = Types.START_INV
        if "###next###" in self.text.lower():
            self.type = Types.NEXT
        if "###end###" in self.text.lower():
            self.type = Types.END
        if isinstance(self.type, Enum):
            return True
        # return False, f"WARNING: No type detected for <h6> that starts at character {self.idx_start}"
        return False


class HtmlFormatter(Qc.QObject):
    log = Qc.Signal(str, int, int)

    def __init__(self, parent):
        super().__init__(parent)
        self.num_cleared_previous_html_elements = None
        self.num_cleared_h6 = None

    def process(self, in_html_text, remove_generated_elements=True, save_file_path=""):
        self.num_cleared_h6 = 0
        self.num_cleared_previous_html_elements = 0
        previous_type = Types.END
        out_html_data = in_html_text

        h6_elements = self._get_h6_html_data(in_html_text)
        if remove_generated_elements:
            out_html_data = self._remove_h6_elements(h6_elements, out_html_data)

        error_msg = "ERROR: wrong h6 sequence {}->{}. Possible sequences: START->NEXT->END or START_INV->NEXT->END."
        num_sequences = 0
        is_ok = True
        for h6_tag in h6_elements:
            if not is_ok:
                break

            if h6_tag.type == Types.START:
                out_html_data = out_html_data.replace(h6_tag.text,
                                                      '<div class="ss_container"><div class="ss_column_1">', 1)
                if previous_type != Types.END:
                    error_msg = error_msg.format(previous_type, Types.START)
                    is_ok = False
            if h6_tag.type == Types.START_INV:
                out_html_data = out_html_data.replace(h6_tag.text,
                                                      '<div class="ss_container"><div class="ss_column_2">', 1)
                if previous_type != Types.END:
                    error_msg = error_msg.format(previous_type, Types.START_INV)
                    is_ok = False
            if h6_tag.type == Types.NEXT:
                if previous_type == Types.START:
                    out_html_data = out_html_data.replace(h6_tag.text, '</div><div class="ss_column_2">', 1)
                elif previous_type == Types.START_INV:
                    out_html_data = out_html_data.replace(h6_tag.text, '</div><div class="ss_column_1">', 1)
                else:
                    error_msg = error_msg.format(previous_type, Types.NEXT)
                    is_ok = False
            if h6_tag.type == Types.END:
                out_html_data = out_html_data.replace(h6_tag.text, '<div class="ss_end"></div></div></div>', 1)
                num_sequences += 1
                if previous_type != Types.NEXT:
                    error_msg = error_msg.format(previous_type, Types.END)
                    is_ok = False
            previous_type = h6_tag.type

        if previous_type != Types.END:
            is_ok = False
            error_msg = "ERROR:  h6 sequence does not end with END tag. " \
                        "Possible sequences: START->NEXT->END or START_INV->NEXT->END."

        self._append_to_file(save_file_path, in_html_text, is_ok)

        if not is_ok:
            self.log.emit(error_msg, logging.ERROR, 5000)
            return ""

        self.log.emit("Successfully inserted '{}' two-columns sections (cleared '{}' previously generated HTML and '{}'"
                      " h6 tags).".format(num_sequences, self.num_cleared_previous_html_elements, self.num_cleared_h6
                                          ), logging.INFO, 5000)
        return out_html_data

    @staticmethod
    def _get_h6_html_data(in_html_text):
        all_header6_tags = []
        for m in re.finditer('<h6', in_html_text):
            cur = Header6()
            cur.idx_start = m.start()
            cur.idx_end = in_html_text.find("</h6>", m.start()) + len("</h6>")
            cur.text = in_html_text[cur.idx_start:cur.idx_end]
            if cur.detect_type():
                all_header6_tags += [cur]
        return all_header6_tags

    @staticmethod
    def _replace_substring(in_old, in_idx_start, in_idx_end, in_new_char):
        return in_old[:in_idx_start] + in_new_char + in_old[in_idx_end + 1:]

    def _remove_h6_elements(self, in_h6_elements, in_html_data):
        out_html_data = in_html_data

        num_ss_divs = 0
        num_line_breaks = out_html_data.count('\n')
        out_html_data = out_html_data.replace('\n', '')
        patterns = ['<div class="ss_container">', '<div class="ss_column_1">', '<div class="ss_column_2">',
                    '</div><div class="ss_column_2">', '</div><div class="ss_column_1">',
                    '<div class="ss_end"></div></div></div>']
        for pattern in patterns:
            num_ss_divs += out_html_data.count(pattern)
            out_html_data = out_html_data.replace(pattern, '')

        self.num_cleared_h6 = len(in_h6_elements)
        self.num_cleared_previous_html_elements = num_ss_divs
        self.log.emit(f"Cleared '{len(in_h6_elements)}' h6 elements, '{num_line_breaks}' "
                      f"line breaks and '{num_ss_divs}' generated patterns", logging.INFO, 5000)

        return out_html_data

    def _append_to_file(self, file_path, original_html, is_ok, line_length=120):
        if file_path == "":
            return

        lines = []
        line_len = 0
        cur = ""
        for i in range(0, len(original_html)):
            cur += original_html[i]
            line_len += 1
            if line_len >= line_length and cur[-1] == ">":
                lines += [cur]
                cur = ""
                line_len = 0
        if cur != ">":
            lines += [cur]

        now = datetime.now()
        try:
            with open(file_path, 'a') as f:
                for _ in range(3):
                    f.write("=" * (line_length + 20) + "\n")
                f.write(f'\nTime: {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
                if is_ok:
                    f.write('HTML Formatting succeeded\n')
                else:
                    f.write(f'HTML Formatting FAILED!\n')
                f.write("\n\nOriginal html=\n")
                for line in lines:
                    f.write(line + "\n")
                f.write("\n\n\n\n\n\n")
                self.log.emit("Successfully written original HTML to 'save file'", logging.INFO, 5000)
        except IOError:
            self.log.emit(f"WARNING: Could not write to file {file_path}.", logging.WARNING, 5000)
