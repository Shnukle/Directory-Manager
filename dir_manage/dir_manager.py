from pathlib import Path

def delete_files(filepath):
    p = Path(filepath)
    for file in p.glob('*.*'):
        try:
            file.unlink()
        except PermissionError:
            print(f"Permission error: Could not delete {file}")