import plotly.express as px

# Datos directamente en listas
plataformas = ['Google Classroom', 'Moodle', 'Microsoft Teams', 'Otra plataforma']
respuestas = [4, 2, 3, 2]

# Crear gráfico de pastel
fig = px.pie(
    names=plataformas,
    values=respuestas,
    title='Plataforma educativa más utilizada'
)

# Mostrar gráfico
fig.show()

# El gráfico de pastel o circular representa proporciones o porcentajes de un total.
# Es perfecto para visualizar cómo se divide un conjunto en partes.

