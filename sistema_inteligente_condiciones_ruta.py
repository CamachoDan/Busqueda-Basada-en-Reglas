# Evalúa las condiciones de una ruta para llegar a un lugar
def main():

    # --------------------------------------------------------
    # 1. BASE DE CONOCIMIENTO
    # --------------------------------------------------------

    # Guardamos información conocida sobre cada lugar
    base_conocimiento = {

        "Parque": {"zona": "comercial"},
        "Centro": {"zona": "comercial"},
        "Estacion": {"zona": "transporte"},
        "Barrio": {"zona": "residencial"},
        "Zona Industrial": {"zona": "industrial"}
    }


    # Definimos las rutas
    rutas = {

        ("Parque", "Barrio"):
            ["Parque", "Centro", "Barrio"],

        ("Parque", "Zona Industrial"):
            ["Parque", "Centro", "Estacion", "Zona Industrial"],

        ("Centro", "Barrio"):
            ["Centro", "Estacion", "Barrio"],

        ("Centro", "Zona Industrial"):
            ["Centro", "Estacion", "Zona Industrial"]
    }

    # Horario en el que funciona el Metro
    METRO_INICIO = 4
    METRO_FIN = 23

    # Horario en el que funciona el bus
    BUS_INICIO = 5
    BUS_FIN = 22

    # En minutos
    LIMITE_CAMINAR = 10

    print("\n========== RUTAS DISPONIBLES ==========")

    # Mostramos todas las rutas
    for origen_ruta, destino_ruta in rutas:
        print(f"- {origen_ruta} -> {destino_ruta}")

    # Seleccion de la ruta deseada
    print("\n========== SELECCIÓN DE RUTA ==========")

    # Pedimos el punto donde se comenzará el recorrido
    origen = input("Punto de salida: ").strip()

    # Pedimos el punto al que se desea llegar
    destino = input("Punto de destino: ").strip()

    # Buscamos la ruta y creamos una clave usando origen y destino
    clave = (origen, destino)


    # Verificamos si la ruta existe
    if clave not in rutas:
        print("\nNo existe esa ruta en el sistema.")

        print("\nLas rutas disponibles son:")

        # Mostramos nuevamente las rutas válidas
        for origen_ruta, destino_ruta in rutas:

            print(f"- {origen_ruta} -> {destino_ruta}")

        print("\nEl programa finalizará.")

        # finaliza el programa
        return

    # si la ruta si existe
    ruta = rutas[clave]

    print("\n========== INFORMACIÓN DEL VIAJE ==========")

    # Pedimos la hora de salida
    hora = int(input("Hora de salida (0-23): "))

    # Pedimos el estado del clima
    clima = input(
        "Está: ¿soleado? ¿nublado? ¿lluvia?): "
    ).strip().lower()

    # Pedimos el medio de transporte
    medio = input(
        "Transporte: (metro, bus, indrive): "
    ).strip().lower()

    # Pedimos cuánto caminará antes del transporte
    caminar_antes = int(
        input("Minutos caminando antes del transporte: ")
    )

    # Pedimos cuánto caminará después del transporte
    caminar_despues = int(
        input("Minutos caminando después del transporte: ")
    )

    # Indica si alguna regla de riesgo alto se activó
    riesgo_alto = False

    # Guardamos las condiciones encontradas
    condiciones_riesgo = []

    # Guardamos las recomendaciones generadas
    recomendaciones = []

    # Si está de MADRUGADA
    # SI la hora está entre 0 y 4, ENTONCES existe una condición de riesgo
    if 0 <= hora < 5:
        riesgo_alto = True
        condiciones_riesgo.append(
            "La salida se realiza durante la madrugada."
        )
        recomendaciones.append(
            "Evitar realizar el trayecto durante la madrugada."
        )


    # Si está de NOCHE y para una ZONA INDUSTRIAL
    if hora >= 19 or hora < 5:

        # Recorremos cada punto de la ruta
        for punto in ruta:

            # Consultamos el tipo de zona.
            zona = base_conocimiento[punto]["zona"]

            # SI la zona es industrial,
            # ENTONCES activamos una condición de riesgo
            if zona == "industrial":
                riesgo_alto = True
                condiciones_riesgo.append(
                    "La ruta pasa por una zona industrial de noche."
                )
                recomendaciones.append(
                    "Evitar la zona industrial durante la noche."
                )
                # Ya encontramos la zona industrial, por lo tanto no necesitamos seguir buscando
                break

    # SI está lloviendo Y la persona debe caminar,
    # ENTONCES recomendamos reducir el tiempo caminando
    if clima == "lluvia" and (
        caminar_antes > 0 or caminar_despues > 0
    ):
        # Registramos la condición.
        condiciones_riesgo.append(
            "El clima puede dificultar el desplazamiento."
        )
        # Generamos la recomendación
        recomendaciones.append(
            "Reducir el tiempo caminando debido a la lluvia."
        )

    # Disponibilidad del metro (si metro es seleccionado)
    if medio == "metro":
        # SI el Metro está dentro de su horario,
        # ENTONCES está disponible
        if METRO_INICIO <= hora <= METRO_FIN:
            print("\nEl Metro está disponible.")
        else:
            riesgo_alto = True
            condiciones_riesgo.append(
                "El Metro no está disponible a esa hora."
            )
            recomendaciones.append(
                "Utilizar otro medio de transporte."
            )

    # SI camina más de 10 minutos antes del transporte
    if caminar_antes > LIMITE_CAMINAR:

        riesgo_alto = True

        condiciones_riesgo.append(
            f"Debe caminar {caminar_antes} minutos antes del transporte."
        )

        recomendaciones.append(
            "Buscar un punto de transporte más cercano."
        )


    # SI camina más de 10 minutos después del transporte
    if caminar_despues > LIMITE_CAMINAR:

        riesgo_alto = True

        condiciones_riesgo.append(
            f"Debe caminar {caminar_despues} minutos después del transporte."
        )

        recomendaciones.append(
            "Buscar un transporte que deje más cerca del destino."
        )

    # Eliminamos condiciones repetidas manteniendo el orden.
    condiciones_riesgo = list(
        dict.fromkeys(condiciones_riesgo)
    )

    # Eliminamos recomendaciones repetidas.
    recomendaciones = list(
        dict.fromkeys(recomendaciones)
    )

    # SI se activó alguna regla de riesgo alto.
    if riesgo_alto:
        nivel = "RIESGO ALTO"

    # SI hay condiciones pero ninguna es de riesgo alto.
    elif condiciones_riesgo:
        nivel = "PRECAUCIÓN"

    # Si no hay condiciones.
    else:
        nivel = "CONDICIONES FAVORABLES"

    print("\n========== RESULTADO ==========")

    # Mostramos la ruta encontrada.
    print("Ruta:", " -> ".join(ruta))

    # Mostramos el medio de transporte.
    print("Transporte:", medio)

    # Mostramos el nivel calculado.
    print("Nivel:", nivel)

    # CONDICIONES
    print("\nCondiciones:")

    if condiciones_riesgo:
        for condicion in condiciones_riesgo:
            print("-", condicion)
    else:
        print("- No se identificaron condiciones de riesgo.")

    # RECOMENDACIONES
    print("\nRecomendaciones:")

    if recomendaciones:
        for recomendacion in recomendaciones:
            print("-", recomendacion)
    else:
        print("- No se requieren recomendaciones adicionales.")
# Ejecutar programa
main()