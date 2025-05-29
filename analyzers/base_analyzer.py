from analyzers import html_analyzer, python_analyzer, js_analyzer
import logging, csv

# Mapping of file extensions to their respective analyzers
file_type_analyzer_map = {
    "html": html_analyzer,
    "py": python_analyzer,
    "js": js_analyzer
}


def generate_csv(categorized_files):
    try:
        for file_type, file_list in categorized_files.items():
            analyzer = file_type_analyzer_map.get(file_type)
            if analyzer:  # Ensure an analyzer is available for this file type
                analyzer.process_line_for_csv(file_list)
                
    except Exception as e:
        logging.error(f"An error occurred during analysis: {e}")


def write_csv_summary(csv_data, out_file):
    try:
        with open(out_file, "w", newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["FileType", "File", "Directory", "FileName", "Type", "Content"])
            writer.writerows(csv_data)  # Write all rows
    except Exception as e:
        logging.error(f"An error occurred while writing to the CSV summary file: {e}")