#Integrantes:
#-Bastidas Merchan Joel
#-Tabares Piza Elkin
#-Velez Litardo Roberto
#-Villamar Muñiz Nohelia



#esta es una clase de agregacion
class Clientes:
#esta clase crea un objeto de tipo cliente
    def __init__(self, id_cliente: int, cedula: str, nombres: str, apellidos: str, telefono: str, email: str):
        self._id_cliente = id_cliente
        self._cedula = cedula
        self._nombres = nombres
        self._apellidos = apellidos
        self._telefono = telefono
        self._email = email


    #metodos getter/settter & str
    @property
    def id_cliente(self):
        return self._id_cliente
    @id_cliente.setter
    def id_cliente(self, nuevo_id_cliente: int):
        if not isinstance(nuevo_id_cliente, int):
            raise ValueError("El ID debe ser un número entero")
        if nuevo_id_cliente <= 0:
            raise ValueError("El ID debe ser mayor a 0")
        self._id_cliente = nuevo_id_cliente

    @property
    def cedula(self):
        return self._cedula
    @cedula.setter
    def cedula(self, nueva_cedula: str):
        if not isinstance(nueva_cedula, str):
            raise ValueError("La cédula debe ser un texto")
        if not nueva_cedula.strip():
            raise ValueError("La cédula no puede estar vacía")
        self._cedula = nueva_cedula.strip()

    @property
    def nombres(self):
        return self._nombres
    @nombres.setter
    def nombres(self, nuevo_nombres: str):
        if not isinstance(nuevo_nombres, str):
            raise ValueError("Los nombres deben ser texto")
        if not nuevo_nombres.strip():
            raise ValueError("Los nombres no pueden estar vacíos")
        self._nombres = nuevo_nombres.strip()

    @property
    def apellidos(self):
        return self._apellidos
    @apellidos.setter
    def apellidos(self, nuevo_apellidos: str):
        if not isinstance(nuevo_apellidos, str):
            raise ValueError("Los apellidos deben ser texto")
        if not nuevo_apellidos.strip():
            raise ValueError("Los apellidos no pueden estar vacíos")
        self._apellidos = nuevo_apellidos.strip()

    @property
    def telefono(self):
        return self._telefono
    @telefono.setter
    def telefono(self, nuevo_telefono: str):
        if not isinstance(nuevo_telefono, str):
            raise ValueError("El teléfono debe ser texto")
        if not nuevo_telefono.strip():
            raise ValueError("El teléfono no puede estar vacío")
        self._telefono = nuevo_telefono.strip()

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, nuevo_email: str):
        if not isinstance(nuevo_email, str):
            raise ValueError("El email debe ser texto")
        if not nuevo_email.strip():
            raise ValueError("El email no puede estar vacío")
        self._email = nuevo_email.strip()

    def __str__(self):
        return (f"ID: {self._id_cliente} | Cédula: {self._cedula} | Nombres: {self._nombres} "
                f"| Apellidos: {self._apellidos} | Teléfono: {self._telefono} | Email: {self._email}")


def prueba_clientes():
    print("=== Sistema de Gestión de Clientes ===")

    try:
        #creacion de objetos de prueba
        cliente1 = Clientes(123, "0952871705", "Joel", "Bastidas", "0961454372", "joelbasti23@gmail.com")
        cliente2 = Clientes(456, "0923456789", "María", "López", "0987654321", "maria.lopez@gmail.com")
        cliente3 = Clientes(789, "0934567890", "Carlos", "Pérez", "0976543210", "carlos.perez@gmail.com")

        print("--- Clientes Registrados ---")
        print(cliente1)
        print(cliente2)
        print(cliente3)

        print("--- Modificando datos del cliente 1 ---")
        cliente1.telefono = "0999888777"
        cliente1.email = "joel.nuevo@gmail.com"
        print(cliente1)

    except ValueError as e:
        print(f"Error al crear cliente: {e}")

        #Prueba de validaciones
    print("--- Pruebas de Validación ---")

    try:
        print("Intentando crear cliente con ID inválido (string)...")
        cliente_error = Clientes("abc", "0952871705", "Test", "Usuario", "0961454372", "test@gmail.com")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print("Intentando crear cliente con nombre vacío...")
        cliente_error2 = Clientes(999, "0952871705", "", "Usuario", "0961454372", "test@gmail.com")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print("Intentando asignar ID negativo...")
        cliente1.id_cliente = -5
    except ValueError as e:
        print(f"Error: {e}")

    print("Programa finalizado")

#comando para llamar al menu de opciones
if __name__ == "__main__":
    prueba_clientes()