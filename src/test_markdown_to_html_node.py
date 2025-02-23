import unittest

from block_markdown import *

class TestMarkdownToHTML(unittest.TestCase):
    def test_convert(self):
        markdown = '''
## This is my **title**\n
Hi I am some very basic markdown but I have some *BOLD* text\n
```This is my code block```\n
1. Hello
2. This is a test\n
* Hello
- This is another test\n
> This is blockquote
> This is more blockquote
'''

        node = markdown_to_html_node(markdown)
        html = node.to_html()
        expected = '<div><h2>This is my <b>title</b></h2><p>Hi I am some very basic markdown but I have some <i>BOLD</i> text</p><p><code>This is my code block</code></p><ol><li>Hello</li><li>This is a test</li></ol><ul><li>Hello</li><li>This is another test</li></ul><blockquote>This is blockquote This is more blockquote</blockquote></div>'
        self.assertEqual(expected, html)

if __name__ == "__main__":
    unittest.main()