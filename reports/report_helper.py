from reports import python_report_gen, html_report_gen, base_report_gen
import csv, sys


def type_of_report(categorized_files):
    file_type_list = []
    for file_type, file_list in categorized_files.items():
         file_type_list.append(file_type)
         
         
    print(f"what type of report would you like?")
    
    while True:
        report_type = input(f"File Type Report Options: {file_type_list}: base ")
        if report_type != "exit":
            if report_type.lower() in file_type_list or report_type.lower() == "base":
                if report_type == "base":
                     base_report_gen.base_reports(categorized_files)
                if report_type == "py":
                    python_report_gen.python_reports(categorized_files)
                if report_type == "html":
                    html_report_gen.html_reports(categorized_files)
        else:
            sys.exit()
