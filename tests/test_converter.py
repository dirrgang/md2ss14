import unittest
from src.converter import md_to_ss14

class TestMdToSS14(unittest.TestCase):

    def test_bold(self):
        self.assertEqual(md_to_ss14("**bold text**"), "[bold]bold text[/bold]")

    def test_italic(self):
        self.assertEqual(md_to_ss14("*italic text*"), "[italic]italic text[/italic]")

    def test_bold_italic(self):
        self.assertEqual(md_to_ss14("***bold italic text***"), "[bolditalic]bold italic text[/bolditalic]")

    def test_heading(self):
        self.assertEqual(md_to_ss14("# Heading 1"), "[head=1]Heading 1[/head]")

    def test_bulleted_list(self):
        self.assertEqual(md_to_ss14("- item 1\n- item 2"), "[bullet/]item 1\n[bullet/]item 2")

    def test_color_span(self):
        self.assertEqual(md_to_ss14('<span style="color:red">red text</span>'), "[color=red]red text[/color]")

    def test_color_font(self):
        self.assertEqual(md_to_ss14('<font color="blue">blue text</font>'), "[color=blue]blue text[/color]")

    def test_remove_html(self):
        self.assertEqual(md_to_ss14("<div>Some text</div>"), "Some text")

if __name__ == "__main__":
    unittest.main()