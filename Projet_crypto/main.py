import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def effectuer_analyse(df):
    result = ""

    # Calculs pour l'analyse des données
    valeurs_manquantes = df.isna().sum()
    moyenne = df.mean()
    valeurs_max = df.max()
    valeurs_min = df.min()
    variance = df.var()
    ecart_type = df.std()

    # Ajouter les résultats de l'analyse à la chaîne de résultats
    result += "Nombre de valeurs manquantes par colonne :\n"
    result += valeurs_manquantes.to_string() + "\n\n"

    result += "Moyennes des valeurs par colonne :\n"
    result += moyenne.to_string() + "\n\n"

    result += "Valeur maximale pour chaque colonne :\n"
    result += valeurs_max.to_string() + "\n\n"

    result += "Valeur minimale pour chaque colonne :\n"
    result += valeurs_min.to_string() + "\n\n"

    result += "Variance pour chaque colonne :\n"
    result += variance.to_string() + "\n\n"

    result += "Écart type pour chaque colonne :\n"
    result += ecart_type.to_string() + "\n\n"

    return result

def sauvegarder_resultats_en_pdf(analysis_content, filename):
    with PdfPages(filename) as pdf:
        fig = plt.figure(figsize=(8, 11)) # Format de page vertical
        plt.text(0.1, 0.5, analysis_content, verticalalignment='center', fontsize=10)
        plt.axis('off')
        pdf.savefig(fig)
        plt.close()

def sauvegarder_graphique_en_pdf(predictions, y_test, filename):
    with PdfPages(filename) as pdf:
        plt.figure(figsize=(8, 6))
        plt.scatter(y_test, predictions, color='blue')
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--', color='red', linewidth=2)
        plt.xlabel('Vraies valeurs')
        plt.ylabel('Prédictions')
        plt.title('Prédictions par rapport aux vraies valeurs')
        pdf.savefig()
        plt.close()

if __name__ == "__main__":
    df = pd.read_csv("nerveflux.csv", sep=";", decimal=",")

    resultat_analyse = effectuer_analyse(df)
    sauvegarder_resultats_en_pdf(resultat_analyse, "resultat_analyse.pdf")

    X = df[['timeOpen', 'timeClose', 'timeHigh', 'timeLow', 'priceOpen', 'priceHigh', 'priceLow', 'priceClose']]
    y = df['volume']  

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    modele = LinearRegression()
    modele.fit(X_train, y_train)

    predictions = modele.predict(X_test)

    rmse = mean_squared_error(y_test, predictions, squared=False)

    print("RMSE:", rmse)
    print("Prédictions:", predictions)

    print("Coefficients du modèle :")
    for i, coef in enumerate(modele.coef_):
        print(f"Coefficient {i+1}: {coef}")

    sauvegarder_graphique_en_pdf(predictions, y_test, "graphique_predictions.pdf")
