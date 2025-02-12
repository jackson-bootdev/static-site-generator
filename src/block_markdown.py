from textnode import *

def markdown_to_blocks(markdown):
    parts = markdown.split("\n\n")
    r_parts = []
    for part in parts:
        if part != "":
            r_parts.append(part.strip())
    return r_parts