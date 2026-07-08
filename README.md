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

## Grupo
* B34

## Estructura del Proyecto
El software se encuentra estructurado bajo un esquema de modularización básica para separar las responsabilidades del sistema:
* `main.py`: Punto de entrada de la aplicación. Aloja el bucle principal de control y la interfaz de usuario en consola.
* `gestion.py`: Contiene la lógica del negocio, incluyendo las funciones de ingreso, egreso, asignación de cocheras y cálculo de tarifas.
* `validaciones.py`: Concentra las funciones de control de tipos de datos.
* `estadisticas.py`: Módulo encargado de procesar los datos históricos y actuales mediante acumuladores y contadores para mostrar reportes analíticos.

## Instrucciones de Uso
El programa consta de un menú manejado por consola, el cual espera el ingreso de números enteros, del 0 al 5. Cada opción del menú es una función a la que se llama para cumplir con el objetivo del usuario. 
Si el usuario no respeta el formato de ingreso de datos, el programa manejará el error y se lo hará saber al usuario.
El programa consta de las siguientes funciones, enumeradas según el número que la llama:
1. Ingresar vehículo: Pide los datos del cliente y determina que se ingrese una patente válida Argentina.
2. Egresar vehículo: Pide la patente del vehículo que egresa del estacionamiento.
3. Verificar disponibilidad: Muestra los espacios disponibles y los espacios ocupados, junto a los datos del vehículo estacionado.
4. Revisar estadísticas: Muestra el actual documento de estadísticas.
5. Modificar tipo de vehículo: Permite modificar el tipo de vehículo asociado a la patente.
6. Cerrar el programa: Prepara el programa para su cierre. Se limpian todas las variables y se guardan las estadísticas.

El programa no necesita la instalación de ninguna librería externa.

## Uso de Inteligencia Artificial
Para el desarrollo de este trabajo, hemos utilizado Gemini. Se utilizó principalmente para comprender por qué el código no funcionaba y realizar consultas ocasionales. En múltiples ocasiones, el código no funcionaba como esperábamos por detalles menores. 
Una consulta donde utilizamos la IA fue en la comprensión del uso de la librería "math" para manipular los datos de las tarifas aplicadas en el programa.
Para el uso de la IA, hemos enviado nuestra consulta o función problemática y le preguntamos al agente por qué la consola nos devolvía tal error (por ejemplo, un loop infinito, un error especificado en tal línea, etc.).
