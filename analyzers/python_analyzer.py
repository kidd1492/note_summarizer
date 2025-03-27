import os
import re

csv_data = []

def process_line_for_csv(file_list):
    """Process each line and store relevant data for CSV."""
    comment_pattern = r"^#|^[\"']{3}"
    function_pattern = r"^def\s+"

    for file in file_list:
        try:
            # Normalize the file path for cross-platform compatibility
            file_part = os.path.normpath(file).split(os.sep)
            directory = file_part[-2] if len(file_part) > 1 else "Unknown"
            file_name = file_part[-1]
            file_type = file_name.split('.')[-1]

            with open(file, 'r', encoding='utf-8') as f:
                for line in f:
                    try:
                        # Initialize a dictionary for each line's data
                        line = line.strip()
                        row = {
                            "FileType": file_type,
                            "File": file,
                            "Directory": directory,
                            "FileName": file_name,
                            "Type": None,  # all data is named and collected in Type
                            "Content": line.strip()
                        }

                        # Classify line content
                        if line.startswith("import") or line.startswith("from"):
                            row["Type"] = "import"
                        elif line.startswith("class"):
                            row["Type"] = "class"
                        elif re.match(function_pattern, line):
                            row["Type"] = "function"
                        elif re.match(comment_pattern, line):
                            row["Type"] = "comment"
                            if line.startswith("#TODO"):
                                row["Type"] = "todo"
                        elif line.startswith("return"):
                            row["Type"] = "return"
                        else:
                            continue
                        # Add the row to the CSV data list
                        csv_data.append(row)
                    except Exception:
                        # Skip problematic lines quietly
                        continue
        except Exception:
            # Skip the entire file if there are issues
            continue

    return csv_data