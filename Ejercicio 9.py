Capacidad = 30
Vehiculos_Dentro=0

while Vehiculos_Dentro<=30:
    print("")
    print("===== ESTACIONAMIENTO =====")
    print("1. Registrar ingreso")
    print("2. Mostrar cantidad de vehículos")
    print("3. Mostrar espacios disponibles")
    print("4. Terminar programa")

    Opcion = input("Selecciona una opción: ")

    # OPCIÓN 1: INGRESO
    if Opcion == "1":
            if Vehiculos_Dentro >= Capacidad:
                print("Estacionamiento lleno")
                print("No hay espacios disponibles")

            else:
                Nombre = input("Nombre del Propietario: ")
                Vehiculos_Dentro=Vehiculos_Dentro+1
                print("")
                print("Resumen")
                print("Nombre del Propietario:", Nombre)

    # OPCIÓN 2: CONTAR VEHÍCULOS
    elif Opcion == "2":
        print("Vehículos estacionados:", Vehiculos_Dentro)

    # OPCIÓN 3: ESPACIOS DISPONIBLES
    elif Opcion == "3":
        Disponibles = Capacidad - Vehiculos_Dentro
        print("Espacios disponibles:", Disponibles)

    # OPCIÓN 4: TERMINAR
    elif Opcion == "4":

        print("Fin del programa")
        break

    else:
        print("Opción no válida")