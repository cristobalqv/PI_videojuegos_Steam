# # Proyecto Individual "Videojuegos Steam"

### INTRODUCCIÓN 
El objetivo de este proyecto consiste en situarnos en el rol de un *MLOps Engineer* y poder crear un sistema de recomendación de videojuegos basado en un conjunto de datos predefinidos de la plataforma Steam. Estas tareas y procedimientos están enfocadas principalmente en la Extracción, Transformación y Carga de datos (ETL), análisis exploratorio de datos (EDA), junto con la epxloración y entrenamiento de un modelo de Machine Learning. Finaliza con el deployment de los datos en FastAPI y renderización en Render para su posterior uso en los entornos productivos

### PROCEDIMIENTO
##### Transformación y Limpieza de Datos (ETL)
Se realizó la extracción, transformación y carga (ETL) de los tres conjuntos de datos entregados. Dos de los conjuntos de datos se encontraban anidados, es decir había columnas con diccionarios o listas de diccionarios, por lo que aplicaron distintas estrategias para transformar las claves de esos diccionarios en columnas. Luego se rellenaron algunos nulos de variables necesarias para el proyecto, se borraron columnas con muchos nulos o que no aportaban al proyecto, para optimizar el rendimiento de la API y teneniendo en cuenta las limitaciones de almacenamiento del deploy. Para las transformaciones se utilizó la librería Pandas.

Los detalles del ETL se puede ver en ETL output_steam_games, ETL australian_users_items y ETL australian_user_reviews.

Feature engineering
Uno de los pedidos para este proyecto fue aplicar un análisis de sentimiento a los reviews de los usuarios. Para ello se creó una nueva columna llamada 'sentiment_analysis' que reemplaza a la columna que contiene los reviews donde clasifica los sentimientos de los comentarios con la siguiente escala:

Por otra parte, y bajo el mismo criterio de optimizar los tiempos de respuesta de las consultas en la API y teniendo en cuenta las limitaciones de almacenamiento en el servicio de nube para deployar la API, se realizaron dataframes auxiliares para cada una de las funciones solicitadas. En el mismo sentido, se guardaron estos dataframes en formato parquet que permite una compresión y codificación eficiente de los datos.

Todos los detalles del desarrollo se pueden ver en la Jupyter Notebook 01d_Feature_eng.

##### ANÁLISIS EXPLORATORIO DE DATOS (EDA)
Se realizó el EDA a los tres conjuntos de datos sometidos a ETL con el objetivo de identificar las variables que se pueden utilizar en la creación del modelo de recmendación. Para ello se utilizó la librería Pandas para la manipulación de los datos y las librerías Matplotlib y Seaborn para la visualización.

En particular para el modelo de recomendación, se terminó eligiendo construir un dataframe específico con el id del usuario que realizaron reviews, los nombres de los juegos a los cuales se le realizaron comentarios y una columna de rating que se construyó a partir de la combinación del análisis de sentimiento y la recomendación a los juegos.

El desarrollo de este análisis se encuentra en la Jupyter Notebook EDA



##### DESARROLLO DE API
Para el desarrolo de la API se decidió utilizar el framework FastAPI, creando las siguientes funciones:

userdata: Esta función tiene por parámentro 'user_id' y devulve la cantidad de dinero gastado por el usuario, el porcentaje de recomendaciones que realizó sobre la cantidad de reviews que se analizan y la cantidad de items que consume el mismo.

countreviews: En esta función se ingresan dos fechas entre las que se quiere hacer una consulta y devuelve la cantidad de usuarios que realizaron reviews entre dichas fechas y el porcentaje de las recomendaciones positivas (True) que los mismos hicieron.

genre: Esta función recibe como parámetro un género de videojuego y devuelve el puesto en el que se encuentra dicho género sobre un ranking de los mismos analizando la cantidad de horas jugadas para cada uno.

userforgenre: Esta función recibe como parámetro el género de un videojuego y devuelve el top 5 de los usuarios con más horas de juego en el género ingresado, indicando el id del usuario y el url de su perfil.

developer: Esta función recibe como parámetro 'developer', que es la empresa desarrolladora del juego, y devuelve la cantidad de items que desarrolla dicha empresa y el porcentaje de contenido Free por año por sobre el total que desarrolla.

sentiment_analysis: Esta función recibe como parámetro el año de lanzamiento de un juego y según ese año devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento, como Negativo, Neutral y Positivo.

recomendacion_juego: Esta función recibe como parámetro el nombre de un juego y devuelve una lista con 5 juegos recomendados similares al ingresado.

recomendacion_usuario: Esta función recibe como parámetro el id de un usuario y devuelve una lista con 5 juegos recomendados para dicho usuario teniendo en cuenta las similitudes entre los usuarios.

NOTA: ambas funciones, recomendacion_juego y recomendacion_usuario se agregaron a la API, pero sólo recomendacion_juego se pudo deployar en Render dado que el conjunto de datos que requiere para hacer la predicción excedía la capacidad de almacenamiento disponible. Por lo tanto, para utilizarla se puede ejecutar la API en local.

El desarrollo de las funciones de consultas generales se puede ver en la Jupyter Notebook 02_funcionesAPI. El desarrollo del código para las funciones del modelo de recomendación se puede ver en la Jupyter Notebook 04_Modelo_recomendacion

El código para generar la API se encuentra en el archivo main.py y las funciones para su funcionamiento se encuentran en api_functions. En caso de querer ejecutar la API desde localHost se deben seguir los siguientes pasos:

##### MODELO DE MACHINE LEARNING

Modelo de aprendizaje automático
Se crearon dos modelos de recomendación, que generan cada uno, una lista de 5 juegos ya sea ingresando el nombre de un juego o el id de un usuario.

En el primer caso, el modelo tiene una relación ítem-ítem, esto es, se toma un juego y en base a que tan similar es ese juego con el resto de los juegos se recomiendan similares. En el segundo caso, el modelo aplicar un filtro usuario-juego, es decir, toma un usuario, encuentra usuarios similares y se recomiendan ítems que a esos usuarios similares les gustaron.

Para generar estos modelos se adoptaron algoritmos basados en la memoria, los que abordan el problema del filtrado colaborativo utilizando toda la base de datos, tratando de encontrar usuarios similares al usuario activo (es decir, los usuarios para los que se les quiere recomendar) y utilizando sus preferencias para predecir las valoraciones del usuario activo.

Para medir la similitud entre los juegos (item_similarity) y entre los usuarios (user_similarity) se utilizó la similitud del coseno que es una medida comúnmente utilizada para evaluar la similitud entre dos vectores en un espacio multidimensional. En el contexto de sistemas de recomendación y análisis de datos, la similitud del coseno se utiliza para determinar cuán similares son dos conjuntos de datos o elementos, y se calcula utilizando el coseno del ángulo entre los vectores que representan esos datos o elementos.

El desarrollo para la creación de los dos modelos se presenta en la Jupyter Notebook 04_Modelo_recomendacion.


##### DESPLIEGUE DE API

### ANEXO: VIDEO
En este video se explica brevemente este proyecto mostrando el funcionamiento de la API.
