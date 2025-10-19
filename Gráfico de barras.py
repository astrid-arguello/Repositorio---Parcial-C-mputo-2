#lineas de exportancion de la libreria 
import plotly.express as px
import pandas as pd

#  Estas lineas de comando son en donde van los datos de entrada
# que son los datos que llevara el grafico de barra
dispositivos = ['Computadora portátil', 'Teléfono móvil', 'Tableta digital', 'Computadora de escritorio']
respuestas = [3, 4, 2, 2]

# Esta linea de comando es la que estructura los datos para la generacion o creacion del grafico
df = pd.DataFrame({'Dispositivo': dispositivos, 'Respuestas': respuestas})

# Estas lineas son las encargadas de crear y mostrar el graficode dispercion 
fig = px.bar(df,
             x='Dispositivo',
             y='Respuestas',
             color='Dispositivo',
             title='Dispositivo más utilizado para tareas académicas')
fig.show()

#Este gráfico muestra la comparación de categorías usando barras verticales.
#Es ideal para representar valores de forma visual y sencilla, como ventas, cantidades o resultados.#
