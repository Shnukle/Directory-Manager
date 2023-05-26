from pathlib import Path

def delete_files(filepath):
    p = Path(filepath)
    for item in p.glob('*'):
        if item.is_file():
            try:
                item.unlink()
            except PermissionError:
                print(f"Permission error: Could not delete {item}")
        elif item.is_dir():
            try:
                item.rmdir()
            except PermissionError:
                print(f"Permission error: Could not delete {item}")

def check_directory(filepath):
    p = Path(filepath)
    for item in p.glob('*'):
        print(item)

def create_directory(filepath):
    p = Path(filepath)
    try:
        p.mkdir()
        print(f"directory {filepath} created.")
    except PermissionError:
        print(f"directory {filepath} couldn't be created due to a permission error.")
    except FileExistsError:
        print(f"directory {filepath} already exists.")

def rename_file(filepath, new_name):
    p = Path(filepath)
    new_path = p.with_name(new_name)
    try:
        p.rename(new_path)
        print(f"path renamed")
    except FileNotFoundError:
        print("file not found")
    except PermissionError:
        print("permmision error")
    



