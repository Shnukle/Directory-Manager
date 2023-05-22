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