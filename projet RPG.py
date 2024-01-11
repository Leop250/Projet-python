import random
import json


def save_game(actual_state):
    with open('save_game.txt', 'w') as file:
        json.dump(actual_state, file)

def load_game():
          try:
              with open('save_game.txt', 'r') as file:
                  actual_state = json.load(file)
                  return actual_state
          except FileNotFoundError:
            return None



def start():
    print("1: Lance une nouvelle partie \n 2: Continue la partie précedente \n 3: Affiche les crédits \n 4: Quitte le jeu")
    action = input()
    if action == "1":
        print("La partie ce lance")
        print("Dans un royaume lointain vivait un soldat fan d'un rappeur: Sefyu. Alors agacé d'entendre en boucle J'peux manger du cassoulet halal en même temps que le mafé il ce fit bannir dans une forêt gardé par un être puissant que peux connaisait")
        print("Allez vous réussir à  sortir du bois d'Arcy?")
        print("il est temps de choisir le type de personage que tu souhaites: ")
        print("Guerrier avec 20 de force,  20 de defense et 100 hp ")
        print("Archer avec 25 de force,  15  de defense et 100 hp ")
        print("Tank avec 15 de force,  25  de defenseet 100 hp ")
        player1 = PlayerRPG()
        player1.player()
        player1.map_init()
        nb_deplacement = 0
        boss = monsters["Le Duc du bois"]["HP"]
        while player1.HP > 0 and boss > 0:
            player1.event()
            player1.level()
            player1.save_and_quit()
            player1.afficher_statut_joueur()
            player1.afficher_carte()



    elif action == "2":
        print("Reprise de la partie précedente")
        load_game()
    elif action == "3":
        print("Les dévelloppeurs de ce jeu sont:\n ZIAT Yanni \n MACQUART DE TERLINE Léopold \n BELBOUAB Younes")
    elif action == "4":
        print("Vous quittez le jeu \n Merci d'avoir jouer  ")
        exit()

    else:
        action = input()

monsters = {
    "gobelin": {
        "HP": 100,
        "strength": 60,
        "defense": 10,
        "XP": 6,
        "attack": 20,
        "soudoyer": 5
    },
    "ogre": {
        "HP": 150,
        "strength": 80,
        "defense": 20,
        "XP": 10,
        "attack": 35,
        "soudoyer": 10
    },
    "dragon": {
        "HP": 200,
        "strength": 90,
        "defense": 30,
        "XP" :  12,
        "attack": 50,
        "soudoyer": 20
    },

    "Le Duc du bois" : {
        "HP": 400,
        "strength": 100,
        "defense": 50,
        "attack": 70,
        "soudoyer": 10000
    }
}


class PlayerRPG:
    attaques_valides = ["basic hit", "je te shoot si t'es chauve"]
    merchant_inventory = {
        "potion regen": 3,
        "potion force": 3,
        "potion defense": 3
    }

    reward = ["potion force", "potion regen", "potion defense"]

    def __init__(self):
        self.visited_positions = set()
        self.classe = 0
        self.strength = 0
        self.defense = 0
        self.HP = 0
        self.XP = 0
        self.x = 3
        self.y = 3
        self.inventory = {
            "potion regen": 1,
            "potion force": 0,
            "potion defense": 1,
            "super potion": 0,
            "PO": 20
        }
        self.attack = {
            "basic hit": [20, 100],
            "je te shoot si t'es chauve": [40, 75]
        }
        game_state = load_game()

        if game_state:

            self.strength = game_state['strength']
            self.defense = game_state['defense']
            self.HP = game_state['HP']
            self.XP = game_state['XP']
            self.x = game_state['x']
            self.y = game_state['y']
            self.inventory = game_state['inventory']

    def afficher_statut_joueur(self):
        print("\033[93mSanté : {}\033[0m".format(self.HP))

    def afficher_carte(self):
        for i, ligne in enumerate(self.game_map):
            for j, tuile in enumerate(ligne):
                if (i, j) == (self.x, self.y):
                    print("\033[93m{}\033[0m".format(tuile), end=" ")
                elif tuile == "gobelin":
                    print("\033[91m{}\033[0m".format(tuile), end=" ")
                elif tuile == "ogre":
                    print("\033[91m{}\033[0m".format(tuile), end=" ")
                elif tuile == "dragon":
                    print("\033[91m{}\033[0m".format(tuile), end=" ")
                elif(i, j) == (self.x, self.y):
                    print("\033[93mJ\033[0m", end=" ")
                else:
                    print(tuile, end=" ")
            print()

    def map_init(self):
        list_obj = []

        for coffre in range(0, 10):
            list_obj.append("coffre")
        for monstre_facile in range(0, 10):
            list_obj.append("goblin")

        for monstre_difficile in range(0, 4):
            list_obj.append("dragon")

        for monstre_moyen in range(0, 5):
            list_obj.append("ogre")

        for feu in range(0, 3):
            list_obj.append("feu de camp")

        list_obj.append("Le Duc du bois")
        list_obj.append("piège - 50pv")

        for super_potion in range(0, 3):
            list_obj.append("super potion")

        for voleur in range(0, 6):
            list_obj.append("voleur de divers")

        for piège in range(0, 3):
            list_obj.append("piège")


        list_obj.append("marchand")
        list_obj.append("marchand")

        random.shuffle(list_obj)
        nb_colonne = 7
        list_obj.insert(nb_colonne*3 + 3, "mid")
        game_map = [list_obj[i:i + nb_colonne] for i in range(0, len(list_obj), nb_colonne)]



        for ligne in game_map:
            print(ligne)

        self.game_map = game_map
        return self.game_map

    def perform_move(self):
        position = self.game_map[self.x][self.y]
        print("vous etes a cet endroit {}".format(position))
        deplacement = input("ou voulez-vous aller ? D pour droite G pour gauche, H pour haut et B pour bas")
        deplacement = deplacement.upper()
        while deplacement not in ["B", "H", "G", "D"]:
            deplacement = input("Où voulez-vous aller ? D pour droite, G pour gauche, H pour haut et B pour bas")

        if deplacement == "G" and self.y > 0:
            self.y -= 1
            print("Vous êtes désormais à : {}".format(self.game_map[self.x][self.y]))
        elif deplacement == "D" and self.y < len(self.game_map[0]) - 1:
            self.y += 1
            print("Vous êtes désormais à : {}".format(self.game_map[self.x][self.y]))
        elif deplacement == "H" and self.x > 0:
            self.x -= 1
            print("Vous êtes désormais à : {}".format(self.game_map[self.x][self.y]))
        elif deplacement == "B" and self.x < len(self.game_map) - 1:
            self.x += 1
            print("Vous êtes désormais à : {}".format(self.game_map[self.x][self.y]))
        else:
            print("Déplacement non valide.")
        return self.game_map[self.x][self.y]

    def player(self):

        choix = ["Tank", "Guerrier", "Archer"]
        print("Choisir entre Guerrier, Archer et Tank")
        classe_choice = input()
        while classe_choice not in choix:
                print("Erreur choisir entre Guerrier, Archer et Tank: ")
                classe_choice = input()
        classe_choice = classe_choice.lower().capitalize()


        if classe_choice == "Guerrier":
            self.classe = "Guerrier"
            self.strength = 20
            self.defense = 20
            self.HP = 100
            self.XP = 0
            print("Votre classe est {} avec force = {}, defense = {} et PV = {}".format(self.classe, self.strength, self.defense, self.HP))

            return (self.classe, self.strength, self.defense, self.HP, self.XP)
        elif classe_choice == "Archer":
            self.classe = "Archer"
            self.strength = 25
            self.defense = 15
            self.HP = 100
            self.XP = 0
            print("Votre classe est {} avec force = {}, defense = {} et PV = {}".format(self.classe, self.strength,self.defense, self.HP))

            return (self.classe, self.strength, self.defense, self.HP, self.XP)
        elif classe_choice == "Tank":
            self.classe = "Tank"
            self.strength = 15
            self.defense = 25
            self.HP = 100
            self.XP = 0
            print("Votre classe est {} avec force = {}, defense = {} et PV = {}".format(self.classe, self.strength,self.defense, self.HP))
            return (self.classe, self.strength, self.defense, self.HP, self.XP)

        else:
            print("Erreur choisir entre Guerrier, Archer et Tank")
            classe_choice = input()

    def inventory_use(self):
        print(self.inventory)
        oui_non = input("utiliser un objet ?")
        oui_non = oui_non.lower()

        if oui_non == "oui":
            choix = input("choisir obj")
            if choix == "potion force" and self.inventory["potion force"] > 0:
                self.strength += 10
                self.inventory["potion force"] -= 1
                print(self.inventory)
                print("Vous avez maintenant {} de force".format(self.strength))
                return (self.classe, self.strength, self.defense, self.HP, self.XP)
            elif choix == "potion regen" and self.inventory["potion regen"] > 0 and self.HP < 100:
                self.HP += 10
                self.inventory["potion regen"] -= 1
                print(self.inventory)
                print("Vous avez maintenant {} de PV".format(self.HP))
                return (self.classe, self.strength, self.defense, self.HP, self.XP)
            elif choix == "potion defense" and self.inventory["potion defense"] > 0:
                self.defense += 10
                self.inventory["potion defense"] -= 1
                print(self.inventory)
                print("Vous avez maintenant {} de defense".format(self.defense))
                return (self.classe, self.strength, self.defense, self.HP, self.XP)

            elif choix == "super potion" and self.inventory["super potion"] > 0:
                self.defense += 10
                self.HP += 10
                self.strength += 10
                self.inventory["super potion"] -= 1
                print(self.inventory)

                return (self.classe, self.strength, self.defense, self.HP, self.XP)

            else:
                return (self.classe, self.strength, self.defense, self.HP, self.XP)

    def combat(self,monster):
        reward = ["potion force", "potion regen", "potion defense"]
        monster_name = monster
        monster = monsters.get(monster)
        hp_memory = monster["HP"]
        soudoyer = input("voulez-vous tenter de soudoyer le monstre: oui ou non: ")
        if soudoyer not in ["oui", "non"]:
            while soudoyer not in ["oui", "non"]:
                print("Veuillez répondre par 'oui' ou 'non'.")
                soudoyer = input("Voulez-vous tenter de soudoyer le monstre ? oui ou non")
            
        soudoyer = soudoyer.lower()

        if self.inventory["PO"] < monster["soudoyer"] and soudoyer == "oui":
            print("dommage vous n'avez pas assez d'or sur vous")
            print(f"il vous manque {monster['soudoyer'] - self.inventory['PO']}PO")
        if self.inventory["PO"] < monster["soudoyer"] or soudoyer != "oui":
            while self.HP > 0 and monster["HP"] > 0:
                atk = input(f"choice an attack {list(self.attack.keys())}")

                while atk not in (self.attack.keys()):
                    print(f"Choisissez une attaque parmi {list(self.attack.keys())}")
                    atk = input(f"Choisissez une attaque parmi {list(self.attack.keys())}")
                atk = atk.lower()
                self.inventory_use()
                accuracy = random.randint(0,100)
                if accuracy <= self.attack[atk][1]:
                    monster["HP"] -= (self.strength + self.attack[atk][0]) - monster["defense"]
                    print(f"vous utiliser {atk}  {monster_name} PV = {monster['HP']}")
                    monster_atk = monster["attack"]
                    if monster_atk <= self.defense and monster["HP"] > 0 :
                        print("votre defense est trop élevé l'attaque du monstre ne vous fait aucun dégats")
                    elif monster["HP"] > 0:
                        self.HP -= monster_atk + self.defense
                        print(f"le monstre vous inflige {monster_atk} de dommage, il vous reste {self.HP} PV")
                else:
                    print("vous ratez votre attaque")
                    monster_atk = monster["attack"]
                    if monster_atk <= self.defense:
                        print("votre defense est trop élevé l'attaque du monstre ne vous fait aucun dégats")

                    else:
                        self.HP =  self.HP - monster_atk + self.defense
                        print(f"le monstre vous inflige {monster_atk - self.defense} de dommage, il vous reste {self.HP} PV")
            if monster["HP"] <= 0 :
                self.XP += monster["XP"]
                monster["HP"] = hp_memory
                print (f"vous avez vaincu le {monster_name} ,vous avez gagné {monster['XP']}xp, vous obtenez {random.choice(reward)}")

            elif self.HP <= 0:
                print("LOOSER TU AS PERDU LOOOOOSER")

        elif self.inventory["PO"] >= monster["soudoyer"] and soudoyer == "oui":
            self.inventory["PO"] -= monster["soudoyer"]
            print("haha les bons comptes font les bons amis, ça va pour cette fois passe ton chemin, vous donner {} PO à {},\n il vous reste {} PO".format(monster["soudoyer"], monster_name, self.inventory["PO"]))



    def event(self):

        position = self.perform_move()
        

        if position in self.visited_positions:
            print("Vous êtes déjà passé par ici. Aucun événement en conséquence.")
            return
        else:
            self.visited_positions.add(position)



        if position == "feu de camp":
            self.HP += 20
            print("vous avez désormais {} HP".format(self.HP))

        elif position == "coffre":
            list_objet = ["potion defense", "potion force", "potion regen", "PO"]
            objet_win = random.choice(["potion_defense", "potion_force", "potion_regène", "PO"])

            if objet_win in self.inventory:
                self.inventory[objet_win] += 1
                print("bravo vous avez gagné {} votre inventaire est maintenant de {}".format(objet_win, self.inventory))
            else:
                self.inventory[objet_win] = 1
                print("bravo vous avez gagné {} votre inventaire est maintenant de {}".format(objet_win, self.inventory))
        elif position == "marchand":
            self.buy_merchant()
        elif position == "goblin":
            self.combat("gobelin")


        elif position == "ogre":
            self.combat("ogre")



        elif position == "dragon":
            self.combat("dragon")



        elif position == "Le Duc du bois":
            print("Vous voila arrivé au début de votre liberté mais avant ça il faudra la gagner. Le Duc du bois vous attend. ")
            self.combat("Le Duc du bois")

        elif position == "piège - 50pv":
            self.HP -= 50
            print("dommage vous vous êtes pris un piège - 50pv vos pv sont donc de {}".format(self.HP))

        elif position == "super potion":
            gain = random.choice(["potion defense", "potion force", "potion regen"])
            self.inventory[gain] += 1
            print("super vous avez gagné une super potion{}".format(gain))

        elif position == "voleur de divers":
            cle_aleatoire = random.choice(list(self.inventory.keys()))

            if self.inventory[cle_aleatoire] > 0: #va faire mois 10pv si l objet aleatoire est pas dans l invent
                self.inventory[cle_aleatoire] -= 1
                print("le voleur vous a pris {}".format(cle_aleatoire))
            else:
                self.HP -= 10
                print("votre inventaire est vide par conséquent tu perds 10 HP")

        elif position == "piège":
            self.HP -= 10
            print("vous etes tomber sur un piège par conséquent vous perdez 10pv ils sont maintenant {} de Pv".format(self.HP))

    def buy_merchant(self):
        print("1: Achat d'une potion de force \n 2: Achat d'une potion de regen \n 3: Achat d'une potion de defense \n 4: Rien n'acheter")
        choice = input()
        if choice == "1" and self.merchant_inventory["potion_force"] > 0:
            self.merchant_inventory["potion_force"] -= 1
            self.inventory["potion_force"] += 1
            print("Vous avez maintenant {} potion de force et {} PO".format(self.inventory["potion_force"], self.inventory["PO"]))
        elif choice == "2" and self.merchant_inventory["potion_regène"] > 0:
            self.merchant_inventory["potion_regène"] -= 1
            self.inventory["potion_regène"] += 1
            self.inventory["PO"] -= 20
            print("Vous avez maintenant {} potion de regen et {} PO".format(self.inventory["potion_regène"], self.inventory["PO"]))
        elif choice == "3" and self.merchant_inventory["potion_defense"] > 0:
            self.merchant_inventory["potion_defense"] -= 1
            self.inventory["potion_defense"] += 1
            print("Vous avez maintenant {} potion de defense et {} PO".format(self.inventory["potion_defense"], self.inventory["PO"]))
        elif choice == "4":
          print("Si mes articles sont guez tu peux dégager")
        else:
            print("Error")

    def level(self):
      if self.classe == "Guerrier":
        if self.XP == 0:
            print("Vous êtes niveau 1 avec force = {}, defense = {} et PV = {}".format(self.strength, self.defense, self.HP))

        elif self.XP >= 4:
            self.strength = 25
            self.defense = 25
            self.HP += 10

            print("Vous êtes niveau 2 avec force = {}, defense = {} et PV = {}".format(self.strength, self.defense, self.HP))

        elif self.XP >= 8:
          self.strength = 30
          self.defense = 30
          self.HP += 10

          self.attack["molotov 4"] = [60, 50]
          print("Vous êtes niveau 3 avec force = {}, defense = {} et PV = {}".format(self.strength,self.defense, self.HP))

        elif self.XP >= 16:
          self.strength = 35
          self.defense = 35
          self.HP += 10

          print("Vous êtes niveau 4 avec force = {}, defense = {} et PV = {}".format(self.strength,self.defense, self.HP))

        elif self.XP >= 32:
          self.strength = 40
          self.defense = 40
          self.HP += 10

          self.attack["Je suis le gardien de mon frère"] = [80, 25]
          print("Vous êtes niveau 5 avec force = {}, defense = {} et PV = {}".format(self.strength,self.defense, self.HP))

        elif self.XP >= 64:
          self.strength = 45
          self.defense = 45
          self.HP += 10

          print("Vous êtes niveau 6 avec force = {}, defense = {} et PV = {}".format(self.strength,self.defense, self.HP))

        elif self.XP >= 64:
          self.strength = 50
          self.defense = 50
          self.HP += 10

          print("Vous êtes niveau 7 avec force = {}, defense = {} et PV = {}".format(self.strength,self.defense, self.HP))

        elif self.classe == "Archer":
          if self.XP == 0:
              print("Vous êtes niveau 1 avec force = {}, defense = {} et PV = {}".format(self.strength, self.defense, self.HP))

          elif self.XP >= 4:
              self.strength = 30
              self.defense = 20
              self.HP += 10

              print("Vous êtes niveau 2 avec force = {}, defense = {} et PV = {}".format(self.strength, self.defense, self.HP))

          elif self.XP >= 8:
            self.strength = 35
            self.defense = 25
            self.HP += 10

            self.attack["MOLOTOV 4"] = [60, 50]
            print("Vous êtes niveau 3 avec force = {}, defense = {} et PV = {}".format(self.strength,self.defense, self.HP))

          elif self.XP >= 16:
            self.strength = 40
            self.defense = 30
            self.HP += 10

            print("Vous êtes niveau 4 avec force = {}, defense = {} et PV = {}".format(self.strength,self.defense, self.HP))

          elif self.XP >= 32:
            self.strength = 45
            self.defense = 35
            self.HP += 10

            self.attack["Je suis le gardien de mon frère"] = [80, 25]
            print("Vous êtes niveau 5 avec force = {}, defense = {} et PV = {}".format(self.strength,self.defense, self.HP))

          elif self.XP >= 64:
            self.strength = 50
            self.defense = 40
            self.HP += 10

            print("Vous êtes niveau 6 avec force = {}, defense = {} et PV = {}".format(self.strength,self.defense, self.HP))

          elif self.XP >= 64:
            self.strength = 55
            self.defense = 45
            self.HP += 10

            print("Vous êtes niveau 7 avec force = {}, defense = {} et PV = {}".format(self.strength,self.defense, self.HP))

          elif self.classe == "Tank":
            if self.XP == 0:
                print("Vous êtes niveau 1 avec force = {}, defense = {} et PV = {}".format(self.strength, self.defense, self.HP))

            elif self.XP >= 4:
                self.strength = 15
                self.defense = 25
                self.HP += 10

                print("Vous êtes niveau 2 avec force = {}, defense = {} et PV = {}".format(self.strength, self.defense, self.HP))

            elif self.XP >= 8:
              self.strength = 20
              self.defense = 30
              self.HP += 10

              self.attack["MOLOTOV 4"] = [60, 50]
              print("Vous êtes niveau 3 avec force = {}, defense = {} et PV = {}".format(self.strength,self.defense, self.HP))

            elif self.XP >= 16:
              self.strength = 25
              self.defense = 35
              self.HP += 10

              print("Vous êtes niveau 4 avec force = {}, defense = {} et PV = {}".format(self.strength,self.defense, self.HP))

            elif self.XP >= 32:
              self.strength = 30
              self.defense = 40
              self.HP += 10

              self.attack["je suis le gardien de mon frère"] = [80, 25]
              print("Vous êtes niveau 5 avec force = {}, defense = {} et PV = {}".format(self.strength,self.defense, self.HP))

            elif self.XP >= 64:
              self.strength = 35
              self.defense = 45
              self.HP += 10

              print("Vous êtes niveau 6 avec force = {}, defense = {} et PV = {}".format(self.strength,self.defense, self.HP))

            elif self.XP >= 64:
              self.strength = 40
              self.defense = 50
              self.HP += 10

              print("Vous êtes niveau 7 avec force = {}, defense = {} et PV = {}".format(self.strength,self.defense, self.HP))

    def save_and_quit(self):
        actual_state = {
            'strength': self.strength,
            'defense': self.defense,
            'HP': self.HP,
            'XP': self.XP,
            'x': self.x,
            'y': self.y,
            'inventory': self.inventory

        }
        save_game(actual_state)
        print("Le jeu a été sauvegardé.")

start()