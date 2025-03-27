from reports import report_helper
from analyzers import base_analyzer
import os, re, sys
from pathlib import Path

#main function processes command line arguments
#  check for reports or path to directory
def main():
    args = sys.argv

    if len(args) == 1:
        print("Please enter report or enter directory path")

    elif len(args) == 2:
        if args[1].lower() == "report":
            report_helper.file_type()
        else:
            directory_name = os.path.normpath(args[1])
            if os.path.isdir(directory_name):
                base_analyzer.generate_csv(directory_name)
            else:
                print("invalid path name! Please try again: ")     
                

if __name__ == "__main__":
    main()