from os import path, listdir, mkdir
from shutil import copy, rmtree


def clean_target_dir(target_dir):
    if not path.exists(target_dir):
        raise FileNotFoundError(f"Target directory not found: {target_dir}")
    print(f"Cleaning target_dir: {target_dir}")
    rmtree(target_dir)
    mkdir(target_dir)


def copy_static_assets(src, dst):
    print("Copying static files to public directory...")
    if not path.exists(dst):
        mkdir(dst)

    for node in listdir(src):
        from_path = path.join(src, node)
        to_path = path.join(dst, node)
        print(f" - {from_path} -> {to_path}")
        if path.isfile(from_path):
            copy(from_path, to_path)
        else:
            copy_static_assets(from_path, to_path)
