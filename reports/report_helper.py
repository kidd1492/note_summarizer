from reports import test
import csv, sys


def type_of_report(file_type_list):
    file_type_list = file_type_list
    print(f"what type of report would you like?")
    
    while True:
        report_type = input(f"File Type Report Options: {file_type_list}: ")
        if report_type != "exit":
            if report_type.lower() in file_type_list:
                if report_type == "py":
                    python_reports(file_type_list)
        else:
            sys.exit()


 #functions one for each type of file 
def python_reports(file_type_list):      
    
        while True:
            print(f"\n Python \n")
            print("1. Full Report\n2. File List\n3. Unique Imports\n4. Classes\n5. Functions\n6. Comments\n")
            function_number = input("Enter Number for Report or exit: ")
            if function_number != "exit":
                with open("reports\csv_files/python_summary.csv", mode='r') as file:
                    data = list(csv.DictReader(file))
                    if function_number == "1": test.main(data)
                    if function_number == "2": test.p_files(data)
                    if function_number == "3": test.imports(data)
                    if function_number == "4": test.classes(data)
                    if function_number == "5": test.functions(data)
                    if function_number == "6": test.comments(data)
            else:
                 type_of_report(file_type_list)
                