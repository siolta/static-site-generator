def extract_title(markdown):
    # Split lines
    # search each line for one that starts with "# "
    # assume it can only be the first line? no, it could be after an image, link, etc
    # if none exist, raise exception
    lines = markdown.split("\n")
    print(markdown)
    for line in lines:
        if line[:2] == "# ":
            return line.lstrip("# ").strip()

        raise ValueError("no title found")


def generate_page(from_path, template_path, dest_path):
    pass
