import unittest
import tree_processing
import bs4


class TestStringMethods(unittest.TestCase):

    def test_group_consecutive_tags1(self):
        html_text = '<span><b>an other</b></span> <span><b>in</b><b>troduction</b></span>'
        doc = bs4.BeautifulSoup(html_text, "html.parser")
        doc = tree_processing.group_consecutive_tags(doc, ["strong", "em", "u", "i", "span", "b"])
        html_res = str(doc)
        self.assertEqual('<span><b>an other introduction</b></span>', html_res)

    def test_group_consecutive_tags2(self):
        html_text = '<span><b>an other</b></span><span><b class="d">in</b><b>troduction</b></span>'
        doc = bs4.BeautifulSoup(html_text, "html.parser")
        doc = tree_processing.group_consecutive_tags(doc, ["strong", "em", "u", "i", "span", "b"])
        html_res = str(doc)
        self.assertEqual('<span><b>an other</b><b class="d">in</b><b>troduction</b></span>', html_res)

    def test_group_consecutive_tags3(self):
        html_text = '<span><b>an other</b></span><span><b class="d">in</b><b class="d">troduction</b></span>'
        doc = bs4.BeautifulSoup(html_text, "html.parser")
        doc = tree_processing.group_consecutive_tags(doc, ["strong", "em", "u", "i", "span", "b"])
        html_res = str(doc)
        self.assertEqual('<span><b>an other</b><b class="d">introduction</b></span>', html_res)


if __name__ == '__main__':
    unittest.main()
