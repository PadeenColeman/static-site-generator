from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("Sorry, no h1 header.")


def generate_page():
    pass
