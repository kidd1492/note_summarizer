import os, csv
from reports import report_helper


def base_reports(categorized_files):
     while True:
            print(f"\n Base \n")
            print("1. File Tree\n")
            function_number = input("Enter Number for Report or exit: ")
            if function_number != "exit":
                with open("reports\csv_files/html_summary.csv", mode='r') as file:
                    data = list(csv.DictReader(file))
                    if function_number == "1": generate_file_tree(directory)
            else:
                 report_helper.type_of_report(categorized_files)



def generate_file_tree(directory):
    ignored_directories = [".git", "env", "enve", "venv"]
    tree = []
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in ignored_directories]
        depth = root.replace(directory, "").count(os.sep)
        indent = " " * 4 * depth
        tree.append(f"{indent}{os.path.basename(root)}/")
        sub_indent = " " * 4 * (depth + 1)
        for f in files:
            tree.append(f"{sub_indent}{f}")
    print("\n".join(tree))
