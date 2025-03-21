from reports import base_report_gen
import csv, sys


def type_of_report(categorized_files):
    analyzed_file_summary(categorized_files)
    #auto generates file_type_list added main
    file_type_list = ["tools"]
    for file_type, file_list in categorized_files.items():
         file_type_list.append(file_type)
         
           
    while True:
        print(f"{file_type_list}: \n")
        print(f"[tools] for general information: \nwhat type of report would you like?\n")
        report_type = input("Select File Type or Exit: ")
        if report_type != "exit":
            if report_type.lower() in file_type_list:
                if report_type == "tools":
                     base_report_gen.base_reports(categorized_files)
                if report_type.lower() == "py":
                    csv_report_file = "reports/csv_files/python_summary.csv"
                    reports(categorized_files, csv_report_file)
                if report_type.lower() == "html":
                    csv_report_file = "reports/csv_files/html_summary.csv"
                    reports(categorized_files, csv_report_file)
        else:
            sys.exit()


def analyzed_file_summary(categorized_files):
    total_analyzed_files = 0
    number_of_file_types = 0
    print()
    for file_type, file_list in categorized_files.items():
        number_of_file_types += 1
        total_analyzed_files += len(file_list)
        print(f"{file_type} files: {len(file_list)}")
    else:
        #total_analyzed_files += len(file_list)
        print(f"\n{number_of_file_types} Files Types Analyzed:  Total Files Paths {total_analyzed_files}\n")


#TODO Clean up these functions. reduce 
def reports(categorized_files, csv_report_file):
    
    file_search_list = ["all"]
    with open(csv_report_file, mode='r') as file:
        data = list(csv.DictReader(file))
        while True:
            for row in data:
                if row["FileName"] not in file_search_list:
                    file_search_list.append(row["FileName"])
                    print(row["FileName"])
            print(f"\nWhat file would you like to analyze:[all] for all files ")
            file_search = input("or [back] to go back to Report Types: ")

            if file_search == "back":type_of_report(categorized_files)
            if file_search in file_search_list:
                data_type(file_search, categorized_files, csv_report_file)


def data_type(file_search, categorized_files, csv_report_file):

    types_of_data = []
    with open(csv_report_file, mode='r') as file:
        data = list(csv.DictReader(file))
        while True:
            for row in data:
                if row["Type"] not in types_of_data:
                    types_of_data.append(row["Type"])
                    print(row["Type"])

            print(f"\nfor all data [main] What data?:")
            data_input = input("or [back] to files: ")
            if data_input == "back":reports(categorized_files, csv_report_file)
            if data_input == "main":print_full_report(csv_report_file, types_of_data)
            if file_search == "all":
                for row in data:    
                    if row["Type"] == data_input:
                        print(row["Type"], row["FileName"], "------", row["Content"])
            if data_input in types_of_data:      
                for row in data:
                    if row["FileName"] == file_search:
                        if row["Type"] == data_input:
                            print(row["Type"], row["FileName"], "------", row["Content"])
            



def print_full_report(csv_report_file, types_of_data):
    #TODO fix the type_of_data_list to auto generate

    with open(csv_report_file, mode='r') as file:
        data = list(csv.DictReader(file))
        
        for item in types_of_data:
            for row in data:
                if row["Type"] == item:
                    print(row["Type"], row["FileName"], "------", row["Content"])
            print("\n")
