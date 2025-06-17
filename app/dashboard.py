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

    # Simula coordenadas para o mapa (não serão mais usadas)
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

    # Gráfico principal
    fig_bar = px.bar(df, x='Municipio', y='Produtividade_Prevista', title='Produtividade Agrícola Prevista',
                     color_discrete_sequence=[colors['primary']])
    fig_bar.update_layout(paper_bgcolor=colors['card'], plot_bgcolor=colors['card'], font_color=colors['text'])

    # Clima
    fig_clima = px.scatter(df, x='Municipio', y='Produtividade_Prevista', size='Produtividade_Prevista',
                           title='Análise Climática por Município', color_discrete_sequence=[colors['primary']])
    fig_clima.update_layout(paper_bgcolor=colors['card'], plot_bgcolor=colors['card'], font_color=colors['text'])

    # Municípios com menor produtividade (alertas)
    df_sorted = df.sort_values(by='Produtividade_Prevista')
    alertas = df_sorted.head(3)['Municipio'].tolist()

    # Municípios com maior produtividade (relatório)
    destaque = df_sorted.tail(3).sort_values(by='Produtividade_Prevista', ascending=False)['Municipio'].tolist()

    # Layout do Dashboard
    layout = html.Div([
        html.H2('📊 Dashboard de Previsão Agrícola', style={'textAlign': 'center', 'color': colors['primary'], 'marginBottom': '30px'}),

        html.Div([
            html.Div([
                html.H4("🚨 Alertas de Risco Climático", style={'color': colors['danger']}),
                html.Ul([
                    html.Li(f"Baixa produtividade em {alertas[0]}"),
                    html.Li(f"Baixa produtividade em {alertas[1]}"),
                    html.Li(f"Baixa produtividade em {alertas[2]}")
                ], style={'color': colors['text'], 'paddingLeft': '20px'})
            ], style={'backgroundColor': colors['card'], 'padding': '20px', 'borderRadius': '10px', 'width': '45%'}),

            html.Div([
                html.H4("📈 Destaques de Produtividade 2025", style={'color': colors['primary']}),
                html.P(f"{destaque[0]} lidera com alta produtividade prevista."),
                html.P(f"{destaque[1]} e {destaque[2]} também mostram forte desempenho."),
                html.P("Indicativo de investimentos bem-sucedidos em tecnologia e manejo.")
            ], style={'backgroundColor': colors['card'], 'padding': '20px', 'borderRadius': '10px', 'width': '45%'})
        ], style={'display': 'flex', 'gap': '20px', 'justifyContent': 'center', 'marginBottom': '40px'}),

        html.Div([
            dcc.Tabs([
                dcc.Tab(label='Gráfico de Barras', children=[
                    dcc.Graph(figure=fig_bar)
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
