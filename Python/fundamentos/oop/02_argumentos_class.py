# ➡️ Pasar argumentos 
# Para poder personalizar nuestras instancia vamos a pasar algunos argumentos al método __init__ 
# y que de esta manera podamos asignarle a los atributos los valores correspondientes.

class Usuario:
   def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

# Creación de la instancias
 
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 30000, 0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 100000, 300000)
fabrizio = Usuario("Fabrizio", "Ortiz", "Fabrizio@gmail.com", 50000, 10000)

# Imprimir valores
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel

#--- Tarea rápida
'''
Crear una clase Estudiante, y asignarle los siguientes atributos:
(rut, nombre, apellido, especialidad, fecha_nac)
Crear 3 instancias para la clase con distintos estudiantes
Imprimir el nombre y apellido concatenado + especialidad
'''

class Estudiante:
   def __init__(self, rut, nombre, apellido, especialidad, fecha_nac):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.fecha_nac = fecha_nac

Luis = Estudiante("21.345.766-6", "Luis", "Contreras", "Programación", "04-04-2008")
Adrian = Estudiante("28.367.565-4", "Adrian", "Salas", "Contabilidad", "15-08-2008")
Matias = Estudiante("23.677.878-k", "Matias", "Ramirez", "Administración Logistica", "15-08-2008")

print(Luis.rut)
print(Luis.nombre)
print(Luis.apellido)
print(Luis.especialidad)
print(Luis.fecha_nac)

print(Adrian.rut)
print(Adrian.nombre)
print(Adrian.apellido)
print(Adrian.especialidad)
print(Adrian.fecha_nac)

print(Matias.rut)
print(Matias.nombre)
print(Matias.apellido)
print(Matias.especialidad)
print(Matias.fecha_nac)

print(f"{Luis.nombre} {Luis.apellido} estudia {Luis.especialidad}")
print(f"{Adrian.nombre} {Adrian.apellido} estudia {Adrian.especialidad}")
print(f"{Matias.nombre} {Matias.apellido} estudia {Matias.especialidad}")