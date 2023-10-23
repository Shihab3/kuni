import os
import time

def get_file_metadata(path):
    try:
        # Get file information using os.stat
        file_info = os.stat(path)
        
        # Extract metadata from the file_info object
        file_metadata = {
            'Size (bytes)': file_info.st_size,
            'Last Modified': time.ctime(file_info.st_mtime),
            'Mode': file_info.st_mode
        }

        return file_metadata
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return None

def set_file_metadata(path, metadata):
    try:
        # Retrieve the current file metadata
        current_metadata = get_file_metadata(path)
        
        if current_metadata is not None:
            # Modify the metadata based on the provided dictionary
            for key, value in metadata.items():
                if key == 'Size (bytes)':
                    # Change the file size (not recommended)
                    os.truncate(path, value)
                elif key == 'Last Modified':
                    # Change the last modified timestamp (not recommended)
                    os.utime(path, (time.time(), time.mktime(time.strptime(value))))
                elif key == 'Mode':
                    # Change the file permissions
                    os.chmod(path, int(value, 8))
                else:
                    print(f"Unsupported metadata attribute: {key}")
    except FileNotFoundError:
        print(f"File '{path}' not found.")

