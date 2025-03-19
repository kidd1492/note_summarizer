# Note Summarizer Project

The **Note Summarizer** is a Python-based project analyzer designed to parse and analyze the structure of Python and Web base files could be great for Flask and Django projects. It will generate CSV reports for each file type, and provide insights into the analyzed codebase. The project is structured to be easily extensible, supporting additional analyzers for other file types (e.g., CSS, JavaScript) in the future.


## Features
- The program collects all file paths in the specified directory for the supported file types (currently Python and HTML).
- Based on the file type, the program calls the appropriate analyzer (e.g., PythonAnalyzer, HTMLAnalyzer).
- Analyzers parse the file content, extract relevant information, and generate a CSV report for each file type.
- CSV reports are saved in the csv_file directory with details about the analyzed files.
- The CSV files can be used for generating detailed reports, visualization, or further analysis.
- Easily integrates with projects built using frameworks like Django and Flask.



## Program Flow
```	
		                note_summarizer/
                           -—main.py  file in note_summarizer/—

def main():
—def get_directory():                  #gets directory from user returns directory
—gather_categorized_files(directory):  #directory transferred to gather files using oswalk()
    —def generate_csv(categorized_files):—--|	
|                                           |            **analyzers/**
|                                           |          —base_analyzer.py—
                                            |
                                            |-def generate_csv(categorized_files): 
	                                                def clean_file(file_list, analyzer):
	                                                    def process_line_for_csv(line, file):
                                                                                     |
                                                                                     |
Add analyzer:  build analyzer with process_line_for_csv(line, file). Analyzer will go into analyzers/.

In base_analyzer.py  add import for analyzer, 2. Add file type to file_type_analyzer_map
 ex("py": python_analyzer,): NO DOT, JUST “py” or whatever file extension and analyzer
               |
               |---------------------------------------------------------------------|
		       |	—python_analyzer.py—
               |----------   def process_line_for_csv(line, file):
                                def write_csv_summary():

                    —html_analyzer.py—
                            def process_line_for_csv(line, file):
                                def write_csv_summary():	

```
## Installation
Clone this repository:

bash
git clone https://github.com/username/note_summarizer.git
Navigate to the project directory:
Set up your venv


### Run the program:
bash
python main.py


License
This project is licensed under the MIT License. See the LICENSE file for more details.