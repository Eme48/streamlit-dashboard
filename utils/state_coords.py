"""
state_coords.py

Este módulo contiene las coordenadas aproximadas (latitud y longitud)
del centro geográfico (centroide) de cada uno de los 50 estados de EE. UU.

Estas coordenadas se utilizan para visualizaciones geográficas como mapas de calor
o mapas de puntos, donde se desea representar datos agregados por estado
(en lugar de ubicaciones específicas dentro del estado).

Fuente aproximada: centroides de estados según datos públicos como SimpleMaps,
OpenStreetMap y el U.S. Census Bureau.

Formato:
    {
        'Nombre_del_Estado': {'lat': valor_latitud, 'lon': valor_longitud},
        ...
    }

Uso recomendado:
    from state_coords import STATE_COORDS
    lat = STATE_COORDS['California']['lat']
    lon = STATE_COORDS['California']['lon']
"""

STATE_COORDS = {
    'Alabama': {'lat': 32.8067, 'lon': -86.7911},
    'Alaska': {'lat': 61.3707, 'lon': -152.4044},
    'Arizona': {'lat': 33.7298, 'lon': -111.4312},
    'Arkansas': {'lat': 34.9697, 'lon': -92.3731},
    'California': {'lat': 36.1162, 'lon': -119.6816},
    'Colorado': {'lat': 39.0598, 'lon': -105.3111},
    'Connecticut': {'lat': 41.5978, 'lon': -72.7554},
    'Delaware': {'lat': 39.3185, 'lon': -75.5071},
    'Florida': {'lat': 27.7663, 'lon': -81.6868},
    'Georgia': {'lat': 33.0406, 'lon': -83.6431},
    'Hawaii': {'lat': 21.0943, 'lon': -157.4983},
    'Idaho': {'lat': 44.2405, 'lon': -114.4788},
    'Illinois': {'lat': 40.3495, 'lon': -88.9861},
    'Indiana': {'lat': 39.8494, 'lon': -86.2583},
    'Iowa': {'lat': 42.0115, 'lon': -93.2105},
    'Kansas': {'lat': 38.5266, 'lon': -96.7265},
    'Kentucky': {'lat': 37.6681, 'lon': -84.6701},
    'Louisiana': {'lat': 31.1695, 'lon': -91.8678},
    'Maine': {'lat': 44.6939, 'lon': -69.3819},
    'Maryland': {'lat': 39.0639, 'lon': -76.8021},
    'Massachusetts': {'lat': 42.2302, 'lon': -71.5301},
    'Michigan': {'lat': 43.3266, 'lon': -84.5361},
    'Minnesota': {'lat': 45.6945, 'lon': -93.9002},
    'Mississippi': {'lat': 32.7416, 'lon': -89.6787},
    'Missouri': {'lat': 38.4561, 'lon': -92.2884},
    'Montana': {'lat': 46.9219, 'lon': -110.4544},
    'Nebraska': {'lat': 41.1254, 'lon': -98.2681},
    'Nevada': {'lat': 38.3135, 'lon': -117.0554},
    'New Hampshire': {'lat': 43.4525, 'lon': -71.5639},
    'New Jersey': {'lat': 40.2989, 'lon': -74.5210},
    'New Mexico': {'lat': 34.8405, 'lon': -106.2485},
    'New York': {'lat': 42.1657, 'lon': -74.9481},
    'North Carolina': {'lat': 35.6301, 'lon': -79.8064},
    'North Dakota': {'lat': 47.5289, 'lon': -99.7840},
    'Ohio': {'lat': 40.3888, 'lon': -82.7649},
    'Oklahoma': {'lat': 35.5653, 'lon': -96.9289},
    'Oregon': {'lat': 44.5720, 'lon': -122.0709},
    'Pennsylvania': {'lat': 40.5908, 'lon': -77.2098},
    'Rhode Island': {'lat': 41.6809, 'lon': -71.5118},
    'South Carolina': {'lat': 33.8569, 'lon': -80.9450},
    'South Dakota': {'lat': 44.2998, 'lon': -99.4388},
    'Tennessee': {'lat': 35.7478, 'lon': -86.6923},
    'Texas': {'lat': 31.0545, 'lon': -97.5635},
    'Utah': {'lat': 40.1500, 'lon': -111.8624},
    'Vermont': {'lat': 44.0459, 'lon': -72.7107},
    'Virginia': {'lat': 37.7693, 'lon': -78.1699},
    'Washington': {'lat': 47.4009, 'lon': -121.4905},
    'West Virginia': {'lat': 38.4912, 'lon': -80.9546},
    'Wisconsin': {'lat': 44.2685, 'lon': -89.6165},
    'Wyoming': {'lat': 42.7559, 'lon': -107.3025}
}
