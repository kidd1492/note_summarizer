from .base_analyzer import BaseAnalyzer
import re

class PythonProjectAnalyzer(BaseAnalyzer):
    def __init__(self, all_file_paths):
        ''' Initialize the analyzer with a file path list'''
        super().__init__(all_file_paths)

        self.python_output_file = "python_output.txt"
        self.python_summary_file = "python_summary.txt"
        self.p_file_count = 0
        self.all_file_paths = all_file_paths

        self.python_files = []
    

    def gather_python_files(self):    
        for file in self.all_file_paths:      
            if file.endswith(".py"):
                self.python_files.append(file)
                self.p_file_count += 1


    def clean_file(self, output):
        """Process files and write results directly to output."""
        for file in self.python_files:
            output.write(" \n")
            output.write(f"{file}\n\n")
            with open(file, 'r', encoding='utf-8') as f:
                for line in f:
                    stripped_line = line.strip()
                    if stripped_line:
                        self.write_processed_line(output, stripped_line, file)


    def write_processed_line(self, output, line, file):
        """Write specific patterns directly to output file."""
        comment_pattern = r"^#|^[\"']{3}"
        if line.startswith("import") or line.startswith("from"):
            output.write(f"[IMPORT]: {line}\n")
        elif line.startswith("def "):
            output.write(f"[FUNCTION]: {line}\n")
        elif line.startswith("class "):
            output.write(f"[CLASS]: {line}\n")      
        elif re.match(comment_pattern, line):     
            output.write(f"\n{line}\n")
            

   
    def analyze(self):
        #Perform full analysis workflow 
        self.file_count()  
        self.gather_python_files()
        with open(self.python_output_file, "w") as output:
            output.write(f"Total Files Analyzed: {self.total_file_count}\n")
            self.clean_file(output)
            output.write(f"\nPython Files Analyzed:{self.p_file_count}")