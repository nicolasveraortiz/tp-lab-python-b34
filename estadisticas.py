from gestion import *

ARCHIVO_STATS = "estadisticas.txt"

def mostrar_stats():
    try:
        archivo = open(ARCHIVO_STATS, "r")
        linea1 = archivo.readline()  # primera línea: total atendidos
        linea2 = archivo.readline()  # segunda línea: ganancias
        linea3 = archivo.readline()  # tercera línea: tiempo total
        archivo.close()

        atendidos_anteriores = int(linea1)
        ganancias_anteriores = float(linea2)
        tiempo_anterior = int(linea3)
    except FileNotFoundError:
        atendidos_anteriores = 0
        ganancias_anteriores = 0.0
        tiempo_anterior = 0

    total_atendidos = atendidos_anteriores + metricas["total_atendidos"]
    acumulador_ganancias = ganancias_anteriores + metricas["acumulador_ganancias"]
    tiempo_total_permanencia = tiempo_anterior + metricas["tiempo_total_permanencia"]

    archivo = open(ARCHIVO_STATS, "w")
    archivo.write(str(total_atendidos) + "\n")
    archivo.write(str(acumulador_ganancias) + "\n")
    archivo.write(str(tiempo_total_permanencia) + "\n")
    archivo.close()

    metricas["total_atendidos"] = 0
    metricas["acumulador_ganancias"] = 0
    metricas["tiempo_total_permanencia"] = 0

    print("\n" + "="*35)
    print("      ESTADÍSTICAS DEL DÍA       ")
    print("="*35)
    print(f" Vehículos atendidos   : {total_atendidos}")
    print(f" Ganancias acumuladas  : ${acumulador_ganancias:.2f}")

    if total_atendidos > 0:
        promedio = tiempo_total_permanencia / total_atendidos
        print(f" Tiempo promedio       : {promedio:.2f} minutos")
    else:
        print(" Tiempo promedio       : Sin datos aún")

    print("="*35)