import re


def file_tree(all_file_paths):
    file_directory_list = []
    file_struct = []
    for file in all_file_paths:
        file = file.replace("\\", "/").split("/")
        if file[-1] not in file_directory_list:file_directory_list.append([file[-1], file[:-1]])
    
    for fd in file_directory_list:
        file_name = fd[0]
        directory_name = fd[1][-1]
        sub_directory = fd[1][-2]

        if sub_directory not in file_struct:file_struct.append(sub_directory)
        if directory_name not in file_struct: file_struct.append(directory_name)
        if file_name not in file_struct: file_struct.append(file_name)

    
    for item in file_struct:
        if re.match(r".\w+$", item):
            print(f"|-{item}\n")
        else:
            print(f"|---{item}")