#Integrantes:
#-Bastidas Merchan Joel
#-Tabares Piza Elkin
#-Velez Litardo Roberto
#-Villamar Muñiz Nohelia



#se importan todos los modulos para ejecutar ls pruebas de cada clase
from clientes import prueba_clientes
from habitacion import prueba_habitaciones
from reserva import prueba_reserva
from reserva_estandar import prueba_reserva_estandar
from reserva_suite import prueba_reserva_suite

#funcion para mostrar el menu de pruebas
def mostrar_menu():

    print("" + "=" * 60)
    print(" " * 10 + "SISTEMA DE GESTIÓN HOTELERA")
    print("=" * 60)
    print("Seleccione la prueba que desea ejecutar:")
    print("1. Prueba de Clientes")
    print("2. Prueba de Habitaciones")
    print("3. Prueba de Reserva Base")
    print("4. Prueba de Reserva Estándar")
    print("5. Prueba de Reserva Suite")
    print("0. Salir")
    print("=" * 60)


def main():
    while True:
        #bucle while para que se muestre el menu hasta que se ingrese un valor valido
        mostrar_menu()

        try:
            opcion = input("Ingrese su opción: ").strip()

            if opcion == "0":
                print("" + "=" * 60)
                print(" " * 15 + "¡Gracias por usar el sistema!")
                print("=" * 60 + "")
                break

            elif opcion == "1":
                prueba_clientes()

            elif opcion == "2":
                prueba_habitaciones()

            elif opcion == "3":
                prueba_reserva()

            elif opcion == "4":
                prueba_reserva_estandar()

            elif opcion == "5":
                prueba_reserva_suite()

            else:
                print("Opción no válida. Por favor, seleccione una opción del menú.")
                continue

            if opcion != "5":
                input("Presione ENTER para volver al menú principal...")

        except KeyboardInterrupt:
            print("Interrupción detectada. Cerrando el sistema...")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")
            input("Presione ENTER para continuar...")

#comando para llamar al menu de opciones
if __name__ == "__main__":
    main()