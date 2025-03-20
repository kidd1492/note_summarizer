from reports import report_helper
from analyzers import html_analyzer, python_analyzer
import os, re

# Mapping of file extensions to their respective analyzers
file_type_analyzer_map = {
    "html": html_analyzer,
    "py": python_analyzer,
    # Add more file types and analyzers if needed
}



def main():
    directory = get_directory()
    categorized_files = gather_categorized_files(directory)
    generate_csv(categorized_files)
    report_helper.type_of_report(categorized_files)
    

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
    allowed_extensions = [".py", ".md", ".html"]  # Update to add more file types
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


def generate_csv(categorized_files):
    categorized_files = categorized_files
    for file_type, file_list in categorized_files.items():
        analyzer = file_type_analyzer_map.get(file_type)
        if analyzer:  # Ensure an analyzer is available for this file type
            clean_file(file_list, analyzer)
    analyzed_file_summary(categorized_files)


def clean_file(file_list, analyzer):
    """Process files and store results in CSV format."""
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                if stripped_line:
                   analyzer.process_line_for_csv(stripped_line, file)


def analyzed_file_summary(categorized_files):
    total_analyzed_files = 0
    number_of_file_types = 0

    for file_type, file_list in categorized_files.items():
        total_analyzed_files += 1
        analyzer = file_type_analyzer_map.get(file_type)
        if analyzer:  # Ensure an analyzer is available for this file type
            number_of_file_types += 1
            total_analyzed_files += len(file_list)
            print(f"{file_type} Number of files: {len(file_list)}")
        else:
            print(f"{file_type} Number of files: {len(file_list)} --- No Analyzer")
            total_analyzed_files += len(file_list)
    print(f"\n{number_of_file_types} Files Types Analyzed:  Total Files Paths {total_analyzed_files}\n")


if __name__ == "__main__":
    main()