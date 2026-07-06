# Sistema de Gestión de Estacionamiento - Laboratorio de Python

## Descripción General
Este sistema fue desarrollado en Python para ejecutarse exclusivamente a través de la consola. Su objetivo principal es administrar el funcionamiento integral de un estacionamiento, permitiendo el registro de ingreso y egreso de vehículos, el cálculo automatizado del tiempo de permanencia, el control estricto de los espacios disponibles en tiempo real y la liquidación del importe a pagar por cada usuario. Adicionalmente, el programa procesa de forma interna variables contadoras y acumuladoras para generar métricas estadísticas sobre la tasa de ocupación, la cantidad total de vehículos atendidos y el tiempo promedio de permanencia en el establecimiento.

## Integrantes
* **Clivio Nicolás Vera Ortiz**
* **Santiago, Mac Donald**
* **Luciano Gabriel, Pereyra Brest**
* **Santiago, Solari**

## Comisión
* K1.2

## Estructura del Proyecto
El software se encuentra estructurado bajo un esquema de modularización básica para separar las responsabilidades del sistema:
* `main.py`: Punto de entrada de la aplicación. Aloja el bucle principal de control y la interfaz de usuario en consola.
* `gestion.py`: Contiene la lógica del negocio, incluyendo las funciones de ingreso, egreso, asignación de cocheras y cálculo de tarifas.
* `validaciones.py`: Concentra las funciones de control de tipos de datos, sanitización de inputs y manejo de errores para evitar fallas críticas en la ejecución.
* `estadisticas.py`: Módulo encargado de procesar los datos históricos y actuales mediante acumuladores y contadores para mostrar reportes analíticos.


