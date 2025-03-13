from analyzers import PythonProjectAnalyzer, BaseAnalyzer
import os, re


def main():
    directory = get_directory()
    analyze = PythonProjectAnalyzer(directory)
    analyze.analize()
    analyze.full_report()

    files = analyze.files
    print(files)

    '''
    analyzer = BaseAnalyzer(directory)
    analyzer.gather_files()
    files = analyzer.files
    print(files)
    '''


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


if __name__ == "__main__":
    main()