class SuscripcionStreaming:
    costos_suscripcion = {"Gratis": 0, "Estandar": 5.99, "Premium": 10.99}

    def __init__(self, usuario, tipo_suscripcion="Gratis"):
        self.usuario = usuario
        self.tipo_suscripcion = tipo_suscripcion
        self.costo_mensual = self.costos_suscripcion[tipo_suscripcion]
        self.saldo_pendiente = self.costo_mensual

    def realizar_pago(self, monto):
        self.saldo_pendiente -= monto
        if self.saldo_pendiente < 0:
            self.saldo_pendiente = 0
        print(f"Usuario: {self.usuario}")
        print(f"Monto pagado: {monto}")
        print(f"Saldo actual: {self.saldo_pendiente}")

    def cambiar_suscripcion(self, nuevo_tipo):
        self.tipo_suscripcion = nuevo_tipo
        self.costo_mensual = self.costos_suscripcion[nuevo_tipo]
        self.saldo_pendiente = self.costo_mensual
        print(f"Cambio de suscripción a: {nuevo_tipo}")

    def ver_contenido_exclusivo(self):
        if self.tipo_suscripcion == "Gratis":
            print("Acceso denegado al contenido, suscríbete :c")
        else:
            print(f"Acceso permitido al contenido exclusivo para :D {self.usuario}")

    def mostrar_info_suscripcion(self):
        print(f"Nombre: {self.usuario}")
        print(f"Suscripción: {self.tipo_suscripcion}")
        print(f"Costo: {self.costo_mensual}")
        print(f"Saldo: {self.saldo_pendiente}")

user1 = SuscripcionStreaming("XxLoboSolitarioxX", "Gratis")
user1.ver_contenido_exclusivo()
user1.cambiar_suscripcion("Estandar")
user1.realizar_pago(5.99)
user1.mostrar_info_suscripcion()

user2 = SuscripcionStreaming("Atlas777", "Estandar")
user2.ver_contenido_exclusivo()
user2.cambiar_suscripcion("Premium")
user2.realizar_pago(5.00)
user2.realizar_pago(10.00)
user2.mostrar_info_suscripcion()

user3 = SuscripcionStreaming("NoobyLol15", "Premium")
user3.realizar_pago(2.50)
user3.ver_contenido_exclusivo()
user3.mostrar_info_suscripcion()