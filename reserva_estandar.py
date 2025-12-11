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
class ReservaEstandar(Reserva):
#esta clase crea un objeto de tipo reserva estandar
    def __init__(self, cod_reserva: int, cliente: Clientes, habitacion: Habitacion,
                 fecha_entrada: str, fecha_salida: str, num_noches: int,
                 estado: str, incluye_desayuno: bool):
        #metodo super
        super().__init__(cod_reserva, cliente, habitacion, fecha_entrada,
                         fecha_salida, num_noches, estado)
        self.incluye_desayuno = incluye_desayuno

    #metodo getter/setter &str
    @property
    def incluye_desayuno(self):
        return self._incluye_desayuno
    @incluye_desayuno.setter
    def incluye_desayuno(self, valor: bool):
        if not isinstance(valor, bool):
            raise ValueError("incluye_desayuno debe ser True o False")
        self._incluye_desayuno = valor

    def calcular_costo(self) -> float:
        costo_base = self._habitacion.precio_noche * self._num_noches
        descuento = costo_base * 0.05
        costo_con_descuento = costo_base - descuento

        if self._incluye_desayuno:
            costo_desayuno = 10.0 * self._num_noches
            costo_total = costo_con_descuento + costo_desayuno
        else:
            costo_total = costo_con_descuento

        return costo_total

    def mostrar_info(self) -> str:
        desayuno = "Con desayuno" if self._incluye_desayuno else "Sin desayuno"
        return (f"[ESTÁNDAR] Reserva #{self._cod_reserva} | "
                f"Cliente: {self._cliente.nombres} {self._cliente.apellidos} | "
                f"Habitación: {self._habitacion.numero_habitacion} | "
                f"{desayuno} | "
                f"Costo: ${self.calcular_costo():.2f} | "
                f"Estado: {self._estado.capitalize()}")

    def __str__(self):
        desayuno = "Sí" if self._incluye_desayuno else "No"
        costo_base = self._habitacion.precio_noche * self._num_noches
        descuento = costo_base * 0.05

        return (f"{'=' * 80}\n"
                f"RESERVA ESTÁNDAR #{self._cod_reserva}\n"
                f"{'=' * 80}\n"
                f"Cliente: {self._cliente.nombres} {self._cliente.apellidos} (ID: {self._cliente.id_cliente})\n"
                f"Teléfono: {self._cliente.telefono} | Email: {self._cliente.email}\n"
                f"Habitación: N° {self._habitacion.numero_habitacion} - {self._habitacion.tipo.capitalize()}\n"
                f"Capacidad: {self._habitacion.capacidad} personas\n"
                f"Entrada: {self._fecha_entrada} | Salida: {self._fecha_salida} | Noches: {self._num_noches}\n"
                f"Incluye desayuno: {desayuno}\n"
                f"Estado: {self._estado.capitalize()}\n"
                f"--- Desglose de costos ---\n"
                f"Costo base: ${costo_base:.2f}\n"
                f"Descuento (5%): -${descuento:.2f}\n"
                f"Desayuno: ${10.0 * self._num_noches if self._incluye_desayuno else 0:.2f}\n"
                f"COSTO TOTAL: ${self.calcular_costo():.2f}\n"
                f"{'=' * 80}")


def prueba_reserva_estandar():
    print("=== Sistema de Reservas Estándar ===")

    try:
        #creacion de objetos de prueba
        cliente1 = Clientes(101, "0952871705", "Joel", "Bastidas", "0961454372", "joel@gmail.com")
        cliente2 = Clientes(102, "0923456789", "María", "López", "0987654321", "maria@gmail.com")

        habitacion1 = Habitacion(201, "simple", 2, 60.00, "disponible")
        habitacion2 = Habitacion(305, "doble", 3, 80.00, "disponible")

        reserva1 = ReservaEstandar(
            cod_reserva=2001,
            cliente=cliente1,
            habitacion=habitacion1,
            fecha_entrada="2024-12-10",
            fecha_salida="2024-12-13",
            num_noches=3,
            estado="confirmada",
            incluye_desayuno=True
        )

        reserva2 = ReservaEstandar(
            cod_reserva=2002,
            cliente=cliente2,
            habitacion=habitacion2,
            fecha_entrada="2024-12-15",
            fecha_salida="2024-12-20",
            num_noches=5,
            estado="pendiente",
            incluye_desayuno=False
        )

        print("--- Reservas Estándar Creadas ---")
        print(reserva1)
        print(reserva2)

        print("--- Agregando desayuno a reserva 2 ---")
        reserva2.incluye_desayuno = True
        print(f"Desayuno incluido: {reserva2.incluye_desayuno}")
        print(f"Nuevo costo: ${reserva2.calcular_costo():.2f}")

        print("--- Información Resumida ---")
        print(reserva1.mostrar_info())
        print(reserva2.mostrar_info())

    except ValueError as e:
        print(f"Error: {e}")
            #prueba de validaciones
    print("--- Pruebas de Validación ---")

    try:
        print("Intentando asignar desayuno como string en lugar de bool...")
        reserva1.incluye_desayuno = "si"
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print("Intentando asignar desayuno como número...")
        reserva1.incluye_desayuno = 1
    except ValueError as e:
        print(f"Error: {e}")

    print("Programa finalizado")

#comando para llamar al menu de opciones
if __name__ == "__main__":
    prueba_reserva_estandar()