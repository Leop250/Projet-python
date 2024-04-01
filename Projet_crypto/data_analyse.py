import pandas as pd

def perform_analysis(df):
    result = ""

    # Calculations for data analysis
    missing_values = df.isna().sum()
    moyenne = df.mean()
    max_values = df.max()
    min_values = df.min()
    var_values = df.var()
    ecart_type = df.std()

    # Add analysis results to the result string
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

    return result