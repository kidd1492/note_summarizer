import os
import re
import logging

from analyzers import base_analyzer
csv_data = []

def process_line_for_csv(file_list):
    tag_pattern = r"<(\w+)"  # Extracts HTML tags
    attribute_pattern = r"(\w+)=[\"']([^\"']+)[\"']"  # Captures attributes
    comment_pattern = r"<!--(.*?)-->"  # Identifies HTML comments
    doctype_pattern = r"<!DOCTYPE\s+\w+>"  # Detects DOCTYPE declarations
    script_style_pattern = r"<(script|style)[^>]*>.*?</\1>"  # Captures embedded scripts or styles
    link_pattern = r"<a\s+[^>]*href=[\"']([^\"']+)[\"']"  # Finds hyperlinks
    form_pattern = r"<form\s+[^>]*action=[\"']([^\"']+)[\"']"  # Identifies forms and actions
    input_pattern = r"<input\s+[^>]*type=[\"']([^\"']+)[\"']"  # Detects input fields in forms

    for file in file_list:
        try:
            file_part = os.path.normpath(file).split(os.sep)
            directory = file_part[-2] if len(file_part) > 1 else "Unknown"
            file_name = file_part[-1]
            file_type = file_name.split('.')[-1]

            with open(file, 'r', encoding='utf-8') as f:
                for line in f:
                    try:
                        line = line.strip()
                        row = {
                            "FileType": file_type,
                            "File": file,
                            "Directory": directory,
                            "FileName": file_name,
                            "Type": None,
                            "Content": line.strip()
                        }

                        if re.match(tag_pattern, line):
                            match = re.search(tag_pattern, line)
                            if match:
                                row["Type"] = "HTML Tag"
                                row["Content"] = match.group(1)

                        elif re.findall(attribute_pattern, line):
                            row["Type"] = "Attributes"
                            row["Content"] = ", ".join([f"{attr}={val}" for attr, val in re.findall(attribute_pattern, line)])

                        elif re.match(comment_pattern, line):
                            match = re.search(comment_pattern, line)
                            if match:
                                row["Type"] = "Comment"
                                row["Content"] = match.group(1).strip()

                        elif re.match(doctype_pattern, line):
                            row["Type"] = "DOCTYPE"
                            row["Content"] = line.strip()

                        elif re.match(script_style_pattern, line):
                            match = re.search(r"<(script|style)", line)
                            if match:
                                row["Type"] = f"{match.group(1).capitalize()} Block"
                                row["Content"] = "Embedded Code"

                        elif re.match(link_pattern, line):
                            match = re.search(link_pattern, line)
                            if match:
                                row["Type"] = "Hyperlink"
                                row["Content"] = match.group(1)

                        elif re.match(form_pattern, line):
                            match = re.search(form_pattern, line)
                            if match:
                                row["Type"] = "Form"
                                row["Content"] = match.group(1)

                        elif re.match(input_pattern, line):
                            match = re.search(input_pattern, line)
                            if match:
                                row["Type"] = "Input Field"
                                row["Content"] = match.group(1)

                        csv_data.append(row)

                    except Exception as e:
                        logging.error(f"Error processing line in {file}: {e}")

        except FileNotFoundError:
            logging.error(f"File not found: {file}")
        except PermissionError:
            logging.error(f"Permission denied for file: {file}")
        except Exception as e:
            logging.error(f"An error occurred while processing {file}: {e}")

    base_analyzer.write_csv_summary(csv_data, "reports/csv_files/html_summary.csv")