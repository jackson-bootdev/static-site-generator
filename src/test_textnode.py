import unittest

from textnode import TextNode, TextType, split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_url_is_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)

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

if __name__ == "__main__":
    unittest.main()
