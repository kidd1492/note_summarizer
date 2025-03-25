from reports import report_helper
from analyzers import analyzer
import os, re, sys


def main():
    args = sys.argv

    if len(args) == 1:
        print("Please enter report or enter directory path")

    elif len(args) == 2:
        if args[1].lower() == "report":
            report_helper.file_type()
        else:
            path_pattern = r"^[A-Z]:[\\/](?:[^\\/]+[\\/])*[^\\/]*$"
    
            directory_name = args[1].replace("\\", "/")  
            if re.match(path_pattern, directory_name): 
                if os.path.isdir(directory_name):
                    categorized_files = gather_categorized_files(directory_name)
                    generate_csv(categorized_files)
            else:
                print("invalid path name! Please try again: ")     


def gather_categorized_files(directory):
    allowed_extensions = [".py", ".md", ".html"]  # Update to add more file types
    ignored_directories = [".git", "env", "enve", "venv"]
    categorized_files = {}

    for root, dirs, files in os.walk(directory): 
        dirs[:] = [d for d in dirs if d not in ignored_directories]# Skip ignored directories
        for file in files:
            # Check if the file's extension is in the allowed list
            if any(file.endswith(ext) for ext in allowed_extensions):
                ext = file.split('.')[-1]  # Extract the file extension (without dot)

                # Initialize the list for this file type if not already present
                if ext not in categorized_files:
                    categorized_files[ext] = []
                # Append the file path to the appropriate list
                categorized_files[ext].append(os.path.join(root, file))

    return categorized_files


def generate_csv(categorized_files):
    categorized_files = categorized_files
    for file_type, file_list in categorized_files.items():
        for file in file_list:
            with open(file, 'r', encoding='utf-8') as f:
                for line in f:
                    stripped_line = line.strip()
                    if stripped_line:
                        analyzer.process_line_for_csv(stripped_line, file)


if __name__ == "__main__":
    main()