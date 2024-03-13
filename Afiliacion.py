import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# DataFrame con la información de las 32 provincias
data_provincia = {
    "Provincia": ["Azua", "Bahoruco", "Barahona", "Dajabon", "Distrito Nacional", "Duarte", "El Seybo", "Elias Piña",
                  "Espaillat", "Hato Mayor del Rey", "Hermanas Mirabal", "Independencia", "La Altagracia", "La Romana",
                  "La vega", "Maria Trinidad Sanchez", "Monseñor Nouel", "Monte Plata", "Montecristi", "Pedernales",
                  "Peravia", "Puerto Plata", "Samana", "San Cristóbal", "San jose de Ocoa", "San Juan de la Maguana",
                  "San Pedro de Macorís", "Sanchez Ramirez", "Santiago", "Santiago Rodriguez", "Santo Domingo", "Valverde",
                  "Total general"],
    "Afiliados 2020": [36193, 21667, 38736, 17413, 339756, 55690, 19245, 23042, 48879, 19335, 22997, 13691, 27047, 37952,
                      70310, 26829, 30665, 39038, 19769, 4427, 22834, 56716, 16162, 89466, 14977, 72456, 49960, 34251, 165241,
                      16860, 135074, 25870, 1612548],
    "Afiliados 2021": [37203, 21522, 38617, 17111, 427452, 55736, 20271, 21974, 49323, 20642, 22463, 14398, 40555, 46140,
                      73109, 25901, 31353, 38959, 19381, 4500, 23280, 62397, 16167, 94667, 14518, 71153, 56790, 33799, 179092,
                      16304, 172007, 26709, 1793493],
    "Afiliados 2022": [39088, 22226, 39753, 17385, 491162, 58849, 20768, 21757, 49981, 20961, 22772, 15333, 44787, 49335,
                      75265, 27484, 32369, 39713, 19891, 4688, 24540, 65183, 17809, 98457, 14490, 71540, 59579, 34808, 190124,
                      16417, 196901, 28115, 1931530],
    "Afiliados 2023": [39776, 21684, 39113, 16678, 524372, 53686, 20073, 21226, 47847, 20315, 21009, 15325, 45054, 49813,
                      72377, 24965, 30616, 39486, 18743, 4752, 23135, 62942, 16380, 98987, 13869, 69502, 57762, 32968, 188558,
                      15461, 212489, 26133, 1945096]
}

data_afiliados = {
    "Año": [202312, 202312],
    "Total Afiliado": [2241509.00, 1042214.00],
    "Sexo": ["Hombre", "Mujer"],
    "Rango Edad": ["15-85", "15-89"]
}

data_ars = {
    'ARS': ['SENASA', 'PRIMERA ARS', 'ARS MAPHRE SALUD', 'OTRAS ARS'],
    'Afiliados': [1688290, 1350000, 850000, 1516798],
}

df_provincia = pd.DataFrame(data_provincia)
df_afiliados = pd.DataFrame(data_afiliados)
df_ars = pd.DataFrame(data_ars)

# Calculo total general por año
df_total_general = pd.DataFrame({
    "Año": ["Afiliados 2020", "Afiliados 2021", "Afiliados 2022", "Afiliados 2023"],
    "Total General": [1612548, 1793493, 1931530, 1945096]
})

# Calculo de porcentaje para el gráfico de ARS
df_ars['Porcentaje'] = (df_ars['Afiliados'] / df_ars['Afiliados'].sum()) * 100

# Inicializar la aplicación Dash
app = dash.Dash(__name__)
server = app.server
# diseño del dashboard
app.layout = html.Div(children=[
    html.H1(children='Distribucion de Afiliados por Provincia y Año ,ARS ,Sexo'),

    # Gráfico de Provincias
    dcc.Graph(
        id='provincias-chart',
        figure=px.bar(df_provincia[df_provincia['Provincia'] != 'Total general'],
                       x='Provincia', y=['Afiliados 2020', 'Afiliados 2021', 'Afiliados 2022', 'Afiliados 2023'],
                       title='Afiliados por Provincia y Año')
    ),

    # Mini gráfico Total General
    dcc.Graph(
        id='total-general-mini-chart',
        figure=px.bar(df_total_general, x='Año', y='Total General', title='Total General Afiliados por Año')
    ),

    # Gráfico de ARS con porcentaje
    dcc.Graph(
        id='ars-chart',
        figure=px.pie(df_ars, names='ARS', values='Afiliados', title='Afiliados por ARS',
                      labels={'Afiliados': 'Porcentaje'}, hover_data=['Porcentaje'])
    ),

    # Gráfico de Afiliados por Sexo
    dcc.Graph(
        id='afiliados-sexo-chart',
        figure=px.bar(df_afiliados, x='Sexo', y='Total Afiliado', color='Sexo', title='Afiliados por Sexo')
    )
])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
