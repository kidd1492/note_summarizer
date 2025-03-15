from reports import test

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
            report_type = input(f"File Type Report Oprions: {self.file_type_list}")
            if report_type.lower() in self.file_type_list:
                print("Exiting the loop. Goodbye!")
                break
            
        if report_type == "py":
            test.main()