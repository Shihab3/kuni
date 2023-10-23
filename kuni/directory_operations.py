import os

def list_files_and_directories(directory):
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    print(f'File: {entry.name}')
                elif entry.is_dir():
                    print(f'Directory: {entry.name}')
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
