import csv


def main():

    file_search = input("What file would you like to analyze: ")
    type_of_data = input("what data? ")


    with open("reports/csv_files/python_summary.csv", mode='r') as file:
        data = list(csv.DictReader(file))
        for row in data: 
            if row["FileName"] == file_search:
                if row["Type"] == type_of_data:
                    print(row["Type"], row["FileName"], "------", row["Content"])
        print()   




if __name__ == "__main__":
    main()
