# Actividad: Gestor de inventario


#1.- Creación: Crear una lista llamada inventario que contenga los siguientes articulos
# Articulos = ["laptop", "ratón", "monitor", "cable hdmi"]

inventario = ["laptop", "ratón", "monitor", "cable hdmi"]
print(inventario)

#2.- Expansión: Utiliza el método correspondiente para agregar "impresora" y "teclado" al final de la lista.

inventario.append("impresora")
inventario.append("teclado")
print(inventario)

#3.- Conteo: Utiliza la función integrada para mostar cuantos elementos totales hay en la lista.

print(len(inventario))

#4.- Acceso y modificación: modifica "teclado" por "teclado mecánico"

inventario[5] = "teclado mecanico"
print(inventario)

#5.- Slicing: Crea una nueva lista llamada "promoción", deben contener solo los 3 primeros elementos de la lista "inventario".

promocion = ["laptop", "ratón", "monitor", "cable hdmi"]

print(promocion[:3])

#6.- Mostrar la lista de inventario ordenado alfabeticamente

inventario.sort()
print(inventario)

#7.- Elimina el último elemento de la lista inventario mostrando el elemento eliminado y la lista final.

eliminado = inventario.pop
print("articulo eliminado: " ,eliminado)
print(inventario)