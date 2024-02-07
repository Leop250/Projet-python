from Etudiant import *
from gestion_etudiant import *

# Fonctions pour la coloration du texte
def blue_text(text):
    return f"\033[34m{text}\033[0m"

def green_text(text):
    return f"\033[32m{text}\033[0m"

def red_text(text):
    return f"\033[31m{text}\033[0m"

print(blue_text("Que voulez-vous faire :"))
print(green_text("Tapez '1' pour rechercher un étudiant"))
print(green_text("Tapez '2' pour supprimer un étudiant"))
print(green_text("Tapez '3' pour ajouter un étudiant"))
print(green_text("Tapez '4' pour visualiser la liste des étudiants"))
print(green_text("Tapez '5' pour modifier un étudiant"))
print(red_text("Tapez '6' pour quitter le programme"))

choix = input()

while choix != "6":
    if choix == "1":
        id = input("Entrez le numéro de l'étudiant (ID) que vous cherchez : ")
        Etudiant.rechercher_etudiant(id)
    
    elif choix == "2":
        id_etudiant = input("Entrez l'ID de l'étudiant que vous souhaitez supprimer : ")
        Etudiant.supp_etudiant(id_etudiant)
    
    elif choix == "3":
        nom = input("Nom de l'étudiant : ")
        prenom = input("Prénom de l'étudiant : ")
        matricule_id = input("Matricule ID de l'étudiant : ")
        adresse = input("Adresse de l'étudiant : ")
        numero_tel = input("Numéro de téléphone de l'étudiant : ")
        email = input("Email de l'étudiant : ")
        class_niveau = input("Classe/Niveau de l'étudiant : ")
        
        etudiant = Etudiant(nom, prenom, matricule_id, adresse, numero_tel, email, class_niveau)
        etudiant.ajouter_etudiant()
    
    elif choix == "4":
        for etudiant in Etudiant.dico_etudiants.values():
            print(etudiant)
    
    elif choix == "5":
        Etudiant.modifier_etudiant()
    
    else:
        print(red_text("Saisie invalide. Veuillez entrer un choix valide."))

    print(blue_text("Que voulez-vous faire :"))
    print(green_text("Tapez '1' pour rechercher un étudiant"))
    print(green_text("Tapez '2' pour supprimer un étudiant"))
    print(green_text("Tapez '3' pour ajouter un étudiant"))
    print(green_text("Tapez '4' pour visualiser la liste des étudiants"))
    print(green_text("Tapez '5' pour modifier un étudiant"))
    print(red_text("Tapez '6' pour quitter le programme"))

    choix = input()
