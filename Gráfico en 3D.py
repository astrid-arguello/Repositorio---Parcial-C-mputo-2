import plotly.express as px

# Datos
frecuencias = ['Siempre', 'A veces', 'Rara vez', 'Nunca']
respuestas = [4, 2, 4, 1]
porcentajes = [36.4, 18.2, 36.4, 9.1]  # Ejemplo de tercer valor para el eje Z

# Crear gráfico 3D de dispersión
fig = px.scatter_3d(
    x=frecuencias,
    y=respuestas,
    z=porcentajes,
    color=frecuencias,
    size=respuestas,
    title='Frecuencia de uso de herramientas de colaboración (Gráfico 3D)'
)

# Mostrar gráfico
fig.show()

# El gráfico 3D permite visualizar tres dimensiones de datos al mismo tiempo (X, Y, Z).
# Es útil para analizar relaciones complejas o comparar varios valores simultáneamente.
