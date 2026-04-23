import os

# Ejercicio 1

# Calcula experiencia

def multiplica_por_2(num):
    result = []
    for i in range(num + 1):
        result.append(i * 2)
    return result
def ejercicio1():
    result1 = multiplica_por_2(5)
    print(result1)


# Debe retornar: [0, 2, 4, 6, 8, 10]

#Ejercicio 2

# Analiza publicaciones

def suma_y_resta(list):
    suma = list[0] + list[1]
    resta = list[0] - list[1]
    print(f"suma: {suma}")
    return resta

def ejercicio2():
    resta = suma_y_resta([120, 115])
    print(f"retorno / resta: {resta}")

# Imprime: 235 y retorna: 5

#Ejercicio 3

# Puntaje ajustado

def sumatoria_menos_longitud(sumatoria):
    total = sum(sumatoria)
    longitud = len(sumatoria)
    resultado = total - longitud
    print(f"Total = {total}, longitud = {longitud}")
    return resultado
def ejercicio3():
    retornar = sumatoria_menos_longitud([10, 5, 3, 7])
    print(f"El resultado del retorno es: {retornar}")
# Suma total = 25, longitud = 4, debe retornar: 21

#Ejericio 4

# Ajusta visualizaciones

def valores_multiplicados_segundo(lista):
    if len(lista) < 2:
        print(len(lista))
        return[]
    else:
        segEle = lista[1]
        nuevaLista = []
        for i in lista:
            nuevaLista.append(i * segEle)
        long = len (nuevaLista)
        print(long)
        return nuevaLista
def ejercicio4():
    retornar = valores_multiplicados_segundo([100, 3, 50, 20])
    print(f"El resultado del retorno es: {retornar}")

# Imprime: 4 y retorna: [300, 9, 150, 60]
valores_multiplicados_segundo([100])
# Imprime: 1 y retorna: []

#Ejericio 5

# Genera precio fijo

def valor_multiplicado_longitud(a, b):
    multilist = []
    for i in range(0, b):
        multilist.append(a * b)
    return multilist

def ejercicio5():
    result1 = valor_multiplicado_longitud(5, 2)
    print(f"Resultado 1: {result1}")
# Debe retornar: [10, 10]
    result2 = valor_multiplicado_longitud(7, 5)
    print(f"Resultado 2: {result2}")
# Debe retornar: [35, 35, 35, 35, 35]

def limpiar_consola():
    os.system('cls')

continuar = True
while continuar:
    print("\n--- Ejercicos Python---")
    print("--- 1.- Ejercicio 1 ---")
    print("--- 2.- Ejercicio 2 ---")
    print("--- 3.- Ejercicio 3 ---")
    print("--- 4.- Ejercicio 4 ---")
    print("--- 5.- Ejercicio 5 ---")
    opcion = input("\n---- Elige una opción: (1-5) (0 para salir) =")
    if opcion == "1":
        print("\nEjecutando ejercicio 1: ")
        ejercicio1()
    elif opcion == "2":
        print("\nEjecutando ejercicio 2: ")
        ejercicio2()
    elif opcion == "3":
        print("\nEjecutando ejercicio 3: ")
        ejercicio3()
    elif opcion == "4":
        print("\nEjecutando ejercicio 4: ")
        ejercicio4()
    elif opcion == "5":
        print("\nEjecutando ejercicio 5: ")
        ejercicio5()
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opcion no valida, intenta otra vez")