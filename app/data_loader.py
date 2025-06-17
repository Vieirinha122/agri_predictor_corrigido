
import pandas as pd

# Funções de carregamento dos dados simulados
def load_ibge_data():
    data = {
        'Municipio': [
            'Chapecó', 'Ribeirão Preto', 'Petrolina', 'Londrina', 'Uberlândia',
            'Cascavel', 'São José do Rio Preto', 'Dourados', 'Juazeiro', 'Sinop'
        ],
        'Producao': [1000, 1500, 1200, 1100, 1300, 1600, 1700, 1400, 1250, 1350],
        'Ano': [2022] * 10
    }
    return pd.DataFrame(data)

def load_inmet_data():
    data = {
        'Municipio': [
            'Chapecó', 'Ribeirão Preto', 'Petrolina', 'Londrina', 'Uberlândia',
            'Cascavel', 'São José do Rio Preto', 'Dourados', 'Juazeiro', 'Sinop'
        ],
        'Precipitacao': [200, 180, 220, 210, 190, 170, 160, 230, 240, 185],
        'Temperatura': [25, 24, 26, 23, 22, 27, 28, 21, 20, 24],
        'Ano': [2022] * 10
    }
    return pd.DataFrame(data)
