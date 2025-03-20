from reports import python_report_gen, html_report_gen, base_report_gen
import csv, sys


def type_of_report(categorized_files):
    analyzed_file_summary(categorized_files)

    file_type_list = ["exit", "All"]
    for file_type, file_list in categorized_files.items():
         file_type_list.append(file_type)
         
         
    print(f"what type of report would you like?")
    
    while True:
        report_type = input(f"{file_type_list}: \n\n")
        if report_type != "exit":
            if report_type.lower() in file_type_list:
                if report_type == "main":
                     base_report_gen.base_reports(categorized_files)
                if report_type == "py":
                    python_report_gen.python_reports(categorized_files)
                if report_type == "html":
                    html_report_gen.html_reports(categorized_files)
        else:
            sys.exit()


def analyzed_file_summary(categorized_files):
    total_analyzed_files = 0
    number_of_file_types = 0
    print()
    for file_type, file_list in categorized_files.items():
        #total_analyzed_files += 1
        number_of_file_types += 1
        total_analyzed_files += len(file_list)
        print(f"{file_type} files: {len(file_list)}")
    else:
        #total_analyzed_files += len(file_list)
        print(f"\n{number_of_file_types} Files Types Analyzed:  Total Files Paths {total_analyzed_files}\n")