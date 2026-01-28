import unittest
from htmlnode import HTMLNode



class TestHTMLNode(unittest.TestCase):
    def test_eq(self):

        test_dict = {
    "href": "https://www.google.com",
    "target": "_blank",
}
            
        node = HTMLNode(props=test_dict)
        node2 = HTMLNode(props=test_dict)
        self.assertEqual(node, node2)
    
    def test_eq2(self):
        test_dict = {
    "href": "https://www.google.com",
    "target": "_blank",
}
        test_dict2 = {
    "href": "https://www.google.com",
    "target": "_blanuuu",
}       
        node = HTMLNode(props=test_dict)
        node2 = HTMLNode(props=test_dict2)
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()