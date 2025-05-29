# AI-Powered Code Security Scanner

## Overview
This project is a **security-focused code analyzer** designed to scan **Python, HTML, and JavaScript** projects for **potential vulnerabilities** before they enter production. It aims to help **developers and non-programmers** catch security flaws in AI-generated code, ensuring safe and secure software development.  Python-based project analyzer designed to parse and analyze the structure of Python and Web base files could be great for Flask and Django projects. It will generate a CSV reports with each file type, and provide insights into the analyzed codebase. The project is structured to be easily extensible, supporting additional analyzers for other file types (e.g., CSS, ) in the future.

## Features
- ✅ **Multi-language analysis** (Python, HTML, JavaScript)
- ✅ **Structured extraction** using regex-based analyzers
- ✅ **Automated security scanning** for common risks
- ✅ **CSV-based reporting** for easy review
- ✅ **AI-driven security analysis** using a custom **Ollama model**
- ✅ **Simple CLI-based execution** with directory scanning


## Program Flow
```	
		                                     note_summarizer/
-—main.py--
    -gather_categorized_files(directory)                
    -base_analyzer.generate_csv(categorized_files):--|                         analyzers/
    |                                                |	        
    |                                                |         --base_analyzer.py—
    |                                                |-------------gather_categorized_files(categorized_files)    
    |---reports/                                                   -create_csv_summary()
    |  csv_files/                                                  -analyzer.process_line_for_csv(file_list)|
    |     * pythonm_summary.csv                                    -write_csv_summary(csv_data, out_file)   |
                                                                                                            |
                                                                          --python_analyzer.py-_            |
                                                                    -def process_line_for_csv(file_list)----|
                                                                                                            |
                                                                          --html_analyzer.py--              |
                                                                    --def process_line_for_csv(file_list)---|
                                                                                                                                                                                                    --html_analyzer.py--              |
                                                                    --def process_line_for_csv(file_list)--=|     
```

Future Enhancements
🚀 Expand detection for more security vulnerabilities
🚀 Support additional programming languages
🚀 Integrate CI/CD automated security scans
🚀 Improve AI model's security understandin


## Installation
Clone this repository:

bash
git clone https://github.com/kidd1492/note_summarizer.git
Navigate to the project directory:
Set up your venv
pip install requirements.txt (pandas)


### Run the program:
bash
- python main.py # will give back enter directory path

1. run main.py with a directory path to analyze the files...
python main.py C:/Desktop/SomeDirectory  # if valid directory will generate the csv


License
This project is licensed under the MIT License. See the LICENSE file for more details.