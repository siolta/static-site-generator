from sys import argv
from copystatic import clean_target_dir, copy_static_assets
from generate_content import generate_pages_recursive


TARGET_PATH = "./docs"
STATIC_PATH = "./static"
CONTENT_PATH = "./content"
TEMPLATE_PATH = "./template.html"


def main():
    basepath = "/"
    if len(argv) > 1:
        print("args:", argv)
        basepath = argv[1]

    clean_target_dir(TARGET_PATH)

    print("Copying static files to target directory...")
    copy_static_assets(STATIC_PATH, TARGET_PATH)

    print("Generating pages...")
    generate_pages_recursive(
        CONTENT_PATH, TEMPLATE_PATH, TARGET_PATH, basepath)


if __name__ == "__main__":
    main()
