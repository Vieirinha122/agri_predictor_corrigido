import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from app import dashboard

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG], suppress_callback_exceptions=True)
server = app.server

# Estilos reutilizáveis
colors = {
    'background': '#1a1a1a',
    'card': '#2a2a2a',
    'primary': '#00FFAA',
    'danger': '#FF4D4D',
    'text': '#EAEAEA'
}

input_style = {
    'backgroundColor': '#1c1c1c',
    'color': 'white',
    'border': '1px solid #00FFAA',
    'fontSize': '16px'
}

button_style = {
    'backgroundColor': colors['text'],
    'color': 'black',
    'fontWeight': 'bold',
    'transition': '0.3s',
    'fontSize': '16px'
}

app.layout = html.Div(id='main-content', children=[
    html.Div(id='login-area', children=[
        html.Div([
            html.H2('🌱 Preditor Agrícola', style={
                'textAlign': 'center',
                'marginBottom': '30px',
                'color': colors['primary'],
                'fontWeight': 'bold'
            }),
            dbc.Input(id='username', placeholder='Usuário', type='text',
                      className='mb-3', style=input_style),
            dbc.Input(id='password', placeholder='Senha', type='password',
                      className='mb-3', style=input_style),
            dbc.Button('Entrar', id='login-button', color='success', className='w-100', style=button_style),
            html.Div(id='login-message', className='mt-3', style={
                'color': colors['danger'],
                'textAlign': 'center',
                'fontWeight': 'bold',
                'fontSize': '14px'
            })
        ], style={
            'backgroundColor': colors['card'],
            'padding': '40px',
            'borderRadius': '12px',
            'boxShadow': '0 0 25px rgba(0,255,170,0.2)',
            'width': '100%',
            'maxWidth': '400px'
        })
    ], style={
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center',
        'height': '100vh',
        'backgroundColor': colors['background'],
        'padding': '10px'
    }),
    html.Div(id='loading-area')
])

# Callback de login
@app.callback(
    Output('login-message', 'children'),
    Output('loading-area', 'children'),
    Input('login-button', 'n_clicks'),
    State('username', 'value'),
    State('password', 'value'),
    prevent_initial_call=True
)
def check_login(n_clicks, username, password):
    if username == 'adm' and password == 'adm123':
        loading_layout = html.Div([
            dbc.Spinner(color='success', size='lg', fullscreen=True, type='grow'),
            html.H4('🔄 Carregando, por favor aguarde...', style={
                'color': colors['text'],
                'marginTop': '20px'
            }),
            dcc.Interval(id='wait-interval', interval=5000, n_intervals=0, max_intervals=1)
        ], style={
            'textAlign': 'center',
            'paddingTop': '200px',
            'backgroundColor': colors['background'],
            'height': '100vh'
        })

        return '', loading_layout
    else:
        return '❌ Usuário ou senha incorretos.', ''

# Callback para redirecionar ao dashboard
@app.callback(
    Output('main-content', 'children', allow_duplicate=True),
    Input('wait-interval', 'n_intervals'),
    prevent_initial_call=True
)
def show_dashboard(n_intervals):
    if n_intervals:
        return dashboard.layout
    raise PreventUpdate

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
