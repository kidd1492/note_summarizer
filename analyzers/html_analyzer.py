import csv
import re

html_summary_file = "reports/csv_files/html_summary.csv"
#p_file_count = 0
html_files = []

# Lists to store CSV rows
csv_data = []


def analyze(all_file_paths):
    gather_html_files(all_file_paths)
    clean_file()
    write_csv_summary()

    print(f"Results saved in: {html_summary_file}")


#gather all html files append them to list
def gather_html_files(all_file_paths):    
    for file in all_file_paths:      
        if file.endswith(".html"):
            html_files.append(file)


def clean_file():
    """Process files and store results in CSV format."""
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                if stripped_line:
                    process_line_for_csv(stripped_line, file)


def process_line_for_csv(line, file):
    """Process each line and store relevant data for CSV."""
    tag_pattern = r"<[^>]+>"       # Match HTML tags
    comment_pattern = r"<!--.*?-->"  # Match HTML comments

    # Initialize a dictionary for each line's data
    row = {
        "File": file,
        "Type": None,  # tag, comment, text
        "Content": line.strip()
    }

    if re.match(comment_pattern, line.strip(), re.DOTALL):
        row["Type"] = "comment"
    elif re.match(tag_pattern, line.strip()):
        row["Type"] = "tag"
    elif line.strip():  # Non-empty line that's not a tag or comment
        row["Type"] = "text"
    else:
        return  # Ignore blank or irrelevant lines

    csv_data.append(row)  # Add the row to the CSV data list

def process_html_file(file_path):
    """Extract information from an HTML file."""
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            process_line_for_csv(line, file_path)

def write_csv_summary():
    """Write the collected data to a CSV file."""
    with open(html_summary_file, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["File", "Type", "Content"])
        writer.writeheader()  # Write column headers
        writer.writerows(csv_data)  # Write all rows