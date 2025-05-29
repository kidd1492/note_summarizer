import os
import re
import logging

from analyzers import base_analyzer
csv_data = []

def process_line_for_csv(file_list):
    import_pattern = r"^\s*import\s+(\w+)"
    function_pattern = r"^\s*function\s+(\w+)\s*\("
    arrow_function_pattern = r"^\s*(const|let|var)\s+(\w+)\s*=\s*\(.*?\)\s*=>"
    variable_pattern = r"^\s*(const|let|var)\s+(\w+)\s*="
    loop_pattern = r"^\s*(for|while)\s*\("
    condition_pattern = r"^\s*(if|else\s*if|else)\s*\("
    event_listener_pattern = r"^\s*\w+\.addEventListener\s*\("
    comment_pattern = r"^\s*(//.*|/\*.*\*/)"  # Captures single-line and block comments
    return_pattern = r"^\s*return\s+[\w\s,]+;"
    exception_handling_pattern = r"^\s*(try|catch|finally)\s*"

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
                            "Type": None,
                            "Content": line.strip()
                        }

                        if re.match(import_pattern, line):
                            match = re.search(import_pattern, line)
                            if match:
                                row["Type"] = "Import"
                                row["Content"] = match.group(1)

                        elif re.match(function_pattern, line):
                            match = re.search(function_pattern, line)
                            if match:
                                row["Type"] = "Function"
                                row["Content"] = match.group(1)

                        elif re.match(arrow_function_pattern, line):
                            match = re.search(arrow_function_pattern, line)
                            if match:
                                row["Type"] = "Arrow Function"
                                row["Content"] = match.group(2)

                        elif re.match(variable_pattern, line):
                            match = re.search(variable_pattern, line)
                            if match:
                                row["Type"] = "Variable"
                                row["Content"] = match.group(2)

                        elif re.match(loop_pattern, line):
                            match = re.search(loop_pattern, line)
                            if match:
                                row["Type"] = "Loop"
                                row["Content"] = match.group(1)

                        elif re.match(condition_pattern, line):
                            match = re.search(condition_pattern, line)
                            if match:
                                row["Type"] = "Conditional Statement"
                                row["Content"] = match.group(1)

                        elif re.match(event_listener_pattern, line):
                            row["Type"] = "Event Listener"
                            row["Content"] = line

                        elif re.match(comment_pattern, line):
                            row["Type"] = "Comment"
                            row["Content"] = line

                        elif re.match(return_pattern, line):
                            row["Type"] = "Return Statement"
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

    base_analyzer.write_csv_summary(csv_data, "reports/csv_files/js_summary.csv")