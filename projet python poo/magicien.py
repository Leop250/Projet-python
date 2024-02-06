from personage import Personnage  # Assurez-vous que les noms de fichiers et les imports sont corrects

import random

class Magicien(Personnage):
    FORCE_FRAPPE_1 = 10
    FORCE_FRAPPE_2 = 15

    def __init__(self, nom, vie, force, degats, tour="joueur1"):
        # Appel du constructeur de la classe parent (Personnage)
        super().__init__(nom, vie, force, degats, tour)
        
    def lanceUnSort(self, adversaire):
        print(f"{self.nom} lance un sort sur {adversaire.nom}")
        adversaire.recoitDegat(self, self.FORCE_FRAPPE_1)
        self.FORCE_FRAPPE_1 +=1
        print("l'attaque lanceUnSort à agumneté de 1 ", self.FORCE_FRAPPE_1)
        
    def LanceUnRayonDeLumièreSombre(self, adversaire):
        adversaire.recoitDegat(self, self.FORCE_FRAPPE_2)
        self.FORCE_FRAPPE_2 +=1
        print("l'attque LanceUnRayonDeLumièreSombre à augmnté de 1", self.FORCE_FRAPPE_2)
        
    def attaque(self, adversaire):
        attaque_possible = ["lanceUnSort", "LanceUnRayonDeLumièreSombre"]
        choix = random.choice(attaque_possible)

        
        if choix == "lanceUnSort":
            self.lanceUnSort(adversaire)
            print("jutilise l'attaque lanceUnSort")
            
        elif choix == "LanceUnRayonDeLumièreSombre":
            self.LanceUnRayonDeLumièreSombre(adversaire)
            print("jutilise l'attaque LanceUnRayonDeLumièreSombre")

# Exemple d'utilisation




