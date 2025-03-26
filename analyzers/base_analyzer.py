from analyzers import html_analyzer, python_analyzer
import os, csv

# Mapping of file extensions to their respective analyzers
file_type_analyzer_map = {
    "html": html_analyzer,
    "py": python_analyzer,
    # Add more file types and analyzers if needed
}


def generate_csv(directory):
    categorized_files = gather_categorized_files(directory)
    create_csv_summary()
    for file_type, file_list in categorized_files.items():
        analyzer = file_type_analyzer_map.get(file_type)
        if analyzer:  # Ensure an analyzer is available for this file type
            csv_data = analyzer.process_line_for_csv(file_list)     
            write_csv_summary(csv_data)           


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


def create_csv_summary():
    with open(summary_file, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["FileType", "File", "Directory", "FileName", "Type", "Content"])
        writer.writeheader()  # Write column headers


summary_file = "reports/csv_files/file_summary.csv"
def write_csv_summary(csv_data):
    with open(summary_file, "a", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["FileType", "File", "Directory", "FileName", "Type", "Content"])
        writer.writerows(csv_data)  # Write all rows