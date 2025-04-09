from copystatic import clean_target_dir, copy_static_assets
from generate_content import generate_pages_recursive


PUBLIC_PATH = "./public"
STATIC_PATH = "./static"
CONTENT_PATH = "./content"
TEMPLATE_PATH = "./template.html"


def main():
    clean_target_dir(PUBLIC_PATH)

    print("Copying static files to public directory...")
    copy_static_assets(STATIC_PATH, PUBLIC_PATH)

    print("Generating pages...")
    generate_pages_recursive(CONTENT_PATH, TEMPLATE_PATH, PUBLIC_PATH)


if __name__ == "__main__":
    main()
