# load_data.py
import os
import pandas as pd
from tqdm import tqdm
import time
from utils import print_colored

def load_data():
    while True:
        try:
            filename = input("Entrez le nom du fichier CSV (ou chemin absolu) : ")
            if not os.path.isfile(filename):
                raise FileNotFoundError("Le fichier spécifié n'existe pas.")
            if not filename.endswith('.csv'):
                raise ValueError("Le fichier spécifié n'est pas un fichier CSV.")
            break
        except (FileNotFoundError, ValueError) as e:
            print_colored(str(e), 'red')
            print_colored("Veuillez réessayer.", 'yellow')
    
    while True:
        try:
            separator = input("Entrez le séparateur utilisé dans le fichier CSV (ex: ',' pour virgule, ';' pour point-virgule, '\\t' pour tabulation) : ")
            if separator == '\\t':
                separator = '\t'
            if separator in [',', ';', '\t']:
                break
            else:
                raise ValueError("Séparateur non valide.")
        except ValueError as e:
            print_colored(str(e), 'red')
            print_colored("Veuillez réessayer.", 'yellow')

    with tqdm(total=100, desc="Chargement des données", leave=True) as pbar:
        time.sleep(1)
        pbar.update(100)
    
    try:
        data = pd.read_csv(filename, sep=separator, encoding='latin1')
    except pd.errors.ParserError as e:
        print_colored("Erreur de parsing du fichier CSV :", 'red')
        print_colored(str(e), 'red')
        print_colored("Veuillez vérifier le séparateur utilisé ou la structure du fichier.", 'yellow')
        return load_data()
    
    print_colored("Voici un aperçu des premières lignes du dataset :", 'yellow')
    print(data.head())

    while True:
        confirm = input("Est-ce le bon dataset ? (Oui/Non) : ").strip().lower()
        if confirm in ['oui', 'non']:
            break
        else:
            print_colored("Merci de rentrer une valeur correcte (Oui/Non).", 'red')
    
    if confirm == 'non':
        print_colored("Veuillez recharger le fichier avec les bonnes configurations.", 'yellow')
        return load_data()
    
    return data, filename


