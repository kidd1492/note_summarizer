from reports import base_report_gen
import pandas as pd
import sys

def type_of_report(categorized_files):
     #user_input = input("what type of data do you want to view? : ")
     analyzed_file_summary(categorized_files)
     file_type()


def file_type():
    df = pd.read_csv('reports/csv_files/file_summary.csv')

    types_of_files = df["FileType"].unique()
    while True:
        print(f"\n{types_of_files}\n")
        print("What types of files would you like to explore? : ")
        selected_file_type = input("[exit] to quit or select file type: ")
        if selected_file_type == "exit":sys.exit()
        if selected_file_type in types_of_files:
            select_file(df, selected_file_type )
            break


def select_file(df, selected_file_type): 
    type = df[df['FileType'] == selected_file_type ] 
    type = type[['FileName', 'Type', 'Content']]
    
    file_list = type['FileName'].unique()
    
    while True:
        print("\n")
        for item in file_list:print(item)
        print("\n","Type file name or [all] for all files")
        selected_file = input("or [back] to go back to File Types: ")
        if selected_file == "back":file_type()
        elif selected_file in file_list or selected_file == "all":
            select_data(df, selected_file, selected_file_type, type)


def select_data(df, selected_file, selected_file_type, type):
    if selected_file != "all":
        data_type = type[type['FileName'] == selected_file]
        data_list = data_type['Type'].unique()
        while True:
            print("\n")
            for item in data_list:print(item)
            print(f"\n [back] to go back to file selection:")
            selected_data = input("Select Data Type: ")
            if selected_data == "back":select_file(df, selected_file_type)
            if selected_data == "all":
                print("\n")
                print(data_type)
            elif selected_data in data_list:
                filtered_df = data_type[data_type['Type'] == f"{selected_data}"]
                print("\n")
                print(filtered_df)

    else:
        data_list = type['Type'].unique()
        while True:
            
            print("\n")
            for item in data_list:print(item)
            print(f"\n [back] to go back to file selection:")
            selected_data = input("Select Data Type: ")
            if selected_data == "back":select_file(df, selected_file_type)
            elif selected_data in data_list:
                filtered_df = type[type['Type'] == f"{selected_data}"]
                print("\n")
                print(filtered_df)
        

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

