from reports.python_d import test

class BaseAnalyzer:
    def __init__(self, all_file_paths, file_type_list):
        ''' Initialize the analyzer with a types list and file list'''

        self.all_file_paths = all_file_paths
        self.file_type_list = file_type_list
        self.file_count = 0


    def count_files(self):
        for file in self.all_file_paths: self.file_count += 1


    def reports(self):
        self.count_files()
        print()
        print(f"Analyzed files {self.file_count} \n")
        print(f"what type of report would you like?")

        while True:
            report_type = input(f"File Type Report Oprions: {self.file_type_list}: ")
            if report_type.lower() in self.file_type_list:
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