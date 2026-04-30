#Repaso para la prueba

#1 Crear una función que reciba una lista de números enteros y muestre cuál es el número mayor y cuál es el menor.

def numeroMayorMenor(listado):
    menor = min (listado)
    mayor = max (listado)
    print(f"El número mayor es {mayor}\nEl numero menor es: {menor}")

def ejercicio1():
    limit = int(input("Ingrese un limite de numeros: "))
    Listanumeros = []
    i = 1 
    while i <= limit:
        num = int(input(f"Ingresa un número entero {i} de {limit}: "))
        Listanumeros.append(num)
        i += 1
    numeroMayorMenor(Listanumeros)
ejercicio1()

#2 Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene.

def contadorvocales(letra):
    vocales = "aeiouAEIOU"
    return letra in vocales

def contar_vocales(texto):
    contador = 0

    for letra in texto:
        if contadorvocales(letra):
            contador += 1

    print(f"La cadena contiene {contador} vocales")

def ejericicio_contar_vocales():
    texto = input("Ingrese una cadena de texto: ")
    contar_vocales(texto)
ejericicio_contar_vocales()

#3 Crear una función que reciba una lista de nombres y muestre únicamente aquellos que tengan más de 5 letras.

def nombres_filtrados(lista):
    resultado = []
    for nombre in lista:
        if len(nombre) > 5:
            resultado.append(nombre)
    return resultado

def mostrarletras():
    nombres = []
    nombreslargos = []
    cantidad = int(input("¿Cuantos nombres desea ingresar?: "))

    for i in range (cantidad):
        nombre = input ("Ingrese un nombre: ")
        print(f"{nombre} agregado con exito a la lista.")
        nombres.append(nombre)

    nombreslargos = nombres_filtrados(nombres)
    print(f"Los nombres con más de 5 letras son: \n- {('\n- ').join(nombreslargos)}")
mostrarletras()

#4 Crear una función que reciba una lista de notas (números decimales), calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).

def listanotas(notas):
    lista = 0
    promedio = 0
    for i in range(len(notas)):
        lista += notas[i]
        promedio = lista / (len(notas))

    if promedio >= 4.0 and promedio <= 7.0:
        print(f"El estudiante aprueba con un {promedio}")
    elif promedio >= 1.0 and promedio <= 3.9:
        print(f"El estudiante reprueba con un {promedio}")
    else:
        return"Error" 

def ejercicio4():
    largo = int(input("¿Cuantas notas va a ingresar?: "))
    nota  = []
    for i in range (largo):
        inp = float(input(f"Ingrese nota {i + 1}: "))
        if inp != "":
            nota.append(inp)
    print(listanotas(nota))
ejercicio4()

#5 Crear una función que reciba una lista de precios de productos y aplique un descuento del 10%, mostrando el valor original y el nuevo valor.

def descuento(valor):
    sumaLista = sum(valor)
    precioInicial = sumaLista
    descuento = sumaLista * 0.1
    precioFinal = precioInicial - descuento
    print(f"El precio inicial del producto es: \n{precioInicial}\ny con descuento \n{precioFinal}")

def valores():
    cantidadProductos = int(input("Ingrese la cantidad de productos que quiera: \n"))
    listaPrecios = []
    for i in range(cantidadProductos):
        valorProducto = float(input("Ingrese el valor del producto: \n"))
        listaPrecios.append(valorProducto)
    descuento(listaPrecios)
valores()

#6 Crear una función que reciba un número entero y determine si es par o impar.

def parImpar(numero):
    if numero % 2 == 0:
        print(f"El numero {numero} es Par.")
    elif numero % 3 == 0:
        print(f"El numero {numero} es Impar.")
    else:
        print("Error")

def recibirNum():
    num = int(input("Ingrese un numero: "))
    parImpar(num)
recibirNum()

#7 Crear una función que reciba una lista de edades y muestre cuántas personas son mayores de edad (18 años o más).

def edades(lista):
    num = 0
    for i in range(len(lista)):
        if lista[i] >= 18:
            num += 1
    return num

def personas():
    edad = []
    inp = int(input("Cuantas personas van a ingresar hoy?: "))
    for i in range(inp):
        var = int(input(">> "))
        if var !="":
            edad.append(var)
        else:
            print("Por favor ingresar valor valido")
    resultado = edades(edad)
    print(f"Hay {resultado} personas mayores de edad")
personas()

#8 Crear una función que reciba una lista de palabras y permita buscar cuántas veces aparece una palabra específica ingresada por el usuario.

def vecesqueAparece(palabras):
    buscar = input("Ingrese la palabra que desea buscar: ")
    vecesqueAparece = 0
    for i in range(len(palabras)):
        vecesqueAparece += 1
    print(f"La palabra {buscar} aparece {vecesqueAparece} en la lista.")

def recibirPalabras():
    cantidad = int(input("Ingrese la cantidad de palabras: "))
    listaPalabras = []
    for i in range(cantidad):
        palabra = input(f"{i + 1}.")
        listaPalabras.append(palabra)
    vecesqueAparece(listaPalabras)
recibirPalabras()


#9 Crear una función que reciba una lista de números y genere una nueva lista que contenga únicamente los números positivos.

def ejericicio9():
    pass

#10 Crear una función que reciba una lista de productos (utilizando diccionarios con nombre y stock) y muestre cuáles tienen un stock menor a 5 unidades.

def ejercicio10():
    pass





# Menu

continuar = True
while continuar:
    print("\n--- Ejercicos Python---")
    print("--- 1.- Ejercicio 1 ---")
    print("--- 2.- Ejercicio 2 ---")
    print("--- 3.- Ejercicio 3 ---")
    print("--- 4.- Ejercicio 4 ---")
    print("--- 5.- Ejercicio 5 ---")
    print("--- 6.- Ejercicio 6 ---")
    print("--- 7.- Ejercicio 7 ---")
    print("--- 8.- Ejercicio 8 ---")
    print("--- 9.- Ejercicio 9 ---")
    print("--- 10.- Ejercicio 10 ---")
    opcion = input("\n---- Elige una opción: (1-10) (0 para salir) =")
    if opcion == "1":
        print("\nEjecutando ejercicio 1: ")
        ejercicio1()
    elif opcion == "2":
        print("\nEjecutando ejercicio 2: ")
        ejericicio_contar_vocales()
    elif opcion == "3":
        print("\nEjecutando ejercicio 3: ")
        mostrarletras()
    elif opcion == "4":
        print("\nEjecutando ejercicio 4: ")
        ejercicio4()
    elif opcion == "5":
        print("\nEjecutando ejercicio 5: ")
        valores()
    elif opcion == "6":
        print("\nEjecutando ejercicio 6: ")
        recibirNum()
    elif opcion == "7":
        print("\nEjecutando ejercicio 7: ")
        personas()
    elif opcion == "8":
        print("\nEjecutando ejercicio 8: ")
        recibirPalabras()
    elif opcion == "9":
        print("\nEjecutando ejercicio 9: ")
        ()
    elif opcion == "10":
        print("\nEjecutando ejercicio 10: ")
        ()
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opcion no valida, intenta otra vez")
