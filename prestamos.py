prestamos = []


def menu_prestamos():

    while True:

        print("\n=== PRÉSTAMOS ===")
        print("1. Registrar préstamo")
        print("2. Registrar devolución")
        print("9. Volver")
        

        opcion = input("Seleccione una opción: ")

        match opcion:

            case "1":
                print("Función pendiente")

            case "2":
                print("Función pendiente")

            case "9":
                break
            case _:
                print("Opción inválida")
