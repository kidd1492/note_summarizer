from analyzers import html_analyzer, python_analyzer

html_files = []
python_files = []


#function to seperate all the file types in one place.
def gather_file_by_type(all_file_paths, file_type_list):    
    for file in all_file_paths:      
        if file.endswith(".py"): python_files.append(file)
        if file.endswith(".html"): html_files.append(file)
    start_analyzers(file_type_list)


#function to gather data into csv
def start_analyzers(file_type_list):
    
    if "py" in file_type_list: python_analyzer.analyze(python_files)
    if "html" in file_type_list: html_analyzer.analyze(html_files)

        