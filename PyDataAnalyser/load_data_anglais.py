# load_data_anglais.py
import pandas as pd
from utils_anglais import print_colored

def load_data_a():
    while True:
        try:
            filename = input("Enter the path to the CSV file: ")
            data = pd.read_csv(filename, error_bad_lines=False)
            print_colored(f"Data loaded successfully from {filename}.", 'green')
            return data, filename
        except pd.errors.ParserError as e:
            print_colored(f"Error parsing the file: {e}", 'red')
            print_colored("Please check the file format and try again.", 'yellow')
        except FileNotFoundError:
            print_colored("File not found. Please enter a valid file path.", 'red')
        except Exception as e:
            print_colored(f"An error occurred: {e}", 'red')
