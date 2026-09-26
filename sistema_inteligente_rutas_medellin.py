"""
Actividad 2 - Búsqueda y sistemas basados en reglas.

Sistema inteligente de rutas para las líneas A y B del Metro de Medellín.
El programa representa las estaciones como una base de conocimiento,
aplica reglas lógicas y usa el algoritmo A* para encontrar la ruta con
menor cantidad de tramos entre el inicio y el destino seleccionados.

Fuentes consultadas para el orden de las estaciones:
https://www.metrodemedellin.gov.co/usuarios/sistema-integrado/linea-a
https://www.metrodemedellin.gov.co/usuarios/sistema-integrado/linea-b

Nota: es una simulación académica y no consulta el estado real del servicio.
"""

# Se importa heapq para manejar la cola de prioridad que necesita A*.
import heapq


# Se almacena el nombre de la estación autorizada para cambiar entre A y B.
ESTACION_TRANSFERENCIA = "San Antonio"

# Se define la Línea A en el orden oficial de sur a norte.
LINEA_A = [
    "La Estrella",
    "Sabaneta",
    "Itagüí",
    "Envigado",
    "Ayurá",
    "Aguacatala",
    "Poblado",
    "Industriales",
    "Exposiciones",
    "Alpujarra",
    "San Antonio",
    "Parque Berrío",
    "Prado",
    "Hospital",
    "Universidad",
    "Caribe",
    "Tricentenario",
    "Acevedo",
    "Madera",
    "Bello",
    "Niquía",
]

# Se define la Línea B en el orden oficial de oriente a occidente.
LINEA_B = [
    "San Antonio",
    "Cisneros",
    "Suramericana",
    "Estadio",
    "Floresta",
    "Santa Lucía",
    "San Javier",
]

# Se reúne cada línea con su nombre para facilitar el procesamiento.
LINEAS = {
    "Línea A": LINEA_A,
    "Línea B": LINEA_B,
}

# Se dejan vacíos los cierres porque normalmente todas las conexiones operan.
TRAMOS_CERRADOS = set()

# Para simular un cierre, se puede reemplazar la línea anterior por esta:
# TRAMOS_CERRADOS = {frozenset(("Poblado", "Industriales"))}


# Esta regla comprueba que dos estaciones sean consecutivas en una línea.
def regla_estaciones_consecutivas(estacion_1, estacion_2, estaciones_linea):
    # Se busca la posición de la primera estación dentro de la línea.
    posicion_1 = estaciones_linea.index(estacion_1)
    # Se busca la posición de la segunda estación dentro de la línea.
    posicion_2 = estaciones_linea.index(estacion_2)
    # La conexión es válida únicamente cuando las posiciones difieren en uno.
    return abs(posicion_1 - posicion_2) == 1


# Esta regla determina si un tramo puede utilizarse durante la búsqueda.
def regla_tramo_disponible(estacion_1, estacion_2):
    # Se crea un conjunto sin orden para reconocer el tramo en ambos sentidos.
    tramo = frozenset((estacion_1, estacion_2))
    # El tramo se permite cuando no aparece en la lista de cierres.
    return tramo not in TRAMOS_CERRADOS


# Esta regla permite cambiar de línea solamente en San Antonio.
def regla_transferencia_permitida(estacion):
    # Se devuelve verdadero cuando la estación es la transferencia autorizada.
    return estacion == ESTACION_TRANSFERENCIA


# Esta función transforma las líneas en un grafo de estaciones conectadas.
def construir_grafo():
    # Se crea un diccionario vacío para guardar la base de conocimiento.
    grafo = {}

    # Se recorren por separado la Línea A y la Línea B.
    for nombre_linea, estaciones in LINEAS.items():
        # Se recorren las posiciones que tienen una estación siguiente.
        for indice in range(len(estaciones) - 1):
            # Se obtiene la estación actual.
            estacion_actual = estaciones[indice]
            # Se obtiene la siguiente estación de la misma línea.
            estacion_siguiente = estaciones[indice + 1]

            # Se aplica la regla lógica de estaciones consecutivas.
            if regla_estaciones_consecutivas(
                estacion_actual, estacion_siguiente, estaciones
            ):
                # Se crea la lista de conexiones de la estación actual si falta.
                grafo.setdefault(estacion_actual, [])
                # Se crea la lista de conexiones de la estación siguiente si falta.
                grafo.setdefault(estacion_siguiente, [])
                # Se registra el recorrido de ida con costo de un tramo.
                grafo[estacion_actual].append((estacion_siguiente, nombre_linea, 1))
                # Se registra el recorrido de regreso con el mismo costo.
                grafo[estacion_siguiente].append((estacion_actual, nombre_linea, 1))

    # Se devuelve el grafo que representa la red del Metro.
    return grafo


# Se construye una vez el grafo que utilizará el algoritmo de búsqueda.
GRAFO = construir_grafo()

# Se crea un índice con las posiciones de cada estación en sus líneas.
POSICIONES = {}

# Se recorren todas las líneas para llenar el índice de posiciones.
for nombre_linea, estaciones in LINEAS.items():
    # Se obtiene el número de posición y el nombre de cada estación.
    for posicion, estacion in enumerate(estaciones):
        # Se guarda la línea y la posición; San Antonio pertenecerá a dos líneas.
        POSICIONES.setdefault(estacion, []).append((nombre_linea, posicion))

# Se guarda la posición de San Antonio dentro de cada línea.
POSICION_TRANSFERENCIA = {
    # Se obtiene la posición de transferencia en la Línea A.
    "Línea A": LINEA_A.index(ESTACION_TRANSFERENCIA),
    # Se obtiene la posición de transferencia en la Línea B.
    "Línea B": LINEA_B.index(ESTACION_TRANSFERENCIA),
}


# Esta función estima los tramos restantes y actúa como heurística de A*.
def heuristica(estacion_actual, destino):
    # Se crea una lista para almacenar todas las estimaciones posibles.
    estimaciones = []

    # Se revisan las líneas a las que pertenece la estación actual.
    for linea_actual, posicion_actual in POSICIONES[estacion_actual]:
        # Se revisan las líneas a las que pertenece el destino.
        for linea_destino, posicion_destino in POSICIONES[destino]:
            # Si ambas estaciones están en la misma línea, no hay transferencia.
            if linea_actual == linea_destino:
                # Se calcula la separación mínima por cantidad de estaciones.
                estimacion = abs(posicion_actual - posicion_destino)
            # Si están en líneas diferentes, se estima el paso por San Antonio.
            else:
                # Se estiman los tramos desde la estación actual a San Antonio.
                hasta_transferencia = abs(
                    posicion_actual - POSICION_TRANSFERENCIA[linea_actual]
                )
                # Se estiman los tramos desde San Antonio hasta el destino.
                desde_transferencia = abs(
                    posicion_destino - POSICION_TRANSFERENCIA[linea_destino]
                )
                # Se suman las dos partes del recorrido estimado.
                estimacion = hasta_transferencia + desde_transferencia

            # Se agrega la estimación obtenida a la lista de posibilidades.
            estimaciones.append(estimacion)

    # Se devuelve la menor estimación disponible.
    return min(estimaciones)


# Esta función ejecuta A* para hallar la ruta con menos tramos permitidos.
def buscar_mejor_ruta(inicio, destino):
    # Cada elemento guarda prioridad, costo, estación, ruta y líneas utilizadas.
    frontera = []

    # Se agrega la estación inicial con costo acumulado igual a cero.
    heapq.heappush(
        frontera,
        (heuristica(inicio, destino), 0, inicio, [inicio], []),
    )

    # Se registra el menor costo conocido para llegar a cada estación.
    mejor_costo = {inicio: 0}

    # La búsqueda continúa mientras existan alternativas por revisar.
    while frontera:
        # Se extrae la alternativa con el menor valor estimado de f(n).
        _, costo_actual, estacion_actual, ruta, lineas_usadas = heapq.heappop(
            frontera
        )

        # Si se llegó al destino, se devuelve la solución encontrada.
        if estacion_actual == destino:
            # Se retorna la ruta, las líneas y el número total de tramos.
            return ruta, lineas_usadas, costo_actual

        # Se ignora una alternativa si ya existe otra más económica.
        if costo_actual > mejor_costo.get(estacion_actual, float("inf")):
            # Se continúa con la siguiente alternativa de la frontera.
            continue

        # Se revisan todas las estaciones conectadas con la estación actual.
        for estacion_vecina, linea, costo_tramo in GRAFO[estacion_actual]:
            # Se aplica la regla que excluye los tramos cerrados.
            if not regla_tramo_disponible(estacion_actual, estacion_vecina):
                # Se descarta el tramo cerrado y se revisa la siguiente conexión.
                continue

            # Se calcula el costo acumulado al avanzar hasta la estación vecina.
            nuevo_costo = costo_actual + costo_tramo

            # Se comprueba si la nueva alternativa mejora el costo conocido.
            if nuevo_costo < mejor_costo.get(estacion_vecina, float("inf")):
                # Se actualiza el mejor costo conocido para la estación vecina.
                mejor_costo[estacion_vecina] = nuevo_costo
                # Se calcula f(n) sumando el costo real y la heurística.
                prioridad = nuevo_costo + heuristica(estacion_vecina, destino)
                # Se guarda la alternativa en la cola de prioridad.
                heapq.heappush(
                    frontera,
                    (
                        prioridad,
                        nuevo_costo,
                        estacion_vecina,
                        ruta + [estacion_vecina],
                        lineas_usadas + [linea],
                    ),
                )

    # Si la frontera se vacía, no existe una ruta con los tramos disponibles.
    return None, None, None


# Esta función crea una lista única de estaciones para el menú de usuario.
def obtener_estaciones():
    # dict.fromkeys conserva el orden y elimina el San Antonio repetido.
    return list(dict.fromkeys(LINEA_A + LINEA_B))


# Esta función muestra el menú y solicita una estación válida.
def seleccionar_estacion(mensaje, estaciones):
    # Se repite la solicitud hasta que el usuario escriba una opción correcta.
    while True:
        # Se muestra el significado de la selección solicitada.
        print(f"\n{mensaje}")

        # Se muestran todas las estaciones con una numeración sencilla.
        for numero, estacion in enumerate(estaciones, start=1):
            # Se imprime el número y el nombre de la estación.
            print(f"{numero:2}. {estacion}")

        # Se captura la respuesta escrita por el usuario.
        respuesta = input("Escriba el número de la estación: ").strip()

        # Se verifica que la respuesta contenga únicamente números.
        if respuesta.isdigit():
            # Se convierte la respuesta de texto a número entero.
            opcion = int(respuesta)

            # Se comprueba que el número corresponda a una estación del menú.
            if 1 <= opcion <= len(estaciones):
                # Se devuelve el nombre de la estación elegida.
                return estaciones[opcion - 1]

        # Se informa que la entrada no corresponde a una opción válida.
        print("Opción no válida. Intente nuevamente.")


# Esta función identifica los cambios de línea incluidos en una ruta.
def obtener_transferencias(ruta, lineas_usadas):
    # Se crea una lista vacía para registrar las transferencias.
    transferencias = []

    # Se comparan las líneas utilizadas en cada par de tramos consecutivos.
    for indice in range(1, len(lineas_usadas)):
        # Se detecta una transferencia cuando cambia el nombre de la línea.
        if lineas_usadas[indice] != lineas_usadas[indice - 1]:
            # La estación de cambio es la ubicada entre los dos tramos.
            estacion_cambio = ruta[indice]

            # Se aplica la regla que autoriza la transferencia en San Antonio.
            if regla_transferencia_permitida(estacion_cambio):
                # Se registra la estación donde debe cambiarse de línea.
                transferencias.append(estacion_cambio)

    # Se devuelve la lista de transferencias encontradas.
    return transferencias


# Esta función principal coordina la interacción con el usuario.
def ejecutar_sistema():
    # Se muestra el título del proyecto.
    print("=" * 64)
    # Se presenta el nombre del sistema inteligente.
    print("SISTEMA INTELIGENTE DE RUTAS - METRO DE MEDELLÍN")
    # Se aclara el alcance académico del programa.
    print("Simulación académica de las líneas A y B")
    # Se cierra visualmente el encabezado.
    print("=" * 64)

    # Se obtiene la lista única de estaciones disponibles.
    estaciones = obtener_estaciones()

    # Se solicita el punto que representa el inicio del recorrido.
    inicio = seleccionar_estacion("INICIO DEL RECORRIDO", estaciones)
    # Se solicita el punto que representa el destino del recorrido.
    destino = seleccionar_estacion("DESTINO DEL RECORRIDO", estaciones)

    # Se aplica la regla que exige dos puntos diferentes.
    if inicio == destino:
        # Se informa que no es necesario realizar ningún desplazamiento.
        print("\nEl inicio y el destino son iguales; no se requiere recorrido.")
        # Se termina la función principal.
        return

    # Se ejecuta el algoritmo A* con los puntos elegidos.
    ruta, lineas_usadas, total_tramos = buscar_mejor_ruta(inicio, destino)

    # Se muestra un mensaje cuando las reglas impiden encontrar una ruta.
    if ruta is None:
        # Se informa que no existe un recorrido disponible en la simulación.
        print("\nNo existe una ruta disponible con los tramos habilitados.")
        # Se termina la función principal.
        return

    # Se identifican las transferencias necesarias durante el recorrido.
    transferencias = obtener_transferencias(ruta, lineas_usadas)

    # Se presenta el encabezado de los resultados.
    print("\nRESULTADO DE LA BÚSQUEDA")
    # Se imprime la estación seleccionada como inicio.
    print(f"Inicio del recorrido: {inicio}")
    # Se imprime la estación seleccionada como destino.
    print(f"Destino del recorrido: {destino}")
    # Se imprime la secuencia completa de estaciones calculada por A*.
    print("Mejor ruta:", " -> ".join(ruta))
    # Se imprime la cantidad de desplazamientos entre estaciones.
    print(f"Cantidad de tramos: {total_tramos}")

    # Se informa si el recorrido requiere al menos una transferencia.
    if transferencias:
        # Se presentan las estaciones de transferencia encontradas.
        print("Transferencia necesaria en:", ", ".join(transferencias))
    # Si no cambia la línea, se informa que la ruta es directa.
    else:
        # Se presenta el mensaje correspondiente a una sola línea.
        print("Recorrido directo: no requiere transferencia entre líneas.")

    # Se imprime una explicación sencilla del resultado producido.
    print(
        "Explicación: A* seleccionó la ruta permitida con la menor "
        "cantidad de tramos según la base de conocimiento."
    )


# Esta condición ejecuta el programa solo cuando se abre este archivo.
if __name__ == "__main__":
    # Se llama a la función principal del sistema inteligente.
    ejecutar_sistema()
