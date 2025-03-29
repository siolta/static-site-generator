from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(document):
    blocks = [block.strip() for block in document.split("\n\n") if block != ""]
    return blocks


def block_to_block_type(block):
    if re.match(r"^#{1,6}", block):
        return BlockType.HEADING
    if block[:3] == "```" and block.rstrip("\n")[-3:] == "```":
        return BlockType.CODE
    for line in block:
        pass
    return BlockType.PARAGRAPH
