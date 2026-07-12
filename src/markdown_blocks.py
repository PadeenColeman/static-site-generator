from enum import Enum
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType
from htmlnode import ParentNode


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    clean_blocks = []
    for i in range(len(blocks)):
        if blocks[i] == "":
            continue
        else:
            clean_blocks.append(blocks[i].strip())
    return clean_blocks


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown):
    number_of_hashes = 0
    i = 0
    while len(markdown) > i and markdown[i] == "#":
        number_of_hashes += 1
        i += 1
    if (
        number_of_hashes >= 1
        and number_of_hashes <= 6
        and i < len(markdown)
        and markdown[i] == " "
    ):
        return BlockType.HEADING
    if markdown.startswith("```\n") and markdown.endswith("```"):
        return BlockType.CODE
    lines = markdown.split("\n")
    valid_quote = True
    for line in lines:
        if line.startswith(">"):
            continue
        else:
            valid_quote = False
            break
    if valid_quote:
        return BlockType.QUOTE
    valid_unordered_list = True
    for line in lines:
        if line.startswith("- "):
            continue
        else:
            valid_unordered_list = False
            break
    if valid_unordered_list:
        return BlockType.UNORDERED_LIST
    expected_number = 1
    valid_ordered_list = True
    for line in lines:
        if line.startswith(f"{expected_number}. "):
            expected_number += 1
        else:
            valid_ordered_list = False
            break
    if valid_ordered_list:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            children.append(paragraph_to_html_node(block))
        elif block_type == BlockType.HEADING:
            children.append(heading_to_html_node(block))
        elif block_type == BlockType.QUOTE:
            children.append(quote_to_html_node(block))
        elif block_type == BlockType.CODE:
            children.append(code_to_html_node(block))
        elif block_type == BlockType.UNORDERED_LIST:
            children.append(ul_to_html_node(block))
        elif block_type == BlockType.ORDERED_LIST:
            children.append(ol_to_html_node(block))
    return ParentNode("div", children)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    # now 'level' tells you h1..h6
    text = block[level + 1 :]  # skip the #s AND the space
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        # strip the leading '>' and surrounding whitespace from 'line'
        # then append the cleaned text to new_lines
        stripped = line.lstrip(">").strip()
        new_lines.append(stripped)
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def ul_to_html_node(block):
    lines = block.split("\n")
    list_items = []
    for line in lines:
        # strip the leading '-' and surrounding whitespace from 'line'
        stripped = line.lstrip("-").strip()
        children = text_to_children(stripped)  # inline parsing per item
        list_items.append(ParentNode("li", children))
    return ParentNode("ul", list_items)


def ol_to_html_node(block):
    lines = block.split("\n")
    list_items = []
    for line in lines:
        # strip the leading number and surrounding whitespace from 'line'
        stripped = line.split(". ", 1)[1]
        children = text_to_children(stripped)  # inline parsing per item
        list_items.append(ParentNode("li", children))
    return ParentNode("ol", list_items)


def code_to_html_node(block):
    stripped = block[4:-3]
    raw_node = TextNode(stripped, TextType.TEXT)  # or whatever your TEXT type is called
    child = text_node_to_html_node(raw_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])
