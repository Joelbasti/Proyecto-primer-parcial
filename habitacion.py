#Integrantes:
#-Bastidas Merchan Joel
#-Tabares Piza Elkin
#-Velez Litardo Roberto
#-Villamar Muñiz Nohelia


#esta es una clase de composicion
class Habitacion:
#esta clase crea un objeto de tipo habitacion
    def __init__(self, numero_habitacion: int, tipo: str, capacidad: int, precio_noche: float, estado: str):
        self._numero_habitacion = numero_habitacion
        self._tipo = tipo
        self._capacidad = capacidad
        self._precio_noche = precio_noche
        self._estado = estado

    #metodos getter/setter & str
    @property
    def numero_habitacion(self):
        return self._numero_habitacion
    @numero_habitacion.setter
    def numero_habitacion(self, numero: int):
        if not isinstance(numero, int):
            raise ValueError("El número de habitación debe ser un entero")
        if numero <= 0:
            raise ValueError("El número de habitación debe ser positivo")
        self._numero_habitacion = numero

    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, tipo: str):
        if not isinstance(tipo, str):
            raise ValueError("El tipo debe ser texto")
        if not tipo.strip():
            raise ValueError("El tipo de habitación no puede estar vacío")
        self._tipo = tipo.strip().lower()

    @property
    def capacidad(self):
        return self._capacidad
    @capacidad.setter
    def capacidad(self, capacidad: int):
        if not isinstance(capacidad, int):
            raise ValueError("La capacidad debe ser un número entero")
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor a 0")
        self._capacidad = capacidad

    @property
    def precio_noche(self):
        return self._precio_noche
    @precio_noche.setter
    def precio_noche(self, precio: float):
        if not isinstance(precio, (int, float)):
            raise ValueError("El precio debe ser un número")
        if precio <= 0:
            raise ValueError("El precio por noche debe ser positivo")
        self._precio_noche = float(precio)

    @property
    def estado(self):
        return self._estado
    @estado.setter
    def estado(self, estado: str):
        if not isinstance(estado, str):
            raise ValueError("El estado debe ser texto")
        if not estado.strip():
            raise ValueError("El estado no puede estar vacío")
        estados_validos = ['disponible', 'ocupada', 'mantenimiento']
        if estado.lower() not in estados_validos:
            raise ValueError(f"Estado debe ser uno de: {', '.join(estados_validos)}")
        self._estado = estado.strip().lower()


    def __str__(self):
        return (f"Habitación N° {self._numero_habitacion} | Tipo: {self._tipo.capitalize()} | "
                f"Precio/noche: ${self._precio_noche:.2f} | Capacidad: {self._capacidad} personas | "
                f"Estado: {self._estado.capitalize()}")

if __name__ == "__main__":
    print("=== Sistema de Gestión de Habitaciones ===")
def prueba_habitaciones():
    try:
        #creación de objetos de prueba
        hab1 = Habitacion(101, "simple", 2, 50.00, "disponible")
        hab2 = Habitacion(201, "doble", 3, 80.00, "disponible")
        hab3 = Habitacion(301, "suite", 4, 150.00, "ocupada")
        hab4 = Habitacion(401, "presidencial", 6, 250.00, "mantenimiento")

        print("--- Habitaciones Registradas ---\n")
        habitaciones = [hab1, hab2, hab3, hab4]
        for i, hab in enumerate(habitaciones, 1):
            print(f"{i}. {hab}")

        print("\n--- Modificando habitación 301 ---")
        hab3.estado = "disponible"
        hab3.precio_noche = 160.00
        print(f"Estado actualizado: {hab3.estado}")
        print(f"Precio actualizado: ${hab3.precio_noche:.2f}")
        print(hab3)

        print("\n--- Habitaciones Disponibles ---")
        disponibles = [h for h in habitaciones if h.estado == 'disponible']
        for i, hab in enumerate(disponibles, 1):
            print(f"{i}. {hab}")

    except ValueError as e:
        print(f"Error: {e}")

        #prueba de validaciones de los setter
    print("--- Pruebas de Validación ---")

    try:
        print("Intentando crear habitación con número negativo...")
        hab_error = Habitacion(-5, "simple", 2, 50.00, "disponible")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print("Intentando asignar tipo vacío...")
        hab1.tipo = ""
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print("Intentando asignar precio como string...")
        hab1.precio_noche = "cincuenta"
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print("Intentando asignar estado inválido...")
        hab1.estado = "limpieza"
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print("Intentando asignar capacidad negativa...")
        hab1.capacidad = -2
    except ValueError as e:
        print(f"Error: {e}")

    print("Programa finalizado")
if __name__ == "__main__":
    prueba_habitaciones()