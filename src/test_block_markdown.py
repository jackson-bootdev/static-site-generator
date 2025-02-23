import unittest

from textnode import *
from block_markdown import *

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks_basic(self):
        md = '''
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item'''

        expect = [
            '# This is a heading',
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
            '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        ]

        self.assertEqual(expect, markdown_to_blocks(md))

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_heading(self):
        md = '''## This is a heading\nAnd we have an extra line here'''
        self.assertEqual(BlockType.HEADING, block_to_block_type(md))

    def test_block_to_block_code(self):
        md = '''```
This is a heading\nAnd we have an extra line here
```'''
        self.assertEqual(BlockType.CODE, block_to_block_type(md))

    def test_block_to_block_ordered_list(self):
        md = '''1. This is a heading\n2. And we have an extra line here'''
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(md))

    def test_block_to_block_paragraph_1(self):
        md = ""
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(md))

    def test_block_to_block_paragraph_2(self):
        md = '''This is a paragraph\nchur'''
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(md))

if __name__ == "__main__":
    unittest.main()