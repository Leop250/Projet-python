from Etudiant import *


def ajouter_etudiant(self):
    self.dico_etudiants[self.matriculeID]={
        "nom": self.nom,
        "prenom": self.prenom,
        "matriculeID": self.matriculeID,
        "adresse": self.adresse,
        "numero telephone": self.numerotel,
        "email": self.email,
        "class niveau": self.classniveau
    }

@classmethod
def rechercher_etudiant(cls, id_recherche):
    #recherche de la base de donnée
    if id_recherche in cls.dico_etudiants:
        print("l'étudiant est bien dans la base de donnée")
        etudiant_a_afficher= cls.dico_etudiants[id_recherche]
        print("Informations actuelles de l'étudiant : ")
        for key, value in etudiant_a_afficher.items():
            print(key + ":", value)


    else:
        print("l'etudiant n'est pas dedans")
#methode pour modifier les informations des étudiants 
#sert a accder a la valeur du dico
@classmethod
def modifier_etudiant(cls):
    id_modification = input("Entrez l'ID de l'étudiant que vous souhaitez modifier : ")
    if id_modification in cls.dico_etudiants:
        print("L'étudiant est bien dans la base de données. Vous pouvez procéder à la modification.")
        etudiant_a_modifier = cls.dico_etudiants[id_modification]

        # Afficher les informations actuelles de l'étudiant
        print("Informations actuelles de l'étudiant : ")
        for key, value in etudiant_a_modifier.items():
            print(key + ":", value)

        # Sélectionner quelle information modifier
        que_modifier = input("Que voulez-vous modifier ? (1 pour nom, 2 pour prénom, 3 pour matriculeID, 4 pour numéro de téléphone, 5 pour email): ")
        nouvelle_valeur = input("Entrez la nouvelle valeur : ")

        # Modifier l'information sélectionnée
        if que_modifier == "1":
            etudiant_a_modifier["nom"] = nouvelle_valeur
        elif que_modifier == "2":
            etudiant_a_modifier["prenom"] = nouvelle_valeur
        elif que_modifier == "3":
            etudiant_a_modifier["matriculeID"] = nouvelle_valeur
        elif que_modifier == "4":
            etudiant_a_modifier["numero telephone"] = nouvelle_valeur
        elif que_modifier == "5":
            etudiant_a_modifier["email"] = nouvelle_valeur
        else:
            print("Option invalide.")
            return

        print("Modification effectuée avec succès.")

@classmethod
def supp_etudiant(cls, id):
    if id in cls.dico_etudiants:
        print("L'étudiant est bien dans la base de données. Nous allons donc pouvoir le supprimer.")
        #supp la personne du dico 
        cls.dico_etudiants.pop(id)
    else:
        print("L'étudiant n'est pas dans la base de données.")


