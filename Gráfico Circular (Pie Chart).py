import plotly.express as px
import pandas as pd

plataformas = ['Google Classroom', 'Moodle', 'Microsoft Teams', 'Otra plataforma']
respuestas = [4, 2, 3, 2]

df = pd.DataFrame({'Plataforma': plataformas, 'Respuestas': respuestas})

fig = px.pie(df,
             names='Plataforma',
             values='Respuestas',
             title='Plataforma educativa más utilizada')
fig.show()

#El gráfico de pastel o circular representa proporciones o porcentajes de un total.
#Es perfecto para visualizar cómo se divide un conjunto en partes.