from .base_analyzer import BaseAnalyzer
import csv
import re

class PythonProjectAnalyzer(BaseAnalyzer):
    def __init__(self, all_file_paths):
        super().__init__(all_file_paths)
        self.python_summary_file = "python_summary.csv"
        self.p_file_count = 0
        self.all_file_paths = all_file_paths
        self.python_files = []

        # Lists to store CSV rows
        self.csv_data = []

    def gather_python_files(self):    
        for file in self.all_file_paths:      
            if file.endswith(".py"):
                self.python_files.append(file)
                self.p_file_count += 1

    def clean_file(self):
        """Process files and store results in CSV format."""
        for file in self.python_files:
            with open(file, 'r', encoding='utf-8') as f:
                for line in f:
                    stripped_line = line.strip()
                    if stripped_line:
                        self.process_line_for_csv(stripped_line, file)

    def process_line_for_csv(self, line, file):
        """Process each line and store relevant data for CSV."""
        comment_pattern = r"^#|^[\"']{3}"
        function_pattern = r"^def\s+"

        # Initialize a dictionary for each line's data
        row = {
            "File": file,
            "Type": None,  # import, class, function, comment
            "Content": line
        }

        if line.startswith("import") or line.startswith("from"):
            row["Type"] = "import"
        elif line.startswith("class "):
            row["Type"] = "class"
        elif re.match(function_pattern, line):
            row["Type"] = "function"
        elif re.match(comment_pattern, line):
            row["Type"] = "comment"
        else:
            return  # Ignore lines that don't match any pattern

        self.csv_data.append(row)  # Add the row to the CSV data list

    def write_csv_summary(self):
        """Write the collected data to a CSV file."""
        with open(self.python_summary_file, "w", newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["File", "Type", "Content"])
            writer.writeheader()  # Write column headers
            writer.writerows(self.csv_data)  # Write all rows

    def analyze(self):
        """Perform the full analysis workflow and output to CSV."""
        self.file_count()
        self.gather_python_files()
        self.clean_file()
        self.write_csv_summary()
        print(f"Python files analyzed: {self.p_file_count}")
        print(f"Results saved in: {self.python_summary_file}")
