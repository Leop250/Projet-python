from prepare_data import *
from prepare_data_anglais import create_time_index
from plot_data import *
from save_data import *
from utils import *
from encoder_variable import *
from load_data import *

def main_f():
    data, filename = load_data()
    
    while True:
        print("\nQue souhaitez-vous faire ?")
        print("1. Afficher les informations sur le dataset")
        print("2. Préparer le jeu de données (Suppression des NaN, des valeurs aberrantes, des doublons et renommage des colonnes)")
        print("3. Renommer les colonnes")
        print("4. Supprimer les doublons")
        print("5. Traiter les valeurs aberrantes")
        print("6. Regrouper des colonnes")
        print("7. Créer une colonne d'indice temporel")
        print("8. Créer un graphique")
        print("9. Supprimer des colonnes")
        print("10. Encoder les variables")
        print("11. Sauvegarder les modifications")
        print("12. Quitter")

        choix = input("Entrez le numéro de votre choix : ")
        
        if choix == '1':
            show_info(data)
        elif choix == '2':
            data = prepare_data(data)
        elif choix == '3':
            rename_column(data)
        elif choix == '4':
            remove_duplicates(data)
        elif choix == '5':
            valeur_aberante(data)
        elif choix == '6':
            supp_columns(data)
        elif choix == '7':
            create_time_index(data)
        elif choix == '8':
            create_plot(data)
        elif choix == '9':
            supp_columns(data)
        elif choix == '10':
            encoder_variables(data)
        elif choix == '11':
            sauvegarder(data)
        elif choix == '12':
            print("Merci d'avoir utilisé l'outil.")
            break
        else:
            print_colored("Choix invalide. Veuillez entrer un numéro valide.", 'red')

if __name__ == "__main__":
    main_f()
