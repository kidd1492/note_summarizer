import csv
from reports import report_helper

def python_reports(categorized_files):      
    
        while True:
            print(f"\n Python \n") 
            print("1. Full Report\n2. File List\n3. Unique Imports\n4. Classes\n5. Functions\n6. Comments\n"
            "7. TODO Comments")
            function_number = input("Enter Number for Report or exit: ")
            if function_number != "exit":
                with open("reports\csv_files/python_summary.csv", mode='r') as file:
                    data = list(csv.DictReader(file))
                    if function_number == "1": full_report(data)
                    if function_number == "2": p_files(data)
                    if function_number == "3": imports(data)
                    if function_number == "4": classes(data)
                    if function_number == "5": functions(data)
                    if function_number == "6": comments(data)
                    if function_number == "7": TODO(data)
            else:
                report_helper.type_of_report(categorized_files)


def full_report(data):
    p_files(data)
    imports(data)
    classes(data)
    functions(data) 
    comments(data)
    TODO(data)


def TODO(data):
    print()
    for row in data:
        if row["Type"] == "todo":print(f"{row['Content']}")


def p_files(data):
    python_files = []
    print()
    # Collect file names in python_files
    for row in data:
        if row["File"] not in python_files: python_files.append(row["File"])
    print(f"{python_files}\n")


def imports(data):
    imports_list = []
    # Collect all imports in a list
    for row in data:
        if row["Type"] == "import":
            row = row["Content"].split()
            if row[0] == "import":
                if row[1] not in imports_list: 
                    if "," in row[1]:
                        one = row[1].split(",")
                        for i in one:
                            if i not in imports_list:
                                imports_list.append(i)
                else:
                    imports_list.append(row[1:])                   

            if row[0] == "from":
                if row[1].startswith("."):
                    continue
                else:
                    imports_list.append(row[1]) 
    print(f"Imports: \n")
    for item in imports_list: print(item)
    print()


def classes(data):
    print(f"Class: \n")
    for row in data:
        if row["Type"] == "class":
            print(f"{row['Content']}")
    print()


def functions(data):
    print(f"Functions: \n")
    for row in data:
        if row["Type"] == "function": print(row["Content"])
    print()


def comments(data):
    # Collect all comments from all files
    print(f"Comments: \n")
    for row in data:
        if row["Type"] == "comment": print(row["Content"])
    print()
