
import re

csv_data = []


def process_line_for_csv(file_list):
    """Process each line and store relevant data for CSV."""
    script_pattern = r"<script[^>]*>"
    link_pattern = r"<link[^>]*>"
    image_pattern = r"<img[^>]*>"
    meta_pattern = r"<meta[^>]*>"
    inline_style_pattern = r"style\s*=\s*['\"]"
    comment_pattern = r"<!--.*-->"


    for file in file_list:
        try:
            file_part = file.split("\\" or "/") 
            directory = file_part[-2]
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
                        if re.match(script_pattern, line):
                            row["Type"] = "script"
                        elif re.match(link_pattern, line):
                            row["Type"] = "link"
                        elif re.match(image_pattern, line):
                            row["Type"] = "image"
                        elif re.match(meta_pattern, line):
                            row["Type"] = "meta"
                        elif re.search(inline_style_pattern, line):
                            row["Type"] = "inline_style"
                        elif re.match(comment_pattern, line):
                            row["Type"] = "comment"
                        else:
                            continue  # Ignore blank or irrelevant lines

                        csv_data.append(row)  # Add the row to the CSV data list
                    except Exception:
                        # Skip problematic lines quietly
                        continue
        except Exception:
            # Skip the entire file if there are issues
            continue
                    
    return csv_data
