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


def main():
    data, filename = load_data()
    
    while True:
        print("\nQue souhaitez-vous faire ?")
        print("1. Afficher les informations sur le dataset")
        print("2. Preparer le jeu de données (Suppression des NaN, des doublons et renommage des colonnes)")
        print("3. Renommer les colonnes")
        print("4. Supprimer les doublons")
        print("5. Regrouper des colonnes")
        print("6. Créer une colonne d'indice temporel")
        print("7. Pour créer un graphique")
        print("8. Supprimer des colonnes")
        print("9. Encoder les varaiables ")
        print("10. Sauvegarder les modifications")
        print("11. Pour quitter")

        choix = input("Entrez le numéro de votre choix : ")
        
        if choix == '1':
            show_info(data)
        elif choix == '2':
            data = prepare_data(data)
        elif choix == '3':
            rename_column(data)
        elif choix == '4':
            data = remove_duplicates(data)
        elif choix == '5':
            regrouper_columns(data)
        elif choix == '6':
            creat_index_temporel(data)
        elif choix == '7':
            create_plot(data)
        elif choix == "8":
            data = remove_columns(data)
        elif choix == '9':
            encoder_variables(data)
        elif choix == '10':
            sauvegarder(data, filename)
        elif choix == '11':
            break
        else:
            print_colored("Choix invalide. Veuillez entrer un numéro valide.", 'red')

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

def remove_columns(data):
    print("Voici les colonnes de votre jeu de données :")
    for i in data.columns:
        print(i)
    
    column_drop = input("Entrez le nom de la colonne que vous souhaitez supprimer : ")
    
    while column_drop not in data.columns:
        print_colored("La colonne n'existe pas.", 'red')
        column_drop = input("Entrez à nouveau le nom de la colonne que vous souhaitez supprimer : ")
    
    data = data.drop(column_drop, axis=1)
    print_colored("Voici le nouveau jeu de données sans la colonne", 'green', column_drop)
    print(data)
    return data

def regrouper_columns(data):
    while True:
        choix_regrouper_des_colonnes = input("Voulez-vous regrouper plusieurs colonnes dans le dataset ? (Oui/Non) : ").strip().lower()
        if choix_regrouper_des_colonnes in ['oui', 'non']:
            break
        else:
            print_colored("Merci de rentrer une valeur correcte (Oui/Non).", 'red')
    
    if choix_regrouper_des_colonnes == 'oui':
        column_a_regrouper_list = []
        while True:
            column_a_regrouper = input("Entrez le nom de la colonne à regrouper (tapez STOP pour arrêter) : ")
            if column_a_regrouper.lower() == "stop":
                break
            if column_a_regrouper in data.columns:
                column_a_regrouper_list.append(column_a_regrouper)
            else:
                print_colored(f"La colonne '{column_a_regrouper}' n'existe pas dans le jeu de données.", 'red')

        if not column_a_regrouper_list:
            print_colored("Aucune colonne valide n'a été sélectionnée.", 'red')
            return

        if verifier_types_compatibles(data, column_a_regrouper_list):
            print_colored("Les types des colonnes à regrouper sont compatibles.", 'green')
            new_column_name = input("Entrez le nom de la nouvelle colonne combinée: ")
            data[new_column_name] = data[column_a_regrouper_list].astype(str).agg(' '.join, axis=1)
            print_colored(f"Colonnes regroupées avec succès dans la nouvelle colonne '{new_column_name}'.", 'green')
        else:
            print_colored("Les types des colonnes à regrouper ne sont pas compatibles.", 'red')
    else:
        print_colored("Aucun regroupement de colonnes demandé.", 'yellow')

def verifier_types_compatibles(data, columns):
    types = set(data[column].dtype for column in columns)
    return len(types) == 1

def sauvegarder(data, filename):
    while True:
        choix_sauvegarde = input("Voulez-vous sauvegarder les modifications sur le même fichier ou sur un nouveau fichier ?\n1. Sur le même fichier\n2. Sur un nouveau fichier\nEntrez le numéro de votre choix : ")
        if choix_sauvegarde in ['1', '2']:
            break
        else:
            print_colored("Choix invalide. Veuillez entrer 1 ou 2.", 'red')
    
    if choix_sauvegarde == '1':
        save_data(data, filename)
    elif choix_sauvegarde == '2':
        new_filename = input("Entrez le nom du nouveau fichier pour sauvegarder les données (ex: data_modified.csv) : ")
        save_data(data, new_filename)

def save_data(data, filename):
    if not filename.endswith('.csv'):
        filename += '.csv'
    data.to_csv(filename, index=False)  
    print_colored(f"Données sauvegardées avec succès dans le fichier '{filename}'.", 'green')

def creat_index_temporel(data):
    while True:
        choix_index = input("Voulez-vous créer une colonne d'index temporel pour avoir un suivi dans le temps, cela peut être utile pour la création de graphiques ? (Oui/Non) : ").strip().lower()
        if choix_index in ['oui', 'non']:
            break
        else:
            print_colored("Merci de rentrer une valeur correcte (Oui/Non).", 'red')
    
    if choix_index == "oui":
        print_colored("Vous avez choisi de créer une colonne d'index temporel", 'yellow')
        new_column = input("Entrez le nom de la colonne que vous souhaitez donner à votre colonne d'index temporel : ")
        nombre_de_lignes = len(data)
        data[new_column] = range(1, nombre_de_lignes + 1)
        print_colored(f"Votre colonne {new_column}, d'index temporel a été créée avec succès.", 'green')
        print(data)
    
    elif choix_index == "non":
        print_colored("Vous avez choisi de ne pas créer une colonne d'index temporel", 'yellow')

from sklearn.preprocessing import LabelEncoder

from sklearn.preprocessing import LabelEncoder
import pandas as pd

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

# Exemple d'utilisation de la fonction dans le contexte de votre programme principal
if __name__ == "__main__":
    main()


def create_plot(data):
    print("Types de graphiques disponibles :")
    print("1. Diagramme en barres")
    print("2. Diagramme en nuage de points")
    print("3. Diagramme en boîte")
    print("4. Histogramme")

    while True:
        choix_graphique = input("Entrez le numéro correspondant au type de graphique que vous souhaitez créer : ").strip()
        if choix_graphique in ['1', '2', '3', '4']:
            break
        else:
            print("Type de graphique invalide.")

    if choix_graphique == '1':
        create_bar_chart(data)
    elif choix_graphique == '2':
        create_scatter_plot(data)
    elif choix_graphique == '3':
        create_box_plot(data)
    elif choix_graphique == '4':
        create_histogram(data)
    elif choix_graphique == '5':
        create_graph_classique(data)


def create_bar_chart(data):
    for i in data.columns:
        print(i)
    while True:
        x_axis = input("Entrez le nom de la colonne pour l'axe des abscisses : ").strip()
        if x_axis in data.columns and pd.api.types.is_numeric_dtype(data[x_axis]):
            break
        else:
           
           print_colored("La colonne n'existe pas ou ne contient pas des données numériques.", 'yellow')
    
    while True:
        y_axis = input("Entrez le nom de la colonne pour l'axe des ordonnées : ").strip()
        if y_axis in data.columns and pd.api.types.is_numeric_dtype(data[y_axis]):
            break
        else:
           print_colored("La colonne n'existe pas ou ne contient pas des données numériques.", 'yellow')
    
    plt.bar(data[x_axis], data[y_axis])
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.title("Diagramme en barres")
    plt.show()

def create_scatter_plot(data):
    for i in data.columns:
        print(i)
    while True:
        x_axis = input("Entrez le nom de la colonne pour l'axe des abscisses : ").strip()
        if x_axis in data.columns and pd.api.types.is_numeric_dtype(data[x_axis]):
            break
        else:
            print_colored("La colonne n'existe pas ou ne contient pas des données numériques.", 'yellow')
    
    while True:
        y_axis = input("Entrez le nom de la colonne pour l'axe des ordonnées : ").strip()
        if y_axis in data.columns and pd.api.types.is_numeric_dtype(data[y_axis]):
            break
        else:
            print_colored("La colonne n'existe pas ou ne contient pas des données numériques.", 'yellow')
    
    plt.scatter(data[x_axis], data[y_axis])
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.title("Diagramme en nuage de points")
    plt.show()

def create_box_plot(data):
    for i in data.columns:
        print(i)
    while True:
        x_axis = input("Entrez le nom de la colonne pour l'axe des abscisses : ").strip()
        if x_axis in data.columns and pd.api.types.is_numeric_dtype(data[x_axis]):
            break
        else:
            print_colored("La colonne n'existe pas ou ne contient pas des données numériques.", 'yellow')
    
    while True:
        y_axis = input("Entrez le nom de la colonne pour l'axe des ordonnées : ").strip()
        if y_axis in data.columns and pd.api.types.is_numeric_dtype(data[y_axis]):
            break
        else:
            print_colored("La colonne n'existe pas ou ne contient pas des données numériques.", 'yellow')
    
    plt.boxplot(data[y_axis], labels=[x_axis])
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.title("Diagramme en boîte")
    plt.show()

def create_histogram(data):
    for i in data.columns:
        print(i)
    while True:
        column = input("Entrez le nom de la colonne pour laquelle vous souhaitez créer l'histogramme : ").strip()
        if column in data.columns and pd.api.types.is_numeric_dtype(data[column]):
            break
        else:
            print_colored("La colonne n'existe pas ou ne contient pas des données numériques.", 'yellow')


    plt.hist(data[column])
    plt.xlabel(column)
    plt.ylabel("Fréquence")
    plt.title("Histogramme")
    plt.show()


def create_graph_classique(data):
    for i in data.columns:
        print(i)
    while True:
        x_axis = input("Entrez le nom de la colonne pour l'axe des abscisses : ").strip()
        if x_axis in data.columns and pd.api.types.is_numeric_dtype(data[x_axis]):
            break
        else:
            print_colored("La colonne n'existe pas ou ne contient pas des données numériques.", 'yellow')
    
    while True:
        y_axis = input("Entrez le nom de la colonne pour l'axe des ordonnées : ").strip()
        if y_axis in data.columns and pd.api.types.is_numeric_dtype(data[y_axis]):
            break
        else:
            print_colored("La colonne n'existe pas ou ne contient pas des données numériques.", 'yellow')
    
    plt.plot(x_axis, y_axis)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.show()
    

