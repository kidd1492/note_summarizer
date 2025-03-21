import csv
from reports import report_helper

#TODO Clean up these functions. reduce 
def python_reports(categorized_files):
    
    file_search_list = ["all"]
    with open("reports/csv_files/python_summary.csv", mode='r') as file:
        data = list(csv.DictReader(file))
        while True:
            for row in data:
                if row["FileName"] not in file_search_list:
                    file_search_list.append(row["FileName"])
                    print(row["FileName"])
            print(f"\nWhat file would you like to analyze:[all] for all files ")
            file_search = input("or [back] to go back to Report Types: ")

            if file_search == "back":report_helper.type_of_report(categorized_files)
            if file_search in file_search_list:
                data_type(file_search, categorized_files)


def data_type(file_search, categorized_files):

    types_of_data = []
    with open("reports/csv_files/python_summary.csv", mode='r') as file:
        data = list(csv.DictReader(file))
        while True:
            for row in data:
                if row["Type"] not in types_of_data:
                    types_of_data.append(row["Type"])
                    print(row["Type"])
            print(f"\nfor all data [main] What data?:")
            data_input = input("or [back] to files: ")
            if data_input == "back":python_reports(categorized_files)
            if data_input == "main":print_full_report(categorized_files)
            if file_search == "all":
                for row in data:    
                    if row["Type"] == data_input:
                        print(row["Type"], row["FileName"], "------", row["Content"])
            if data_input in types_of_data:      
                for row in data:
                    if row["FileName"] == file_search:
                        if row["Type"] == data_input:
                            print(row["Type"], row["FileName"], "------", row["Content"])
            


#TODO make a function to print out all reports'
def print_full_report(categorized_files):
    type_of_data_list = ["import", "function", "todo", "comment"]
    with open("reports/csv_files/python_summary.csv", mode='r') as file:
        data = list(csv.DictReader(file))
        
        for item in type_of_data_list:
            for row in data:
                if row["Type"] == item:
                    print(row["Type"], row["FileName"], "------", row["Content"])
            print("\n")
