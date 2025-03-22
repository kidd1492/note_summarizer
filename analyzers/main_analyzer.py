import csv
import re

csv_data = []
file_summary_file = "reports/csv_files/file_summary.csv"


def clean_file(categorized_files):
    categorized_files = categorized_files
    for file_type, file_list in categorized_files.items():
        for file in file_list:
            #TODO put in error checking if it can't read the line or file
            with open(file, 'r', encoding='utf-8') as f:
                for line in f:
                    stripped_line = line.strip()
                    if stripped_line:
                        process_line_for_csv(stripped_line, file)



def process_line_for_csv(line, file):
    #python pattens
    comment_pattern = r"^#|^[\"']{3}"
    function_pattern = r"^def\s+"
    #html patterns
    tag_pattern = r"<a.+>"       # Match HTML tags
    comment_pattern = r"<!--.*?-->"  # Match HTML comments
    h1_pattern = r"<h1>"  # Match HTML comments
    div_pattern = r"<div .+>"
    
    file_part = file.split("\\" or "/") 
    directory = file_part[-2]
    file_name = file_part[-1]
    file_type = file_name.split(".")[-1]


    # Initialize a dictionary for each line's data
    row = {
        "FileType" : file_type,
        "File": file,
        "Directory": directory,
        "FileName": file_name,
        "Type": None,  # import, class, function, comment
        "Content": line
    }
    #python Type
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
    #html Type
    elif re.match(comment_pattern, line.strip(), re.DOTALL):
        row["Type"] = "comment"
    elif re.match(tag_pattern, line.strip()):
        row["Type"] = "link"
    elif re.match(h1_pattern, line.strip()):
        row["Type"] = "h1"
    elif re.match(div_pattern, line.strip()):
        row["Type"] = "div"
    else:
        return  # Ignore lines that don't match any pattern

    csv_data.append(row)  # Add the row to the CSV data list
    write_csv_summary()

#TODO get this function in a central location
def write_csv_summary():
    """Write the collected data to a CSV file."""
    with open(file_summary_file, "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["FileType", "File", "Directory", "FileName", "Type", "Content"])
        writer.writeheader()  # Write column headers
        writer.writerows(csv_data)  # Write all rows
