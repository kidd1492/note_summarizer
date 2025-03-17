from reports import report_helper
from analyzers import base_analyzer
import os, re


def main():
    directory = get_directory()
    all_file_paths, file_type_list = gather_files(directory)
    base_analyzer.gather_file_by_type(all_file_paths, file_type_list)
    report_helper.type_of_report(all_file_paths, file_type_list)
    

def get_directory():
    ''' ask user for filepath '''
    path_pattern = r"^[A-Z]:[\\/](?:[^\\/]+[\\/])*[^\\/]*$"

    while True:
        directory_name = input("ex. C:/Desktop/file_name\nFile Path Name:").replace("\\", "/")  
        if re.match(path_pattern, directory_name):
            try:
                if os.path.isdir(directory_name):
                    return directory_name
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")      


def gather_files(directory):
    all_file_paths = []
    file_type_list = []
    '''Gather all .py files in directory'''
    allowed_extensions = [".py", ".md", ".txt", ".html"]
    for root, dirs, files in os.walk(directory):
        # Skip .git directories entirely and enve
        dirs[:] = [d for d in dirs if d not in [".git", "env", "enve", "venv"]]
        for file in files:
            # Check if the file's extension is in the allowed list
            if any(file.endswith(ext) for ext in allowed_extensions):
                all_file_paths.append(os.path.join(root, file))
                #add to list for file types
                ext = file.split('.')[-1]
                if ext not in file_type_list:
                    file_type_list.append(ext)
    return [all_file_paths, file_type_list]



if __name__ == "__main__":
    main()