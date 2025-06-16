
from app.data_loader import load_ibge_data, load_inmet_data
from app.model import train_model, prepare_features
import pandas as pd
import os

if not os.path.exists('data'):
    os.makedirs('data')

ibge_df = load_ibge_data()
inmet_df = load_inmet_data()
X, y = prepare_features(ibge_df, inmet_df)
model = train_model(X, y)
predictions = model.predict(X)

result_df = pd.DataFrame({
    'Municipio': ibge_df['Municipio'],
    'Produtividade_Prevista': predictions
})
result_df.to_csv('data/predictions.csv', index=False)
print('Predições salvas em data/predictions.csv')
