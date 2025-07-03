# 6 Avance_1_Grupo_12
#   KENDALL ELIAS QUIRÓS PANIAGUA
#   ANA SABRINA JIMENEZ BARQUERO
#   JOSE ANDRES RIVERA HERRERA


preguntar = True

while preguntar:
    print("MENÚ DE OPCIONES")
    print("1. Incluir")
    print("2. Consultar")
    print("3. Modificar")
    print("4. Borrar")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): \r\n")
 

    if opcion == "1":
        print("Elegiste la opcion: Incluir datos")
        precioventa = int(input("Cual es el precio de venta de los huevos? \r\n"))
        cantidadhuevos = int(input("Cual fue la cantidad de huevos producidos esta semana? \r\n"))
        gastosmantenimeinto = int(input("Cuantos fueron los gastos por mantenimeinto? \r\n"))
        gastosdeagua = int(input("Cuanto fue el gasto de agua? \r\n"))
        

    elif opcion == "2":
        print("Has elegido consultar datos.")
        resultadoventa = int(precioventa * cantidadhuevos)

        print(f"Para el dia de hoy tienes: {cantidadhuevos}")
        print(f"Y se espera recibir {resultadoventa} colones por la venta de estos huevos")


    elif opcion == "3":
        print("Has elegido modificar datos.")


    elif opcion == "4":
        print("Has elegido borrar datos.")


    elif opcion == "5":
        print("Saliendo del programa. ¡Adios!")

        break

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
