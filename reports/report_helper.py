from reports import base_report_gen
import csv, sys

csv_report_file = "reports/csv_files/file_summary.csv"


def type_of_report(categorized_files): 
    #auto generates file_type_list added main
    file_type_list = []
    for file_type, file_list in categorized_files.items():
         file_type_list.append(file_type)
             
    while True:
        print(f"\nwhat type of report would you like?\n")
        print(f"{file_type_list}: \n")
        type = input("Select File Type or Exit: ")
        
        if type != "exit":
            if type.lower() in file_type_list:
                files(categorized_files, type)
                return        
        else:
            sys.exit()


def files(categorized_files, type):
    file_list = ["all"]
    
    with open(csv_report_file, mode='r') as file:
        data = list(csv.DictReader(file))
    
        for row in data:
            if row["FileType"] == type:
                if row["FileName"] not in file_list:file_list.append(row["FileName"])

    while True:
        print("Files")
        for name in file_list:print(name) 

        print(f"\nWhat file would you like to analyze:[all] for all files ")
        file_search = input("or [back] to go back to Report Types: ")

        if file_search == "back":
            type_of_report(categorized_files)
            break
        elif file_search in file_list:
            data_type(categorized_files, type, file_search)
        else:
            continue
            


def data_type(categorized_files, type, file_list):
    data_opptions = ["all",]
    with open(csv_report_file, mode='r') as file:
        data = list(csv.DictReader(file))
        if file_list.lower() == "all":
            for row in data:
                if row["FileType"] == type:
                    if row["Type"] not in data_opptions:data_opptions.append(row["Type"])
        else:
            for row in data:
                if row["FileType"] == type:
                    if row["FileName"] == file_list:
                        if row["Type"] not in data_opptions:data_opptions.append(row["Type"])

        while True:
            print("\n")
            for name in data_opptions:print(name) 
            print(f"\nfor all data [all]:")
            data_input = input("or [back] to files: ")
            if data_input == "back":
                files(categorized_files, type)
                break
            elif file_list == "all":
                print("\n")
                for row in data:
                    if row["FileType"] == type:
                        if row["Type"] == data_input:
                            print(row["Type"], row["FileName"], "------", row["Content"])
            elif data_input == "all":
                print("\n")
                for row in data:
                    if row["FileType"] == type:
                        if row["FileName"] == file_list:
                            print(row["Type"], row["FileName"], "------", row["Content"])

            elif data_input in data_opptions:
                print("\n")
                for row in data:
                    if row["FileType"] == type:
                        if row["FileName"] == file_list:
                            if row["Type"] == data_input:
                                print(row["Type"], row["FileName"], "------", row["Content"])
            
            else:
                continue
                
               
