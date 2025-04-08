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
    pass
