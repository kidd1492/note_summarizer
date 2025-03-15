# Note Summarizer Project

The **Note Summarizer** is a Python-based project analyzer designed to parse and analyze the structure of Python and HTML files, generate CSV reports, and provide insights into the analyzed codebase. The project is structured to be easily extensible, supporting additional analyzers for other file types (e.g., CSS, JavaScript) in the future.

## Features

- Analyze Python and HTML files.
- Extract meaningful data such as imports, functions, classes, comments, and file-specific details.
- Generate detailed CSV reports for each file type.
- Easily integrates with projects built using frameworks like Django and Flask.

## Project Structure

```plaintext
note_summarizer/
├── analyzers/
│   ├── __init__.py
│   ├── base_analyzer.py         # Base class for all analyzers
│   ├── html_analyzer.py         # Analyzer for HTML files
│   ├── python_analyzer.py       # Analyzer for Python files
│   └── (Add future analyzers here)
├── main.py                      # Entry point for the program
├── reports/                     # (Optional) Directory for report generation
|   |__ test.py                  #python summary report displays on screen
|   |
│   └── (Add report-specific modules here)
|   |__ python_summary.csv           # Generated CSV file with analysis results
└── utils/                       # (Optional) Utilities used by the project
    └── (Add helper functions or scripts here)
```

## Workflow
Start the Program:

- Run the main.py file.

- Enter the directory containing the files you want to analyze.

- Gather Files:

The program collects all file paths in the specified directory for the supported file types (currently Python and HTML).

## Analyze Files:

- Based on the file type, the program calls the appropriate analyzer (e.g., PythonAnalyzer, HTMLAnalyzer).

- Analyzers parse the file content, extract relevant information, and generate a CSV report.

## Output:

- CSV reports are saved in the root directory with details about the analyzed files.

## Process CSV Data:

The CSV files can be used for generating detailed reports, visualization, or further analysis.

### Example Output

Python files analyzed: 7
Results saved in: python_summary.csv

## Installation
Clone this repository:

bash
git clone https://github.com/username/note_summarizer.git
Navigate to the project directory:


### Run the program:

bash
python main.py


License
This project is licensed under the MIT License. See the LICENSE file for more details.