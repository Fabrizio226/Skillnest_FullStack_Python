class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
       self.nombre = nombre
       self.email = email
       self.suscripcion = suscripcion
       self.lista_reproduccion = []

    def agregar_a_lista(self, titulo):
       """Agrega un contenido a la lista de reproducción del usuario."""
       self.lista_reproduccion.append(titulo)
       print(f"Titulo '{titulo}' agregado correctamente.")


    def ver_contenido(self, titulo):
       """Simula que el usuario reproduce un contenido."""
       for titulo in self.lista_reproduccion:
          print(f"El usuario {self.nombre} esta viendo '{titulo}'")
       else:
          print(f"Titulo no encontrado: {titulo}")


    def cambiar_suscripcion(self, nueva_suscripcion):
       """Cambia el tipo de suscripción del usuario."""
       subsAntigua = self.suscripcion
       self.suscripcion = nueva_suscripcion
       print(f"La suscripción cambió de {subsAntigua} a {nueva_suscripcion}")


    def mostrar_info_usuario(self):
       """Muestra la información del usuario y su lista de reproducción."""
       print(f"Nombre: {self.nombre}")
       print(f"Email: {self.email}")
       print(f"Suscripcion: {self.suscripcion}")
       if len(self.lista_reproduccion) == 0:
            print("La lista de reproducción esta vacia.")
       else:
            print(f"Lista de reproducción: n\- {"n\-".join(self.lista_reproduccion)}")

neiro = UsuarioStreaming("Neiro", "Neiro@gmail.com")
neiro.agregar_a_lista("Scream")
neiro.cambiar_suscripcion("Gratis")
neiro.ver_contenido("Scream")
neiro.mostrar_info_usuario()

mauro = UsuarioStreaming("Mauro", "Mauro@gmail.com")
mauro.agregar_a_lista("Rapidos y Furiosos")
mauro.cambiar_suscripcion("Estándar")
mauro.ver_contenido("Rapidos y Furiosos")
mauro.mostrar_info_usuario()

reo = UsuarioStreaming("Reo", "Reo@gmail.com")
reo.agregar_a_lista("Scary Movie")
reo.cambiar_suscripcion("Premium")
reo.ver_contenido("Scary Movie")
reo.mostrar_info_usuario()