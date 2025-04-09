from os import path, mkdir
from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    # Split lines
    # search each line for one that starts with "# "
    # assume it can only be the first line? no, it could be after an image, link, etc
    # if none exist, raise exception
    lines = markdown.splitlines()
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith("#") and not stripped_line.startswith("##"):
            return stripped_line[1:].strip()

    raise ValueError("no title found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as from_handle, open(template_path) as template_handle:
        markdown = from_handle.read()
        template = template_handle.read()
        html = markdown_to_html_node(markdown).to_html()
        title = extract_title(markdown)
        new_template = template.replace("{{ Title }}", title)
        new_template = new_template.replace("{{ Content }}", html)

        dest_pathname = path.dirname(dest_path)
        if not path.exists(dest_pathname):
            mkdir(dest_pathname)
        with open(dest_path, "w") as dest_file:
            dest_file.write(new_template)
