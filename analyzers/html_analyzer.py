from .base_analyzer import BaseAnalyzer
import re, os

class HTMLAnalyzer(BaseAnalyzer):
    def __init__(self, directory):
        ''' Initialize the analyzer with a target directory'''
        super().__init__(self, directory)
