from analyzers import base_analyzer
import re

csv_data = []


def process_line_for_csv(file_list):
    """Process each line and store relevant data for CSV."""
    h1_pattern = r"<h1>"
    tag_pattern = r"<a.+>"       # Match HTML tags
    html_comment_pattern = r"<!--.*?-->"  # Match HTML comments

    for file in file_list:

        file_part = file.split("\\" or "/") 
        directory = file_part[-2]
        file_name = file_part[-1]
        file_type = file_name.split('.')[-1]

        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
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

                if re.match(html_comment_pattern, line.strip(), re.DOTALL):
                    row["Type"] = "comment"
                elif re.match(tag_pattern, line.strip()):
                    row["Type"] = "link"
                elif re.match(h1_pattern, line.strip()):  # Non-empty line that's not a tag or comment
                    row["Type"] = "h1"
                else:
                    continue  # Ignore blank or irrelevant lines

                csv_data.append(row)  # Add the row to the CSV data list
    return csv_data
