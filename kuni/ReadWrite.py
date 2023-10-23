from pathlib import Path

def search_line(file_path, pattern):
    try:
        with open(file_path, "r") as file:
            return any(line for line in file if pattern in line)
    except FileNotFoundError:
        return False

def remove_line(file_path, target_line):
    try:
        file_path = Path(file_path)
        temp_file_path = file_path.with_name(file_path.name + ".temp")

        with open(file_path, "r") as file_input, open(temp_file_path, "w") as output:
            output.writelines(line for line in file_input if line.strip("\n") != target_line)

        temp_file_path.replace(file_path)
    except FileNotFoundError:
        pass

def write_text_data(file_path, data):
    with open(file_path, "w") as file:
        file.write(data)

def append_text_data(file_path, data):
    with open(file_path, "a") as file:
        file.write(data)

def append_line_text(file_path, data):
    with open(file_path, "a") as file:
        file.write('\n' + data)

def read_lines(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        return []

def write_data(file_path, data):
    data_bytes = data.encode('utf-8')
    with open(file_path, "wb") as file:
        file.write(data_bytes)

def read_data(file_path):
    try:
        with open(file_path, "rb") as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return None

