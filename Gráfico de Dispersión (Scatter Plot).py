import plotly.express as px

# Datos directamente en listas
software = [
    'Procesadores y hojas de cálculo',
    'Programas especializados',
    'Plataformas de videoconferencia',
    'Apps de notas'
]
respuestas = [2, 2, 4, 3]

# Crear gráfico de dispersión
fig = px.scatter(
    x=software,
    y=respuestas,
    size=respuestas,       # Tamaño de los puntos según las respuestas
    color=software,        # Colores distintos por categoría
    title='Tipo de software más útil en la formación académica',
    labels={'x': 'Tipo de software', 'y': 'Número de respuestas'}
)

# Mostrar gráfico
fig.show()

# El gráfico de dispersión muestra la relación entre dos variables numéricas.
# Sirve para observar patrones, correlaciones o comportamientos entre los datos.

