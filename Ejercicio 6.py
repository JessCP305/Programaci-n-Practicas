Hora = 8
def ceil(x): 
    return int(-(-x // 1))
while Hora < 22:
    print("Registro")
    Hora = float(input("Hora de Entrada:"))
    Placas = input("Placas:")
    Nombre = input("Nombre del Propietario:")
    Hora_Salida = float(input("Hora de salida:"))
    Tiempo = Hora_Salida-Hora
    opciones = int(input("1.Moto 2.Automóvil 3.Camioneta 4.Camión"))
    match opciones:
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
    if Hora >= 22:
        print("Estacionamiento Cerrado")
    else:
        print("Resumen")
        print("Nombre del Propietario",Nombre)
        print("Placa del Vehiculo:", Placas)
        print("Hora registrada:", Hora)
        print("Tiempo transcurrido:", int(Tiempo*100)/100)
        print("Importe a pagar:", Importe)
        print("")