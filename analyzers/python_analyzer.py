import os
import re

csv_data = []

def process_line_for_csv(file_list):
    import_pattern = r"^import\s+|^from\s+\w+\s+import"
    function_pattern = r"^def\s+"
    class_pattern = r"^class\s+"
    todo_pattern = r"^#TODO"
    comment_pattern = r"^#|^[\"']{3}"
    main_entry_pattern = r"^if\s+__name__\s*==\s*['\"]__main__['\"]:"
    return_pattern = r"^return"
    exception_handling_pattern = r"^try:|^except:|^finally:"

    
  

    for file in file_list:
        try:
            file_part = os.path.normpath(file).split(os.sep)
            directory = file_part[-2] if len(file_part) > 1 else "Unknown"
            file_name = file_part[-1]
            file_type = file_name.split('.')[-1]

            with open(file, 'r', encoding='utf-8') as f:
                for line in f:
                    try:
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
                        if re.match(import_pattern, line):
                            row["Type"] = "import"
                        elif re.match(function_pattern, line):
                            row["Type"] = "function"
                        elif re.match(class_pattern, line):
                            row["Type"] = "class"
                        elif re.match(todo_pattern, line):
                            row["Type"] = "todo"
                        elif re.match(comment_pattern, line):
                            row["Type"] = "comment"
                        elif re.match(main_entry_pattern, line):
                            row["Type"] = "main_entry"
                        elif re.match(return_pattern, line):
                            row["Type"] = "return"
                        elif re.match(exception_handling_pattern, line):
                            row["Type"] = "exception_handling"
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