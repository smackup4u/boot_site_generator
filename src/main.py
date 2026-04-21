from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
def main():
    print("Hello World") #print hello world, will be called via main.sh
    x = TextNode("Just a test", TextType.LINK, "www.google.com")
    print(x)
    return x


if __name__ == "__main__":
    y = main()
    test_dict = {
    "href": "https://www.google.com",
    "target": "_blank",
    }
    test = HTMLNode(props=test_dict)
    test2 = LeafNode("p","Hello World!")
    test3 = LeafNode("a", "ClickMe!", test_dict)
    
    parent1 = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )
    #scratchpad
    
    st_1 = "056888604"
    nu_1 = 456664
    
    countries = ["America", "Canada", "Australia", "China", "Chile"]
    for c in countries[:]:      #difference between countries (mutable) and countries[:]
        if c.startswith("C"):
            countries.remove(c)
    print(countries)
