import csv
import re

csv_data = []
python_summary_file = "reports/csv_files/python_summary.csv"


def process_line_for_csv(line, file):
    """Process each line and store relevant data for CSV."""
    comment_pattern = r"^#|^[\"']{3}"
    function_pattern = r"^def\s+"

    # Initialize a dictionary for each line's data
    row = {
        "File": file,
        "Type": None,  # import, class, function, comment
        "Content": line
    }
    #TODO this is a todo comment
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
        

    else:
        return  # Ignore lines that don't match any pattern

    csv_data.append(row)  # Add the row to the CSV data list
    write_csv_summary()

def write_csv_summary():
    """Write the collected data to a CSV file."""
    with open(python_summary_file, "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["File", "Type", "Content"])
        writer.writeheader()  # Write column headers
        writer.writerows(csv_data)  # Write all rows
