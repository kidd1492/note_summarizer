import os, re

class BaseAnalyzer:
    def __init__(self, all_file_paths):
        ''' Initialize the analyzer with a target directory'''
        self.all_file_paths = all_file_paths
        self.total_file_count = 0


    def file_count(self):
        for file in self.all_file_paths:
            self.total_file_count += 1
                   
