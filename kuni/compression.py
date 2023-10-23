import gzip
import zipfile

def compress_file(file_path, compression_format):
    compressed_file_path = f"{file_path}.{compression_format}"

    if compression_format == 'gzip':
        try:
            with open(file_path, 'rb') as original_file, gzip.open(compressed_file_path, 'wb') as compressed_file:
                compressed_file.writelines(original_file)
        except Exception as e:
            print(f"An error occurred during compression: {str(e)}")
    elif compression_format == 'zip':
        try:
            with zipfile.ZipFile(compressed_file_path, 'w', zipfile.ZIP_DEFLATED) as archive:
                archive.write(file_path, arcname='compressed_file')
        except Exception as e:
            print(f"An error occurred during compression: {str(e)}")
    else:
        print("Unsupported compression format")

def decompress_file(file_path, compression_format):
    decompressed_file_path = file_path.rstrip(f".{compression_format}")

    if compression_format == 'gzip':
        try:
            with gzip.open(file_path, 'rb') as compressed_file, open(decompressed_file_path, 'wb') as original_file:
                original_file.writelines(compressed_file)
        except Exception as e:
            print(f"An error occurred during decompression: {str(e)}")
    elif compression_format == 'zip':
        try:
            with zipfile.ZipFile(file_path, 'r') as archive:
                archive.extractall(path='.', members=None)
        except Exception as e:
            print(f"An error occurred during decompression: {str(e)}")
    else:
        print("Unsupported compression format")
