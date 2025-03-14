from .base_analyzer import BaseAnalyzer
import re, os

class HTMLAnalyzer(BaseAnalyzer):
    def __init__(self, directory):
        ''' Initialize the analyzer with a target directory'''
        super().__init__(directory)

        self.html_output_file = "html_output_file.txt"
        self.html_summary_file = "html_summary_file.txt"
        
        self.lines = []
        
        
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
        self.gather_files()
        self.clean_file()
        print(self.html_files)