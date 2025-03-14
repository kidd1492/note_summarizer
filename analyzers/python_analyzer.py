from .base_analyzer import BaseAnalyzer
import re, os

class PythonProjectAnalyzer(BaseAnalyzer):
    def __init__(self, directory):
        ''' Initialize the analyzer with a target directory'''
        super().__init__(directory)

        self.python_output_file = "python_output.txt"
        self.python_summary_file = "python_summary.txt"
        self.python_files = []
        self.lines = []
        self.comments = []


    def gather_python_files(self):
        '''Gather only Python (.py) files'''
        for file in self.files:
            # Check if the file's extension is in the allowed list
            if file.endswith(".py"):
                self.python_files.append(file)


    def clean_file(self):
        ''' Read Python files, remove blank lines, and process content. '''   
        for file in self.python_files:
            with open(file, 'r', encoding='utf-8') as f:
                for line in f:
                    stripped_line = line.strip()
                    if stripped_line == '':
                        continue
                    else:
                        self.lines.append(stripped_line)
            

    def gather_comments(self):
        '''TODO get better doc string
        next line until end'''
        comment_pattern = r"^#|^[\"']{3}"    
        for line in self.lines:      
            if re.match(comment_pattern, line):
                self.comments.append(line)


    def write_files(self, out_file):
        """all file paths in project folder"""
        with open(out_file, "a") as output:
            output.write("\n")
            output.write(f"All File Paths\n")
            for file in self.python_files:
                output.write(f"{file}\n")



    def write_functions(self, out_file):
        """gather all function decorators in files"""
        function_pattern = r"^def\s+"
        with open(out_file, "a") as output:
            output.write("\n")
            output.write(f"\nAll Functions\n")
            for line in self.lines:
                if re.match(function_pattern, line):
                    output.write(f"{line}\n")
  

    def write_imports(self, out_file):
        '''gathers all import statements from files'''
        import_pattern = r"^(import\s+|from\s+\w+\s+import\s+)"
        with open(out_file, "a") as output:
            output.write("\n")
            output.write(f"\nAll Imports\n")
            for line in self.lines:
                if re.match(import_pattern, line):
                    output.write(f"{line}\n")


    def write_comments(self, out_file):
        '''funtion to get comments and docstring append to report'''
        with open(out_file, "a") as output:
            output.write("\n\n")
            output.write("Python Comments:\n")
            for line in self.comments:      
                output.write(f"{line}\n")


    '''TODO write function for get classes
    get lines with class, self,'''


    def write_report(self, out_file):
        ''' outputs all files, imports, def, comments'''
        import_pattern = r"^(import\s+|from\s+\w+\s+import\s+)"
        function_pattern = r"^def\s+"
        class_pattern = r"^class\s+"
        with open(out_file, "w") as output:
            for full_path in self.python_files:
                output.write("\n")
                output.write("Analyzed Files:\n")
                output.write(f"{full_path}\n\n")
                output.write("Imports:\n\n")

                file = open(full_path, "r" )
                data = file.readlines()

                for line in data: 
                    line = line.strip()
                    if line == '':
                        continue

                    if re.match(import_pattern, line):
                        output.write(f"{line}\n")
                
                    if re.match(class_pattern, line):
                            output.write(f"{line}\n")

                    if re.match(function_pattern, line):
                            output.write(f"{line}\n")


    def analyze(self):
        ''''
        Perform full analysis workflow
        '''
        self.gather_files()
        self.gather_python_files()
        self.clean_file()
        self.gather_comments()


    def full_report(self):
        '''Full reort file, imports, functions for each file'''
        self.write_report(self.python_output_file)
        self.write_comments(self.python_output_file)


    def summary_report(self):
        self.write_files(self.python_summary_file)
        self.write_comments(self.python_summary_file)
        self.write_functions(self.python_summary_file)
        self.write_imports(self.python_summary_file)
