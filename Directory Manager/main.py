from pathlib import Path
from dir_manage import dir_manager

while True:
    operation = input("select operation (check_directory, delete_contents, rename_file, create_directory, quit) ")

    if operation == "delete_contents":
        usrinput = input("enter directory: ")
        path = Path(usrinput)
        if path.exists() == True:
            confirm = input("are you sure you want to permanantly the contents? [Y] [N] ")
            if confirm == 'y':
                dir_manager.delete_files(usrinput)
            else: print("files unchanged")
        else: print("directory could not be found")

    elif operation == "check_directory":
        usrinput = input("enter directory: ")
        path = Path(usrinput)
        if path.exists() == True:
            dir_manager.check_directory(usrinput)
        else: print("directory could not be found")

    elif operation == "create_directory":
        usrinput = input("enter directory: ")
        path = Path(usrinput)
        dir_manager.create_directory(usrinput)

    elif operation == "rename_file":
        usrinput = input("enter path of file you want to rename ")
        newName = input("enter new name ")
        dir_manager.rename_file(usrinput, newName)
    
    elif operation == "quit":
        break

    else: print("operation not available. ")
