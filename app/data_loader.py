
import pandas as pd

def load_ibge_data():
    data = {
        'Municipio': ['Município A', 'Município B', 'Município C'],
        'Producao': [1000, 1500, 1200],
        'Ano': [2022, 2022, 2022]
    }
    return pd.DataFrame(data)

def load_inmet_data():
    data = {
        'Municipio': ['Município A', 'Município B', 'Município C'],
        'Precipitacao': [200, 180, 220],
        'Temperatura': [25, 24, 26],
        'Ano': [2022, 2022, 2022]
    }
    return pd.DataFrame(data)
