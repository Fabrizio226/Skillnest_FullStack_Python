# Creación de la clase usuario - entidad 
class Usuario:
    def __init__(self): #Constructor
        self.nombre = "Nariyoshi"
        self.apellido = "Miyagi"
        self.email = "miyagi@codingdojo.la"
        self.limite_credito = 30000
        self.saldo_pagar = 0

# Instancias de una clase
miyagi = Usuario()
daniel = Usuario()
fabrizio = Usuario()

#Accedemos a los atributos de la instancia
print(miyagi.nombre) #Imprime: Nariyoshi
print(miyagi.apellido)
print(miyagi.email)
print(miyagi.limite_credito)
print(miyagi.saldo_pagar)
print(daniel.nombre) #Imprime: Nariyoshi

# Nuevos valores asignados a atributos de la instancia

daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
daniel.email = "daniel@gmail.com"
daniel.limite_credito = 100000
daniel.saldo_pagar = 300000
print(daniel.nombre) #Imprime: Daniel
print(daniel.apellido)
print(daniel.email)
print(daniel.limite_credito)
print(daniel.saldo_pagar)

# Valores a nueva instancia
fabrizio.nombre = "fabrizio"
fabrizio.apellido = "ortiz"
fabrizio.email = "fabrizio@gmail.com"
fabrizio.limite_credito = 50000
fabrizio.saldo_pagar = 10000

# Imprimir nombre de cada instancia

print(miyagi.nombre)
print(daniel.nombre)
print(fabrizio.nombre)


