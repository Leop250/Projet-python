import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas



df = pd.read_csv("nerveflux.csv", sep=";", decimal=",")
dataframe_df =pd.DataFrame(df)

print(dataframe_df)


def save_to_pdf(content, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    y_coordinate = 750  # Définir la coordonnée Y de départ pour l'affichage du contenu
    for line in content.split('\n'):
        if y_coordinate < 30:  # Si la position Y devient trop basse, ajoutez une nouvelle page
            c.showPage()
            c.setFont("Helvetica", 12)
            y_coordinate = 750
        c.drawString(100, y_coordinate, line)
        y_coordinate -= 15  # Déplacer la coordonnée Y vers le bas pour afficher la prochaine ligne
    c.save()
result = ""

# je calcule le nombre de valeurs manquante par colones
missing_values = df.isna().sum()
print("Nombre de valeurs manquantes par colonne :")
print(missing_values)

#face au resultat  precedent, on decouvre que il y a pas de donnée manquante par colones donc pas beosins de les traiter

# Je calcule le nombre de lignes dans le DataFrame
nombre_de_lignes = df.shape[0]
print("Nombre de lignes dans le dataset :", nombre_de_lignes)

# je calcul la moynenees des valeurs par colones
moyenne = dataframe_df.mean()
print("la moyennes des valeurs par colones est:" )
print(moyenne)

#je calcule  la valeure max pour chaque colones

max_values = dataframe_df.max()
print("\nLa valeur Maximum pour chaque colonnes est: \n")
print(max_values)

#Je calcul la valeur minimun pour chaquez  colones 
min_values = dataframe_df.min()
print("La valeur mininum pour chaque colones est:")
print(min_values)

# je calcul la varience pour chaque colones
var_values = dataframe_df.var()
print("la varaiance pour chaque colones est: ")
print(var_values)

# je calcul l'ecart type pour chaque colones
ecart_type= dataframe_df.std()
print ("L'echantillon d'ecart type pour chaque colonnes est:\n")
print (ecart_type)


# je cree un induce temporel
compteur = list(range(1, 354))  
df['compteur'] = compteur
print(df)



# Ajouter les résultats d'analyse avec Pandas
result += "Nombre de valeurs manquantes par colonne :\n"
result += missing_values.to_string() + "\n\n"

result += "Moyennes des valeurs par colonne :\n"
result += moyenne.to_string() + "\n\n"

result += "Valeur maximale pour chaque colonne :\n"
result += max_values.to_string() + "\n\n"

result += "Valeur minimale pour chaque colonne :\n"
result += min_values.to_string() + "\n\n"

result += "Variance pour chaque colonne :\n"
result += var_values.to_string() + "\n\n"

result += "Écart type pour chaque colonne :\n"
result += ecart_type.to_string() + "\n\n"

# Ajouter d'autres résultats d'analyse si nécessaire

# Enregistrer dans le PDF
save_to_pdf(result, "resultat_analyse_python.pdf")
