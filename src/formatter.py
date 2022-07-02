from enum import Enum
import re
import PySide6.QtCore as Qc
import logging
import bs4
from datetime import datetime
import tree_processing


class Types(Enum):
    START = 0
    START_INV = 1
    NEXT = 2
    END = 3


TYPE_TO_MARKER = {
    Types.START: "###start###",
    Types.START_INV: "###start_inv###",
    Types.NEXT: "###next###",
    Types.END: "###end###",
}

TYPES_MARKERS = {
    "###start###": Types.START,
    "###start_inv###": Types.START_INV,
    "###next###": Types.NEXT,
    "###end###": Types.END,
}


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
    w_msg = Qc.Signal(str, str, int, int)

    def __init__(self, parent):
        super().__init__(parent)
        self.num_cleared_previous_html_elements = None
        self.num_cleared_h6 = None

    def process(self, in_html_text, in_settings):
        self.num_cleared_h6 = 0
        self.num_cleared_previous_html_elements = 0
        previous_type = Types.END
        out_html_data = in_html_text

        out_html_data = self._pre_processing(out_html_data, in_settings)
        # return out_html_data
        if in_settings["clear_elements"]:
            out_html_data = self._remove_h6_elements(out_html_data)
        out_html_data = self._check_for_merged_h6_tags(out_html_data)
        h6_elements = self._get_h6_html_data(out_html_data)
        if in_settings["clear_elements"]:
            self.log.emit(f"Cleared '{len(h6_elements)}' h6 elements, '{self.num_line_breaks}'  line breaks and "
                          f"'{self.num_cleared_previous_html_elements}' generated patterns", logging.INFO, 5000)

        error_msg = "ERROR: wrong h6 sequence {}->{}. Possible sequences: START->NEXT->END or START_INV->NEXT->END."
        window_msg = "ERROR: some <h6> tags do not have the appropriate order:\n\n"
        window_msg += self.get_h6_positions_report_str(out_html_data)
        window_msg += "\nPlease correct the tags so that all sequences are as follows:\n" \
                      "START->NEXT->END or START_INV->NEXT->END."

        num_sequences = 0
        is_ok = True

        if not self._check_h6_depth_correctness(out_html_data):
            error_msg = f"ERROR: h6 elements do not have the same depth."
            window_msg = "ERROR: some <h6> tags do not have the appropriate depth in the HTML Tree:\n\n"
            window_msg += self.get_h6_positions_report_str(out_html_data)
            window_msg += "\nPlease correct the tags so that each 3 consecutive tags have in the same depth."
            is_ok = False

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

        if in_settings["save_origins_to_file"]:
            self._append_to_file(in_settings["save_file_path"], in_html_text, is_ok)

        if not is_ok:
            self.log.emit(error_msg, logging.ERROR, 5000)
            if window_msg != "":
                self.w_msg.emit(window_msg, "Error message", 1000, 800)
            return ""

        self.log.emit("Successfully inserted '{}' two-columns sections (cleared '{}' previously generated HTML and '{}'"
                      " h6 tags).".format(num_sequences, self.num_cleared_previous_html_elements, self.num_cleared_h6
                                          ), logging.INFO, 5000)
        return out_html_data

    @staticmethod
    def get_h6_positions_report(in_html_text):
        doc = bs4.BeautifulSoup(in_html_text, "html.parser")
        report = []
        for match in doc.find_all("h6"):
            match_str = str(match).lower()
            for marker in TYPES_MARKERS:
                if marker in match_str:
                    report_line = [marker]
                    cur_tag = match
                    while cur_tag:
                        report_line += [cur_tag.name]
                        cur_tag = cur_tag.parent
                    report += [report_line]

        return report

    @staticmethod
    def get_h6_positions_report_str(in_html_text):
        report_str = ""
        for i, line in enumerate(HtmlFormatter.get_h6_positions_report(in_html_text)):
            parents = list(reversed(line))
            report_str += f"{i}. Depth:{len(line) - 1}  =>  {' -> '.join(parents)}\n"
        return report_str

    def _check_for_merged_h6_tags(self, in_html_text):
        doc = bs4.BeautifulSoup(in_html_text, "html.parser")
        num_correction = 0
        for match in doc.find_all("h6"):
            match_str = str(match).lower()
            for init_marker in ["###start###", "###start_inv###"]:
                if init_marker in match_str and "###end###" in match_str:
                    new_div_before1 = doc.new_tag("h6")
                    new_div_before1.string = "###end###"
                    match.insert_before(new_div_before1)
                    new_div_before2 = doc.new_tag("h6")
                    new_div_before2.string = init_marker
                    match.insert_before(new_div_before2)
                    num_correction += 1

        for match in doc.find_all("h6"):
            match_str = str(match).lower()
            for init_marker in ["###start###", "###start_inv###"]:
                if init_marker in match_str and "###end###" in match_str:
                    match.decompose()
                    continue

        if num_correction != 0:
            self.log.emit(f"corrected {num_correction} merge start and end h6 tags", logging.INFO, 5000)
        return str(doc)

    def _pre_processing(self, in_html_text, settings):
        doc = bs4.BeautifulSoup(in_html_text, "html.parser")

        if settings["pre_proc_clear_shopify_tags"]:
            tree_processing.unwrap_shopify_useless_strong_tags(doc)
            self.log.emit("unwrap_shopify_useless_strong_tags finished", logging.DEBUG, 5000)

        if settings["pre_proc_unwrap_without_class"]:
            doc = tree_processing.unwrap_tags_without_classes(doc, settings["pre_proc_unwrap_without_class_affected"])
            self.log.emit("unwrap_tags_without_classes finished", logging.DEBUG, 5000)

        if settings["pre_proc_remove_attributes"]:
            doc = tree_processing.remove_none_class_attributes(doc, settings["pre_proc_remove_attributes_affected"])
            self.log.emit("remove_none_class_attributes finished", logging.DEBUG, 5000)

        if settings["pre_proc_unwrap_no_content"]:
            doc = tree_processing.unwrap_tags_with_no_content(doc, settings["pre_proc_unwrap_no_content_affected"])
            self.log.emit("unwrap_tags_with_no_content finished", logging.DEBUG, 5000)

        if settings["pre_proc_group_consecutive"]:
            doc = tree_processing.group_consecutive_tags(doc, settings["pre_proc_group_consecutive_affected"])
            self.log.emit("pre_proc_group_consecutive finished", logging.DEBUG, 5000)

        if settings["pre_proc_clear_shopify_tags"] or settings["pre_proc_unwrap_without_class"] or\
                settings["pre_proc_remove_attributes"] or settings["pre_proc_unwrap_no_content"] or\
                settings["pre_proc_group_consecutive"]:
            self.log.emit("pre-processing successful!", logging.INFO, 5000)
        return str(doc)

    def _check_h6_depth_correctness(self, in_html_text):
        doc = bs4.BeautifulSoup(in_html_text, "html.parser")
        depth_correctness_idx = 0
        for match in doc.find_all("h6"):
            depth_correctness_idx += 1
            father = match.parent

            num_formatter_h6_tags = 0
            for match_siblings in father.find_all("h6", recursive=False):
                cur = Header6()
                cur.text = str(match_siblings)
                if cur.detect_type():
                    num_formatter_h6_tags += 1
            if num_formatter_h6_tags == 0:
                depth_correctness_idx -= 1
            self.log.emit(f"check_h6_depth_correctness: h6 idx:{depth_correctness_idx} "
                          f"- num siblings:{num_formatter_h6_tags} - text:'{match.text}'", logging.DEBUG, 5000)

            if num_formatter_h6_tags % 3 != 0:
                return False
        return True

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

    def _remove_h6_elements(self, in_html_data):
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

        self.num_line_breaks = num_line_breaks
        self.num_cleared_previous_html_elements = num_ss_divs
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
