import csv

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
