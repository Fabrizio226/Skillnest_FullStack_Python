def multiplicacion(num1, num2): #definimos la función multiplación con los parámetros num1 y num2
   resultado = num1 * num2     #instrucciones dentro de la función
   return resultado            #regresamos valor de resultado

resultado_multiplicacion = multiplicacion(5, 5) #Llamado a la función con argumentos 5 y 5
print(resultado_multiplicacion) #Se guarda en la variable el resultado que la función regresó. Imprime: 25

a = int(input("Ingrese primer numero: "))
b = int(input("Ingrese segundo numero: "))
resultado_multiplicacion = multiplicacion(a, b)
print(resultado_multiplicacion)

def buenos_dias(nombre):
    print("Buenos días "+nombre)

buenos_dias("alegría")
buenos_dias("al amor")
buenos_dias("a la vida")
buenos_dias("señor Sol")
buenos_dias("Repartidor")

# Devolución de valores
def buenos_dias2(nombre):
    return "Buenos días "+nombre

#El valor de retorno de la función es "Buenos días Python", por lo que el valor de mi variable frase será ese

frase = buenos_dias2("Python")
frase = buenos_dias2("mcr")
print(frase) #Imprime: Buenos días Python

# Ejercicio de retorno valor
# Crear una función que reciba dos parametros (Una frase + una palabra).
# Devolver el valor de la frase completa a imprimir
def mifrase(frase, palabra):
    return f"{frase} {palabra}"

frase = input("Ingrese una frase: ")
palabra = input("Ingrese una palabra: ")
resultadofrase = mifrase(frase, palabra)
print(resultadofrase)
