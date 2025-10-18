import plotly.express as px

# Datos de ejemplo
dispositivos = ["Computadora portátil", "Teléfono móvil", "Tableta", "Computadora de escritorio"]
respuestas = [3, 4, 2, 2]

# Crear gráfico de barras
fig = px.bar(
    x=dispositivos,
    y=respuestas,
    title="Dispositivo más usado por los estudiantes",
    labels={"x": "Dispositivo", "y": "Número de respuestas"},
    color=dispositivos
)

# Mostrar en el navegador
fig.show()
