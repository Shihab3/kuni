import zipfile
import tarfile

def create_archive(files, archive_name, compression_format):
    if compression_format == 'zip':
        with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as archive:
            for file in files:
                archive.write(file)
    elif compression_format == 'tar':
        with tarfile.open(archive_name, 'w') as archive:
            for file in files:
                archive.add(file)
    else:
        print("Unsupported compression format")

def extract_archive(archive_path, destination_directory):
    if archive_path.endswith('.zip'):
        with zipfile.ZipFile(archive_path, 'r') as archive:
            archive.extractall(destination_directory)
    elif archive_path.endswith('.tar') or archive_path.endswith('.tar.gz') or archive_path.endswith('.tgz'):
        with tarfile.open(archive_path, 'r') as archive:
            archive.extractall(destination_directory)
    else:
        print("Unsupported archive format")

