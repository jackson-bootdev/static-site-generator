from textnode import *
from htmlnode import *
from generate import *
from block_markdown import *

def main():
    clear_directory('./public')
    copy_directory('./static', './public')
    generate_pages_recursive('./content/', './template.html', './public/')

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    file = open(from_path, "r")
    markdown = file.read()
    file.close()

    file = open(template_path, "r")
    template = file.read()
    file.close()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    result = template.replace("{{ Title }}", title[2:])
    result = result.replace("{{ Content }}", html)

    destination = dest_path
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    with open(destination, "w") as f:
        f.write(result)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_list = os.listdir(dir_path_content)
    for dir in dir_list:
        fp = os.path.join(dir_path_content, dir)
        if os.path.isfile(fp):
            tp = os.path.join(dest_dir_path, "index.html")
            generate_page(fp, template_path, tp)
        else:
            tp = os.path.join(dest_dir_path, dir)
            generate_pages_recursive(fp, template_path, tp)

main()
