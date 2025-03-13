from .base_analyzer import BaseAnalyzer
import re, os

class PythonProjectAnalyzer(BaseAnalyzer):
    def __init__(self, directory, output_file="output.txt"):
        ''' Initialize the analyzer with a target directory'''
        super().__init__(directory, output_file)
        self.output_file = output_file
        self.imports = []
        self.functions = []


    def gather_files(self, allowed_extensions=None):
        '''Gather only Python (.py) files'''
        allowed_extensions = allowed_extensions or [".py"]
        super().gather_files(allowed_extensions)


    def get_functions(self):
        """gather all function decorators in files"""
        function_pattern = r"^def\s+"
        for line in self.lines:
            if re.match(function_pattern, line):
                self.functions.append(line)
  

    def get_imports(self):
        '''gathers all import statements from files'''
        import_pattern = r"^(import\s+|from\s+\w+\s+import\s+)"
        for line in self.lines:
            if re.match(import_pattern, line):
                self.imports.append(line)

    '''TODO write function for get classes
    get lines with class, self,'''

    def write_report(self):

        import_pattern = r"^(import\s+|from\s+\w+\s+import\s+)"
        function_pattern = r"^def\s+"
        class_pattern = r"^class\s+"
        with open(self.output_file, "w") as output:
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


    def write_comments(self):
        '''funtion to get comments and docstring append to report'''
        with open(self.output_file, "a") as output:
            output.write("\n\n")
            output.write("Python Comments:\n")
            for line in self.comments:      
                output.write(f"{line}\n")


    def analize(self):
        ''''
        Perform full analysis workflow
        '''
        self.gather_files()
        self.clean_file()
        self.gather_comments()
        self.get_functions()
        self.get_imports()


    def full_report(self):
        '''Full reort file, imports, functions for each file'''
        self.write_report()
        self.write_comments()
