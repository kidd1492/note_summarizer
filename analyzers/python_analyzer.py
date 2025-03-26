from analyzers import base_analyzer
import re

summary_file = "reports/csv_files/python_summary.csv"
csv_data = []
def process_line_for_csv(file_list):
    """Process each line and store relevant data for CSV."""
    comment_pattern = r"^#|^[\"']{3}"
    function_pattern = r"^def\s+"

    for file in file_list:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                if stripped_line:
                    file_part = file.split("\\" or "/") 
                    directory = file_part[-2]
                    file_name = file_part[-1]
                    file_type = file_name.split('.')[-1]

                    # Initialize a dictionary for each line's data
                    row = {
                        "FileType": file_type, 
                        "File": file,
                        "Directory": directory,
                        "FileName": file_name,
                        "Type": None,  # all data is named and collected in Type
                        "Content": line.strip()
                        }
                    
                    if line.startswith("import") or line.startswith("from"):
                        row["Type"] = "import"
                    elif line.startswith("class "):
                        row["Type"] = "class"
                    elif re.match(function_pattern, line):
                        row["Type"] = "function"
                    elif re.match(comment_pattern, line):
                        row["Type"] = "comment"
                        if line.startswith("#TODO"):
                            row["Type"] = "todo"
                    else:
                        continue
                    csv_data.append(row)  # Add the row to the CSV data list
    return csv_data