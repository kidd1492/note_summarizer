from reports import base_report_gen
import csv, sys

csv_report_file = "reports/csv_files/file_summary.csv"


def type_of_report(categorized_files): 
    #auto generates file_type_list added main
    file_type_list = ["tools"]
    for file_type, file_list in categorized_files.items():
         file_type_list.append(file_type)
         
           
    while True:
        print(f"[tools] for general information: \nwhat type of report would you like?\n")
        print(f"{file_type_list}: \n")
        report_type = input("Select File Type or Exit: ")
        
        if report_type != "exit":
            if report_type.lower() in file_type_list:
                if report_type == "tools":
                     base_report_gen.base_reports(categorized_files)
                if report_type.lower() == "py":
                    reports(categorized_files, "py")
                if report_type.lower() == "html":
                    reports(categorized_files, "html")
        else:
            sys.exit()


#TODO Clean up these functions. reduce 
#TODO make a function for printing information and one for writing data
def reports(categorized_files, type):
    
    file_search_list = ["all"]
    with open(csv_report_file, mode='r') as file:
        data = list(csv.DictReader(file))
        while True:
            print("\n")
            for row in data:
                if row["FileType"] == type:
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
            print("\n")
            for row in data:
                if row["Type"] not in types_of_data:
                    types_of_data.append(row["Type"])
                    print(row["Type"])

            print(f"\nfor all data [main] What data?:")
            data_input = input("or [back] to files: ")
            if data_input == "back":reports(categorized_files)
            if data_input == "main":
                for item in types_of_data:
                    for row in data:
                        if row["Type"] == item:
                            print(row["Type"], row["FileName"], "------", row["Content"])
            print("\n")
            if file_search == "all":
                for row in data:    
                    if row["Type"] == data_input:
                        print(row["Type"], row["FileName"], "------", row["Content"])
            if data_input in types_of_data:      
                for row in data:
                    if row["FileName"] == file_search:
                        if row["Type"] == data_input:
                            print(row["Type"], row["FileName"], "------", row["Content"])
                    
