from .base_analyzer import BaseAnalyzer
import re, os

class PythonProjectAnalyzer(BaseAnalyzer):
    def __init__(self, directory):
        ''' Initialize the analyzer with a target directory'''
        super().__init__(directory)

        self.output_file = "output_file.txt"
        self.summary_file = "summary_report.txt"


    def gather_files(self, allowed_extensions=None):
        '''Gather only Python (.py) files'''
        allowed_extensions = allowed_extensions or [".py"]
        super().gather_files(allowed_extensions)


    def write_files(self, out_file):
        """all file paths in project folder"""
        with open(out_file, "a") as output:
            output.write("\n")
            output.write(f"All File Paths\n")
            for file in self.files:
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
            for full_path in self.files:
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


    def analize(self):
        ''''
        Perform full analysis workflow
        '''
        self.gather_files()
        self.clean_file()
        self.gather_comments()


    def full_report(self):
        '''Full reort file, imports, functions for each file'''
        self.write_report(self.output_file)
        self.write_comments(self.output_file)


    def summary_report(self):
        self.write_files(self.summary_file)
        self.write_comments(self.summary_file)
        self.write_functions(self.summary_file)
        self.write_imports(self.summary_file)
