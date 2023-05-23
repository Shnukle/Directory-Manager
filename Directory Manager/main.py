from pathlib import Path
from dir_manage import dir_manager

usrinput = input("enter directory: ")

path = Path(usrinput)

if path.exists() == True:
    dir_manager.check_directory(usrinput)
    confirm = input("are you sure you want to permanantly delete these files? [Y] [N] ")
    if confirm == 'y':
        dir_manager.delete_files(usrinput)
    else: print("files unchanged")
else: print("error: directory could not be found")