from analyzers import html_analyzer, python_analyzer
import csv

# Mapping of file extensions to their respective analyzers
file_type_analyzer_map = {
    "html": html_analyzer,
    "py": python_analyzer,
    # Add more file types and analyzers if needed
}


def generate_csv(categorized_files):
    categorized_files = categorized_files

    for file_type, file_list in categorized_files.items():
        analyzer = file_type_analyzer_map.get(file_type)
        if analyzer:  # Ensure an analyzer is available for this file type
            clean_file(file_list, analyzer)
    process_line_for_csv(categorized_files)
    analyzed_file_summary(categorized_files)


def clean_file(file_list, analyzer):
    """Process files and store results in CSV format."""
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                if stripped_line:
                   analyzer.process_line_for_csv(stripped_line, file)
        

def analyzed_file_summary(categorized_files):
    total_analyzed_files = 0
    number_of_file_types = 0

    for file_type, file_list in categorized_files.items():
        total_analyzed_files += 1
        analyzer = file_type_analyzer_map.get(file_type)
        if analyzer:  # Ensure an analyzer is available for this file type
            number_of_file_types += 1
            total_analyzed_files += len(file_list)
            print(f"{file_type} Number of files: {len(file_list)}")
        else:
            print(f"{file_type} Number of files: {len(file_list)} --- No Analyzer")
            total_analyzed_files += len(file_list)
    print(f"\n{number_of_file_types} Files Types Analyzed:  Total Files Paths {total_analyzed_files}\n")



csv_data = []
file_summary = "reports/csv_files/file_summary.csv"
def process_line_for_csv(categorized_files):
    with open(file_summary, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["Type", "File"])
        writer.writeheader()  # Write column headers

        for file_type, file_list in categorized_files.items():
            for file in file_list:
                row = {
                    "Type": None,  # py, html, txt, js
                    "File": None,  
                }

                row["Type"] = file_type
                row["File"] = file
                csv_data.append(row)  # Add the row to the CSV data list
                write_csv_summary()



def write_csv_summary(): 
    """Write the collected data to a CSV file."""
    with open(file_summary, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["Type", "File"])
        writer.writeheader()  # Write column headers
        writer.writerows(csv_data)  # Write all rows