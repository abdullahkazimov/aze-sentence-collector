import subprocess
import os

def list_files(folder_path):
    try:
        # Get the list of files in the specified folder
        files = os.listdir(folder_path)
        res = []
        for file in files:
            if file.startswith('dev'):
                res.append(file)
        return res

    except FileNotFoundError:
        print(f"The specified folder '{folder_path}' does not exist.")
    except PermissionError:
        print(f"Permission error accessing folder '{folder_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        try:
            subprocess.run(['mkdir', folder_path], check=True)
            #print(f"Folder '{folder_path}' created successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error: Unable to create folder '{folder_path}'.")
            print(f"Error message: {e}")
    else:
        pass
        #print(f"Folder '{folder_path}' already exists.")


def install(package):
    try:
        import pandas as pd
    except ImportError:
        print(f"Installing {package}...")
        subprocess.run(['pip', 'install', package])
    else:
        pass
        #print(f"{package} is already installed.")

fname = 'Abdullah'
lname = 'Kazimov'
allowed_pattern = r'[ a-zA-Z0-9!#%*()-=+:;"\',.?öğıəçşü]'
inf = float('inf')
min_word_limit = 5 # 0 if you don't wanna set lower limit
max_word_limit = 50 # inf if you don't wanna set upper limit
def get_score():
    pass
def install_requirements():
    pass