import csv
from reports import report_helper

def python_reports(categorized_files):
    
    file_search_list = []
    with open("reports/csv_files/python_summary.csv", mode='r') as file:
        data = list(csv.DictReader(file))
        while True:
            for row in data:
                if row["FileName"] not in file_search_list:
                    file_search_list.append(row["FileName"])
                    print(row["FileName"])
            print("\n", "or [back] to go back to Report Types")
            file_search = input("What file would you like to analyze: ")

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
            data_input = input("what data? ")
            if data_input == "back":python_reports(categorized_files)
            if data_input in types_of_data: 
                for row in data:
                    if row["FileName"] == file_search:
                        if row["Type"] == data_input:
                            print(row["Type"], row["FileName"], "------", row["Content"])
        
