import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    html_node = HTMLNode(
        "p",
        "This is some test text",
        None,
        {
            "href": "https://www.duckduckgo.com",
            "target": "_blank"
        }
    )

    empty_html_node = HTMLNode()

    def test_props_to_html(self):
        expect = ' href="https://www.duckduckgo.com" target="_blank"'
        self.assertEqual(self.html_node.props_to_html(), expect)
    
    def test_props_to_html_empty(self):
        self.assertEqual(self.empty_html_node.props_to_html(), "")
    
    def test_none_defaults(self):
        self.assertEqual(self.empty_html_node.tag, None)
        self.assertEqual(self.empty_html_node.value, None)
        self.assertEqual(self.empty_html_node.children, None)
        self.assertEqual(self.empty_html_node.props, None)
    


class TestLeafNode(unittest.TestCase):
    leaf_node = LeafNode(
        "p",
        "This is some test text",
        {"href": "https://www.duckduckgo.com"}
    )

    def test_leaf_to_html(self):
        expect = '<p href="https://www.duckduckgo.com">This is some test text</p>'
        self.assertEqual(self.leaf_node.to_html(), expect)

class TestParantNode(unittest.TestCase):
    leaf_node_1 = LeafNode(
        "p",
        "This is some test text",
        {"href": "https://www.duckduckgo.com"}
    )

    leaf_node_2 = LeafNode(
        "h2",
        "This is some more test text",
        {"href": "https://www.ecosia.com"}
    )

    parent_node_1 = ParentNode(
        "div",
        [leaf_node_1, leaf_node_2],
        {"style": "color=blue"}
    )

    parent_node_2 = ParentNode(
        "div",
        [leaf_node_1, parent_node_1],
        None
    )

    def test_to_html(self):
        expect = '<div style="color=blue"><p href="https://www.duckduckgo.com">This is some test text</p><h2 href="https://www.ecosia.com">This is some more test text</h2></div>'
        self.assertEqual(expect, self.parent_node_1.to_html())

    def test_to_html_with_nested(self):
        expect = '<div><p href="https://www.duckduckgo.com">This is some test text</p><div style="color=blue"><p href="https://www.duckduckgo.com">This is some test text</p><h2 href="https://www.ecosia.com">This is some more test text</h2></div></div>'
        self.assertEqual(expect, self.parent_node_2.to_html())

if __name__ == "__main__":
    unittest.main()
