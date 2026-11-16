# Variables iniciales
Hora = 12
def ceil(x): 
    return int(-(-x // 1))
while True:
    print("")
    print("===== ESTACIONAMIENTO =====")
    print("1. Registrar ingreso")
    print("2. Terminar programa")

    Opcion = input("Selecciona una opción: ")

    # OPCIÓN 1: INGRESO
    if Opcion == "1":
        Hora = float(input("Hora de Entrada: "))
        Hora_Salida = float(input("Hora de salida: "))
        Tiempo = Hora_Salida-Hora
        Nombre = input("Nombre del Propietario: ")
        Placas = input("Placa del vehiculo: ")
        Tipo = int(input("1.Moto 2.Automóvil 3.Camioneta 4.Camión"))
        Tipo_Vehiculo=["Moto", "Automóvil", "Camioneta", "Camión"]
        match Tipo:
                case 1:
                    Costo=10
                    Importe = ceil(Tiempo)*Costo
                    print("Costo a pagar:", Importe)
                case 2:
                    Costo=15
                    Importe = ceil(Tiempo)*Costo
                    print("Costo a pagar:", Importe)
                case 3:
                    Costo=20
                    Importe = ceil(Tiempo)*Costo
                    print("Costo a pagar:", Importe)
                case 4:
                    Costo=30
                    Importe = ceil(Tiempo)*Costo
                    print("Costo a pagar:", Importe)
                case _:
                    print("Opción no valida")
        print("")
        print("Resumen")
        print("Nombre del Propietario:", Nombre)
        print("Placa del Vehiculo:", Placas)                            
        print("Hora registrada:", Hora)
        print("Tipo de vehiculo:", Tipo_Vehiculo[Tipo-1])
        print("Costo a pagar:", Importe)

    # OPCIÓN 2: TERMINAR
    elif Opcion == "2":

        print("Fin del programa")
        break

    else:
        print("Opción no válida")