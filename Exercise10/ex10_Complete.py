import glob
import os


while True:
    # Get the directory name from user input
    dir_path = input("Enter the directory path: ")

    # Use the glob.glob() function to obtain the list of filenames
    file_list = glob.glob(os.path.join(dir_path, '*'))
    if len(file_list) == 0:
        print("No files found in the specified directory.")
        continue
    for file_path in file_list:
     file_size = os.path.getsize(file_path)
     if file_size > 0:
         file_name = os.path.basename(file_path)
         print(f"{file_name} ({file_size} bytes)")
    # Ask the user if they want to see files in a different directory
    choice = input("Do you want to see files in another directory? (y/n): ")
    if choice.lower() != "y":
        break
