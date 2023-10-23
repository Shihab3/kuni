def compare_files(file1, file2):
    try:
        with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
            content1 = f1.read()
            content2 = f2.read()
            
            if content1 == content2:
                return True
            else:
                return False
    except FileNotFoundError:
        print("One or both files not found.")
        return False
