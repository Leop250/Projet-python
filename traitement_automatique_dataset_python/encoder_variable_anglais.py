# encoder_variables.py
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from tqdm import tqdm
import time
from utils import print_colored

def encoder_variables(data):
    while True:
        choice_encoder = input("Do you want to encode the variables? This is necessary for linear model prediction. (Yes/No): ").strip().lower()
        if choice_encoder in ['yes', 'no']:
            break
        else:
            print_colored("Please enter a valid value (Yes/No).", 'red')

    if choice_encoder == "yes":
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

        print_colored("Variables successfully encoded.", 'green')
    elif choice_encoder == "no":
        print_colored("You have chosen not to encode the variables.", 'yellow')
