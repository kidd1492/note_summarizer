#File Summarizer Tool
## -Overview
The File Summarizer Tool is a Python-based utility designed to gather and process files from a directory structure. It allows users to filter files by extension, exclude specific directories (e.g., .git, env, enve), and prepares the groundwork for summarizing or analyzing the content of those files.

#Features
-Directory Traversal: Recursively walks through a specified directory and its subdirectories.
-File Filtering: Gathers only files with specified extensions (e.g., .py, .txt, .js).
-Exclusion of Directories: Automatically skips directories like .git, env, and enve to streamline processing.

Output: The script will print a list of gathered files that meet the filtering criteria.

Current Project Structure
plaintext.
Analyzed Files:
C:/Users/chris/Desktop/note_summarizer\main.py

Imports:

import os, re
import inspect

Functions:

def main():
def gather_files(directory, allowed_extensions):
def write_report(paths):

Analyzed Files:
C:/Users/chris/Desktop/note_summarizer\python_analyzer.py

##Next Steps

-Specify Allowed File Extensions: Define the file extensions you want to include in the allowed_extensions list (e.g., [".py", ".txt"]).
-Implement a summarization feature to process and summarize the gathered files.

Add support for saving summarized content to a new directory or database.

Enhance error handling.

License
This project is licensed under the MIT License. See LICENSE for more details.
