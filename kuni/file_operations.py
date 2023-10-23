import shutil
import os

def copy_file(source, destination):
    try:
        shutil.copy2(source, destination)
        print(f"File copied from '{source}' to '{destination}'")
    except FileNotFoundError:
        print(f"Source file '{source}' not found.")

def rename_file(path, new_name):
    try:
        os.rename(path, os.path.join(os.path.dirname(path), new_name))
        print(f"File '{path}' renamed to '{new_name}'")
    except FileNotFoundError:
        print(f"File '{path}' not found.")

def delete_file(path):
    try:
        os.remove(path)
        print(f"File '{path}' deleted.")
    except FileNotFoundError:
        print(f"File '{path}' not found.")
    except IsADirectoryError:
        print(f"'{path}' is a directory. Use 'shutil.rmtree' to delete directories.")

def change_file_permissions(path, mode):
    try:
        os.chmod(path, mode)
        print(f"File permissions changed for '{path}'")
    except FileNotFoundError:
        print(f"File '{path}' not found.")
    except PermissionError:
        print(f"Permission denied when changing file permissions for '{path}'")
