# plot_data.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from utils import print_colored

def create_plot(data):
    print("Pour créer un graphique, veuillez spécifier les colonnes à utiliser.")

    while True:
        try:
            x_col = input("Entrez le nom de la colonne pour l'axe des x : ")
            y_col = input("Entrez le nom de la colonne pour l'axe des y : ")
            if x_col in data.columns and y_col in data.columns:
                break
            else:
                raise ValueError("Colonnes non valides, veuillez réessayer.")
        except ValueError as e:
            print_colored(str(e), 'red')
            print_colored("Veuillez réessayer.", 'yellow')

    while True:
        print("Choisissez le type de graphique :")
        print("1. Histogramme")
        print("2. Boxplot")
        print("3. Scatterplot")
        print("4. Quitter")
        
        choix_plot = input("Entrez le numéro de votre choix : ")
        
        if choix_plot == '1':
            plt.figure(figsize=(10, 6))
            sns.histplot(data[x_col], kde=True)
            plt.title(f"Histogramme de {x_col}")
            plt.xlabel(x_col)
            plt.ylabel("Fréquence")
            plt.show()
        elif choix_plot == '2':
            plt.figure(figsize=(10, 6))
            sns.boxplot(x=data[x_col], y=data[y_col])
            plt.title(f"Boxplot de {x_col} et {y_col}")
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.show()
        elif choix_plot == '3':
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x=data[x_col], y=data[y_col])
            plt.title(f"Scatterplot de {x_col} et {y_col}")
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.show()
        elif choix_plot == '4':
            break
        else:
            print_colored("Choix invalide. Veuillez entrer un numéro valide.", 'red')
