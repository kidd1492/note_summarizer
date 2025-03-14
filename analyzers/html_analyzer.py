from .base_analyzer import BaseAnalyzer
import re, os

class HTMLAnalyzer(BaseAnalyzer):
    def __init__(self, all_file_paths):
        ''' Initialize the analyzer with a target directory'''
        super().__init__(all_file_paths)

        self.html_output_file = "html_output_file.txt"
        self.html_summary_file = "html_summary_file.txt"
        self.all_file_paths = all_file_paths
        self.html_files = []
        self.lines = []


    def gather_html_files(self):    
        for file in self.all_file_paths:      
            if file.endswith(".html"):
                self.html_files.append(file)




    def clean_file(self):
        '''
        Read all files and remove blank lines
        '''
        for file in self.html_files: 
            with open(file, "r") as f:
                for line in f:
                    stripped_line = line.strip()
                    if stripped_line == '':
                        continue
                    else:
                        self.lines.append(stripped_line)


    def analyze(self):
        self.gather_html_files()
        self.clean_file()
        