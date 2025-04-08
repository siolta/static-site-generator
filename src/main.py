from copystatic import clean_target_dir, copy_static_assets
from generate_page import extract_title


PUBLIC_DIR = "./public"
STATIC_DIR = "./static"

TEST_MD = """
# this is a title

## this is not
"""


def main():
    # clean_target_dir(PUBLIC_DIR)
    # copy_static_assets(STATIC_DIR, PUBLIC_DIR)
    print(extract_title(TEST_MD))


if __name__ == "__main__":
    main()
