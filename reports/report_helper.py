from reports import python_report_gen
from reports import html_report_gen
from reports import base_report_gen
import csv, sys


def type_of_report(all_file_paths, file_type_list):
    file_type_list = file_type_list
    all_file_paths = all_file_paths
    print(f"what type of report would you like?")
    
    while True:
        report_type = input(f"File Type Report Options: {file_type_list}: base ")
        if report_type != "exit":
            if report_type.lower() in file_type_list or report_type.lower() == "base":
                if report_type == "base":
                     base_reports(all_file_paths, file_type_list)
                if report_type == "py":
                    python_reports(all_file_paths, file_type_list)
                if report_type == "html":
                    html_reports(all_file_paths, file_type_list)
        else:
            sys.exit()


 #functions one for each type of file 
def python_reports(all_file_paths, file_type_list):      
    
        while True:
            print(f"\n Python \n")
            print("1. Full Report\n2. File List\n3. Unique Imports\n4. Classes\n5. Functions\n6. Comments\n")
            function_number = input("Enter Number for Report or exit: ")
            if function_number != "exit":
                with open("reports\csv_files/python_summary.csv", mode='r') as file:
                    data = list(csv.DictReader(file))
                    if function_number == "1": python_report_gen.main(data)
                    if function_number == "2": python_report_gen.p_files(data)
                    if function_number == "3": python_report_gen.imports(data)
                    if function_number == "4": python_report_gen.classes(data)
                    if function_number == "5": python_report_gen.functions(data)
                    if function_number == "6": python_report_gen.comments(data)
            else:
                type_of_report(all_file_paths, file_type_list)
                

def html_reports(all_file_paths, file_type_list):      
    
        while True:
            print(f"\n HTML \n")
            print("1. Full Report\n2. File List\n3. Comments\n4. Text\n")
            function_number = input("Enter Number for Report or exit: ")
            if function_number != "exit":
                with open("reports\csv_files/html_summary.csv", mode='r') as file:
                    data = list(csv.DictReader(file))
                    if function_number == "1": html_report_gen.main(data)
                    if function_number == "2": html_report_gen.html_files(data)
                    if function_number == "3": html_report_gen.comments(data)
                    if function_number == "4": html_report_gen.text(data)
            else:
                 type_of_report(all_file_paths, file_type_list)


def base_reports(all_file_paths, file_type_list):
     while True:
            print(f"\n Base \n")
            print("1. File Tree\n")
            function_number = input("Enter Number for Report or exit: ")
            if function_number != "exit":
                with open("reports\csv_files/html_summary.csv", mode='r') as file:
                    data = list(csv.DictReader(file))
                    if function_number == "1": base_report_gen.file_tree(all_file_paths)
            else:
                 type_of_report(all_file_paths, file_type_list)