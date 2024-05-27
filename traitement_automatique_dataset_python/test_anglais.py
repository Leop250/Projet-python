import pandas as pd
from tqdm import tqdm
import time
import os
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

def print_colored(message, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'reset': '\033[0m'
    }
    print(f"{colors[color]}{message}{colors['reset']}")

import chardet

def load_data():
    while True:
        try:
            filename = input("Enter the name of the CSV file (or absolute path): ")
            if not os.path.isfile(filename):
                raise FileNotFoundError("The specified file does not exist.")
            if not filename.endswith('.csv'):
                raise ValueError("The specified file is not a CSV file.")
            break
        except (FileNotFoundError, ValueError) as e:
            print_colored(str(e), 'red')
            print_colored("Please try again.", 'yellow')
    while True:
        try:
            separator = input("Enter the separator used in the CSV file (e.g., ',' for comma, ';' for semicolon, '\\t' for tab): ")
            if separator == '\\t':
                separator = '\t'
            if separator in [',', ';', '\t']:
                break
            else:
                raise ValueError("Invalid separator.")
        except ValueError as e:
            print_colored(str(e), 'red')
            print_colored("Please try again.", 'yellow')

    with tqdm(total=100, desc="Loading data", leave=True) as pbar:
        time.sleep(1)
        pbar.update(100)
    try:
        data = pd.read_csv(filename, sep=separator, encoding='latin1')
    except pd.errors.ParserError as e:
        print_colored("Error parsing the CSV file:", 'red')
        print_colored(str(e), 'red')
        print_colored("Please check the separator used or the file structure.", 'yellow')
        return load_data()
    
    print_colored("Here is a preview of the first few lines of the dataset:", 'yellow')
    print(data.head())

    while True:
        confirm = input("Is this the correct dataset? (Yes/No): ").strip().lower()
        if confirm in ['yes', 'no']:
            break
        else:
            print_colored("Please enter a valid value (Yes/No).", 'red')
    
    if confirm == 'no':
        print_colored("Please reload the file with the correct configurations.", 'yellow')
        return load_data()
    
    return data, filename


def main():
    data, filename = load_data()
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Show information about the dataset")
        print("2. Prepare the dataset (Remove NaNs, duplicates, and rename columns)")
        print("3. Rename columns")
        print("4. Remove duplicates")
        print("5. Group columns")
        print("6. Create a time index column")
        print("7. Create a plot")
        print("8. Remove columns")
        print("9. Encode variables")
        print("10. Save modifications")
        print("11. Quit")

        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            show_info(data)
        elif choice == '2':
            data = prepare_data(data)
        elif choice == '3':
            rename_column(data)
        elif choice == '4':
            data = remove_duplicates(data)
        elif choice == '5':
            group_columns(data)
        elif choice == '6':
            create_time_index(data)
        elif choice == '7':
            create_plot(data)
        elif choice == "8":
            data = remove_columns(data)
        elif choice == '9':
            encode_variables(data)
        elif choice == '10':
            save_data(data, filename)
        elif choice == '11':
            break
        else:
            print_colored("Invalid choice. Please enter a valid number.", 'red')

def show_info(data):
    print_colored("\nDataset Information:", 'yellow')
    with tqdm(total=100, desc="Calculating information", leave=True) as pbar:
        time.sleep(1)
        pbar.update(50)
        print(data.info())
        pbar.update(25)
        print(data.describe())
        pbar.update(25)
    for column in data.columns:
        print(f"The size of column {column} is {len(data[column])}")
    print("Here are the first few lines of the dataset:")
    print(data.head())

def prepare_data(data):
    remove_nan(data)
    data = remove_duplicates(data)
    rename_column(data)
    return data

def remove_nan(data):
    with tqdm(total=100, desc="Analyzing missing data", leave=True) as pbar:
        time.sleep(1)
        pbar.update(100)
    num_rows_with_nan = data.isna().any(axis=1).sum()
    percentage_rows_with_nan = (num_rows_with_nan / len(data)) * 100
    print(f"Percentage of rows with at least one NaN: {percentage_rows_with_nan:.2f}%")
    while True:
        choice_nan = input("Do you want to remove rows with NaN? (Yes/No): ").strip().lower()
        if choice_nan in ['yes', 'no']:
            break
        else:
            print_colored("Please enter a valid value (Yes/No).", 'red')
    if choice_nan == 'yes':
        data.dropna(inplace=True)
        print_colored("Rows with NaN have been removed.", 'green')
    elif choice_nan == 'no':
        print_colored("Rows with NaN have not been removed.", 'yellow')

def rename_column(data):
    while True:
        choice_rename_column = input("Do you want to rename the columns of the dataset? (Yes/No): ").strip().lower()
        if choice_rename_column in ['yes', 'no']:
            break
        else:
            print_colored("Please enter a valid value (Yes/No).", 'red')
    
    if choice_rename_column == 'yes':
        for col in tqdm(data.columns, desc="Renaming columns", leave=True):
            while True:
                choice_rename = input(f"Do you want to rename the column '{col}'? (Yes/No): ").strip().lower()
                if choice_rename in ['yes', 'no']:
                    break
                else:
                    print_colored("Please enter a valid value (Yes/No).", 'red')
            
            if choice_rename == 'yes':
                new_name = input("Enter the new name for the column: ").strip()
                data.rename(columns={col: new_name}, inplace=True)
                print_colored("Moving to the next column.", 'yellow')
            elif choice_rename == 'no':
                print_colored("Moving to the next column.", 'yellow')
        
        print_colored("Column names after renaming:", 'green')
        print(data.columns)
    elif choice_rename_column == 'no':
        print_colored("No renaming performed.", 'yellow')


def remove_duplicates(data):
    print_colored("Analyzing duplicates...", 'yellow')
    duplicates = data[data.duplicated(keep=False)]

    print("Identified duplicates:")
    print(duplicates)

    num_duplicates = len(duplicates)
    print(f"Number of identified duplicate rows: {num_duplicates}")

    while True:
        choice_duplicate = input("Do you want to remove duplicates from the dataset? (Yes/No): ").strip().lower()
        if choice_duplicate in ['yes', 'no']:
            break
        else:
            print_colored("Please enter a valid value (Yes/No).", 'red')

    if choice_duplicate == 'yes':
        original_count = len(data)
        data.drop_duplicates(inplace=True)
        removed_count = original_count - len(data)
        print_colored(f"Duplicates have been removed. {removed_count} fewer rows.", 'green')
    elif choice_duplicate == 'no':
        print_colored("No duplicates have been removed.", 'yellow')
    return data

def remove_columns(data):
    print("Here are the columns of your dataset:")
    for i in data.columns:
        print(i)
    
    column_drop = input("Enter the name of the column you want to remove: ")
    
    while column_drop not in data.columns:
        print_colored("The column does not exist.", 'red')
        column_drop = input("Enter the name of the column you want to remove again: ")
    
    data = data.drop(column_drop, axis=1)
    print_colored("Here is the new dataset without the column", 'green', column_drop)
    print(data)
    return data

def group_columns(data):
    while True:
        choice_group_columns = input("Do you want to group multiple columns in the dataset? (Yes/No): ").strip().lower()
        if choice_group_columns in ['yes', 'no']:
            break
        else:
            print_colored("Please enter a valid value (Yes/No).", 'red')
    
    if choice_group_columns == 'yes':
        columns_to_group_list = []
        while True:
            column_to_group = input("Enter the name of the column to group (type STOP to stop): ")
            if column_to_group.lower() == "stop":
                break
            if column_to_group in data.columns:
                columns_to_group_list.append(column_to_group)
            else:
                print_colored(f"The column '{column_to_group}' does not exist in the dataset.", 'red')

        if not columns_to_group_list:
            print_colored("No valid columns selected.", 'red')
            return

        if check_compatible_types(data, columns_to_group_list):
            print_colored("The types of the columns to group are compatible.", 'green')
            new_column_name = input("Enter the name of the new combined column: ")
            data[new_column_name] = data[columns_to_group_list].astype(str).agg(' '.join, axis=1)
            print_colored(f"Columns successfully grouped into the new column '{new_column_name}'.", 'green')
        else:
            print_colored("The types of the columns to group are not compatible.", 'red')
    else:
        print_colored("No column grouping requested.", 'yellow')

def check_compatible_types(data, columns):
    types = set(data[column].dtype for column in columns)
    return len(types) == 1

def save_data(data, filename):
    while True:
        choice_save = input("Do you want to save the modifications to the same file or to a new file?\n1. Same file\n2. New file\nEnter the number of your choice: ")
        if choice_save in ['1', '2']:
            break
        else:
            print_colored("Invalid choice. Please enter 1 or 2.", 'red')
    
    if choice_save == '1':
        save_data(data, filename)
    elif choice_save == '2':
        new_filename = input("Enter the name of the new file to save the data (e.g., data_modified.csv): ")
        save_data(data, new_filename)

def create_time_index(data):
    while True:
        choice_index = input("Do you want to create a time index column for temporal tracking, which can be useful for creating graphs? (Yes/No): ").strip().lower()
        if choice_index in ['yes', 'no']:
            break
        else:
            print_colored("Please enter a valid value (Yes/No).", 'red')
    
    if choice_index == "yes":
        print_colored("You have chosen to create a time index column", 'yellow')
        new_column = input("Enter the name for your time index column: ")
        num_rows = len(data)
        data[new_column] = range(1, num_rows + 1)
        print_colored(f"Your {new_column} time index column has been successfully created.", 'green')
        print(data)
    
    elif choice_index == "no":
        print_colored("You have chosen not to create a time index column", 'yellow')

from sklearn.preprocessing import LabelEncoder

def encode_variables(data):
    while True:
        choice_encode = input("Do you want to encode the variables? This is necessary for linear model prediction. (Yes/No): ").strip().lower()
        if choice_encode in ['yes', 'no']:
            break
        else:
            print_colored("Please enter a valid value (Yes/No).", 'red')

    if choice_encode == "yes":
        print_colored("You have chosen to encode the variables.", 'yellow')
        columns_to_encode = [col for col in data.columns if data[col].dtype == 'object' or data[col].dtype == 'O']
        
        with tqdm(total=len(columns_to_encode), desc="Encoding variables", leave=True) as pbar:
            for col in columns_to_encode:
                try:
                    data[col] = data[col].astype(str)
                    label_encoder = LabelEncoder()
                    data[col] = label_encoder.fit_transform(data[col])
                    pbar.update(1)
                except Exception as e:
                    print_colored(f"Error encoding column '{col}': {e}", 'red')
                    continue

        print_colored("Variables encoded successfully.", 'green')
    elif choice_encode == "no":
        print_colored("You have chosen not to encode the variables.", 'yellow')

def create_plot(data):
    print("Available types of plots:")
    print("1. Bar chart")
    print("2. Scatter plot")
    print("3. Box plot")
    print("4. Histogram")

    while True:
        choice_plot = input("Enter the number corresponding to the type of plot you want to create: ").strip()
        if choice_plot in ['1', '2', '3', '4']:
            break
        else:
            print("Invalid plot type.")

    if choice_plot == '1':
        create_bar_chart(data)
    elif choice_plot == '2':
        create_scatter_plot(data)
    elif choice_plot == '3':
        create_box_plot(data)
    elif choice_plot == '4':
        create_histogram(data)


def create_bar_chart(data):
    for i in data.columns:
        print(i)
    while True:
        x_axis = input("Enter the name of the column for the x-axis: ").strip()
        if x_axis in data.columns and pd.api.types.is_numeric_dtype(data[x_axis]):
            break
        else:
            print_colored("The column does not exist or does not contain numerical data.", 'yellow')
    
   
    while True:
        y_axis = input("Enter the name of the column for the y-axis: ").strip()
        if y_axis in data.columns and pd.api.types.is_numeric_dtype(data[y_axis]):
            break
        else:
            print_colored("The column does not exist or does not contain numerical data.", 'yellow')

    plt.figure(figsize=(10, 6))
    plt.bar(data[x_axis], data[y_axis])
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.title(f"Bar Chart of {y_axis} vs {x_axis}")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

def create_scatter_plot(data):
    for i in data.columns:
        print(i)
    while True:
        x_axis = input("Enter the name of the column for the x-axis: ").strip()
        if x_axis in data.columns and pd.api.types.is_numeric_dtype(data[x_axis]):
            break
        else:
            print_colored("The column does not exist or does not contain numerical data.", 'yellow')
    
    while True:
        y_axis = input("Enter the name of the column for the y-axis: ").strip()
        if y_axis in data.columns and pd.api.types.is_numeric_dtype(data[y_axis]):
            break
        else:
            print_colored("The column does not exist or does not contain numerical data.", 'yellow')

    plt.figure(figsize=(10, 6))
    plt.scatter(data[x_axis], data[y_axis])
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.title(f"Scatter Plot of {y_axis} vs {x_axis}")
    plt.grid(True)
    plt.show()

def create_box_plot(data):
    for i in data.columns:
        print(i)
    while True:
        x_axis = input("Enter the name of the column for the x-axis: ").strip()
        if x_axis in data.columns and pd.api.types.is_numeric_dtype(data[x_axis]):
            break
        else:
            print_colored("The column does not exist or does not contain numerical data.", 'yellow')

    plt.figure(figsize=(10, 6))
    data.boxplot(column=x_axis)
    plt.title(f"Box Plot of {x_axis}")
    plt.grid(True)
    plt.show()

def create_histogram(data):
    for i in data.columns:
        print(i)
    while True:
        column = input("Enter the name of the column for the histogram: ").strip()
        if column in data.columns and pd.api.types.is_numeric_dtype(data[column]):
            break
        else:
            print_colored("The column does not exist or does not contain numerical data.", 'yellow')

    plt.figure(figsize=(10, 6))
    plt.hist(data[column], bins=20, edgecolor='black')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title(f"Histogram of {column}")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
