from textnode import *
from inline_markdown import *
from htmlnode import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    parts = markdown.split("\n\n")
    r_parts = []
    for part in parts:
        if part != "":
            r_parts.append(part.strip())
    return r_parts

def block_to_block_type(block):
    lines = block.splitlines()

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING

    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE

    if block.startswith("> "):
        for line in lines:
            if not line.startswith("> "):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    if block.startswith(("* ", "- ")):
        for line in lines:
            if not line.startswith(("* ", "- ")):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    
    count = 1
    if block.startswith(f"{str(count)}. "):
        count = 1
        for line in lines:
            if not line.startswith(f"{str(count)}. "):
                return BlockType.PARAGRAPH
            count += 1
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    parent = ParentNode("div", [])
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        parent.children.append(block_to_html_node(block))
    return parent

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match(block_type):
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.CODE:
            return code_to_html_node(block)
        case BlockType.ORDERED_LIST:
            return ordered_list_to_html_node(block)
        case BlockType.UNORDERED_LIST:
            return unordered_list_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case _:
            raise ValueError("invalid block type")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    hash_count = block.split(' ', 1)[0].count("#")
    text = block[hash_count + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{hash_count}", children)

def code_to_html_node(block):
    code = LeafNode("code", block[4:-3]) # I didn't use text_to_children here as I don't believe that applies for code snippets
    return ParentNode("pre", [code])

def ordered_list_to_html_node(block):
    parent = ParentNode("ol", [])
    lines = block.split("\n")
    for line in lines:
        children = text_to_children(line[3:])
        parent.children.append(ParentNode("li", children))
    return parent

def unordered_list_to_html_node(block):
    parent = ParentNode("ul", [])
    lines = block.split("\n")
    for line in lines:
        children = text_to_children(line[2:])
        parent.children.append(ParentNode("li", children))
    return parent

def quote_to_html_node(block):
    new_lines = []
    lines = block.split("\n")
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)