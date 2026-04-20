"""
En este archivo pondrás en práctica el uso de bucles 'for' en Python,
usando ejemplos inspirados en videojuegos y situaciones atractivas.
"""

# 1. Generador de niveles
# Imprime todos los niveles del 0 al 100 (incluyendo el 100).
# (Tu código aquí)

for niveles in range(0, 101, 1):
    print(niveles)


# 2. Potenciadores de energía (Múltiplos de 2)
# Imprime los números múltiplos de 2 desde 2 hasta 500 (incluyendo el 500).
# (Tu código aquí)

for potenciadornivel in range (0, 502, 2):
    print (potenciadornivel)


# 3. Trampa de emojis
# Recorre los puntos del 1 al 100.
# - Si el número es divisible por 5, imprime "😀"
# - Si es divisible por 10, imprime "😮"
# ¡Cuidado con la prioridad en tus condicionales!
# (Tu código aquí)

for puntosemoji in range (0, 101, 1):
    if puntosemoji % 10 == 0:
        print("😮")
    elif puntosemoji % 5 == 0:
        print("😀")
    else:
        print(puntosemoji)


# 4. Suma colosal
# Suma todos los números pares del 0 al 500,000 e imprime la suma total.
# (Tu código aquí)

result = 0
for sumcolosal in range (0, 500001, 2):
    result += sumcolosal

print("resultado:",result)



# 5. Retroceso temporal
# Desde 2024, retrocede de 3 en 3 hasta 0 o menos.
# Imprime cada valor en la cuenta regresiva.
# (Tu código aquí)

for yearssisi in range(2024, -3, -3):
    print(yearssisi)


# 6. Contador dinámico
# Declara las variables inicio, fin, y salto (por ejemplo: inicio=3, fin=10, salto=2).
# Imprime los números en el rango que sean múltiplos de 'salto'.
# (Tu código aquí)

inicio = 4
fin = 101
salto = 6

for sistemaestelar in range (inicio, fin, salto):
    if inicio % salto:
        print(sistemaestelar)

# Ejemplo: si inicio = 3, fin = 10, y salto = 2
# Se imprimiría: 4, 6, 8, 10

#¿Cuál de estos ejercicios te pareció más útil o interesante para aplicarlo en un contexto real, ya sea un videojuego o cualquier aplicación?

#R: El ejericio 6 por los sitemas de inicio, los checkpoints y el final para un videojuego plataformero