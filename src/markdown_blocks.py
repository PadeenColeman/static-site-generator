def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    clean_blocks = []
    for i in range(len(blocks)):
        if blocks[i] == "":
            continue
        else:
            clean_blocks.append(blocks[i].strip())
    return clean_blocks
