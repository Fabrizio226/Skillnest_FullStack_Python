class Usuario:
   def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

   def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
       self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido
   def aumentar_credito(self, aumento):
       self.limite_credito += aumento
   def cambiarCorreo(self, email):
       self.email = email


miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

miyagi.hacer_compra(2000)
print(f"Primera compra de {miyagi.nombre}: ${miyagi.saldo_pagar}")
segundacompra = 300
miyagi.hacer_compra(segundacompra)
print(f"Segunda compra: ${segundacompra}")
# Imprimir cuanto credito le queda a Miyagi
print(f"Credito disponible: ${miyagi.limite_credito - miyagi.saldo_pagar}")


# Compras de daniel, 2 compras y muestra saldo a pagar
print("----Compras de Daniel----")
daniel.hacer_compra(45)
print(daniel.saldo_pagar) #Imprime: 45

# Tarea
'''
1.- Crear un nuevo método que permita aumnetar el límite  de créditos 
Imprimir el nuevo limite de crédito.

2.- Crear un método que permita cambiar el correo de la instancia.
Mostrar el correo.
'''

miyagi.aumentar_credito(2000)
print(f"El nuevo aumento de {miyagi.apellido} es: ${miyagi.limite_credito}")

miyagi.cambiarCorreo("miyagi23@gmail.com")
print(f"El nuevo correo de {miyagi.apellido} es: {miyagi.email}")

