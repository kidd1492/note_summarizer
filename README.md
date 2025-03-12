# File Summarizer Tool
## -Overview
The File Summarizer Tool is a Python-based utility designed to gather and process files from a directory structure. It allows users to filter files by extension, exclude specific directories (e.g., .git, env, enve), and prepares the groundwork for summarizing or analyzing the content of those files.


## Features
- Directory Traversal: Recursively walks through a specified directory and its subdirectories.
- File Filtering: Gathers only files with specified extensions (e.g., .py, .txt, .js).
- Exclusion of Directories: Automatically skips directories like .git, env, and enve to streamline processing.

## Current Project Structure
- note_summarizer/
  - analyzers/
    - \__init__.py
    - base_analyzer.py
    - python_analyzer.py
  
  - main.py

## output.txt
- Output.txt: The script will print the following...
- 
Analyzed Files:
C:/Users/chris/Desktop/note_summarizer\main.py

Imports:

import os, re
import inspect
def main():
def gather_files(directory, allowed_extensions):
def write_report(paths): ...

...
Python Comments:
''' ask user for filepath '''
''' Initialize the analyzer with a target directory'''
'''Gather only Python (.py) files'''
"""gather all function decorators in files"""
'''gathers all import statements from files'''

## Next Steps

- Enhance error handling.
- Add support for saving summarized content to a new directory or database.
- Add support for other file types.
- Add method to create a json file.

License
This project is licensed under the MIT License. See LICENSE for more details.
