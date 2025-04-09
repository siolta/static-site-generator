import os
from copystatic import clean_target_dir, copy_static_assets
from generate_content import generate_page


PUBLIC_PATH = "./public"
STATIC_PATH = "./static"
CONTENT_PATH = "./content"
TEMPLATE_PATH = "./template.html"


def main():
    clean_target_dir(PUBLIC_PATH)

    print("Copying static files to public directory...")
    copy_static_assets(STATIC_PATH, PUBLIC_PATH)

    print("Generating pages...")
    md_index_path = os.path.join(CONTENT_PATH, "index.md")
    html_index_path = os.path.join(PUBLIC_PATH, "index.html")
    generate_page(md_index_path, TEMPLATE_PATH, html_index_path)


if __name__ == "__main__":
    main()
