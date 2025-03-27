import os
import re

csv_data = []

def process_line_for_csv(file_list):
    """Process .js files and extract relevant information for CSV."""
    function_pattern = r"^function\s+|const\s+\w+\s*=\s*\(.*\)\s*=>"
    variable_pattern = r"^var\s+|^let\s+|^const\s+"
    event_pattern = r"\.addEventListener\("
    api_call_pattern = r"fetch|axios"
    import_pattern = r"^import\s+|^require\("
    
    for file in file_list:
        try:
            # Normalize the file path for cross-platform compatibility
            file_part = os.path.normpath(file).split(os.sep)
            directory = file_part[-2] if len(file_part) > 1 else "Unknown"
            file_name = file_part[-1]
            file_type = file_name.split('.')[-1]

            if file_type != "js":
                # Skip files that are not .js
                continue
            
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
                            "Type": None,  # The type of line content (e.g., function, variable)
                            "Content": line.strip()
                        }

                        # Classify line content
                        if re.match(function_pattern, line):
                            row["Type"] = "function"
                        elif re.match(variable_pattern, line):
                            row["Type"] = "variable"
                        elif re.search(event_pattern, line):
                            row["Type"] = "event_listener"
                        elif re.search(api_call_pattern, line):
                            row["Type"] = "api_call"
                        elif re.match(import_pattern, line):
                            row["Type"] = "import"
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