from enum import Enum
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node
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
            pass
            # build a heading node
        elif block_type == BlockType.QUOTE:
            pass
            # build a quote node
        elif block_type == BlockType.CODE:
            pass
            # build a code node
        elif block_type == BlockType.UNORDERED_LIST:
            pass
            # build an unordered list node
        elif block_type == BlockType.ORDERED_LIST:
            pass
            # build an ordered list node
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
