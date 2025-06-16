import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from app import dashboard
from dash import ctx
import time

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
server = app.server  # Para hospedagem futura se quiser

# Estado de controle para saber se o usuário logou
login_success = False

app.layout = html.Div(id='main-content', children=[
    html.Div(id='login-area', children=[
        html.H2('Login'),
        dbc.Input(id='username', placeholder='Usuário', type='text', className='mb-2'),
        dbc.Input(id='password', placeholder='Senha', type='password', className='mb-2'),
        dbc.Button('Entrar', id='login-button', color='primary'),
        html.Div(id='login-message', className='mt-2')
    ]),
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
        # Retorna o spinner de loading
        loading_layout = html.Div([
            dbc.Spinner(color='primary', size='lg'),
            html.H4('Carregando, por favor aguarde...'),
            dcc.Interval(id='wait-interval', interval=5000, n_intervals=0, max_intervals=1)
        ], style={'textAlign': 'center', 'marginTop': '100px'})

        return '', loading_layout, dash.no_update
    else:
        return 'Usuário ou senha incorretos.', '', dash.no_update

# Callback para trocar para o dashboard depois de 5 segundos
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
    app.run_server(host='0.0.0.0', port=5000, debug=True)
