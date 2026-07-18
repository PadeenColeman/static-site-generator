import os, shutil


def delete_public_start_copy(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    os.mkdir(destination)
    recursive_copy(source, destination)


def recursive_copy(source, destination):
    if os.path.isfile(source):
        shutil.copy(source, destination)
    else:
        for item in os.listdir(source):
            source_path = os.path.join(source, item)
            dest_path = os.path.join(destination, item)
            if os.path.isfile(source_path):
                print(f"Copying file: {source_path} -> {dest_path}")
                shutil.copy(source_path, dest_path)
            else:
                print(f"Creating directory: {dest_path}")
                os.mkdir(dest_path)
                recursive_copy(source_path, dest_path)
