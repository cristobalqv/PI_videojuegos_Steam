# IMPORTACIONES
from fastapi import FastAPI
import pandas as pd
import uvicorn 

# DATASETS
df_items_developer = pd.read_parquet('C:\\Users\\cquir\\OneDrive\\Escritorio\\Data Science SH\\Proyecto Individual 1\\bases de datos\\df_items_developer_unido.parquet')
df_reviews = pd.read_parquet('C:\\Users\\cquir\\OneDrive\\Escritorio\\Data Science SH\\Proyecto Individual 1\\bases de datos\\dfreviews_unido.parquet')
df_gastos_items = pd.read_parquet('C:\\Users\\cquir\\OneDrive\\Escritorio\\Data Science SH\\Proyecto Individual 1\\bases de datos\\df_gastos_items_unido.parquet')
dfdesarrolladores_recomendados = pd.read_parquet('C:\\Users\\cquir\\OneDrive\\Escritorio\\Data Science SH\\Proyecto Individual 1\\bases de datos\\dfdesarrolladores_recomendados_unido.parquet')
df_playtime_forever = pd.read_parquet('C:\\Users\\cquir\\OneDrive\\Escritorio\\Data Science SH\\Proyecto Individual 1\\bases de datos\\df_playtime_forever_unido.parquet')

# Iniciamos aplicacion
app = FastAPI()


if __name__=="__main__":
    uvicorn.run("main:app", port=8000)



@app.get("/developer/{dev}")
def developer(desarrollador):
    '''
    Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.
    '''
    empresa_desarrolladora = df_items_developer[df_items_developer['developer'] == desarrollador]
    # Cantidad de items por año
    items_por_año = empresa_desarrolladora.groupby('anio_lanzamiento')['item_id'].count()
    # Cantidad de elementos gratis por año
    contenido_free = empresa_desarrolladora[empresa_desarrolladora['price']==0.00].groupby('anio_lanzamiento')['item_id'].count()
    # Porcentaje items gratis por año
    porcentaje_gratis = ((contenido_free/items_por_año)*100).fillna(0).astype(int)

    result_dict = {'Cantidad anual': items_por_año.to_dict(),
                   'Porcentaje de juegos que son gratis': porcentaje_gratis.to_dict()}
    
    tabla = pd.DataFrame(result_dict)
    
    return tabla



