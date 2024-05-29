# prepare_data.py
import pandas as pd
from tqdm import tqdm
import time
from utils import print_colored

def show_info(data):
    print_colored("\nInformations sur le dataset :", 'yellow')
    with tqdm(total=100, desc="Calcul des informations", leave=True) as pbar:
        time.sleep(1)
        pbar.update(50)
        print(data.info())
        pbar.update(25)
        print(data.describe())
        pbar.update(25)
    for column in data.columns:
        print(f"La taille de la colonne {column} est de {len(data[column])}")
    print("voici les première lignes du jeu de données: ")
    print(data.head())

def prepare_data(data):
    supp_na(data)
    valeur_aberante(data)
    data = remove_duplicates(data)
    rename_column(data)
    return data

def supp_na(data):
    with tqdm(total=100, desc="Analyse des données manquantes", leave=True) as pbar:
        time.sleep(1)
        pbar.update(100)
    nb_lignes_avec_nan = data.isna().any(axis=1).sum()
    pourcentage_lignes_avec_nan = (nb_lignes_avec_nan / len(data)) * 100
    print(f"Pourcentage de lignes avec au moins un NaN: {pourcentage_lignes_avec_nan:.2f}%")

    if nb_lignes_avec_nan >0:
        while True:
            choix_na = input("Voulez-vous supprimer les lignes avec NaN ? (Oui/Non) : ").strip().lower()
            if choix_na in ['oui', 'non']:
                break
            else:
                print_colored("Merci de rentrer une valeur correcte (Oui/Non).", 'red')
        if choix_na == 'oui':
            data.dropna(inplace=True)
            print_colored("Les lignes avec NaN ont été supprimées.", 'green')
        elif choix_na == 'non':
            print_colored("Les lignes avec NaN n'ont pas été supprimées.", 'yellow')
    else:
        print_colored("Aucun doublons dans votre datastet.", 'green')


def rename_column(data):
    while True:
        choix_rename_column = input("Voulez-vous renommer les colonnes du dataset ? (Oui/Non) : ").strip().lower()
        if choix_rename_column in ['oui', 'non']:
            break
        else:
            print_colored("Merci de rentrer une valeur correcte (Oui/Non).", 'red')
    
    if choix_rename_column == 'oui':
        for col in tqdm(data.columns, desc="Renommage des colonnes", leave=True):
            while True:
                choix_renommer = input(f"Voulez-vous renommer la colonne '{col}' ? (Oui/Non) : ").strip().lower()
                if choix_renommer in ['oui', 'non']:
                    break
                else:
                    print_colored("Merci de rentrer une valeur correcte (Oui/Non).", 'red')
            
            if choix_renommer == 'oui':
                nouveau_nom = input("Entrez le nouveau nom de la colonne: ").strip()
                data.rename(columns={col: nouveau_nom}, inplace=True)
                print_colored("Passons à la colonne suivante.", 'yellow')
            elif choix_renommer == 'non':
                print_colored("Passons à la colonne suivante.", 'yellow')
        
        print_colored("Noms des colonnes après renommage :", 'green')
        print(data.columns)
    elif choix_rename_column == 'non':
        print_colored("Aucun renommage effectué.", 'yellow')

def remove_duplicates(data):
    print_colored("Analyse des doublons en cours...", 'yellow')
    duplicates = data[data.duplicated(keep=False)]

    print("Doublons identifiés :")
    print(duplicates)

    nombre_doublons = len(duplicates)
    print(f"Nombre de lignes en doublons identifiées : {nombre_doublons}")

    while True:
        choix_doublon = input("Voulez-vous supprimer les doublons du dataset ? (Oui/Non) : ").strip().lower()
        if choix_doublon in ['oui', 'non']:
            break
        else:
            print_colored("Merci de rentrer une valeur correcte (Oui/Non).", 'red')

    if choix_doublon == 'oui':
        original_count = len(data)
        data.drop_duplicates(inplace=True)
        removed_count = original_count - len(data)
        print_colored(f"Les doublons ont été supprimés. {removed_count} lignes en moins.", 'green')
    elif choix_doublon == 'non':
        print_colored("Aucun doublon n'a été supprimé.", 'yellow')
    return data

def supp_columns(data):
    print("Voici les colonnes de votre jeu de données :")
    for i in data.columns:
        print(i)
    
    while True:
        column_name = input("Entrez le nom de la colonne à supprimer (ou tapez 'exit' pour quitter): ")
        if column_name == 'exit':
            break
        if column_name in data.columns:
            data.drop(column_name, axis=1, inplace=True)
            print_colored(f"Colonne '{column_name}' supprimée.", 'green')
        else:
            print_colored("Colonne non trouvée, veuillez réessayer.", 'red')
    
    return data

def regrouper_columns(data):
    while True:
        try:
            columns_to_merge = input("Entrez les noms des colonnes à regrouper (séparés par des virgules) : ").split(',')
            columns_to_merge = [col.strip() for col in columns_to_merge if col.strip() in data.columns]
            if len(columns_to_merge) < 2:
                raise ValueError("Veuillez entrer au moins deux colonnes existantes.")
            break
        except ValueError as e:
            print_colored(str(e), 'red')
            print_colored("Veuillez réessayer.", 'yellow')

    new_column_name = input("Entrez le nom de la nouvelle colonne regroupée : ")
    data[new_column_name] = data[columns_to_merge].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
    print_colored(f"Les colonnes {', '.join(columns_to_merge)} ont été regroupées en une nouvelle colonne '{new_column_name}'.", 'green')

def create_index_temporel(data):
    print("Pour créer une colonne d'indice temporel, vous devez fournir une colonne de dates.")
    
    while True:
        date_column = input("Entrez le nom de la colonne de dates (ou tapez 'exit' pour quitter): ")
        if date_column == 'exit':
            break
        if date_column in data.columns:
            try:
                data[date_column] = pd.to_datetime(data[date_column])
                data.set_index(date_column, inplace=True)
                print_colored(f"La colonne '{date_column}' a été convertie en indice temporel.", 'green')
                break
            except Exception as e:
                print_colored(f"Erreur lors de la conversion : {e}", 'red')
                print_colored("Veuillez vérifier le format de la colonne de dates et réessayer.", 'yellow')
        else:
            print_colored("Colonne non trouvée, veuillez réessayer.", 'red')


def valeur_aberante(data):
    numeric_columns = data.select_dtypes(include=['number']).columns
    print("Analyse des colonnes numériques pour les valeurs aberrantes...")
    
    for col in numeric_columns:
        q1 = data[col].quantile(0.25)
        q3 = data[col].quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers = data[(data[col] < lower_bound) | (data[col] > upper_bound)]
        
        num_outliers = len(outliers)

        print(f"Colonne '{col}': {num_outliers} valeurs aberrantes détectées.")
        
        if num_outliers > 0:
            choix_outliers = input(f"Voulez-vous traiter les valeurs aberrantes de la colonne '{col}' ? (Oui/Non) : ").strip().lower()
            if choix_outliers == 'oui':
                methode = input("Choisissez une méthode pour traiter les valeurs aberrantes (supprimer/remplacer) : ").strip().lower()
                
                if methode == 'supprimer':
                    data = data[(data[col] >= lower_bound) & (data[col] <= upper_bound)]
                    print_colored(f"Les valeurs aberrantes de la colonne '{col}' ont été supprimées.", 'green')
                elif methode == 'remplacer':
                    choix_remplacement = input("Choisissez une méthode de remplacement (moyenne/mediane) : ").strip().lower()
                    if choix_remplacement == 'moyenne':
                        mean_value = data[col].mean()
                        data[col] = data[col].apply(lambda x: mean_value if x < lower_bound or x > upper_bound else x)
                        print_colored(f"Les valeurs aberrantes de la colonne '{col}' ont été remplacées par la moyenne.", 'green')
                    elif choix_remplacement == 'mediane':
                        median_value = data[col].median()
                        data[col] = data[col].apply(lambda x: median_value if x < lower_bound or x > upper_bound else x)
                        print_colored(f"Les valeurs aberrantes de la colonne '{col}' ont été remplacées par la médiane.", 'green')
            else:
                print_colored(f"Les valeurs aberrantes de la colonne '{col}' n'ont pas été traitées.", 'yellow')
        else:
            print_colored(f"Aucune valeur aberrante n'a été détectée dans la colonne '{col}'.", 'green')
    
    return data
