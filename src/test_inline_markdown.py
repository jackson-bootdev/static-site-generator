import unittest

from textnode import *
from inline_markdown import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold_split(self):
        node = TextNode("This is a **bold** statement", TextType.TEXT)
        splits = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual("This is a ", splits[0].text)
        self.assertEqual(TextType.TEXT, splits[0].text_type)

        self.assertEqual("bold", splits[1].text)
        self.assertEqual(TextType.BOLD, splits[1].text_type)

        self.assertEqual(" statement", splits[2].text)
        self.assertEqual(TextType.TEXT, splits[2].text_type)

class TestExtractImages(unittest.TestCase):
    def test_bold_split(self):
        matches = extract_markdown_images('This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)')
        self.assertEqual([('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')], matches)

class TestExtractLinks(unittest.TestCase):
    def test_bold_split(self):
        matches = extract_markdown_links('This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)')
        self.assertEqual([('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')], matches)

class TestSplitNodesImage(unittest.TestCase):
    def test_basic_split(self):
        node = TextNode(
            "This is text with a link ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/not_real.png) plus extra",
            TextType.TEXT
        )
        expect = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "obi wan", TextType.IMAGE, "https://i.imgur.com/not_real.png"
            ),
            TextNode(" plus extra", TextType.TEXT)
        ]
        result = split_nodes_image([node])
        self.assertEqual(expect, result)

class TestSplitNodesLink(unittest.TestCase):
    def test_basic_split(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) plus extra",
            TextType.TEXT
        )
        expect = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
            TextNode(" plus extra", TextType.TEXT)
        ]
        result = split_nodes_link([node])
        self.assertEqual(expect, result)

class TestTextToTextNodes(unittest.TestCase):
    def test_basic_text_to_textnode(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expect = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(expect, text_to_textnodes(text))

if __name__ == "__main__":
    unittest.main()