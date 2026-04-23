
datos = [
    {"nombre": "Carlos", "puntaje": 80},
    {"nombre": "María", "puntaje": 95},
    {"nombre": "Pedro", "puntaje": 70}
]


# 1. Cambiar el puntaje de Pedro a 75
# 2. Crear función que imprima:
#    "Carlos obtuvo 80 puntos"
# 3. Crear función que reciba "nombre" o "puntaje" e imprima solo esos valores

datos = [
    {"nombre": "Carlos", "puntaje": 80},
    {"nombre": "María", "puntaje": 95},
    {"nombre": "Pedro", "puntaje": 70}
]

# 1

datos[2]["puntaje"] = 75

print(datos)

def mostrar_datos(datos):
    for item in datos:
        print(f"{item['nombre']} obtuvo {item['puntaje']}")

mostrar_datos(datos)

# 2
def imprimir_carlos(datos):
    for item in datos:
        if item["nombre"] == "Carlos":
            print(f"{item['nombre']} obtuvo 80 puntos")

imprimir_carlos(datos)

# 3
def mostrar_valores(datos, clave):
    for item in datos:
        if clave in item:
            print(item[clave])