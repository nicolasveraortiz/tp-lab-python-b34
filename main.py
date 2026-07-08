from gestion import *
from estadisticas import *
from validaciones import *

acciones = {
    1: ingresar_vehiculo,
    2: opcion_egresar,
    3: verificar_disp,
    4: mostrar_stats,
    5: modificar_tipo_vehiculo
}
           
opcion = None
while True:
    try:
        opcion = int(input("Menu de opciones: \n1. Ingresar vehiculo \n2. Egresar vehiculo "
                           "\n3. Verificar disponibilidad \n4. Revisar estadísticas "
                           "\n5. Modificar tipo de vehículo \n0. Cerrar el programa \nIngrese un número para avanzar: "))
        if opcion not in range(0, 6):
            raise ValueError #acá causo el error apropósito, asi se contemplan todos los casos que no estén dentro de ese rango
            
    except ValueError:
        print("Error: Debes ingresar un número del 0 al 5 para avanzar\n")
        continue 
    
    if opcion in acciones:
        acciones[opcion]()

    elif opcion == 0:
        vaciar_estacionamiento()
        mostrar_stats()
        break

    opcion = None

print("Se han guardado las estadísticas y se han quitado todos los vehiculos del estacionamiento. Gracias por usar el programa.")
