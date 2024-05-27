# save_data.py
import pandas as pd
from utils import print_colored

def save_data(data, filename):
    try:
        new_filename = input("Enter the name of the save file (with .csv extension): ")
        data.to_csv(new_filename, index=False, encoding='latin1')
        print_colored(f"Changes have been saved to the file {new_filename}.", 'green')
    except Exception as e:
        print_colored(f"Error during saving: {e}", 'red')
