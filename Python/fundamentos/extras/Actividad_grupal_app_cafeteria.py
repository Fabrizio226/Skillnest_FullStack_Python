class CafeteriaCliente:
    total_clientes = 0  

    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos_acumulados = 0
        self.saldo_pendiente = 0
        self.tipo_membresia = "Bronce"

        CafeteriaCliente.total_clientes += 1

    def realizar_compra(self, monto):
        self.saldo_pendiente += monto
        puntos = (monto // 1000) * 10
        self.puntos_acumulados += puntos
        print(f"{self.nombre} realizó una compra de ${monto}. Puntos ganados: {puntos}.")

    def pagar_saldo(self, monto):
        if monto > self.saldo_pendiente:
            print(f"No se puede pagar más de lo que debe. Saldo pendiente: ${self.saldo_pendiente}")
        else:
            self.saldo_pendiente -= monto
            print(f"{self.nombre} pagó ${monto}. Saldo restante: ${self.saldo_pendiente}")

    @classmethod
    def mostrar_total_clientes(cls):
        print(f"Total de clientes registrados: {cls.total_clientes}")

    @staticmethod
    def validar_membresia(tipo):
        membresias_validas = ["Bronce", "Plata", "Oro"]
        return tipo in membresias_validas

cliente1 = CafeteriaCliente("Ana")
cliente2 = CafeteriaCliente("Luis")
cliente3 = CafeteriaCliente("María")

print("\n--- Prueba 1 ---")
cliente1.realizar_compra(3000)
cliente1.pagar_saldo(1000)

print("\n--- Prueba 2 ---")
cliente2.realizar_compra(1500)
cliente2.pagar_saldo(2000)

print("\n--- Prueba 3 ---")
CafeteriaCliente.mostrar_total_clientes()

print("\n--- Prueba 4 ---")
print("Validar membresía 'Plata':", CafeteriaCliente.validar_membresia("Plata"))
print("Validar membresía 'Diamante':", CafeteriaCliente.validar_membresia("Diamante"))

print("\n--- Estado final de clientes ---")
for cliente in [cliente1, cliente2, cliente3]:
    print(f"Cliente: {cliente.nombre}, Saldo: ${cliente.saldo_pendiente}, Puntos: {cliente.puntos_acumulados}, Membresía: {cliente.tipo_membresia}")