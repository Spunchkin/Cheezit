import os
import shutil
import sys
import search

argc = len(sys.argv)

script_directory = os.path.dirname(os.path.abspath(__file__))
log_file_directory = os.path.join(script_directory, "logs")
log_file_path = os.path.join(script_directory, "logs.clog")

def reverse_sort_by_type(directory):
    folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
    for folder in folders:
        folder_path = os.path.join(directory, folder)
        files = os.listdir(folder_path)
        for file in files:
            source_path = os.path.join(folder_path, file)
            destination_path = os.path.join(directory, file)
            try:
                shutil.move(source_path, destination_path)
            except:
                print(f"Error moving file {file} back to {directory}")
        try:
            os.rmdir(folder_path)  # Delete the empty folder
        except:
            print(f"Error deleting folder {folder_path}")

def reverse_sort_by_name(directory):
    folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
    for folder in folders:
        folder_path = os.path.join(directory, folder)
        files = os.listdir(folder_path)
        for file in files:
            source_path = os.path.join(folder_path, file)
            destination_path = os.path.join(directory, file)
            try:
                shutil.move(source_path, destination_path)
            except:
                print(f"Error moving file {file} back to {directory}")
        try:
            os.rmdir(folder_path)  # Delete the empty folder
        except:
            print(f"Error deleting folder {folder_path}")

if argc > 1:
    if sys.argv[1] == "-h":
        print("Help: -s type directory : Sort(-s type(1.filetype, 2.name))  -rs type directory : Reverse Sort(-s type(1.filetype, 2.name))  -l: Logs")
    elif sys.argv[1] == "-s":
        if argc > 2:
            if argc == 4:
                directory = sys.argv[3]
            else:
                directory = os.getcwd()
            if sys.argv[2] in ("1", "filetype"):
                extensions = search.get_unique_file_extensions(directory)
                for item in extensions:
                    if item:
                        folder_path = os.path.join(directory, item)
                        if not os.path.exists(folder_path):
                            os.mkdir(folder_path)
                        files = search.search_files(directory, item)
                        for file in files:
                            if file.endswith(item):
                                try:
                                    shutil.move(file, folder_path)
                                except:
                                    print("file either does not exist, or has already been moved")
                            else:
                                pass
                with open(log_file_path, "a") as log:
                    log.write(f"  Sorted files in {directory}, sorted by type")
                    log.close()

            elif sys.argv[2] in ("2", "name"):
                for filename in os.listdir(directory):
                    if os.path.isfile(os.path.join(directory, filename)):
                        file_first_letter = (filename[0]).capitalize()
                        folder_path = os.path.join(directory, file_first_letter)
                        if not os.path.exists(folder_path):
                            os.makedirs(folder_path)
                        source_path = os.path.join(directory, filename)
                        destination_path = os.path.join(folder_path, filename)
                        shutil.move(source_path, destination_path)
                with open(log_file_path, "a") as log:
                    log.write(f"  Sorted files in {directory}, sorted by name")
                    log.close()

    elif sys.argv[1] == "-l":
        with open(log_file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line, end="")
    
    elif sys.argv[1] == "-r": 
        if argc > 2:
            if argc > 3:
                directory = sys.argv[3]
            else:
                directory = os.getcwd()
            if sys.argv[2] in ["type", "1"]:
                reverse_sort_by_type(directory)
                with open(log_file_path, "a") as log:
                    log.write(f"  Reversed sorting by type in {directory}")
                    log.close()
            elif sys.argv[2] in ["name", "2"]:
                reverse_sort_by_name(directory)
                with open(log_file_path, "a") as log:
                    log.write(f"  Reversed sorting by name in {directory}")
                    log.close()

            
else:
    print("No arguments specified")
