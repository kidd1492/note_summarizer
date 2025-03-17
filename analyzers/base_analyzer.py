from reports import report_helper
from analyzers import html_analyzer, python_analyzer
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
        
        if "py" in self.file_type_list:
            python_analyzer.analyze(self.all_file_paths)

        if "html" in self.file_type_list:
            html_analyzer.analyze(self.all_file_paths)


    def reports(self):
        self.count_files()
        print()
        print(f"Analyzed files {self.file_count} \n")
        report_helper.type_of_report(self.file_type_list, self.all_file_paths)
        

        