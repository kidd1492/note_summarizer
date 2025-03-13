import os, re

class BaseAnalyzer:
    def __init__(self, directory):
        ''' Initialize the analyzer with a target directory'''

        self.directory = directory
        self.files = []
        

    def gather_files(self):
        '''Gather all .py files in directory'''
        allowed_extensions = [".py", ".md", "txt"]
        for root, dirs, files in os.walk(self.directory):
            # Skip .git directories entirely and enve
            dirs[:] = [d for d in dirs if d not in [".git", "env", "enve"]]
            for file in files:
                # Check if the file's extension is in the allowed list
                if any(file.endswith(ext) for ext in allowed_extensions):
                    self.files.append(os.path.join(root, file))
                