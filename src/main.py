from textnode import TextNode, TextType
from htmlnode import HTMLNode
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
    