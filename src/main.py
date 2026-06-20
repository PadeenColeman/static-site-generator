from textnode import TextNode, TextType


def main():
    inst = TextNode("Example text", TextType.BOLD, "www.duckduckgo.com")
    print(inst)


main()
