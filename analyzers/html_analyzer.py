from .base_analyzer import BaseAnalyzer
import re, os

class HTMLAnalyzer(BaseAnalyzer):
    def __init__(self, directory):
        ''' Initialize the analyzer with a target directory'''
        super().__init__(directory)

        self.html_output_file = "output_file.txt"
        self.html_summary_file = "summary_report.txt"
        self.html_files = []
        self.lines = []


    def analyze(self):
        print("ok you made it! what next?")

    '''
    def gather_html_files(self):
        #Gather only html files (.html) files
        for file in self.files:
            self.html_files.append(file)
    '''