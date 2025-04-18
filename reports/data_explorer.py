from reports import report_helper
import pandas as pd
import os


#opens and reads csv ask user what type of file walks through process
def file_type():
    df = pd.read_csv('reports/csv_files/file_summary.csv')
    df = df[["FileType", "Directory", "FileName", "Type", "Content"]].copy()


    types_of_files = df["FileType"].unique()
    while True:
        clear_screen()
        print(f"{'='*40}\n")
        print(f"FILE TYPE:\n")
        print(f"{'='*40}\n\n")
        print(f"\n{types_of_files}\n")
        print("What types of files would you like to explore? : ")
        selected_file_type = input("[exit] to quit or select file type: ")

        if selected_file_type == "exit":report_helper.main_menu()
        if selected_file_type in types_of_files:
            select_file(df, selected_file_type)
            break


#function displays all files gives user opptions: all, save, select file
def select_file(df, selected_file_type): 
    type = df[df['FileType'] == selected_file_type ] 
    type = type[['FileName', 'Type', 'Content']]
    
    file_list = type['FileName'].unique()
    
    while True:
        clear_screen()
        print(f"{'='*40}\n")
        print(f"FILES:\n")
        print(f"{'='*40}\n\n")
       
        for item in file_list:print(item)
        print("\n","Type file name or [all] for all files")
        selected_file = input("or [back] to go back to File Types: ")
        if selected_file == "back":file_type()
        
        elif selected_file in file_list or selected_file == "all":
            select_data(df, selected_file, selected_file_type, type)


# function displays all data types avalable ask user to select one. 
# all will print all data for the selection.
def select_data(df, selected_file, selected_file_type, type):
    clear_screen()
    if selected_file != "all":
        data_type = type[type['FileName'] == selected_file]
        data_list = data_type['Type'].unique()
        while True:
            
            print(f"{'='*40}\n")
            print(f"DATA TYPE:\n")
            print(f"{'='*40}\n\n")
            print(data_type["Type"].value_counts())
            print(f"\n [back] to go back to file selection:")
            selected_data = input("Select Data Type: ")
            if selected_data == "back":select_file(df, selected_file_type)
            if selected_data == "all":
                clear_screen()
                print("\n")
                print(data_type)
            elif selected_data in data_list:
                filtered_df = data_type[data_type['Type'] == f"{selected_data}"]
                clear_screen()
                print("\n")
                print(filtered_df)
            

    else:
        clear_screen()
        data_list = type['Type'].unique()
        while True:
            print(f"{'='*40}\n")
            print(f"DATA TYPE:\n")
            print(f"{'='*40}\n\n")

            print(type["Type"].value_counts())
            print(f"\n [back] to go back to file selection:")
            selected_data = input("Select Data Type: ")
            
            if selected_data == "back":select_file(df, selected_file_type)
            elif selected_data in data_list:
                filtered_df = type[type['Type'] == f"{selected_data}"]
                clear_screen()
                print("\n")
                print(filtered_df)


def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  
        os.system('clear')      