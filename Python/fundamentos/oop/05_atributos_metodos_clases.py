# Atributos; métodos de clase, métodos estáticos

# Función repaso.
# Crear una función que valide usuario y contraseña

def validadordeusuario(user, password):
    if user == "matias123" and password == "matias123":
        print(f"Bienvenido, {user}!")
        return True
    else:
        print("Acceso denegado")
        return False

def enviarDatos():
    usrname = input("Ingrese su nombre de ususario: ")
    password = input("Ingrese su contraseña: ")
    validador = validadordeusuario(usrname, password)

enviarDatos()

# Definición de la calse 
class estudiante:
    #Atributo de clase
    colegio = "Liceo Vate Vicente Huidobro"
    # Lista en donde se muestra todos los estudiantes
    # La lista en donde estan todos los estudiantes
    Estudiantes = []

    # Metodo constructor 
    def __init__(self, nombre, nota):
        #Atributos de la instancia
        self.nombre = nombre
        self.nota = nota

# Metodo de instancia

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")
    # Agregar alumnos a la lista de estudiantes
        estudiante.Estudiantes.append(self)

    # Metodo de clase
    # Usa "CLS" porque trabaja con información de la clase
    @classmethod
    def cambiar_colegio(cls, nuevo_nombre):
        cls.colegio = nuevo_nombre

    @classmethod # Contar la cantidad de estudiantes
    def cantidad_estudiantes(cls):
        return len(cls.Estudiantes)
    # Metodo estático
    # Este no usa CLS ni SELF, solo parametros
    @staticmethod
    def aprobar(nota):
        if nota >= 4.0:
            return True
        else:
            return False

# Creación de objetos (Instancias)
e1 = estudiante("Donovan", 4.0)
e2 = estudiante("Randy", 6.7)
e3 = estudiante("Lusu", 3.9)

# Uso de métodos de instancias
print("== MÉTODO DE INSTANCIAS ==")
# Mostrar datos de estudiantes
e1.mostrar_info()
print()
e2.mostrar_info()
print()
e3.mostrar_info
print()

# Atributo de clase
print("== ATRIBUTO DE CLASE ==")
print(e1.colegio)
print(e2.colegio)
print(e3.colegio)
print()

# Uso de método de clase
print("== MÉTODO DE CLASE ==")
estudiante.cambiar_colegio("Purkuyen")
e1.colegio = "VVH" # Modifica el atributo de la instancia en la clase
print(e1.colegio)
print(e2.colegio)
print(e3.colegio)

# Contar estudiantes
print("== CONTAR ESTUDIANTES ==")
print(f"total de estudiantes: {estudiante.cantidad_estudiantes()}")

# Método estatico

print("=== MÉTODO ESTÁTICO ===")

print(f"¿{e1.nombre} aprueba?")
print(estudiante.aprobar(e1.nota))
print()

print(f"¿{e2.nombre} aprueba?")
print(estudiante.aprobar(e2.nota))
print()

print(f"¿{e3.nombre} aprueba?")
print(estudiante.aprobar(e3.nota))
print()