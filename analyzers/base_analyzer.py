import os, re

class BaseAnalyzer:
    def __init__(self, directory, output_file="output.txt"):
        ''' Initialize the analyzer with a target directory'''

        self.directory = directory
        self.output_file = output_file
        self.files = []
        self.lines = []
        self.comments = []


    def gather_files(self, allowed_extensions=None):
        '''Gather all .py files in directory'''
        allowed_extensions = allowed_extensions
        for root, dirs, files in os.walk(self.directory):
            # Skip .git directories entirely and enve
            dirs[:] = [d for d in dirs if d not in [".git", "env", "enve"]]
            for file in files:
                # Check if the file's extension is in the allowed list
                if any(file.endswith(ext) for ext in allowed_extensions):
                    self.files.append(os.path.join(root, file))


    def clean_file(self):
        '''
        Read all files and remove blank lines
        '''
        for file in self.files: 
            with open(file, "r") as f:
                for line in f:
                    stripped_line = line.strip()
                    if stripped_line == '':
                        continue
                    else:
                        self.lines.append(stripped_line)


    def gather_comments(self):
        comment_pattern = r"^#|^[\"']{3}"    
        for line in self.lines:      
            if re.match(comment_pattern, line):
                self.comments.append(line)
                #print(self.comments)