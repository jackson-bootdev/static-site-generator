import unittest

from htmlnode import HTMLNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node

class TestParantNode(unittest.TestCase):
    text_node_1 = TextNode("This is some test text", TextType.LINK, "https://www.duckduckgo.com")

    leaf_node_1 = LeafNode(
        "a",
        "This is some test text",
        {"href": "https://www.duckduckgo.com"}
    )

    def test_to_html(self):
        self.assertEqual(self.leaf_node_1, text_node_to_html_node(self.text_node_1))
        
if __name__ == "__main__":
    unittest.main()
