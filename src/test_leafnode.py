import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p2(self):
        node = LeafNode("h1", "Welcome to My Website")
        self.assertEqual(node.to_html(), "<h1>Welcome to My Website</h1>")


    def test_leaf_to_html_p3(self):
        node = LeafNode("h2", "Welcome to My Website")
        self.assertNotEqual(node.to_html(), "<h1>Welcome to My Website</h1>")



if __name__ == "__main__":
    unittest.main()