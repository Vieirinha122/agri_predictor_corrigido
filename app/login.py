import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from app import dashboard

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG], suppress_callback_exceptions=True)  # Tema escuro bonito
server = app.server

# Layout do Login
app.layout = html.Div(id='main-content', children=[
    html.Div(id='login-area', children=[
        html.Div([
            html.H2('🌾 Bem-vindo ao Preditor Agrícola', style={'textAlign': 'center', 'marginBottom': '20px', 'color': '#00FFAA'}),
            dbc.Input(id='username', placeholder='Usuário', type='text', className='mb-3', style={'backgroundColor': '#1c1c1c', 'color': 'white'}),
            dbc.Input(id='password', placeholder='Senha', type='password', className='mb-3', style={'backgroundColor': '#1c1c1c', 'color': 'white'}),
            dbc.Button('Entrar', id='login-button', color='success', className='w-100'),
            html.Div(id='login-message', className='mt-3', style={'color': 'red', 'textAlign': 'center'})
        ], style={
            'backgroundColor': '#2a2a2a',
            'padding': '30px',
            'borderRadius': '10px',
            'boxShadow': '0px 0px 20px #00FFAA'
        })
    ], style={
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center',
        'height': '100vh'
    }),

    html.Div(id='loading-area')
])

@app.callback(
    Output('login-message', 'children'),
    Output('loading-area', 'children'),
    Output('main-content', 'children', allow_duplicate=True),
    Input('login-button', 'n_clicks'),
    State('username', 'value'),
    State('password', 'value'),
    prevent_initial_call=True
)
def check_login(n_clicks, username, password):
    if username == 'adm' and password == 'adm123':
        loading_layout = html.Div([
            dbc.Spinner(color='success', size='lg', fullscreen=True, type='grow'),
            html.H4('🔄 Carregando, por favor aguarde...', style={'color': 'white', 'marginTop': '20px'}),
            dcc.Interval(id='wait-interval', interval=5000, n_intervals=0, max_intervals=1)
        ], style={
            'textAlign': 'center',
            'paddingTop': '200px',
            'backgroundColor': '#121212',
            'height': '100vh'
        })

        return '', loading_layout, dash.no_update
    else:
        return '❌ Usuário ou senha incorretos.', '', dash.no_update

# Após 5 segundos, mostra o dashboard
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
