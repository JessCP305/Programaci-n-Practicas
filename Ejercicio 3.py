Hora = 12
Precio=15
def ceil(x): 
    return int(-(-x // 1))
while Hora < 22:
    print("Registro")
    Hora = float(input("Hora de Entrada:"))
    Placas = input("Placas:")
    Nombre = input("Nombre del Propietario:")
    Hora_Salida = float(input("Hora de salida:"))
    Tiempo = Hora_Salida-Hora
    Pagar = ceil(Tiempo)*Precio
    print("")
    if Hora >= 22:
        print("Estacionamiento Cerrado")
    else:
        print("Resumen")
        print("Nombre del Propietario",Nombre)
        print("Placa del Vehiculo:", Placas)
        print("Hora registrada:", Hora)
        print("Tiempo transcurrido:", int(Tiempo*100)/100)
        print("Importe a pagar:", Pagar)
        print("")