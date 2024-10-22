import os

def list_all_file_paths(root_dir, output_file=None, exclude_dirs=None, prefix=''):
    if exclude_dirs is None:
        exclude_dirs = []  # Initialize to an empty list if no directories to exclude

    try:
        # List all items in the directory
        items = os.listdir(root_dir)
    except Exception as e:
        print(f"Error accessing directory {root_dir}: {e}")
        if output_file:
            output_file.write(f"Error accessing directory {root_dir}: {e}\n")
        return

    for item in items:
        path = os.path.join(root_dir, item)  # Full path of the item
        if os.path.isdir(path):
            # Check if the directory is in the exclude list
            if item not in exclude_dirs:
                # Print and/or write the directory path
                print(f"{prefix}{item}/")  # Indicate it's a directory
                if output_file:
                    output_file.write(f"{prefix}{item}/\n")  # Write the directory path to the output file
                # Recursively call this function for the directory
                list_all_file_paths(path, output_file, exclude_dirs, prefix + '    ')  # Increase indentation
        elif os.path.isfile(path):  # Check if it's a file
            # Print and/or write the file path
            print(f"{prefix}{item}")  # Print the file path
            if output_file:
                output_file.write(f"{prefix}{item}\n")  # Write the file path to the output file

# Change the path to your desired directory
root_directory = 'D:/web/web'

# List of folder names to exclude
excluded_folders = ['node_modules']

# Open a file to save the output
with open("all_file_paths.txt", "w") as output_file:
    list_all_file_paths(root_directory, output_file=output_file, exclude_dirs=excluded_folders)