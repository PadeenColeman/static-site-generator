from textnode import TextNode, TextType
from copystatic import recursive_copy, delete_public_start_copy
from gencontent import generate_pages_recursive


def main():
    static_dir = "static"
    public_dir = "public"
    dir_path_public = "./public"
    dir_path_content = "./content"
    template_path = "./template.html"
    delete_public_start_copy(static_dir, public_dir)
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)


main()
