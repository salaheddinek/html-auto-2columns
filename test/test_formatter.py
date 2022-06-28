import unittest
import formatter


class TestFormatterMethods(unittest.TestCase):

    def test_report(self):
        html_text = f'<h6>{formatter.TYPE_TO_MARKER[formatter.Types.START]}</h6><br/>' \
                    f'<h6>{formatter.TYPE_TO_MARKER[formatter.Types.NEXT]}</h6><br/>' \
                    f'<div><h6>{formatter.TYPE_TO_MARKER[formatter.Types.END]}</h6></div>' \
                    f'<h6>random title</h6>'

        print(html_text)
        print(formatter.HtmlFormatter.get_h6_positions_report_str(html_text))
        report = formatter.HtmlFormatter.get_h6_positions_report(html_text)

        self.assertEqual(3, len(report))


if __name__ == '__main__':
    unittest.main()