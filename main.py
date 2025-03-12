import os, re
import inspect

# Main function to drive the program
def main():
    # Specify the target directory
    target_directory = r"C:/Users/chris/Desktop/note_summarizer"  # Update this to your actual directory path
    allowed_extensions = [".py"]  # Add any other extensions you'd like to keep 
    file_list = gather_files(target_directory, allowed_extensions)
    write_report(file_list)
    

# Function to gather all files in a directory
def gather_files(directory, allowed_extensions):
    all_files = []
    
    # Walk through the directory tree
    for root, dirs, files in os.walk(directory):
        # Skip .git directories entirely and enve
        dirs[:] = [d for d in dirs if d not in [".git", "env", "enve"]]
        for file in files:
            # Check if the file's extension is in the allowed list
            if any(file.endswith(ext) for ext in allowed_extensions):
                # Get the full file path
                full_path = os.path.join(root, file)
                all_files.append(full_path)
    return all_files

#TODO transfer this into my class
def write_report(paths):

    import_pattern = r"^(import\s+|from\s+\w+\s+import\s+)"
    function_pattern = r"^def\s+"
    output = open("output_file.txt", "w")

    for full_path in paths:
        output.write("\n")
        output.write("Analyzed Files:\n")
        output.write(f"{full_path}\n\n")
        output.write("Imports:\n\n")

        file = open(full_path, "r" )
        data = file.readlines()

        for line in data: 
            line = line.strip()
            if line == '':
                continue

            if re.match(import_pattern, line):
                output.write(f"{line}\n")
        
            if re.match(function_pattern, line):
                    output.write(f"{line}\n")
        



# Entry point for the script
if __name__ == "__main__":
    main() 
