from analyzers import html_analyzer, python_analyzer
import csv

# Mapping of file extensions to their respective analyzers
file_type_analyzer_map = {
    "html": html_analyzer,
    "py": python_analyzer,
    # Add more file types and analyzers if needed
}


def generate_csv(all_file_paths, file_types):
    categorized_files = gather_file_by_type(all_file_paths, file_types)

    for file_type, file_list in categorized_files.items():
        analyzer = file_type_analyzer_map.get(file_type)
        if analyzer:  # Ensure an analyzer is available for this file type
            clean_file(file_list, analyzer)


def gather_file_by_type(all_file_paths, file_types):
    categorized_files = {file_type: [] for file_type in file_types}
    
    for file in all_file_paths:
        for file_type in file_types:
            if file.endswith(file_type):
                categorized_files[file_type].append(file)
    
    return categorized_files
        

def clean_file(file_list, analyzer):
    """Process files and store results in CSV format."""
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                if stripped_line:
                   analyzer.process_line_for_csv(stripped_line, file)
        