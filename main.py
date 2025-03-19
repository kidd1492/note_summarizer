from reports import report_helper
from analyzers import base_analyzer
import os, re


def main():
    directory = get_directory()
    categorized_files = gather_categorized_files(directory)
    base_analyzer.generate_csv(categorized_files)
    #report_helper.type_of_report()
    

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


def gather_categorized_files(directory):
    allowed_extensions = [".py", ".md", ".txt", ".html", ".css", ".js"]  # Update to add more file types
    ignored_directories = [".git", "env", "enve", "venv"]
    categorized_files = {}

    for root, dirs, files in os.walk(directory):
        # Skip ignored directories
        dirs[:] = [d for d in dirs if d not in ignored_directories]
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


if __name__ == "__main__":
    main()