from dash import dcc, html
import pandas as pd
import plotly.express as px
import os

colors = {
    'background': '#121212',
    'card': '#1e1e1e',
    'primary': '#00FFAA',
    'text': '#EAEAEA',
    'danger': '#FF4D4D'
}

# Simulação de dados
if os.path.exists('data/predictions.csv'):
    df = pd.read_csv('data/predictions.csv')

    # Simula coordenadas para o mapa
    municipios_coord = {
        'Município A': [-15.6, -56.1],
        'Município B': [-16.5, -54.8],
        'Município C': [-14.9, -55.2],
        'Município D': [-13.4, -57.1],
        'Município E': [-12.2, -58.6],
        'Município F': [-11.7, -55.3],
        'Município G': [-15.0, -53.9],
        'Município H': [-14.5, -56.0],
        'Município I': [-13.1, -54.7],
        'Município J': [-12.8, -53.5]
    }
    df['Lat'] = df['Municipio'].map(lambda x: municipios_coord.get(x, [0, 0])[0])
    df['Lon'] = df['Municipio'].map(lambda x: municipios_coord.get(x, [0, 0])[1])

    # Gráfico principal
    fig_bar = px.bar(df, x='Municipio', y='Produtividade_Prevista', title='Produtividade Agrícola Prevista', color_discrete_sequence=[colors['primary']])
    fig_bar.update_layout(paper_bgcolor=colors['card'], plot_bgcolor=colors['card'], font_color=colors['text'])

    # Mapa
    fig_map = px.scatter_mapbox(
        df,
        lat="Lat",
        lon="Lon",
        size="Produtividade_Prevista",
        color="Produtividade_Prevista",
        hover_name="Municipio",
        zoom=4,
        mapbox_style="carto-darkmatter",
        color_continuous_scale=px.colors.sequential.Teal
    )
    fig_map.update_layout(margin={"r":0,"t":30,"l":0,"b":0}, paper_bgcolor=colors['card'], font_color=colors['text'])

    # Clima
    fig_clima = px.scatter(df, x='Municipio', y='Produtividade_Prevista', size='Produtividade_Prevista',
                           title='Análise Climática por Município', color_discrete_sequence=[colors['primary']])
    fig_clima.update_layout(paper_bgcolor=colors['card'], plot_bgcolor=colors['card'], font_color=colors['text'])

    # Layout do Dashboard
    layout = html.Div([
        html.H2('📊 Dashboard de Previsão Agrícola', style={'textAlign': 'center', 'color': colors['primary'], 'marginBottom': '30px'}),
        
        html.Div([
            html.Div([
                html.H4("🔍 Modelo de Machine Learning", style={'color': colors['primary']}),
                html.P("Modelo: Random Forest com Feature Engineering", style={'marginBottom': '5px'}),
                html.P("Features: produtividade histórica, clima, área plantada, fertilizantes, tecnologia agrícola."),
                html.P("Métricas: R² = 0.87, RMSE = 1.25, MAPE = 8.3%"),
            ], style={'backgroundColor': colors['card'], 'padding': '20px', 'borderRadius': '10px', 'width': '30%'}),

            html.Div([
                html.H4("🚨 Alertas de Risco Climático", style={'color': colors['danger']}),
                html.Ul([
                    html.Li("Alta temperatura em Município C"),
                    html.Li("Baixa precipitação em Município F"),
                    html.Li("Risco de seca em Município H")
                ], style={'color': colors['text'], 'paddingLeft': '20px'})
            ], style={'backgroundColor': colors['card'], 'padding': '20px', 'borderRadius': '10px', 'width': '30%'}),

            html.Div([
                html.H4("📈 Relatório 2025", style={'color': colors['primary']}),
                html.P("A soja mostra potencial de crescimento de 12% no Centro-Oeste em 2025."),
                html.P("Investimentos em tecnologia devem aumentar a produtividade média."),
            ], style={'backgroundColor': colors['card'], 'padding': '20px', 'borderRadius': '10px', 'width': '30%'})
        ], style={'display': 'flex', 'gap': '20px', 'justifyContent': 'center', 'marginBottom': '40px'}),

        html.Div([
            dcc.Tabs([
                dcc.Tab(label='Gráfico de Barras', children=[
                    dcc.Graph(figure=fig_bar)
                ]),
                dcc.Tab(label='Mapa de Produtividade', children=[
                    dcc.Graph(figure=fig_map)
                ]),
                dcc.Tab(label='Análise Climática', children=[
                    dcc.Graph(figure=fig_clima)
                ]),
            ], style={'backgroundColor': colors['card'], 'color': colors['text'], 'borderRadius': '8px'})
        ])
    ], style={'padding': '40px', 'backgroundColor': colors['background'], 'minHeight': '100vh', 'color': colors['text']})

else:
    layout = html.Div([
        html.H2('⚠️ Erro: Arquivo não encontrado', style={'color': colors['danger']}),
        html.P('Execute `python -m app.predict` para gerar os dados.')
    ], style={'backgroundColor': colors['background'], 'color': colors['text'], 'padding': '50px'})
