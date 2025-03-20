import csv
from reports import report_helper


def html_reports(categorized_files):      
    
        while True:
            print(f"\n HTML \n")
            print("1. Full Report\n2. File List\n3. Comments\n4. Text\n")
            function_number = input("Enter Number for Report or exit: ")
            if function_number != "exit":
                with open("reports\csv_files/html_summary.csv", mode='r') as file:
                    data = list(csv.DictReader(file))
                    if function_number == "1": main(data)
                    if function_number == "2": html_files(data)
                    if function_number == "3": comments(data)
                    if function_number == "4": text(data)
            else:
                 report_helper.type_of_report(categorized_files)




def main(data):
    html_files(data)
    text(data)
    #classes(data)
    #functions(data) 
    comments(data)

    
def html_files(data):
    html_files = []
    print()
    # Collect file names in python_files
    for row in data:
        if row["File"] not in html_files:
            html_files.append(row["File"])
    #print(f"File List:\n")
    print(f"{html_files}\n")


def text(data):
    # Collect all comments from all files
    print(f"Comments: \n")
    for row in data:
        if row["Type"] == "text":
            print(row["Content"])
    print()


def comments(data):
    # Collect all comments from all files
    print(f"Comments: \n")
    for row in data:
        if row["Type"] == "comment":
            print(row["Content"])
    print()


if __name__ == "__main__":
    main()
