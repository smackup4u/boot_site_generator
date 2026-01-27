import unittest
from textnode import TextType, TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a infinite node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    

    def test_eq4(self):
        node = TextNode("This is a infinite node", TextType.BOLD)
        node2 = TextNode("This is a infinite node", TextType.BOLD)
        node3 = TextNode("This is a infinite node", TextType.BOLD)
        self.assertEqual(node, node3)
    

if __name__ == "__main__":
    unittest.main()

