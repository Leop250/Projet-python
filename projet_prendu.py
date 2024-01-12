import random

class Pendu:
    difficulte = str(input("Choisissez la difficulté (simple, moyenne ou difficile): "))
    list_de_mots_4 = ["chat", "port", "code", "vent", "robe", "main", "bleu", "pied", "cafe", "joie"]
    list_de_mots_6 = ["python", "pomme", "orange", "soleil", "table", "maison", "ananas", "chaise", "fraise", "avion"]
    list_a_8 = ["ordinateur", "elephant", "champion", "aventure", "parapluie", "poussière", "ballon", "etoilee", "banquise", "melodie"]

    @classmethod
    def jouer(cls):
        if cls.difficulte == "simple":
            mots_choisi_S = random.choice(cls.list_de_mots_4)
            print("Vous avez un mot de", len(mots_choisi_S), "lettres.")
            print("J'ai choisi", mots_choisi_S)
            nb_vie = 10
            lettres_trouvees = 0
            lettre_deja_choisie = []
            affichage_mots = ["_"] * len(mots_choisi_S)

            while nb_vie != 0 and lettres_trouvees < len(mots_choisi_S):
                print("Lettres déjà choisies:", lettre_deja_choisie)
                lettre_choisie = input("Choisissez une lettre: ")

                if lettre_choisie in lettre_deja_choisie:
                    print("Vous avez déjà choisi cette lettre.")
                    continue

                lettre_deja_choisie.append(lettre_choisie)

                if lettre_choisie in mots_choisi_S:
                    print("\033[92mLa lettre", lettre_choisie, "est dedans.\033[0m")
                    for i, e in enumerate(mots_choisi_S):
                        if e == lettre_choisie:
                            affichage_mots[i] = lettre_choisie
                    print("Avancement du mot:", " ".join(affichage_mots))
                    lettres_trouvees += 1
                else:
                    print("La lettre", lettre_choisie, "n'est pas dans le mot.")
                    nb_vie -= 1

            if lettres_trouvees == len(mots_choisi_S):
                print("Bravo! Vous avez trouvé le mot:", mots_choisi_S)
            else:
                print("Dommage! Le mot était:", mots_choisi_S)
        if cls.difficulte == "moyenne":
            mots_choisi_S = random.choice(cls.list_de_mots_6)
            print("Vous avez un mot de", len(mots_choisi_S), "lettres.")
            print("J'ai choisi", mots_choisi_S)
            nb_vie = 10
            lettres_trouvees = 0
            lettre_deja_choisie = []
            affichage_mots = ["_"] * len(mots_choisi_S)

            while nb_vie != 0 and lettres_trouvees < len(mots_choisi_S):
                print("Lettres déjà choisies:", lettre_deja_choisie)
                lettre_choisie = input("Choisissez une lettre: ")

                if lettre_choisie in lettre_deja_choisie:
                    print("Vous avez déjà choisi cette lettre.")
                    continue

                lettre_deja_choisie.append(lettre_choisie)

                if lettre_choisie in mots_choisi_S:
                    print("\033[92mLa lettre", lettre_choisie, "est dedans.\033[0m")
                    for i, e in enumerate(mots_choisi_S):
                        if e == lettre_choisie:
                            affichage_mots[i] = lettre_choisie
                    print("Avancement du mot:", " ".join(affichage_mots))
                    lettres_trouvees += 1
                else:
                    print("La lettre", lettre_choisie, "n'est pas dans le mot.")
                    nb_vie -= 1

            if lettres_trouvees == len(mots_choisi_S):
                print("Bravo! Vous avez trouvé le mot:", mots_choisi_S)
            else:
                print("Dommage! Le mot était:", mots_choisi_S)

        if cls.difficulte == "difficile":
            mots_choisi_S = random.choice(cls.list_a_8)
            print("Vous avez un mot de", len(mots_choisi_S), "lettres.")
            print("J'ai choisi", mots_choisi_S)
            nb_vie = 10
            lettres_trouvees = 0
            lettre_deja_choisie = []
            affichage_mots = ["_"] * len(mots_choisi_S)

            while nb_vie != 0 and lettres_trouvees < len(mots_choisi_S):
                print("Lettres déjà choisies:", lettre_deja_choisie)
                lettre_choisie = input("Choisissez une lettre: ")

                if lettre_choisie in lettre_deja_choisie:
                    print("Vous avez déjà choisi cette lettre.")
                    continue

                lettre_deja_choisie.append(lettre_choisie)

                if lettre_choisie in mots_choisi_S:
                    print("\033[92mLa lettre", lettre_choisie, "est dedans.\033[0m")
                    for i, e in enumerate(mots_choisi_S):
                        if e == lettre_choisie:
                            affichage_mots[i] = lettre_choisie
                    print("Avancement du mot:", " ".join(affichage_mots))
                    lettres_trouvees += 1
                else:
                    print("La lettre", lettre_choisie, "n'est pas dans le mot.")
                    nb_vie -= 1

            if lettres_trouvees == len(mots_choisi_S):
                print("Bravo! Vous avez trouvé le mot:", mots_choisi_S)
            else:
                print("Dommage! Le mot était:", mots_choisi_S)
    

            

if __name__ == "__main__":
    Pendu.jouer()
