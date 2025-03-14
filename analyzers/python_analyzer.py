from .base_analyzer import BaseAnalyzer
import re, os

class PythonProjectAnalyzer(BaseAnalyzer):
    def __init__(self, all_file_paths):
        ''' Initialize the analyzer with a target directory'''
        super().__init__(all_file_paths)

        self.python_output_file = "python_output.txt"
        self.python_summary_file = "python_summary.txt"

        self.all_file_paths = all_file_paths

        self.python_files = []
        self.lines = []

    def gather_python_files(self):    
        for file in self.all_file_paths:      
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
            

    def write_files(self, output):
        """all file paths in project folder"""
        output.write(f"All File Paths\n")
        for file in self.python_files:
            output.write(f"{file}\n")


    def write_functions(self, output):
        """gather all function decorators in files"""
        function_pattern = r"^def\s+"
        output.write("\n")
        output.write(f"\nAll Functions\n")
        for line in self.lines:
            if re.match(function_pattern, line):
                output.write(f"{line}\n")
  

    def write_imports(self, output):
        '''gathers all import statements from files'''
        import_pattern = r"^(import\s+|from\s+\w+\s+import\s+)"
        output.write("\n")
        output.write(f"\nAll Imports\n")
        for line in self.lines:
            if re.match(import_pattern, line):
                output.write(f"{line}\n")


    def write_comments(self, output):
        comment_pattern = r"^#|^[\"']{3}"
        output.write("\n")    
        for line in self.lines:      
            if re.match(comment_pattern, line):
                output.write(f"{line}\n")


   
    def analyze(self):
        #Perform full analysis workflow   
        self.gather_python_files()
        self.clean_file()

    def full_report(self):
        '''Full reort file, imports, functions for each file'''
        with open(self.python_output_file, "w") as output:
            self.write_files(output)
            self.write_imports(output)
            self.write_functions(output)
            self.write_comments(output)
