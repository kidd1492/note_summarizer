import re, os


html_output_file = "html_output_file.txt"
html_summary_file = "html_summary_file.txt"

html_files = []
lines = []

def analyze(all_file_paths):
    gather_html_files(all_file_paths)
    clean_file()
    for file in html_files:
        print(file)


#gather all html files append them to list
def gather_html_files(all_file_paths):    
    for file in all_file_paths:      
        if file.endswith(".html"):
            html_files.append(file)


def clean_file():
    
    #Read all files and remove blank lines
    
    for file in html_files: 
        with open(file, "r") as f:
            for line in f:
                stripped_line = line.strip()
                if stripped_line == '':
                    continue
                else:
                    lines.append(stripped_line)

