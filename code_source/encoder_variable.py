# encoder_variables.py
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from tqdm import tqdm
import time
from utils import print_colored

def encoder_variables(data):
    while True:
        choix_encoder = input("Voulez-vous encoder les variables ? Cela est nécessaire pour la prédiction de modèle linéaire. (Oui/Non) : ").strip().lower()
        if choix_encoder in ['oui', 'non']:
            break
        else:
            print_colored("Merci de rentrer une valeur correcte (Oui/Non).", 'red')

    if choix_encoder == "oui":
        print_colored("Vous avez choisi d'encoder les variables.", 'yellow')
        columns_to_encode = [col for col in data.columns if data[col].dtype == 'object' or data[col].dtype == 'O']
        
        with tqdm(total=len(columns_to_encode), desc="Encodage des variables", leave=True) as pbar:
            for col in columns_to_encode:
                try:
                 
                    data[col] = data[col].astype(str)
                    label_encoder = LabelEncoder()
                    data[col] = label_encoder.fit_transform(data[col])
                    pbar.update(1)
                except Exception as e:
                    print_colored(f"Erreur lors de l'encodage de la colonne '{col}': {e}", 'red')
                    continue

        print_colored("Variables encodées avec succès.", 'green')
    elif choix_encoder == "non":
        print_colored("Vous avez choisi de ne pas encoder les variables.", 'yellow')
