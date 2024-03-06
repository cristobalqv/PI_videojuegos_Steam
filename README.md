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

Archivo: [2 datos para consulta.ipynb](https://github.com/cristobalqv/PI_videojuegos_Steam/blob/main/JupyterNotebooks/2%20datos%20para%20consulta.ipynb "2 datos para consulta.ipynb")

Se crearon las siguientes funciones y se utilizó el framework FastAPI:

- developer: Función que devuelve la cantidad de items y porcentaje de contenido Free por año según la empresa desarrolladora

- userdata: Función que devuelve la cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews_recommend y cantidad de items consumidos

- UserForGenre: Función que devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.

- best_developer_year: Función que devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado (reviews.recommend=True y comentarios positivos)

- developer_reviews_analysis: Función que devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.

Archivo: [3 funciones API.ipynb](https://github.com/cristobalqv/PI_videojuegos_Steam/blob/main/JupyterNotebooks/3%20funciones%20API.ipynb "3 funciones API.ipynb")


#### *ANÁLISIS EXPLORATORIO DE DATOS (EDA)*
Se realizó el EDA a los tres conjuntos de datos sometidos a ETL con el objetivo de identificar las variables que se pueden utilizar en la creación del modelo de recmendación. Para ello se utilizó la librería Pandas para la manipulación de los datos y las librerías Matplotlib y Seaborn para la visualización.

En particular para el modelo de recomendación, se terminó eligiendo construir un dataframe específico con el id del usuario que realizaron reviews, los nombres de los juegos a los cuales se le realizaron comentarios y una columna de rating que se construyó a partir de la combinación del análisis de sentimiento y la recomendación a los juegos.

El desarrollo de este análisis se encuentra en la Jupyter Notebook EDA





#### *MODELO DE MACHINE LEARNING*

Modelo de aprendizaje automático
Se crearon dos modelos de recomendación, que generan cada uno, una lista de 5 juegos ya sea ingresando el nombre de un juego o el id de un usuario.

En el primer caso, el modelo tiene una relación ítem-ítem, esto es, se toma un juego y en base a que tan similar es ese juego con el resto de los juegos se recomiendan similares. En el segundo caso, el modelo aplicar un filtro usuario-juego, es decir, toma un usuario, encuentra usuarios similares y se recomiendan ítems que a esos usuarios similares les gustaron.

Para generar estos modelos se adoptaron algoritmos basados en la memoria, los que abordan el problema del filtrado colaborativo utilizando toda la base de datos, tratando de encontrar usuarios similares al usuario activo (es decir, los usuarios para los que se les quiere recomendar) y utilizando sus preferencias para predecir las valoraciones del usuario activo.

Para medir la similitud entre los juegos (item_similarity) y entre los usuarios (user_similarity) se utilizó la similitud del coseno que es una medida comúnmente utilizada para evaluar la similitud entre dos vectores en un espacio multidimensional. En el contexto de sistemas de recomendación y análisis de datos, la similitud del coseno se utiliza para determinar cuán similares son dos conjuntos de datos o elementos, y se calcula utilizando el coseno del ángulo entre los vectores que representan esos datos o elementos.

El desarrollo para la creación de los dos modelos se presenta en la Jupyter Notebook 04_Modelo_recomendacion.


#### *DESPLIEGUE DE API*

## ANEXO: VIDEO
En este video se explica brevemente este proyecto mostrando el funcionamiento de la API.
