import plotly.express as px

# Datos directamente en listas
dispositivos = ['Computadora portátil', 'Teléfono móvil', 'Tableta digital', 'Computadora de escritorio']
respuestas = [3, 4, 2, 2]

# Crear gráfico de barras
fig = px.bar(
    x=dispositivos,
    y=respuestas,
    color=dispositivos,
    title='Dispositivo más utilizado para tareas académicas',
    labels={'x': 'Dispositivo', 'y': 'Número de respuestas'}
)

# Mostrar gráfico
fig.show()

# Este gráfico muestra la comparación de categorías usando barras verticales.
# Es ideal para representar valores de forma visual y sencilla, como ventas, cantidades o resultados.

