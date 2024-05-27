# prepare_data.py
import pandas as pd
from tqdm import tqdm
import time
from utils import print_colored

def show_info(data):
    print_colored("\nDataset information:", 'yellow')
    with tqdm(total=100, desc="Calculating information", leave=True) as pbar:
        time.sleep(1)
        pbar.update(50)
        print(data.info())
        pbar.update(25)
        print(data.describe())
        pbar.update(25)
    for column in data.columns:
        print(f"The size of the column {column} is {len(data[column])}")
    print("Here are the first rows of the dataset:")
    print(data.head())

def prepare_data(data):
    remove_na(data)
    handle_outliers(data)
    remove_duplicates(data)
    rename_columns(data)
    return data

def remove_na(data):
    with tqdm(total=100, desc="Analyzing missing data", leave=True) as pbar:
        time.sleep(1)
        pbar.update(100)
    num_rows_with_na = data.isna().any(axis=1).sum()
    percentage_rows_with_na = (num_rows_with_na / len(data)) * 100
    print(f"Percentage of rows with at least one NaN: {percentage_rows_with_na:.2f}%")

    if num_rows_with_na > 0:
        while True:
            choice_na = input("Do you want to remove rows with NaN? (Yes/No): ").strip().lower()
            if choice_na in ['yes', 'no']:
                break
            else:
                print_colored("Please enter a valid value (Yes/No).", 'red')
        if choice_na == 'yes':
            data.dropna(inplace=True)
            print_colored("Rows with NaN have been removed.", 'green')
        elif choice_na == 'no':
            print_colored("Rows with NaN have not been removed.", 'yellow')
    else:
        print_colored("No duplicates in your dataset.", 'green')

def rename_columns(data):
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
                new_name = input("Enter the new column name: ").strip()
                data.rename(columns={col: new_name}, inplace=True)
                print_colored("Moving on to the next column.", 'yellow')
            elif choice_rename == 'no':
                print_colored("Moving on to the next column.", 'yellow')
        
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
    print(f"Number of duplicate rows identified: {num_duplicates}")

    while True:
        choice_duplicates = input("Do you want to remove duplicates from the dataset? (Yes/No): ").strip().lower()
        if choice_duplicates in ['yes', 'no']:
            break
        else:
            print_colored("Please enter a valid value (Yes/No).", 'red')

    if choice_duplicates == 'yes':
        original_count = len(data)
        data.drop_duplicates(inplace=True)
        removed_count = original_count - len(data)
        print_colored(f"Duplicates have been removed. {removed_count} rows removed.", 'green')
    elif choice_duplicates == 'no':
        print_colored("No duplicates have been removed.", 'yellow')
    return data

def remove_columns(data):
    print("Here are the columns of your dataset:")
    for col in data.columns:
        print(col)
    
    while True:
        column_name = input("Enter the name of the column to remove (or type 'exit' to quit): ")
        if column_name == 'exit':
            break
        if column_name in data.columns:
            data.drop(column_name, axis=1, inplace=True)
            print_colored(f"Column '{column_name}' removed.", 'green')
        else:
            print_colored("Column not found, please try again.", 'red')
    
    return data

def merge_columns(data):
    while True:
        try:
            columns_to_merge = input("Enter the names of the columns to merge (separated by commas): ").split(',')
            columns_to_merge = [col.strip() for col in columns_to_merge if col.strip() in data.columns]
            if len(columns_to_merge) < 2:
                raise ValueError("Please enter at least two existing columns.")
            break
        except ValueError as e:
            print_colored(str(e), 'red')
            print_colored("Please try again.", 'yellow')

    new_column_name = input("Enter the name of the new merged column: ")
    data[new_column_name] = data[columns_to_merge].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
    print_colored(f"The columns {', '.join(columns_to_merge)} have been merged into a new column '{new_column_name}'.", 'green')

def create_time_index(data):
    print("To create a time index column, you need to provide a date column.")
    
    while True:
        date_column = input("Enter the name of the date column (or type 'exit' to quit): ")
        if date_column == 'exit':
            break
        if date_column in data.columns:
            try:
                data[date_column] = pd.to_datetime(data[date_column])
                data.set_index(date_column, inplace=True)
                print_colored(f"The column '{date_column}' has been converted to a time index.", 'green')
                break
            except Exception as e:
                print_colored(f"Error during conversion: {e}", 'red')
                print_colored("Please check the format of the date column and try again.", 'yellow')
        else:
            print_colored("Column not found, please try again.", 'red')

def handle_outliers(data):
    numeric_columns = data.select_dtypes(include=['number']).columns
    print("Analyzing numeric columns for outliers...")
    
    for col in numeric_columns:
        q1 = data[col].quantile(0.25)
        q3 = data[col].quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers = data[(data[col] < lower_bound) | (data[col] > upper_bound)]
        
        num_outliers = len(outliers)

        print(f"Column '{col}': {num_outliers} outliers detected.")
        
        if num_outliers > 0:
            handle_outliers_choice = input(f"Do you want to handle the outliers in column '{col}'? (Yes/No) : ").strip().lower()
            if handle_outliers_choice == 'yes':
                method = input("Choose a method to handle outliers (remove/replace) : ").strip().lower()
                
                if method == 'remove':
                    data = data[(data[col] >= lower_bound) & (data[col] <= upper_bound)]
                    print(f"Outliers in column '{col}' have been removed.")
                elif method == 'replace':
                    replacement_choice = input("Choose a replacement method (mean/median) : ").strip().lower()
                    if replacement_choice == 'mean':
                        mean_value = data[col].mean()
                        data[col] = data[col].apply(lambda x: mean_value if x < lower_bound or x > upper_bound else x)
                        print(f"Outliers in column '{col}' have been replaced with the mean.")
                    elif replacement_choice == 'median':
                        median_value = data[col].median()
                        data[col] = data[col].apply(lambda x: median_value if x < lower_bound or x > upper_bound else x)
                        print(f"Outliers in column '{col}' have been replaced with the median.")
            else:
                print(f"Outliers in column '{col}' have not been handled.")
        else:
            print(f"No outliers detected in column '{col}'.")
    
    return data
