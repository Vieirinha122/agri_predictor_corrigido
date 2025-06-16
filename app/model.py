
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np

def train_model(X, y):
    model = RandomForestRegressor()
    model.fit(X, y)
    return model

def prepare_features(ibge_df, inmet_df):
    df = pd.merge(ibge_df, inmet_df, on=['Municipio', 'Ano'])
    X = df[['Producao', 'Precipitacao', 'Temperatura']]
    y = np.random.randint(1000, 5000, size=len(X))
    return X, y
