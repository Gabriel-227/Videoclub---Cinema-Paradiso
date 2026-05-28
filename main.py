from peliculas import menu_peliculas
from socios import menu_socios
from prestamos import menu_prestamos
from proyecciones import menu_proyecciones
from recomendaciones import menu_recomendaciones


def menu_principal():

    while True:

        print("\n=== CINEMA PARADISO ===")
        print("1. Colección de películas")
        print("2. Socios")
        print("3. Prestamos")
        print("4. Proyecciones de los viernes")
        print("5. Recomendaciones de socios")
        print("0. Salir")

        opcion = input("¿Qué querés hacer?: ")

        match opcion:

            case "1":
                menu_peliculas()

            case "2":
                menu_socios()

            case "3":
                menu_prestamos()
               

            case "4":
                menu_proyecciones()
                

            case "5":
                menu_recomendaciones()
                

            case "0":
                print("Saliendo...")
                break

            case _:
                print("Opción inválida")


menu_principal()



