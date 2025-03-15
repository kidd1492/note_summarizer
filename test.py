import csv

# Load data into a list of dictionaries
with open("python_summary.csv", mode='r') as file:
    data = list(csv.DictReader(file))


#TODO change main function to test call it from main.py
def main():
    imports()
    p_files()
    classes()
    functions() 
    comments()
 
    
def p_files():
    python_files = []
    # Collect file names in python_files
    for row in data:
        if row["File"] not in python_files:
            python_files.append(row["File"])
    print(f"File List:\n")
    print(f"{python_files}\n")


def imports():
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


def classes():
    print(f"Class: \n")
    for row in data:
        if row["Type"] == "class":
            print(f"{row['Content']}")
    print()


def functions():
    print(f"Functions: \n")
    for row in data:
        if row["Type"] == "function":
            print(row["Content"])
    print()


def comments():
    # Collect all comments from all files
    print(f"Comments: \n")
    for row in data:
        if row["Type"] == "comment":
            print(row["Content"])
    print()





if __name__ == "__main__":
    main()
