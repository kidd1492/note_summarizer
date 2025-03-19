#from reports import report_helper
from analyzers import python_analyzer,  html_analyzer
import os, re, csv


# provide a directory you want analyzed
directory = "C:/Users/chris/Desktop/test_flask"

csv_data = []

# Mapping of file extensions to their respective analyzers
file_type_analyzer_map = {
    "html": html_analyzer,
    "py": python_analyzer,
    # Add more file types and analyzers if needed
}


def main():
    categorized_files = gather_categorized_files(directory)
    analyzed_file_summary(categorized_files)


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

'''
#function to search through directory extract wanted files
#ignore directories not wanted
def gather_files(directory):
    all_file_paths = []
    file_type_list = []
    #Gather all .py files in directory
    allowed_extensions = [".py", ".md", ".txt", ".html", ".css", ".js"] #update ect. to add file type
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


#feed a lit of files paths, list of file types convert to categorized_files
def gather_file_by_type(all_file_paths, file_types):
    categorized_files = {file_type: [] for file_type in file_types}
    
    for file in all_file_paths:
        for file_type in file_types:
            if file.endswith(file_type):
                categorized_files[file_type].append(file)
    
    return categorized_files


def clean_file(file_list):
    """Process files and store results in CSV format."""
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                if stripped_line:
                   process_line_for_csv(stripped_line, file)




def process_line_for_csv(line, file):
    """Process each line and store relevant data for CSV."""
    tag_pattern = r"<[^>]+>"       # Match HTML tags
    comment_pattern = r"<!--.*?-->"  # Match HTML comments

    # Initialize a dictionary for each line's data
    row = {
        "File": file,
        "Type": None,  # tag, comment, text
        "Content": line.strip()
    }

    if re.match(comment_pattern, line.strip(), re.DOTALL):
        row["Type"] = "comment"
    elif re.match(tag_pattern, line.strip()):
        row["Type"] = "tag"
    elif line.strip():  # Non-empty line that's not a tag or comment
        row["Type"] = "text"
    else:
        return  # Ignore blank or irrelevant lines

    csv_data.append(row)  # Add the row to the CSV data list
    write_csv_summary()


def write_csv_summary():
    """Write the collected data to a CSV file."""
    with open(html_summary_file, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["File", "Type", "Content"])
        writer.writeheader()  # Write column headers
        writer.writerows(csv_data)  # Write all rows
'''

if __name__ == "__main__":
    main()
   