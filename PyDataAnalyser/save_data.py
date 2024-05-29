# save_data.py
import pandas as pd
from utils import print_colored

def sauvegarder(data):
    try:
        new_filename = input("Entrez le nom du fichier de sauvegarde (avec extension .csv) : ")
        data.to_csv(new_filename, index=False, encoding='latin1')
        print_colored(f"Les modifications ont été sauvegardées dans le fichier {new_filename}.", 'green')
    except Exception as e:
        print_colored(f"Erreur lors de la sauvegarde : {e}", 'red')
