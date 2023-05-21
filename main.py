from pathlib import Path
from dir_manage.dir_manager import delete_files

usrinput = input("enter directory: ")

path = Path(usrinput)

if path.exists() == True:
    delete_files(usrinput)
    print("files deleted")
else: print("error: directory could not be found")