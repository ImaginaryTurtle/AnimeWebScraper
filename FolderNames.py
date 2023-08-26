import os

def get_folder_names(directory):
    folder_names = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            folder_names.append(item)
    return folder_names

def create_anime_list():
    directory = input("Enter the directory path: ")
    if os.path.exists(directory):
        folder_names = get_folder_names(directory)
        if folder_names:
            folder_names.pop(0)
            return folder_names
        else:
            print("No folders found in the directory.")
            return False
    else:
        print("Directory does not exist.")
        return False
