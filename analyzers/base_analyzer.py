from reports import report_helper
from analyzers import html_analyzer
import re

class BaseAnalyzer:
    def __init__(self, all_file_paths, file_type_list):
        ''' Initialize the analyzer with a types list and file list'''

        self.all_file_paths = all_file_paths
        self.file_type_list = file_type_list
        self.file_count = 0


    def count_files(self):
        for file in self.all_file_paths: self.file_count += 1


    def start_analyzers(self):
        
        #if "py" in self.file_type_list:
            #python_analyzer.analyze(self.all_file_paths)

        if "html" in self.file_type_list:
            html_analyzer.analyze(self.all_file_paths)

    #TODO function for directory file tree for files analyzed
    
    def file_tree(self):
        file_directory_list = []
        file_struct = []
        for file in self.all_file_paths:
            file = file.replace("\\", "/").split("/")
            if file[-1] not in file_directory_list:file_directory_list.append([file[-1], file[:-1]])
        
        for fd in file_directory_list:
            file_name = fd[0]
            directory_name = fd[1][-1]
            sub_directory = fd[1][-2]

            if sub_directory not in file_struct:file_struct.append(sub_directory)
            if directory_name not in file_struct: file_struct.append(directory_name)
            if file_name not in file_struct: file_struct.append(file_name)

        
        for item in file_struct:
            if re.match(r".\w+$", item):
                print(f"|-{item}\n")
            else:
                print(f"|---{item}")

        
    #TODO Functions to handel reports interface and function callers can dedicate to class?

    def reports(self):
        self.count_files()
        print()
        print(f"Analyzed files {self.file_count} \n")
        report_helper.type_of_report(self.file_type_list)
        

        