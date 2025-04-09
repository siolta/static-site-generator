from os import path, makedirs, listdir
from pathlib import Path
from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith("#") and not stripped_line.startswith("##"):
            return stripped_line[1:].strip()

    raise ValueError("no title found")


def generate_page(from_path, template_path, dest_path, basepath):
    print(f" * {from_path} {template_path} -> {dest_path}")

    with open(from_path) as from_handle, open(template_path) as template_handle:
        # Read target files
        markdown = from_handle.read()
        template = template_handle.read()

        # convert and extract
        html = markdown_to_html_node(markdown).to_html()
        title = extract_title(markdown)

        # replace in template
        template = template.replace("{{ Title }}", title)
        template = template.replace("{{ Content }}", html)
        template = template.replace('href="/', f'href="{basepath}')
        template = template.replace('src="/', f'src="{basepath}')

        dest_pathname = path.dirname(dest_path)
        if dest_pathname != "":
            makedirs(dest_pathname, exist_ok=True)
        with open(dest_path, "w") as dest_file:
            dest_file.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for node in listdir(dir_path_content):
        from_path = path.join(dir_path_content, node)
        dest_path = path.join(dest_dir_path, node)
        if path.isfile(from_path):
            dest_path = Path(dest_dir_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            print(f" - {from_path} -> {dest_path}")
            generate_pages_recursive(
                from_path, template_path, dest_path, basepath)
