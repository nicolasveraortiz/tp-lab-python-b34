from gestion import *
from estadisticas import *
from validaciones import *

acciones = {1: ingresar_vehiculo,
           2: opcion_egresar,
           3: buscar_patente,
           4: verificar_disp,
           5: mostrar_stats
           }
           
opcion = None
while True:
    try:
        opcion = int(input("Menu de opciones: \n1. Ingresar vehiculo \n2. Egresar vehiculo " \
        "\n3. Buscar patente  \n4. Verificar disponibilidad \n5. Revisar estadísticas \n0. Cerrar el programa \nIngrese un número para avanzar: "))
        if opcion not in range(0,6):
            raise ValueError
    except ValueError:
        print("Error: Debes ingresar un número del 0 al 5 para avanzar")
    if opcion in acciones:
        acciones[opcion]()

    elif opcion == 0:
        vaciar_estacionamiento()
        mostrar_stats()          # guarda en el archivo lo acumulado en esta sesión
        break

    opcion = None
print("Se han guardado las estadísticas y se han quitado todos los vehiculos del estacionamiento. Gracias por usar el programa.")