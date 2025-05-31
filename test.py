import pandas as pd
import os

directory = "C:\\Users\\chris\\Desktop\\notes_app"

'''function to walk through a directory pick what kinds of file it wants
ignoring directories like venv, .git, it then saves the type of file and a list of
files for that type into a dict. returns catagorized files'''

def gather_categorized_files(directory):
    allowed_extensions = ["py", "html", "js", "md", "txt", "db"]  # Update to add more file types
    ignored_directories = [".git", "env", "venv"]
    categorized_files = {}

    try:
        for root, dirs, files in os.walk(directory):
            dirs[:] = [d for d in dirs if d not in ignored_directories]  # Skip ignored directories
            for file in files:
                # Check if the file's extension is in the allowed list
                if any(file.endswith(ext) for ext in allowed_extensions):
                    ext = file.split('.')[-1]  # Extract the file extension (without dot)

                    # Initialize the list for this file type if not already present
                    if ext not in categorized_files:
                        categorized_files[ext] = []
                    # Append the file path to the appropriate list
                    categorized_files[ext].append(os.path.abspath(os.path.join(root, file)))
    except Exception as e:
        print(f"An error occurred while gathering files: {e}")


    for file_type, file_list in categorized_files.items():
        for file in file_list: print(file)



if __name__ == "__main__":
     categorized_files = gather_categorized_files(directory)




'''
csv_file = "reports/csv_files/python_summary.csv"

# Read CSV
df = pd.read_csv(csv_file)


comments = df[df["Type"] == "Comment"]
comment_content = comments["Content"].unique()
print(comment_content)

files = df["FileName"].unique()
print(files)
'''