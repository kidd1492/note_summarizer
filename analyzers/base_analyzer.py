from analyzers import html_analyzer, python_analyzer, js_analyzer
import os, csv

# Mapping of file extensions to their respective analyzers
file_type_analyzer_map = {
    "html": html_analyzer,
    "py": python_analyzer,
    "js": js_analyzer
    # Add more file types and analyzers if needed
}


#called from main.main() takes file list for each file type it check
#if there is an analyzer then hands the list off to analyzer to process lines
def generate_csv(directory):
    categorized_files = gather_categorized_files(directory)
    create_csv_summary()
    for file_type, file_list in categorized_files.items():
        analyzer = file_type_analyzer_map.get(file_type)
        if analyzer:  # Ensure an analyzer is available for this file type
            csv_data = analyzer.process_line_for_csv(file_list)     
            write_csv_summary(csv_data)           


'''function to walk through a directory pick what kinds of file it wants
ignoring directory like venv, .git it then saves the type of file and a list of 
files for that type into a dict. returns catagorized files'''
def gather_categorized_files(directory):
    allowed_extensions = [".py", ".html", "js"]  # Update to add more file types
    ignored_directories = [".git", "env", "venv"]
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


#TODO fix this to be one function??
#function creates the summary file and clears all info then writes the header.
def create_csv_summary():
    with open(summary_file, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["FileType", "File", "Directory", "FileName", "Type", "Content"])
        writer.writeheader()  # Write column headers

#function appends the csv data returned by the analyzer to the csv summary file.
summary_file = "reports/csv_files/file_summary.csv"
def write_csv_summary(csv_data):
    with open(summary_file, "a", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["FileType", "File", "Directory", "FileName", "Type", "Content"])
        writer.writerows(csv_data)  # Write all rows