from copystatic import clean_target_dir, copy_static_assets


PUBLIC_DIR = "./public"
STATIC_DIR = "./static"


def main():
    clean_target_dir(PUBLIC_DIR)
    copy_static_assets(STATIC_DIR, PUBLIC_DIR)


if __name__ == "__main__":
    main()
