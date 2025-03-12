from base_analyzer import BaseAnalyzer
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
   

    #TODO funtion to get comments and docstring append to report


    def analize(self):
        ''''
        Perform full analysis workflow
        '''
        self.gather_files()
        self.clean_file()
        self.get_functions()
        self.get_imports()
        self.write_report()
        


def main():
    directory = get_directory()
    analyzer = PythonProjectAnalyzer(directory)
    analyzer.analize()

def get_directory():
    ''' ask user for filepath '''
    path_pattern = r"^[A-Z]:[\\/](?:[^\\/]+[\\/])*[^\\/]*$"

    while True:
        directory_name = input("ex. C:/Desktop/file_name\nFile Path Name:").replace("\\", "/")  
        if re.match(path_pattern, directory_name):
            try:
                if os.path.isdir(directory_name):
                    return directory_name
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")      


if __name__ == "__main__":
    main()