from textnode import TextNode, TextType
from copystatic import recursive_copy, delete_public_start_copy


def main():
    static_dir = "static"
    public_dir = "public"
    delete_public_start_copy(static_dir, public_dir)


main()
