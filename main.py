# Importaciones
from fastapi import FastAPI
import pandas as pd

# Datasets para utilizar
df_items_developer = pd.read_parquet('C:\\Users\\cquir\\OneDrive\\Escritorio\\Data Science SH\\Proyecto Individual 1\\bases de datos\\df_items_developer_unido.parquet')
df_reviews = pd.read_parquet('C:\\Users\\cquir\\OneDrive\\Escritorio\\Data Science SH\\Proyecto Individual 1\\bases de datos\\dfreviews_unido.parquet')
df_gastos_items = pd.read_parquet('C:\\Users\\cquir\\OneDrive\\Escritorio\\Data Science SH\\Proyecto Individual 1\\bases de datos\\df_gastos_items_unido.parquet')
dfdesarrolladores_recomendados = pd.read_parquet(r"C:\\Users\\cquir\\OneDrive\\Escritorio\\Data Science SH\\Proyecto Individual 1\\bases de datos\\dfdesarrolladores_recomendados_unido.parquet")
df_playtime_forever = pd.read_parquet('C:\\Users\\cquir\\OneDrive\\Escritorio\\Data Science SH\\Proyecto Individual 1\\bases de datos\\df_playtime_forever_unido.parquet')

