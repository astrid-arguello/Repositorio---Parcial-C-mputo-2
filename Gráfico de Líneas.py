
import plotly.express as px
import pandas as pd


frecuencias = ['Siempre', 'A veces', 'Rara vez', 'Nunca']
respuestas = [4, 2, 4, 1]

df = pd.DataFrame({'Frecuencia': frecuencias, 'Respuestas': respuestas})

fig = px.line(df,
              x='Frecuencia',
              y='Respuestas',
              markers=True,
              title='Frecuencia de uso de herramientas de colaboración en línea')
fig.show()

#El gráfico de líneas se utiliza para mostrar la evolución de un valor a lo largo del tiempo. 
#Es útil para representar tendencias, cambios o progresos en períodos determinados.
