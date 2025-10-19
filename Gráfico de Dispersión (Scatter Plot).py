# Importancion de la libreria
import plotly.express as px
import pandas as pd

# En estas dos lineas de codigo es donde van los datos de entrada 
# que llevara el grafico de dispercion.
software = ['Procesadores y hojas de cálculo', 'Programas especializados', 'Plataformas de videoconferencia', 'Apps de notas']
respuestas = [2, 2, 4, 3]

# Esta linea de comandos es donde se estructuran los datos para
# general el grafico de dispercion.
df = pd.DataFrame({'Software': software, 'Respuestas': respuestas})

# Estas lineas de comando son las escargadas de
# Crear y mostrar el grafico de dispercion 
fig = px.scatter(df,
                 x='Software',
                 y='Respuestas',
                 size='Respuestas',
                 color='Software',
                 title='Tipo de software más útil en la formación académica')
fig.show()

#El gráfico de dispersión muestra la relación entre dos variables numéricas. 
#Sirve para observar patrones, correlaciones o comportamientos entre los datos.
