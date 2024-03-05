# IMPORTACIONES
from fastapi import FastAPI
import pandas as pd
import uvicorn 
from mangum import Mangum



# DATASETS
df_items_developer = pd.read_parquet('C:\\Users\\cquir\\OneDrive\\Escritorio\\Data Science SH\\Proyecto Individual 1\\bases de datos\\df_items_developer_unido.parquet')
df_reviews = pd.read_parquet('C:\\Users\\cquir\\OneDrive\\Escritorio\\Data Science SH\\Proyecto Individual 1\\bases de datos\\dfreviews_unido.parquet')
df_gastos_items = pd.read_parquet('C:\\Users\\cquir\\OneDrive\\Escritorio\\Data Science SH\\Proyecto Individual 1\\bases de datos\\df_gastos_items_unido.parquet')
dfdesarrolladores_recomendados = pd.read_parquet('C:\\Users\\cquir\\OneDrive\\Escritorio\\Data Science SH\\Proyecto Individual 1\\bases de datos\\dfdesarrolladores_recomendados_unido.parquet')
df_playtime_forever = pd.read_parquet('C:\\Users\\cquir\\OneDrive\\Escritorio\\Data Science SH\\Proyecto Individual 1\\bases de datos\\df_playtime_forever_unido.parquet')



# Iniciamos aplicacion
app = FastAPI()

handler = Mangum(app)



# FUNCION DEVELOPER
@app.get("/developer/{desarrollador}")
def developer(desarrollador:str):
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
    return result_dict




#FUNCION USERDATA
@app.get("/userdata/{user_id}")
def userdata(user_id:str):
    '''
    Debe devolver la cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews_recommend y cantidad de items consumidos.
    '''
    # Filtramos por usuario
    usuario = df_reviews[df_reviews['user_id'] == user_id]
    # Calculamos cantidad de dinero gastado por ese usuario
    cantidad_dinero = df_gastos_items[df_gastos_items['user_id'] == user_id]['price'].iloc[0]
    # Buscamos la cantidad de items para el usuario
    count_items = df_gastos_items[df_gastos_items['user_id'] == user_id]['items_count'].iloc[0]
    # Total de recomendaciones del usuario
    total_recomendaciones = usuario['reviews_recommend'].sum()
    # Total de reviews por todos los usuarios
    total_reviews = len(df_reviews['user_id'].unique())
    # porcentaje de recomendaciones 
    porcentaje_recomendaciones = (total_recomendaciones/total_reviews)*100
    
    #algunos valores pueden ser nulo, por lo que la api no los reconoce y no corre las instrucciones, por lo que agregamos un condicional para count_items
    count_items = count_items if not pd.isnull(count_items) else 0
      
    diccionario = {'usuario': user_id,
                    'cantidad_dinero': cantidad_dinero,
                    'porcentaje_recomendacion': round(porcentaje_recomendaciones,2),
                    'cantidad_de_items': int(count_items)}  
    return diccionario





#FUNCION USERFORGENRE
@app.get("/UserForGenre/{genre}")
def UserForGenre(genre):
    '''Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.'''
    # Filtra el dataframe por el género de interés
    data_por_genero = df_playtime_forever[df_playtime_forever['genres'] == genre]
    # Agrupa el dataframe y suma la cantidad de horas jugadas
    top_user = data_por_genero.groupby('user_id')['playtime_horas'].sum().reset_index().iloc[0].to_dict()
    
    return top_user





# FUNCION BESTDEVELOPERYEAR
@app.get("/BestDeveloperYear/{year}")
def BestDeveloperYear(year: int): 
    '''Devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado (reviews.recommend = True y comentarios positivos)'''
    # Filtrar solo valores numéricos y convertirlos a entero
    df_filtrado = dfdesarrolladores_recomendados[dfdesarrolladores_recomendados['anio_lanzamiento'].apply(lambda x: x.isdigit())]
    df_filtrado['anio_lanzamiento'] = df_filtrado['anio_lanzamiento'].astype(int) #Con esto filtro solo por valores numericos para que fastapi los pueda leer

    año_seleccionado = df_filtrado[df_filtrado['anio_lanzamiento'] == year]
    # juegos recomendados con sentimiento positivo
    recomendados_positivos = año_seleccionado[(año_seleccionado['reviews_recommend'] == True) & (año_seleccionado['sentiment_analysis'] == 2)]

    agrupado = recomendados_positivos.groupby('developer')[['reviews_recommend', 'sentiment_analysis']].count()

    agrupado['suma'] = agrupado['reviews_recommend'] + agrupado['sentiment_analysis']

    top3 = agrupado['suma'].sort_values(ascending=False).nlargest(3).to_dict()

    return top3





# FUNCION DEVELOPER_REVIEWS_ANALYSIS 
@app.get("/developerreviewsanalysis/{desarrollador}")
def developerreviewsanalysis(desarrollador: str): 
    '''Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.'''
    # filtro por desarrollador
    filtro_desarrollador = dfdesarrolladores_recomendados[dfdesarrolladores_recomendados['developer'] == desarrollador]
    
    sentimientos_positivos = filtro_desarrollador[filtro_desarrollador['sentiment_analysis'] == 2]['sentiment_analysis'].count()
    
    sentimientos_negativos = filtro_desarrollador[filtro_desarrollador['sentiment_analysis'] == 0]['sentiment_analysis'].count()

    diccionario = {'Desarrollador': desarrollador,
                   'Positivos': int(sentimientos_positivos),
                   'Negativos': int(sentimientos_negativos)}

    return diccionario



