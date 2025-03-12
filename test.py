import os, re

class PythonProjectAnalyzer:
    def __init__(self, directory, output_file="output.txt"):
        ''' Initialize the analyzer with a target directory'''

        self.directory = directory
        self.output_file = output_file
        self.files = []
        self.lines = []
        self.imports = []
        self.functions = []

    def gather_files(self, allowed_extensions=None):

        '''Gather all .py files in directory'''
        allowed_extensions = allowed_extensions or [".py"]
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
                    

    #TODO transfer this into my class
    def write_report(self):

        import_pattern = r"^(import\s+|from\s+\w+\s+import\s+)"
        function_pattern = r"^def\s+"
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
                
                    if re.match(function_pattern, line):
                            output.write(f"{line}\n")


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
   

    def analize(self):
        ''''
        Perform full analysis workflow
        '''
        self.gather_files()
        self.clean_file()
        self.get_functions()
        self.get_imports()
        self.write_report()
        


analyzer = PythonProjectAnalyzer(r"C:/Users/chris/Desktop/note_summarizer")
analyzer.analize()

