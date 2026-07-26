from textnode import TextNode, TextType
from copystatic import recursive_copy, delete_public_start_copy
from gencontent import generate_page


def main():
    static_dir = "static"
    public_dir = "public"
    delete_public_start_copy(static_dir, public_dir)
    generate_page("content/index.md", "template.html", "public/index.html")


main()
