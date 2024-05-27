import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

data = pd.read_csv("data_dekuple.csv", encoding='latin1')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Tableau de bord interactif"),

    # Ajouter des graphiques interactifs
    dcc.Graph(
        id='example-graph',
        figure=px.scatter(data, x='x_column', y='y_column', color='color_column', size='size_column', hover_data=['additional_column'])
    ),

    # Ajouter d'autres composants interactifs
    dcc.Dropdown(
        id='dropdown-column',
        options=[{'label': col, 'value': col} for col in data.columns],
        value=data.columns[0]
    ),
    html.Div(id='output-column'),

    # Ajouter d'autres composants selon vos besoins
])

# Définir des callbacks pour rendre l'application interactive
@app.callback(
    dash.dependencies.Output('output-column', 'children'),
    [dash.dependencies.Input('dropdown-column', 'value')]
)
def update_output(value):
    return f"Vous avez sélectionné la colonne : {value}"

# Lancer l'application
if __name__ == '__main__':
    app.run_server(debug=True)
