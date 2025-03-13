from analyzers import PythonProjectAnalyzer, BaseAnalyzer
import os, re


def main():
    directory = get_directory()
    gather_file_types(directory)
    call_python_analyzer(directory)
    
   
def get_directory():
    ''' ask user for filepath '''
    path_pattern = r"^[A-Z]:[\\/](?:[^\\/]+[\\/])*[^\\/]*$"

    while True:
        directory_name = input("ex. C:/Desktop/file_name\nFile Path Name:").replace("\\", "/")  
        if re.match(path_pattern, directory_name):
            try:
                if os.path.isdir(directory_name):
                    return directory_name
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")      


#Uses BaseAnalyzer to get file types and decied what analizer to run
def gather_file_types(directory):
    analyzer = BaseAnalyzer(directory)
    analyzer.gather_files()
    file_type_list = analyzer.file_type_list
    print(file_type_list)


#functions to call the analyzers 
def call_python_analyzer(directory):
    python_analyzer = PythonProjectAnalyzer(directory)
    python_analyzer.analize()
    python_analyzer.full_report()




if __name__ == "__main__":
    main()