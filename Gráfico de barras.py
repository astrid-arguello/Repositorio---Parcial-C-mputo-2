import plotly.express as px
import pandas as pd

# Datos
dispositivos = ['Computadora portátil', 'Teléfono móvil', 'Tableta digital', 'Computadora de escritorio']
respuestas = [3, 4, 2, 2]

# Crear DataFrame
df = pd.DataFrame({'Dispositivo': dispositivos, 'Respuestas': respuestas})

# Gráfico de barras
fig = px.bar(df,
             x='Dispositivo',
             y='Respuestas',
             color='Dispositivo',
             title='Dispositivo más utilizado para tareas académicas')
fig.show()
