import os

#returns all files with a specific extension
def search_files(directory, extension):
    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                result.append(os.path.join(root, file))
    return result
 
def search_files_by_name(directory, name):
    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith(name):
                result.append(os.path.join(root, file))
    return result

def search_files_by_size(directory, size_lessthan, size_greaterthan):
    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            size = os.stat(file)
            size = size.st_size
            if size > size_greaterthan and size < size_lessthan:
                result.append(os.path.join(root, file))
    return result
            
def get_unique_file_extensions(folder_path):
    folder_path = str(folder_path)
    extensions = set()
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = os.path.splitext(filename)[1]
            extensions.add(file_extension.lower())
    return extensions
