import os

def bulk_rename_files(directory, new_names):
    try:
        if not os.path.exists(directory):
            print(f"Directory '{directory}' not found.")
            return

        if not os.path.isdir(directory):
            print(f"'{directory}' is not a directory.")
            return

        files = os.listdir(directory)
        for i, file in enumerate(files):
            if os.path.isfile(os.path.join(directory, file)):
                old_path = os.path.join(directory, file)
                new_name = new_names[i] if i < len(new_names) else file
                new_path = os.path.join(directory, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed '{file}' to '{new_name}'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def bulk_delete_files(directory):
    try:
        if not os.path.exists(directory):
            print(f"Directory '{directory}' not found.")
            return

        if not os.path.isdir(directory):
            print(f"'{directory}' is not a directory.")
            return

        files = os.listdir(directory)
        for file in files:
            if os.path.isfile(os.path.join(directory, file)):
                file_path = os.path.join(directory, file)
                os.remove(file_path)
                print(f"Deleted '{file}'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
