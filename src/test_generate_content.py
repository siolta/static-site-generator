import unittest

from generate_content import extract_title


# --- Markdown title cases ---
MARKDOWN_WITH_TITLE = """
# This is the Main Title

Some introductory text.

## A Subheading
More text here.

# Another H1 (Should not be picked if first one exists)
"""

MARKDOWN_TITLE_NOT_FIRST = """
<a href="https://test.link">Test link</a>

# Title here

some more text
"""

MARKDOWN_NO_SPACE = "#Hello There"

MARKDOWN_EXTRA_SPACE = "  #   Lots of Space   "

MARKDOWN_NO_H1 = """
## This is not H1
Some text.
### Also not H1
"""

MARKDOWN_EMPTY = ""


class TestGeneratePage(unittest.TestCase):
    def test_markdown_with_title(self):
        result = "This is the Main Title"
        self.assertEqual(result, extract_title(MARKDOWN_WITH_TITLE))

    def test_markdown_title_not_first(self):
        result = "Title here"
        self.assertEqual(result, extract_title(MARKDOWN_TITLE_NOT_FIRST))

    def test_markdown_no_space(self):
        result = "Hello There"
        self.assertEqual(result, extract_title(MARKDOWN_NO_SPACE))

    def test_markdown_extra_space(self):
        result = "Lots of Space"
        self.assertEqual(result, extract_title(MARKDOWN_EXTRA_SPACE))

    def test_markdown_no_h1(self):
        with self.assertRaises(ValueError):
            extract_title(MARKDOWN_NO_H1)

    def test_markdown_empty(self):
        with self.assertRaises(ValueError):
            extract_title(MARKDOWN_EMPTY)
