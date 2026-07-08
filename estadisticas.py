from gestion import *

ARCHIVO_STATS = "estadisticas.txt"

def mostrar_stats():
    try:
        archivo = open(ARCHIVO_STATS, "r")
        linea1 = archivo.readline()  # primera línea: total atendidos
        linea2 = archivo.readline()  # segunda línea: ganancias
        linea3 = archivo.readline()  # tercera línea: tiempo total
        linea4 = archivo.readline()  # cuarta línea: total motos
        linea5 = archivo.readline()  # quinta línea: total autos
        linea6 = archivo.readline()  # sexta línea: total camionetas
        archivo.close()

        atendidos_anteriores = int(linea1)
        ganancias_anteriores = float(linea2)
        tiempo_anterior = int(linea3)
        motos_anteriores = int(linea4) if linea4 != "" else 0
        autos_anteriores = int(linea5) if linea5 != "" else 0
        camionetas_anteriores = int(linea6) if linea6 != "" else 0
    except (FileNotFoundError, ValueError):
        atendidos_anteriores = 0
        ganancias_anteriores = 0.0
        tiempo_anterior = 0
        motos_anteriores = 0
        autos_anteriores = 0
        camionetas_anteriores = 0

    total_atendidos = atendidos_anteriores + metricas["total_atendidos"]
    acumulador_ganancias = ganancias_anteriores + metricas["acumulador_ganancias"]
    tiempo_total_permanencia = tiempo_anterior + metricas["tiempo_total_permanencia"]
    total_motos = motos_anteriores + metricas["total_motos"]
    total_autos = autos_anteriores + metricas["total_autos"]
    total_camionetas = camionetas_anteriores + metricas["total_camionetas"]

    archivo = open(ARCHIVO_STATS, "w")
    archivo.write(str(total_atendidos) + "\n")
    archivo.write(str(acumulador_ganancias) + "\n")
    archivo.write(str(tiempo_total_permanencia) + "\n")
    archivo.write(str(total_motos) + "\n")
    archivo.write(str(total_autos) + "\n")
    archivo.write(str(total_camionetas) + "\n")
    archivo.close()

    metricas["total_atendidos"] = 0
    metricas["acumulador_ganancias"] = 0
    metricas["tiempo_total_permanencia"] = 0
    metricas["total_motos"] = 0
    metricas["total_autos"] = 0
    metricas["total_camionetas"] = 0

    print("\n" + "="*35)
    print("      ESTADÍSTICAS TOTALES       ")
    print("="*35)
    print(f" Vehículos atendidos   : {total_atendidos}")
    print(f" Ganancias acumuladas  : ${acumulador_ganancias:.2f}")
    print("-" * 35)
    print(f" Motos ingresadas      : {total_motos}")
    print(f" Autos ingresados      : {total_autos}")
    print(f" Camionetas ingresadas : {total_camionetas}")
    print("-" * 35)

    if total_atendidos > 0:
        promedio = tiempo_total_permanencia / total_atendidos
        print(f" Tiempo promedio       : {promedio:.2f} minutos")
    else:
        print(" Tiempo promedio       : Sin datos aún")

    print("="*35)