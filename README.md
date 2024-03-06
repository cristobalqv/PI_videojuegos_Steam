# Proyecto Individual "Videojuegos Steam"

## INTRODUCCIÓN
El objetivo de este proyecto consiste en situarnos en el rol de un *MLOps Engineer* y poder crear un sistema de recomendación de videojuegos basado en un conjunto de datos predefinidos de la plataforma Steam. Estas tareas y procedimientos están enfocadas principalmente en la Extracción, Transformación y Carga de datos (ETL), análisis exploratorio de datos (EDA), junto con la epxloración y entrenamiento de un modelo de Machine Learning. Finaliza con el deployment de los datos en FastAPI y renderización en Render para su posterior uso en los entornos productivos

## PROCEDIMIENTO
#### *TRANSFORMACIÓN Y LIMPIEZA DE DATOS (ETL)*
Se aplicaron técnicas de Extracción, Transformación y Carga (ETL) para procesar y limpiar los 3 conjuntos de datos. 

Archivos: 
- [1a ETL games.ipynb](https://github.com/cristobalqv/PI_videojuegos_Steam/blob/main/JupyterNotebooks/1a%20ETL%20games.ipynb "1a ETL games.ipynb")
- [1b ETL reviews.ipynb](https://github.com/cristobalqv/PI_videojuegos_Steam/blob/main/JupyterNotebooks/1b%20ETL%20reviews.ipynb "1b ETL reviews.ipynb")
- [1c ETL items.ipynb](https://github.com/cristobalqv/PI_videojuegos_Steam/blob/main/JupyterNotebooks/1c%20ETL%20items.ipynb "1c ETL items.ipynb")


#### *DESARROLLO DE API*
Antes de crear los endpoints solicitados, se prepararon los datos para las consultas en la API, en la que se incluyó principalmente un análisis de sentimientos de las reviews de los usuarios mediante NLP:

Archivo: 
- [2 datos para consulta.ipynb](https://github.com/cristobalqv/PI_videojuegos_Steam/blob/main/JupyterNotebooks/2%20datos%20para%20consulta.ipynb "2 datos para consulta.ipynb")

Se crearon las siguientes funciones y se utilizó el framework FastAPI:

- developer: Función que devuelve la cantidad de items y porcentaje de contenido Free por año según la empresa desarrolladora

- userdata: Función que devuelve la cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews_recommend y cantidad de items consumidos

- UserForGenre: Función que devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.

- best_developer_year: Función que devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado (reviews.recommend=True y comentarios positivos)

- developer_reviews_analysis: Función que devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.

Archivo: 
- [3 funciones API.ipynb](https://github.com/cristobalqv/PI_videojuegos_Steam/blob/main/JupyterNotebooks/3%20funciones%20API.ipynb "3 funciones API.ipynb")


#### *ANÁLISIS EXPLORATORIO DE DATOS (EDA)*
Se realizó el Análisis Exploratorio de Dator a los tres conjuntos de datos sometidos a ETL con el objetivo de identificar las variables que se pueden utilizar en la creación del modelo de recomendación. Para el modelo ML, se creó un dataframe combinando el título del juego, id del usuario y una columna de rating mediante la combinación del análisis de sentimiento y la recomendación de los juegos

Archivo:
- [4 EDA.ipynb](https://github.com/cristobalqv/PI_videojuegos_Steam/blob/main/JupyterNotebooks/4%20EDA.ipynb "4 EDA.ipynb")

#### *MODELO DE MACHINE LEARNING*
Se creó un modelo de recomendación de aprendizaje automático basado en la similitud de los juegos existentes. Para esto se utilizó la similitud del coseno, el que determina que tan similares son dos conjuntos de datos o elementos

Archivo:
- [5 modelo ML.ipynb](https://github.com/cristobalqv/PI_videojuegos_Steam/blob/main/JupyterNotebooks/5%20modelo%20ML.ipynb "5 modelo ML.ipynb")


#### *DESPLIEGUE DE API*
Para el deploy de la API, se utilizó el framework FastAPI, y para un acceso mas práctico se tenía contemplado la renderización mediante Render, la cual es una plataforma que permite la creación y ejecución de apps y webs. Sin embargo, no se pudo completar aquella solicitud debido a problemas de renderización que fueron constantes y por el momento, sin solución (se explica en el video anexo)

Archivo:
- [main.py](https://github.com/cristobalqv/PI_videojuegos_Steam/blob/main/main.py "main.py")


## ANEXO: VIDEO
Video que explica brevemente los procedimientos señalados anteriormente
https://youtu.be/EKTO3jRsiAo
