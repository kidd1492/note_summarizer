import csv
import re

python_summary_file = "reports/csv_files/python_summary.csv"

# Lists to store CSV rows
csv_data = []


def analyze(python_files):
    """Perform the full analysis workflow and output to CSV."""
    clean_file(python_files)
    write_csv_summary()
    
    print(f"Results saved in: {python_summary_file}")

            
def clean_file(python_files):
    """Process files and store results in CSV format."""
    for file in python_files:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                if stripped_line:
                    process_line_for_csv(stripped_line, file)


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

    if line.startswith("import") or line.startswith("from"):
        row["Type"] = "import"
    elif line.startswith("class "):
        row["Type"] = "class"
    elif re.match(function_pattern, line):
        row["Type"] = "function"
    elif re.match(comment_pattern, line):
        row["Type"] = "comment"
    else:
        return  # Ignore lines that don't match any pattern

    csv_data.append(row)  # Add the row to the CSV data list


def write_csv_summary():
    """Write the collected data to a CSV file."""
    with open(python_summary_file, "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["File", "Type", "Content"])
        writer.writeheader()  # Write column headers
        writer.writerows(csv_data)  # Write all rows


if __name__ == "__analyze__":
    analyze()