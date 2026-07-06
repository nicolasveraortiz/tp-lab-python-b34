from datetime import datetime
import math
from validaciones import *

CAPACIDAD = 10
estacionamiento = {}
for i in range(1, CAPACIDAD + 1): # nuestra variable para almacenar los vehiculos es un diccionario.
    estacionamiento[i] = None

metricas = {
    "total_atendidos": 0,
    "tiempo_total_permanencia": 0
}

TARIFA_POR_HORA = 1500.0

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
            
    for cochera in estacionamiento:
        if estacionamiento[cochera] is None:
            estacionamiento[cochera] = {
                "patente": patente,
                "hora_ingreso": datetime.now()
            }
            print(f"\n¡Ingreso exitoso! Vehículo asignado a la Cochera N° {cochera}.")
            return

def egresar_vehiculo():
    patente = leer_patente("Ingrese la patente del vehículo que egresa: ")
    
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
        
    horas_a_cobrar = math.ceil(minutos / 60)
    importe = horas_a_cobrar * TARIFA_POR_HORA
    
    metricas["total_atendidos"] += 1
    metricas["tiempo_total_permanencia"] += minutos
    
    estacionamiento[cochera_encontrada] = None
    
    print("\n" + "-"*35)
    print("        TICKET DE SALIDA        ")
    print("-"*35)
    print(f"Cochera Liberada : N° {cochera_encontrada}")
    print(f"Patente Vehículo : {patente}")
    print(f"Tiempo Total     : {minutos} minutos")
    print(f"Total a Abonar   : ${importe:.2f}")
    print("-"*35)

def buscar_patente(patente):
    print("en desarrollo!!!")

def verificar_disp():
    print("en desarrollo!!!!")
    