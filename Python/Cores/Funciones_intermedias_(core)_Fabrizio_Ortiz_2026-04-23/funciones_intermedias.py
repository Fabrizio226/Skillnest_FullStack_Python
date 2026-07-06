
# Ranking de puntajes de un torneo de eSports
puntajes = [[1000, 1500, 2000], [300, 700, 1400]]

print(puntajes)
puntajes[1][0] = 600
print(puntajes)

# Lista de creadores de contenido en una plataforma de streaming
streamers = [
    {"nombre": "GameNinjaPro", "seguidores": 250000},
    {"nombre": "PixelWarrior", "seguidores": 180000}
]

print(streamers[0]["nombre"])
streamers[0]["nombre"] = "EliteGamerX"
print(streamers[0]["nombre"])

# Eventos en distintas ciudades del mundo
eventos = {
    "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
    "España": ["Madrid", "Barcelona", "Valencia"]
}

print(eventos["Estados Unidos"][2])
eventos["Estados Unidos"][2] = "San Francisco"
print(eventos["Estados Unidos"][2])

# Coordenadas de la sede de un torneo internacional
ubicacion = [
    {"latitud": 34.052235, "longitud": -118.243683}
]

print(ubicacion)

ubicacion[0]["latitud"] = 40.712776
print(ubicacion)

# Funciones que son para recorrer y representar los datos

# Datos de los Streamers
def iterar_diccionario(lista):
    for diccionario in lista:
        datos = []

        for clave, valor in diccionario.items():
            datos.append(f"{clave} - {valor}")

        print(", ".join(datos))

# Obtener valores de un diccionario
def obtener_valores(clave, lista):
    for diccionario in lista:
        print(diccionario[clave])

# Se muestra información de un diccionario con listas
# Diccionario de juegos y de ciudades
def mostrar_informacion(diccionario_categorias):
    for categoria, items in diccionario_categorias.items():
        print(f"\n{len(items)} {categoria.upper()}")

        for item in items:
            print(item)

print("\n=== STREAMERS ===")
iterar_diccionario(streamers)

print("\n=== NOMBRES ===")
obtener_valores("nombre", streamers)

print("\n=== SEGUIDORES ===")
obtener_valores("seguidores", streamers)

categorias = {
    "juegos_populares": [
        "Fortnite",
        "Minecraft",
        "Valorant",
        "GTA V",
    ],
    "ciudades_eventos": [
        "Nueva York",
        "Madrid",
        "Tokio",
    ]
}

print("\n=== CATEGORÍAS ===")
mostrar_informacion(categorias)