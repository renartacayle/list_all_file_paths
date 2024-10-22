# list_all_file_paths

Description
This Python script defines a function list_all_file_paths that recursively lists all files and directories within a specified root directory. It allows for the exclusion of certain directories, making it useful for tasks like generating a directory structure or gathering file paths for further processing.

Key Features:
Recursive Directory Traversal: The function explores all subdirectories and files within the specified root directory.
Exclusion of Directories: Users can specify a list of directory names to exclude from the output, such as node_modules.
Output Options: The script can print the directory structure to the console and optionally write it to a specified output file.
Error Handling: It gracefully handles errors when accessing directories, printing error messages and writing them to the output file if specified.
Usage:
Set the root_directory variable to the desired starting directory path.
Specify any directory names to exclude in the excluded_folders list.
Run the script, and it will create a file named all_file_paths.txt containing the paths of all files and directories, formatted with indentation to indicate hierarchy.
Example Output

The output in all_file_paths.txt might look like this:

"
folder1/
    file1.txt
    file2.txt
folder2/
    subfolder/
        file3.txt
"

This structure visually represents the directory hierarchy while excluding any specified directories.
