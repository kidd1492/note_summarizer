import csv
import re

csv_data = []
summary_file = "reports/csv_files/file_summary.csv"


def process_line_for_csv(line, file):
    """Process each line and store relevant data for CSV."""
    comment_pattern = r"^#|^[\"']{3}"
    function_pattern = r"^def\s+"
    h1_pattern = r"<h1>"
    tag_pattern = r"<a.+>"       # Match HTML tags
    html_comment_pattern = r"<!--.*?-->"  # Match HTML comments

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
        "Content": line
    }
   
    # python rows
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

    #TODO html rows  rework this to be differant analyzers and move the write_csv       
    elif re.match(html_comment_pattern, line.strip(), re.DOTALL):
        row["Type"] = "comment"
    elif re.match(tag_pattern, line.strip()):
        row["Type"] = "link"
    elif re.match(h1_pattern, line.strip()):  # Non-empty line that's not a tag or comment
        row["Type"] = "h1"
    else:
        return  # Ignore lines that don't match any pattern

    csv_data.append(row)  # Add the row to the CSV data list
    write_csv_summary()


#TODO move this function to central loacation
def write_csv_summary():
    """Write the collected data to a CSV file."""
    with open(summary_file, "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["FileType", "File", "Directory", "FileName", "Type", "Content"])
        writer.writeheader()  # Write column headers
        writer.writerows(csv_data)  # Write all rows
