import plotly.express as px
import pandas as pd

software = ['Procesadores y hojas de cálculo', 'Programas especializados', 'Plataformas de videoconferencia', 'Apps de notas']
respuestas = [2, 2, 4, 3]

df = pd.DataFrame({'Software': software, 'Respuestas': respuestas})

fig = px.scatter(df,
                 x='Software',
                 y='Respuestas',
                 size='Respuestas',
                 color='Software',
                 title='Tipo de software más útil en la formación académica')
fig.show()
