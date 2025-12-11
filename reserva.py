#Integrantes:
#-Bastidas Merchan Joel
#-Tabares Piza Elkin
#-Velez Litardo Roberto
#-Villamar Muñiz Nohelia






#se importan los modulos de agregacion y composicion
from clientes import Clientes
from habitacion import Habitacion

#esta es una superclase
class Reserva:
#esta clase crea un objeto de tipo reserva
    def __init__(self, cod_reserva: int, cliente: Clientes, habitacion: Habitacion,
                 fecha_entrada: str, fecha_salida: str, num_noches: int, estado: str):
        self._cod_reserva = cod_reserva
        self._cliente = cliente
        self._habitacion = habitacion
        self._fecha_entrada = fecha_entrada
        self._fecha_salida = fecha_salida
        self._num_noches = num_noches
        self._estado = estado

    #metodos getter/setter & str
    @property
    def cod_reserva(self):
        return self._cod_reserva
    @cod_reserva.setter
    def cod_reserva(self, codigo: int):
        if not isinstance(codigo, int):
            raise ValueError("El código debe ser un número entero")
        if codigo <= 0:
            raise ValueError("El código de reserva debe ser positivo")
        self._cod_reserva = codigo

    @property
    def cliente(self):
        return self._cliente
    @cliente.setter
    def cliente(self, cliente: Clientes):
        if not isinstance(cliente, Clientes):
            raise ValueError("Debe ser un objeto de tipo Clientes")
        self._cliente = cliente

    @property
    def habitacion(self):
        return self._habitacion
    @habitacion.setter
    def habitacion(self, habitacion: Habitacion):
        if not isinstance(habitacion, Habitacion):
            raise ValueError("Debe ser un objeto de tipo Habitacion")
        self._habitacion = habitacion

    @property
    def fecha_entrada(self):
        return self._fecha_entrada
    @fecha_entrada.setter
    def fecha_entrada(self, fecha: str):
        if not isinstance(fecha, str):
            raise ValueError("La fecha debe ser texto")
        if not fecha.strip():
            raise ValueError("La fecha de entrada no puede estar vacía")
        self._fecha_entrada = fecha.strip()

    @property
    def fecha_salida(self):
        return self._fecha_salida
    @fecha_salida.setter
    def fecha_salida(self, fecha: str):
        if not isinstance(fecha, str):
            raise ValueError("La fecha debe ser texto")
        if not fecha.strip():
            raise ValueError("La fecha de salida no puede estar vacía")
        self._fecha_salida = fecha.strip()

    @property
    def num_noches(self):
        return self._num_noches
    @num_noches.setter
    def num_noches(self, noches: int):
        if not isinstance(noches, int):
            raise ValueError("El número de noches debe ser un entero")
        if noches <= 0:
            raise ValueError("El número de noches debe ser mayor a 0")
        self._num_noches = noches

    @property
    def estado(self):
        return self._estado
    @estado.setter
    def estado(self, estado: str):
        if not isinstance(estado, str):
            raise ValueError("El estado debe ser texto")
        if not estado.strip():
            raise ValueError("El estado no puede estar vacío")
        estados_validos = ['pendiente', 'confirmada', 'cancelada', 'completada']
        if estado.lower() not in estados_validos:
            raise ValueError(f"Estado debe ser uno de: {', '.join(estados_validos)}")
        self._estado = estado.strip().lower()

    def calcular_costo(self) -> float:
        costo_base = self._habitacion.precio_noche * self._num_noches
        return costo_base

    def mostrar_info(self) -> str:
        return (f"Reserva #{self._cod_reserva} | Cliente: {self._cliente.nombres} {self._cliente.apellidos} | "
                f"Habitación: {self._habitacion.numero_habitacion} | Estado: {self._estado.capitalize()}")

    def __str__(self):
        return (f"\n{'=' * 80}\n"
                f"RESERVA #{self._cod_reserva}\n"
                f"{'=' * 80}\n"
                f"Cliente: {self._cliente.nombres} {self._cliente.apellidos} (ID: {self._cliente.id_cliente})\n"
                f"Habitación: N° {self._habitacion.numero_habitacion} - {self._habitacion.tipo.capitalize()}\n"
                f"Entrada: {self._fecha_entrada} | Salida: {self._fecha_salida} | Noches: {self._num_noches}\n"
                f"Estado: {self._estado.capitalize()}\n"
                f"Costo Total: ${self.calcular_costo():.2f}\n"
                f"{'=' * 80}")


def prueba_reserva():
    print("=== Sistema de Reservas ===\n")

    try:
        #creacion de objetos de prueba
        cliente1 = Clientes(101, "0952871705", "Joel", "Bastidas", "0961454372", "joel@gmail.com")
        cliente2 = Clientes(102, "0923456789", "María", "López", "0987654321", "maria@gmail.com")

        habitacion1 = Habitacion(201, "doble", 2, 80.00, "disponible")
        habitacion2 = Habitacion(305, "suite", 4, 150.00, "disponible")

        reserva1 = Reserva(
            cod_reserva=1001,
            cliente=cliente1,
            habitacion=habitacion1,
            fecha_entrada="2024-12-15",
            fecha_salida="2024-12-18",
            num_noches=3,
            estado="confirmada"
        )

        reserva2 = Reserva(
            cod_reserva=1002,
            cliente=cliente2,
            habitacion=habitacion2,
            fecha_entrada="2024-12-20",
            fecha_salida="2024-12-25",
            num_noches=5,
            estado="pendiente"
        )

        print("--- Reservas Creadas ---")
        print(reserva1)
        print(reserva2)

        print("--- Modificando estado de reserva 2 ---")
        reserva2.estado = "confirmada"
        print(f"Nuevo estado: {reserva2.estado}")
        print(reserva2.mostrar_info())

        print("--- Modificando número de noches de reserva 1 ---")
        reserva1.num_noches = 5
        print(f"Nuevas noches: {reserva1.num_noches}")
        print(f"Nuevo costo: ${reserva1.calcular_costo():.2f}")

    except ValueError as e:
        print(f"Error: {e}")
        #prueba de validaciones
    print("--- Pruebas de Validación ---")

    try:
        print("Intentando crear reserva con código negativo...")
        reserva_error = Reserva(-1, cliente1, habitacion1, "2024-12-15", "2024-12-18", 3, "confirmada")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print("Intentando asignar estado inválido...")
        reserva1.estado = "finalizada"
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print("Intentando asignar fecha vacía...")
        reserva1.fecha_entrada = ""
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print("Intentando asignar noches como string...")
        reserva1.num_noches = "tres"
    except ValueError as e:
        print(f"Error:{e}")

    print("Programa finalizado")

#comando para llamar al menu de opciones
if __name__ == "__main__":
    prueba_reserva()