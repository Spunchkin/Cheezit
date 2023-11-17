import os
import shutil
import sys
import search

argc = len(sys.argv)

if argc > 1:
    if sys.argv[1] == "-h":
        print("Help: -s type directory : Sort(-s type(1.filetype, 2.name))")
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
                with open("logs.clog", "w") as log:
                    log.write(f"Sorted files in {directory}, sorted by type")
                    log.close()

            elif sys.argv[2] in ("2", "name"):
                for filename in os.listdir(directory):
                    if os.path.isfile(os.path.join(directory, filename)):
                        _, file_extension = os.path.splitext(filename)
                        folder_path = os.path.join(directory, file_extension[1:])
                        
                        if not os.path.exists(folder_path):
                            os.makedirs(folder_path)

                        source_path = os.path.join(directory, filename)
                        destination_path = os.path.join(folder_path, filename)
                        shutil.move(source_path, destination_path)
                with open("logs.clog", "w") as log:
                    log.write(f"Sorted files in {directory}, sorted by name")

    elif sys.argv[1] == "-l":
        with open("logs.clog", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line, end="")

            
else:
    print("No arguments specified")
