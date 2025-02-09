from textnode import *
from htmlnode import *

def main():
    t = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(t)

main()
