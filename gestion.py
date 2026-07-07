from datetime import datetime
import math
from validaciones import *

# constantes
CAPACIDAD = 10 
TARIFA_POR_HORA = 1500.0
TARIFA_MOTO = 1000.0
TARIFA_AUTO = 1500.0 
TARIFA_CAMIONETA = 2000.0

# variables
estacionamiento = {}
for i in range(1, CAPACIDAD + 1): # nuestra variable para almacenar los vehiculos es un diccionario.
    estacionamiento[i] = None

metricas = {
    "total_atendidos": 0,
    "tiempo_total_permanencia": 0,
    "acumulador_ganancias": 0
}

def ingresar_vehiculo():
    libres = 0
    for cochera in estacionamiento:
        if estacionamiento[cochera] is None:
            libres += 1
            
    if libres == 0:
        print("\nError: El estacionamiento está completamente lleno.")
        return

    patente = leer_patente("Ingrese la patente del vehículo (AAA123 o AA123AA): ")
    
    for cochera in estacionamiento:
        datos = estacionamiento[cochera]
        if datos is not None and datos["patente"] == patente:
            print(f"\nError: El vehículo con patente {patente} ya está dentro del establecimiento.")
            return
            
    tipo = ""
    while tipo not in ["MOTO", "AUTO", "CAMIONETA"]:
        tipo = input("Ingrese tipo de vehiculo (MOTO / AUTO / CAMIONETA): "). strip()
        if tipo not in ["MOTO", "AUTO", "CAMIONETA"]:
            print("Error: Tipo de vehiculo invalido. Intente nuevamente.")

    for cochera in estacionamiento:
        if estacionamiento[cochera] is None:
            estacionamiento[cochera] = {
                "patente": patente,
                "tipo": tipo,
                "hora_ingreso": datetime.now()
            }
            print(f"\n¡Ingreso exitoso! Vehículo asignado a la Cochera N° {cochera}.")
            return

def egresar_vehiculo(patente):
    cochera_encontrada = None
    for cochera in estacionamiento:
        datos = estacionamiento[cochera]
        if datos is not None and datos["patente"] == patente:
            cochera_encontrada = cochera
            break
            
    if cochera_encontrada is None:
        print(f"\nError: No se encontró ningún vehículo registrado con la patente {patente}.")
        return
        
    datos = estacionamiento[cochera_encontrada]
    # calculo de minuto
    diferencia = datetime.now() - datos["hora_ingreso"]
    minutos = math.ceil(diferencia.total_seconds() / 60)
    # para el uso de la libreria math, nos hicimos de la ayuda de la IA

    if minutos == 0: # evitamos el error division por cero
        minutos = 1

    horas_estadia = minutos // 60
    minutos_estadia = minutos % 60 


    horas_a_cobrar = math.ceil(minutos / 60)

    tipo_vehiculo = datos["tipo"]
    if tipo_vehiculo == "MOTO": 
        tarifa_aplicada = TARIFA_MOTO
    elif tipo_vehiculo == "AUTO":
        tarifa_aplicada = TARIFA_AUTO
    else: 
        tarifa_aplicada = TARIFA_CAMIONETA 
    importe = horas_a_cobrar * tarifa_aplicada 
    metricas["acumulador_ganancias"] += importe
    metricas["total_atendidos"] += 1
    metricas["tiempo_total_permanencia"] += minutos
    
    estacionamiento[cochera_encontrada] = None
    
    print("\n" + "-"*35)
    print("        TICKET DE SALIDA        ")
    print("-"*35)
    print(f"Cochera Liberada : N° {cochera_encontrada}")
    print(f"Patente Vehículo : {patente}")
    print(f"Tipo Vehiculo    : {tipo_vehiculo}")
    print(f"Tiempo Total     : {horas_estadia} hs y {minutos_estadia} minutos")
    print(f"Total a Abonar   : ${importe:.2f}")
    print("-"*35)

def opcion_egresar():
    patente = leer_patente("Ingrese la patente del vehículo que egresa: ")
    egresar_vehiculo(patente)

def buscar_patente():
    print("\n" + "="*35)
    print("      VEHÍCULOS ESTACIONADOS     ")
    print("="*35)
    
    hay_ocupados = False
    for i in range(1, CAPACIDAD + 1):
        if estacionamiento[i] is not None:
            datos = estacionamiento[i]
            print(f"Estacionamiento N° {i} -> Patente: {datos['patente']}")
            hay_ocupados = True
            
    if not hay_ocupados:
        print("No hay vehículos registrados en este momento.")
    print("="*35)

def verificar_disp():
    libres = 0
    ocupados = 0
    for cochera in estacionamiento:
        if estacionamiento[cochera] is None:
            libres += 1
        else:
            ocupados += 1
            
    print("\n" + "="*35)
    print("    ESTADO DE DISPONIBILIDAD    ")
    print("="*35)
    print(f" Cocheras Libres   : {libres}")
    print(f" Cocheras Ocupadas : {ocupados}")
    print(f" Capacidad Total   : {CAPACIDAD}")
    print("="*35)

def vaciar_estacionamiento():
    # Recorremos las llaves (números de cochera) del diccionario
    for cochera in estacionamiento:
        datos = estacionamiento[cochera]
        
        # Primero verificamos si hay un auto adentro (si no es None)
        if datos is not None:
            # Extraemos la patente accediendo de forma correcta al sub-diccionario
            patente = datos["patente"]
            # Ejecutamos el egreso para que liquide el cobro e impacte las estadísticas
            egresar_vehiculo(patente)