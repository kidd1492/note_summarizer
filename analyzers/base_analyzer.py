from analyzers import html_analyzer, python_analyzer


def start_analyzers(all_file_paths, file_type_list):
    
    if "py" in file_type_list:
        python_analyzer.analyze(all_file_paths)

    if "html" in file_type_list:
        html_analyzer.analyze(all_file_paths)

        