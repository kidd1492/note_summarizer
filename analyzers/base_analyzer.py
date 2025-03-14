import os, re

class BaseAnalyzer:
    def __init__(self, directory):
        ''' Initialize the analyzer with a target directory'''

        self.directory = directory
        self.files = []
        self.file_type_list = []
        
        self.python_files = []
        self.html_files = []

        
    
    def gather_files(self):
        '''Gather all .py files in directory'''
        allowed_extensions = [".py", ".md", ".txt", ".html"]
        for root, dirs, files in os.walk(self.directory):
            # Skip .git directories entirely and enve
            dirs[:] = [d for d in dirs if d not in [".git", "env", "enve", "venv"]]
            for file in files:
                # Check if the file's extension is in the allowed list
                if any(file.endswith(ext) for ext in allowed_extensions):
                    self.files.append(os.path.join(root, file))
                    #add to list for file types
                    ext = file.split('.')[-1]
                    if ext not in self.file_type_list:
                        self.file_type_list.append(ext)

        for file in self.files:    
            # Check if the file's extension is in the allowed list
            if file.endswith(".py"):
                self.python_files.append(file)

            if file.endswith(".html"):
                self.html_files.append(file)

    