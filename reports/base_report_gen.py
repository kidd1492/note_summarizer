import pandas as pd


def generate_summary_report(file_type, report_file):
    csv_file = "reports/csv_files/file_summary.csv"
    
    # Read CSV
    df = pd.read_csv(csv_file)
    
    with open(report_file, "w") as report:
        # Filter by FileType (use any file type dynamically)
        files = df[df["FileType"] == f"{file_type}"]  # Change "html" to desired FileType
        file_count = len(files["FileName"].unique())
        
        # Write FileType summary
        report.write(f"{'='*40}\n")
        report.write(f"SUMMARY REPORT: FILES\n")
        report.write(f"{'='*40}\n\n")
        
        report.write(f"Total Files: {file_count}\n\n")
        
        # List all filenames
        report.write("Filenames:\n")
        for filename in files["FileName"].unique():
            report.write(f"- {filename}\n")
        report.write("\n")
        
        # Process each file
        types_of_data = files["Type"].unique()
        for filename in files["FileName"].unique():
            report.write(f"{'-'*40}\n")
            report.write(f"File: {filename}\n")
            report.write(f"{'-'*40}\n")
            
            for type in types_of_data:
                # Extract content of a specific Type
                contents = files[(files["FileName"] == filename) & (files["Type"] == type)]
                if not contents.empty:
                    report.write(f"\n{type.capitalize()}:\n")
                    for content in contents["Content"]:
                        report.write(f"    {content}\n")
            
            report.write("\n")

    print(f"Summary report generated and saved to '{report_file}'!")
