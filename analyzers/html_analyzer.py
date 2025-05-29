import os
import re
import logging

from analyzers import base_analyzer
csv_data = []

def process_line_for_csv(file_list):
    import_pattern = r"^(from\s+\w+\s+)?import\s+(\w+(,\s*\w+)*)?"
    function_pattern = r"^\s*def\s+(\w+)\s*\("
    class_pattern = r"^\s*class\s+(\w+)\s*:"
    todo_pattern = r"^#TODO"
    comment_pattern = r"^\s*(\"{3}.*?\"|\'{3}.*?\')|^#"
    main_entry_pattern = r"^\s*if\s+__name__\s*==\s*['\"]__main__['\"]:"
    return_pattern = r"^\s*return\s+[\w\s,]+;"
    exception_handling_pattern = r"^\s*(try|except|finally):"

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

                        if re.match(import_pattern, line):
                            row["Type"] = "Import"
                            matches = re.findall(r'\b\w+\b', line)
                            row["Content"] = ', '.join(matches)

                        elif re.match(function_pattern, line):
                            match = re.search(r'(\w+)\s*\(', line)
                            if match:
                                row["Type"] = "Function"
                                row["Content"] = match.group(1)

                        elif re.match(class_pattern, line):
                            match = re.search(r'(\w+):', line)
                            if match:
                                row["Type"] = "Class"
                                row["Content"] = match.group(1)

                        elif re.match(todo_pattern, line):
                            row["Type"] = "Todo"
                            row["Content"] = line

                        elif re.match(comment_pattern, line):
                            row["Type"] = "Comment"
                            row["Content"] = line

                        elif re.match(main_entry_pattern, line):
                            row["Type"] = "Main Entry"
                            row["Content"] = line

                        elif re.match(return_pattern, line):
                            row["Type"] = "Return"
                            row["Content"] = line

                        elif re.match(exception_handling_pattern, line):
                            row["Type"] = "Exception Handling"
                            row["Content"] = line

                        csv_data.append(row)

                    except Exception as e:
                        logging.error(f"Error processing line in {file}: {e}")

        except FileNotFoundError:
            logging.error(f"File not found: {file}")
        except PermissionError:
            logging.error(f"Permission denied for file: {file}")
        except Exception as e:
            logging.error(f"An error occurred while processing {file}: {e}")

    base_analyzer.write_csv_summary(csv_data, "reports/csv_files/html_summary.csv")