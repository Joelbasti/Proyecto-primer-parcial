#Integrantes:
#-Bastidas Merchan Joel
#-Tabares Piza Elkin
#-Velez Litardo Roberto
#-Villamar Muñiz Nohelia













#se importan los modulos que usara la subclase
from reserva import Reserva
from clientes import Clientes
from habitacion import Habitacion

#esta es una subclase
class ReservaSuite(Reserva):
#esta clase crea un objeto de tipo reserva suite
    def __init__(self, cod_reserva: int, cliente: Clientes, habitacion: Habitacion,
                 fecha_entrada: str, fecha_salida: str, num_noches: int,
                 estado: str, servicios_premium: list, tiene_jacuzzi: bool):
        #metodo super
        super().__init__(cod_reserva, cliente, habitacion, fecha_entrada,
                         fecha_salida, num_noches, estado)
        self._servicios_premium = servicios_premium
        self._tiene_jacuzzi = tiene_jacuzzi

    #metodos getter/setter & str
    @property
    def servicios_premium(self):
        return self._servicios_premium
    @servicios_premium.setter
    def servicios_premium(self, servicios: list):
        if not isinstance(servicios, list):
            raise ValueError("servicios_premium debe ser una lista")
        self._servicios_premium = servicios

    @property
    def tiene_jacuzzi(self):
        return self._tiene_jacuzzi
    @tiene_jacuzzi.setter
    def tiene_jacuzzi(self, valor: bool):
        if not isinstance(valor, bool):
            raise ValueError("tiene_jacuzzi debe ser True o False")
        self._tiene_jacuzzi = valor

    def calcular_costo(self) -> float:
        costo_base = self._habitacion.precio_noche * self._num_noches
        recargo = costo_base * 0.20
        costo_con_recargo = costo_base + recargo

        COSTO_SERVICIO = 15.0
        costo_servicios = len(self._servicios_premium) * COSTO_SERVICIO * self._num_noches

        COSTO_JACUZZI = 30.0
        costo_jacuzzi = COSTO_JACUZZI * self._num_noches if self._tiene_jacuzzi else 0

        costo_total = costo_con_recargo + costo_servicios + costo_jacuzzi
        return costo_total

    def mostrar_info(self) -> str:
        servicios = f"{len(self._servicios_premium)} servicios" if self._servicios_premium else "Sin servicios"
        jacuzzi = "✓ Con jacuzzi" if self._tiene_jacuzzi else "Sin jacuzzi"

        return (f"[SUITE] Reserva #{self._cod_reserva} | "
                f"Cliente: {self._cliente.nombres} {self._cliente.apellidos} | "
                f"Habitación: {self._habitacion.numero_habitacion} | "
                f"{servicios} | {jacuzzi} | "
                f"Costo: ${self.calcular_costo():.2f} | "
                f"Estado: {self._estado.capitalize()}")

    def __str__(self):
        costo_base = self._habitacion.precio_noche * self._num_noches
        recargo = costo_base * 0.20
        COSTO_SERVICIO = 15.0
        COSTO_JACUZZI = 30.0
        costo_servicios = len(self._servicios_premium) * COSTO_SERVICIO * self._num_noches
        costo_jacuzzi = COSTO_JACUZZI * self._num_noches if self._tiene_jacuzzi else 0

        servicios_str = ", ".join(self._servicios_premium) if self._servicios_premium else "Ninguno"
        jacuzzi_str = "Sí" if self._tiene_jacuzzi else "No"

        return (f"\n{'=' * 80}\n"
                f"RESERVA SUITE PREMIUM #{self._cod_reserva}\n"
                f"{'=' * 80}\n"
                f"Cliente: {self._cliente.nombres} {self._cliente.apellidos} (ID: {self._cliente.id_cliente})\n"
                f"Teléfono: {self._cliente.telefono} | Email: {self._cliente.email}\n"
                f"Habitación: N° {self._habitacion.numero_habitacion} - {self._habitacion.tipo.capitalize()}\n"
                f"Capacidad: {self._habitacion.capacidad} personas\n"
                f"Entrada: {self._fecha_entrada} | Salida: {self._fecha_salida} | Noches: {self._num_noches}\n"
                f"Servicios premium: {servicios_str}\n"
                f"Jacuzzi privado: {jacuzzi_str}\n"
                f"Estado: {self._estado.capitalize()}\n"
                f"--- Desglose de costos ---\n"
                f"Costo base: ${costo_base:.2f}\n"
                f"Recargo suite (20%): +${recargo:.2f}\n"
                f"Servicios premium: ${costo_servicios:.2f}\n"
                f"Jacuzzi: ${costo_jacuzzi:.2f}\n"
                f"COSTO TOTAL: ${self.calcular_costo():.2f}\n"
                f"{'=' * 80}")


def prueba_reserva_suite():
    print("=== Sistema de Reservas Suite ===", end="\n")

    try:
        #creacion de objetos de prueba
        cliente1 = Clientes(101, "0952871705", "Joel", "Bastidas", "0961454372", "joel@gmail.com")
        habitacion1 = Habitacion(501, "suite", 4, 150.00, "disponible")

        reserva1 = ReservaSuite(
            cod_reserva=1001,
            cliente=cliente1,
            habitacion=habitacion1,
            fecha_entrada="2024-12-15",
            fecha_salida="2024-12-18",
            num_noches=3,
            estado="confirmada",
            servicios_premium=["Spa", "Desayuno gourmet", "Minibar"],
            tiene_jacuzzi=True
        )

        print("--- Creando reserva ---")
        print(reserva1)

        print("--- Modificando servicios premium ---")
        reserva1.servicios_premium = ["Spa", "Cena romántica"]
        print(f"Nuevos servicios: {', '.join(reserva1.servicios_premium)}")
        print(f"Nuevo costo: ${reserva1.calcular_costo():.2f}")

        print(f"{reserva1.mostrar_info()}", end="\n")

    except ValueError as e:
        print(f"Error: {e}")
        #prueba de validaciones
    print("--- Pruebas de Validación ---")

    try:
        print("Intentando asignar servicios como string en lugar de lista...")
        reserva1.servicios_premium = "Spa"
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print("Intentando asignar jacuzzi como string en lugar de bool...")
        reserva1.tiene_jacuzzi = "si"
    except ValueError as e:
        print(f"Error: {e}")

    print("Programa finalizado")

#comando para llamar al menu de opciones
if __name__ == "__main__":
    prueba_reserva_suite()