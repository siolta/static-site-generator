from copystatic import clean_target_dir, copy_static_assets
from generate_page import generate_page


PUBLIC_DIR = "./public"
STATIC_DIR = "./static"
SRC_PATH = "content/index.md"
TEMPLATE_PATH = "template.html"
TARGET_PATH = "public/index.html"


def main():
    clean_target_dir(PUBLIC_DIR)
    copy_static_assets(STATIC_DIR, PUBLIC_DIR)
    generate_page(SRC_PATH, TEMPLATE_PATH, TARGET_PATH)


if __name__ == "__main__":
    main()
