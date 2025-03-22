import csv
import re

csv_data = []
html_summary_file = "reports/csv_files/html_summary.csv"


def process_line_for_csv(line, file):
    """Process each line and store relevant data for CSV."""
    h1_pattern = r"<h1>"
    tag_pattern = r"<a.+>"       # Match HTML tags
    comment_pattern = r"<!--.*?-->"  # Match HTML comments

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
        "Type": None,  # import, class, function, comment
        "Content": line
    }
    #TODO this is a todo comment

    if re.match(comment_pattern, line.strip(), re.DOTALL):
        row["Type"] = "comment"
    elif re.match(tag_pattern, line.strip()):
        row["Type"] = "link"
    elif re.match(h1_pattern, line.strip()):  # Non-empty line that's not a tag or comment
        row["Type"] = "h1"
    else:
        return  # Ignore blank or irrelevant lines

    csv_data.append(row)  # Add the row to the CSV data list
    write_csv_summary()

def write_csv_summary():
    """Write the collected data to a CSV file."""
    with open(html_summary_file, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["FileType", "File", "Directory", "FileName", "Type", "Content"])
        writer.writeheader()  # Write column headers
        writer.writerows(csv_data)  # Write all rows