import csv

def main():
   print()
   python_files = gather_python_files()
   for file in python_files: print(f"{file}")
   print()
   comments()


def gather_python_files():
    python_files = []
    with open("python_summary.csv") as file:
        df = csv.DictReader(file)
        #collect file names in python_files. 
        for row in df:
            if row["File"] not in python_files:
                python_files.append(row["File"])
    return python_files


def comments():
    with open("python_summary.csv") as file:
        df = csv.DictReader(file)
        #collect file names in python_files. 
        for row in df:
            if row["Type"] == "comment":
                print (row["Content"])
    print()



if __name__ == "__main__":
    main()