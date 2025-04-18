import pandas as pd
import sys, os
from reports import base_report_gen, data_explorer, charts

#opens and reads csv ask user what type of file walks through process
def main_menu():
    clear_screen()
    df = pd.read_csv('reports/csv_files/file_summary.csv')
    df = df[["FileType", "Directory", "FileName", "Type", "Content"]].copy()

    while True:
        clear_screen()
        total_files = len(df["FileName"].unique())
        print(f"\nTotal Files: {total_files}\n")
        types_of_files = df["FileType"].unique()
        print(f"{len(types_of_files)} Type of File\n")
        print(f"{types_of_files}\n")
        print(f"{'='*40}\n")
        print(f"MAIN MENU:\n")
        print(f"{'='*40}\n\n")
        
        main_menu_items = ["1. Charts", "2. Explore Files", "3. Save File Type Report"]
        for opption in main_menu_items:print(opption)
        selection = input(f"\nSelect or [exit]: ")
        if selection == "1":charts_menu()
        if selection == "2":data_explorer.file_type()
        if selection == "3":save_file_menu(df)
        if selection.lower() == "exit":
            clear_screen()
            sys.exit()


def charts_menu():    
    while True:
        clear_screen()
        print(f"{'='*40}\n")
        print(f"CHART MENU:\n")
        print(f"{'='*40}\n\n")

        charts_menu_opptions = ["1. File Type Percentage", "2. Data Per File Type", "3. Data Type by FileName"]
        for opption in charts_menu_opptions:print(opption)
        selection = input(f"\nSelect Chart Number or [menu]: ")

        if selection == "1":charts.type_percent_chart()
        if selection == "2":charts.data_percent_chart()
        if selection == "3":charts.data_chart()
        if selection.lower() == "menu":main_menu()


def save_file_menu(df):
    while True:
        clear_screen()
        print(f"{'='*40}\n")
        print(f"SAVE REPORT MENU:\n")
        print(f"{'='*40}\n\n")
        types_of_files = df["FileType"].unique()
        print(f"\n{types_of_files}\n")
        selected_file_type = input("Select File Type or [menu]: ")
        if selected_file_type.lower() == "menu":main_menu()

        if selected_file_type in types_of_files:
            save_file_name = f"saved_reports/{selected_file_type}_summary.txt"
            base_report_gen.generate_summary_report(selected_file_type, save_file_name)
            main_menu()
            break


def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  
        os.system('clear')
