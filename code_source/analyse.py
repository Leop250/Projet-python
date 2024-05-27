                                            
# import numpy as np                                                              
# import matplotlib.pyplot as plt                                                
# import seaborn as sns                                                           
# import pandas as pd                                                             

# data = input(" nom du fichier si dans le meme dossier ou  chemin abslu: ")                                                  
# data = pd.read_csv(data)  
# data.info() 
# data.head() 

# # nb_lignes_avec_nan = data.isna().any(axis=1).sum()


# # pourcentage_lignes_avec_nan = (nb_lignes_avec_nan / len(data)) * 100


# # print(f"Pourcentage de lignes avec au moins un NaN: {pourcentage_lignes_avec_nan:.2f}%")

# def supp_na(data):
#     nb_lignes_avec_nan = data.isna().any(axis=1).sum()


#     pourcentage_lignes_avec_nan = (nb_lignes_avec_nan / len(data)) * 100


#     print(f"Pourcentage de lignes avec au moins un NaN: {pourcentage_lignes_avec_nan:.2f}%")
#     choix_na = int(input(f"Voullez vous supprimer les na celle ci represnte {pourcentage_lignes_avec_nan} % du dataset \n 1 pour oui \n 2 pour non  "))

#     if choix_na == 1:
#         data.dropna(inplace=True)
#         print("Les lignes avec NaN ont été supprimées car elles représentent moins de 5% du dataset.")
#     elif choix_na == 2:
#         print("Les lignes avec NaN n'ont pas été comme vous le souhaiter")
#     else:
#         print("merci de rentrer une valeur correct ")


# def rename_column(data):
    
#     choix_rename_column = int(input("Voulez-vous renommer les colonnes du dataset ? (1 pour oui, 0 pour non): "))
    
#     if choix_rename_column == 1:
        
#         for i in range(len(data.columns)):
#             print(f"{i} : {data.columns[i]}")
#             choix_renommer = int(input(f"Voulez-vous renommer la colonne '{data.columns[i]}' ? (1 pour oui, 0 pour non): "))
            
#             if choix_renommer == 1:
                
#                 nouveau_nom = input("Entrez le nouveau nom de la colonne: ")
#                 data.rename(columns={data.columns[i]: nouveau_nom}, inplace=True)
        
#         print("Noms des colonnes après renommage :", data.columns)
#     else:
#         print("Aucun renommage effectué.")

# def supp_doublon(data):
#     duplicates = data[data.duplicated()]
#     print("Doublons identifiés :")
#     print(duplicates)
 
#     choix_doublon =  int(input("Voulez-vous supprimer les doublons du dataset (1 pour oui, 0 pour non): "))
#     if choix_doublon == 1:
#         data.drop_duplicates(inplace= True)
#         print("les doublons on été supprimer")
#     else:
#         print("Aucun doublon n'a été supprimé")

# def show_info(data):
#     print("Informations sur le dataset :")
#     print(data.info())
#     print(data.describe())

# def verifier_types_compatibles(data, columns):
#     types = set(data[column].dtype for column in columns)
#     return len(types) == 1

# def regrouper_columns(data):
#     choix_regrouper_des_colonnes = int(input("Voulez-vous regrouper plusieurs colonnes dans le dataset ? (1 pour oui, 0 pour non): "))
#     if choix_regrouper_des_colonnes != 1:
#         print("Aucun regroupement de colonnes demandé.")
#         return

#     column_a_regrouper_list = []
#     while True:
#         column_a_regrouper = input("Entrez le nom de la colonne à regrouper (tapez STOP pour arrêter): ")
#         if column_a_regrouper == "STOP":
#             break
#         if column_a_regrouper in data.columns:
#             column_a_regrouper_list.append(column_a_regrouper)
#         else:
#             print(f"La colonne '{column_a_regrouper}' n'existe pas dans le jeu de données.")

#     if not column_a_regrouper_list:
#         print("Aucune colonne valide n'a été sélectionnée.")
#         return
    
#     if verifier_types_compatibles(data, column_a_regrouper_list):
#         print("Les types des colonnes à regrouper sont compatibles.")
#         new_column_name = input("Entrez le nom de la nouvelle colonne combinée: ")
#         data[new_column_name] = data[column_a_regrouper_list].astype(str).agg(' '.join, axis=1)
#         print("Colonnes regroupées avec succès dans la nouvelle colonne '{}'.".format(new_column_name))
#     else:
#         print("Les types des colonnes à regrouper ne sont pas compatibles.")

        
#         # print("5 - Nettoyer les données en supprimant les lignes avec des valeurs manquantes")
#         # print("6 - Trier les données par une colonne spécifiée")
#         # print("7 - Sauvegarder le DataFrame dans un nouveau fichier")
#         # print("8 - Calculer la médiane des colonnes numériques")
#         # print("9 - Calculer l'écart type des colonnes numériques")
#         # print("10 - Visualiser un histogramme d'une colonne numérique")
#         # print("11 - Visualiser un graphique à barres pour une colonne catégorielle")
#         # print("12 - Visualiser un box plot pour les colonnes numériques")
#         # print("0 - Quitter le programme")


# # supp_na(data)
# # rename_column(data)  
# # supp_doublon(data)

# show_info(data)
# regrouper_columns(data)  


print("test")