from dash import dcc, html
import pandas as pd
import plotly.express as px
import os

if os.path.exists('data/predictions.csv'):
    df = pd.read_csv('data/predictions.csv')

    fig = px.bar(df, x='Municipio', y='Produtividade_Prevista', title='Produtividade Agrícola Prevista')

    layout = html.Div([
        html.H1('Dashboard de Previsão Agrícola'),
        dcc.Graph(figure=fig)
    ])
else:
    layout = html.Div([
        html.H1('Erro: CSV de predições não encontrado'),
        html.P('Por favor, rode primeiro: python -m app.predict')
    ])
