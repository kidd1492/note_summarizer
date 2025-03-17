from reports.python_d import test


def type_of_report(file_type_list):

    print(f"what type of report would you like?")
    while True:
        report_type = input(f"File Type Report Options: {file_type_list}: ")
        if report_type.lower() in file_type_list:
            break
        
    if report_type == "py":
        while True:
            print(f"\n Python \n")
            print("1. Full Report\n2. File List\n3. Unique Imports\n 4.Classes\n5.Functions\n6. Comments\n")
            function_number = input("Enter Number for Report or exit: ")
            if function_number != "exit":
                if function_number == "1": test.main()
                if function_number == "2": test.p_files()
                if function_number == "3": test.imports()
                if function_number == "4": test.classes()
                if function_number == "5": test.functions()
                if function_number == "6": test.comments()
            else:
                break