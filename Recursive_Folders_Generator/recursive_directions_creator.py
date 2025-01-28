import os

def create_directories(recursion_levels, folder_names, list_file="list.txt"):
    # Read the last level folder names from the list file
    try:
        with open(list_file, 'r') as file:
            last_level_folders = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: {list_file} not found in the directory.")
        return
    
    # Ensure folder names are parsed correctly
    folder_names = folder_names.split(',')
    
    # Create the directories
    base_path = os.getcwd()
    
    for folder in folder_names:
        first_level_path = os.path.join(base_path, folder)
        os.makedirs(first_level_path, exist_ok=True)
        
        if recursion_levels > 1:
            for subfolder in last_level_folders:
                subfolder_path = os.path.join(first_level_path, subfolder)
                os.makedirs(subfolder_path, exist_ok=True)
    
    print("Done!")

# Input example
if __name__ == "__main__":
    try:
        recursion = int(input("Enter recursion levels (e.g., 2): "))
        folder_input = input("Enter folder names for levels (comma-separated, e.g., 2024,2025): ")
        create_directories(recursion, folder_input)
    except ValueError:
        print("Invalid input! Please enter numeric values for recursion levels.")
