def markdown_to_blocks(document):
    blocks = [block.strip() for block in document.split("\n\n") if block != ""]
    return blocks
