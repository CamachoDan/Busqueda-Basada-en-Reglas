# Sistemas inteligentes de rutas y evaluación de condiciones de viaje

## 1. Descripción

Este proyecto contiene dos sistemas inteligentes desarrollados en Python para aplicar conceptos de representación del conocimiento, reglas lógicas y estrategias de búsqueda.

El primer sistema determina la mejor ruta entre una estación de inicio y una estación de destino dentro de las líneas A y B del Metro de Medellín. Para ello, representa las estaciones como un grafo y utiliza el algoritmo de búsqueda heurística A*.

El segundo sistema, denominado **SI – Condiciones de ruta y seguridad**, evalúa las condiciones asociadas a un recorrido previamente almacenado. Este sistema analiza la hora de salida, el clima, el medio de transporte y el tiempo que debe caminar una persona antes y después de utilizar el transporte. A partir de reglas lógicas, genera un nivel de evaluación y recomendaciones para el usuario.

Los dos desarrollos son simulaciones académicas y no consultan información operativa en tiempo real.

---

## 2. Objetivo

Desarrollar sistemas inteligentes basados en conocimiento que permitan representar y analizar diferentes situaciones relacionadas con la movilidad, mediante la aplicación de reglas lógicas, una función heurística y un algoritmo de búsqueda.

Los objetivos particulares de cada sistema son:

- Calcular la ruta disponible con la menor cantidad de tramos entre dos estaciones de las líneas A y B del Metro de Medellín.
- Evaluar las condiciones de una ruta teniendo en cuenta la hora, el clima, el medio de transporte, las zonas recorridas y el tiempo de caminata.
- Generar recomendaciones a partir de las condiciones identificadas.
- Aplicar conceptos de base de conocimiento, motor de inferencia, reglas lógicas y búsqueda heurística.

---

## 3. Componentes del proyecto

### 3.1. Sistema inteligente de rutas del Metro de Medellín

Este sistema representa las estaciones y conexiones de las líneas A y B del Metro de Medellín.

Las estaciones se almacenan en listas ordenadas y posteriormente se transforman en un grafo:

- Cada estación corresponde a un nodo.
- Cada conexión entre estaciones consecutivas corresponde a una arista.
- Cada desplazamiento tiene un costo de un tramo.
- Las conexiones pueden recorrerse en ambos sentidos.
- San Antonio es la estación de transferencia entre las líneas A y B.

El usuario selecciona:

```text
INICIO DEL RECORRIDO
```

y posteriormente:

```text
DESTINO DEL RECORRIDO
```

El sistema presenta:

- Inicio del recorrido.
- Destino del recorrido.
- Mejor ruta encontrada.
- Cantidad de tramos.
- Transferencia necesaria, cuando corresponda.
- Explicación resumida del resultado.

Para este sistema, la mejor ruta se define como el recorrido disponible con la menor cantidad de tramos entre estaciones.

### 3.2. SI – Condiciones de ruta y seguridad

Este sistema evalúa las condiciones de una ruta almacenada en la base de conocimiento.

Los lugares representados son:

| Lugar | Tipo de zona |
|---|---|
| Parque | Comercial |
| Centro | Comercial |
| Estación | Transporte |
| Barrio | Residencial |
| Zona Industrial | Industrial |

El sistema contiene las siguientes rutas:

```text
Parque -> Barrio
Parque -> Zona Industrial
Centro -> Barrio
Centro -> Zona Industrial
```

Después de seleccionar una ruta válida, el usuario debe proporcionar:

- Hora de salida.
- Estado del clima.
- Medio de transporte.
- Minutos caminando antes de utilizar el transporte.
- Minutos caminando después de utilizar el transporte.

Con esta información, el sistema consulta la base de conocimiento, aplica las reglas y presenta:

- Ruta seleccionada.
- Medio de transporte.
- Nivel de evaluación.
- Condiciones identificadas.
- Recomendaciones generadas.

Los niveles posibles son:

```text
RIESGO ALTO
PRECAUCIÓN
CONDICIONES FAVORABLES
```

El sistema asigna **RIESGO ALTO** cuando se activa alguna regla que establece una condición relevante, como realizar el recorrido durante la madrugada, utilizar el Metro fuera de su horario definido, pasar por una zona industrial durante la noche o caminar más del límite establecido.

El nivel **PRECAUCIÓN** se utiliza cuando se identifican condiciones que requieren atención, pero no se activa una regla clasificada como riesgo alto. Por ejemplo, cuando está lloviendo y el recorrido incluye desplazamientos caminando.

El nivel **CONDICIONES FAVORABLES** se asigna cuando no se identifican condiciones de riesgo ni recomendaciones adicionales.

---

## 4. Librerías utilizadas

### Sistema de rutas del Metro de Medellín

El sistema utiliza la siguiente librería:

```python
import heapq
```

`heapq` pertenece a la biblioteca estándar de Python y permite implementar una cola de prioridad. Esta estructura es utilizada por el algoritmo A* para revisar primero las alternativas con el menor costo estimado.

### SI – Condiciones de ruta y seguridad

El segundo sistema no requiere importar librerías externas. Su funcionamiento se basa en:

- Diccionarios.
- Listas.
- Tuplas.
- Variables booleanas.
- Condicionales.
- Ciclos.
- Entradas y salidas por consola.

Por lo tanto, ninguno de los dos sistemas requiere instalar paquetes adicionales mediante `pip`.

---

## 5. Instrucciones para ejecutarlo en Google Colab

### Paso 1. Abrir Google Colab

Ingrese a [Google Colab](https://colab.research.google.com/) e inicie sesión con una cuenta de Google.

### Paso 2. Crear un cuaderno

Seleccione:

```text
Archivo → Nuevo cuaderno
```

### Paso 3. Ejecutar el sistema de rutas del Metro

Si el código se encuentra guardado en el archivo:

```text
sistema_inteligente_rutas_medellin.py
```

debe subirlo al almacenamiento de la sesión mediante el icono de carpeta del panel izquierdo.

También puede subirlo ejecutando:

```python
from google.colab import files
files.upload()
```

Después debe ejecutar:

```python
%run sistema_inteligente_rutas_medellin.py
```

El programa mostrará el menú de estaciones y solicitará el inicio y el destino del recorrido.

### Paso 4. Ejecutar el sistema de condiciones de ruta y seguridad

El código del sistema **SI – Condiciones de ruta y seguridad** puede ejecutarse directamente en otra celda del cuaderno de Colab.

Si se guarda como un segundo archivo, se recomienda utilizar el nombre:

```text
si_condiciones_ruta_seguridad.py
```

Después de subirlo a Colab, se ejecuta mediante:

```python
%run si_condiciones_ruta_seguridad.py
```

El programa mostrará las rutas disponibles y solicitará:

```text
Punto de salida
Punto de destino
Hora de salida
Estado del clima
Medio de transporte
Minutos caminando antes del transporte
Minutos caminando después del transporte
```

Los nombres del punto de salida y del destino deben escribirse exactamente como aparecen en el menú.

### Paso 5. Revisar los resultados

Cada sistema presentará sus resultados en la consola de Google Colab.

En el primer sistema se debe revisar:

- Ruta calculada.
- Cantidad de tramos.
- Transferencia entre líneas.

En el segundo sistema se debe revisar:

- Ruta seleccionada.
- Nivel calculado.
- Condiciones identificadas.
- Recomendaciones generadas.

---

## 6. Reglas, heurística y algoritmo de búsqueda

### 6.1. Reglas del sistema de rutas del Metro

El sistema de rutas aplica las siguientes reglas:

#### Regla de conexión

```text
SI dos estaciones son consecutivas en una misma línea,
ENTONCES existe una conexión válida entre ellas.
```

#### Regla de disponibilidad

```text
SI un tramo no se encuentra registrado como cerrado,
ENTONCES puede utilizarse durante la búsqueda.
```

#### Regla de transferencia

```text
SI el recorrido cambia entre las líneas A y B,
ENTONCES la transferencia debe realizarse en San Antonio.
```

#### Regla de validación

```text
SI el inicio y el destino son iguales,
ENTONCES no se requiere realizar ningún recorrido.
```

```text
SI la opción ingresada no corresponde a una estación,
ENTONCES se solicita nuevamente la información.
```

### 6.2. Heurística y algoritmo A*

La heurística estima la cantidad de tramos que faltan para llegar desde la estación actual hasta el destino.

- Si las estaciones pertenecen a la misma línea, se calcula la diferencia entre sus posiciones.
- Si pertenecen a líneas diferentes, se estima el recorrido pasando por San Antonio.

El algoritmo A* utiliza la siguiente función:

```text
f(n) = g(n) + h(n)
```

Donde:

- `g(n)` representa el costo real acumulado desde el inicio.
- `h(n)` representa la cantidad estimada de tramos restantes.
- `f(n)` representa el costo total estimado.

A* utiliza una cola de prioridad para explorar primero la alternativa con el menor valor de `f(n)`.

### 6.3. Reglas del SI – Condiciones de ruta y seguridad

El segundo sistema utiliza reglas del tipo:

```text
SI se cumple una condición,
ENTONCES se registra un riesgo o se genera una recomendación.
```

#### Regla de madrugada

```text
SI la hora está entre las 00:00 y las 04:59,
ENTONCES el recorrido se clasifica como riesgo alto.
```

Recomendación:

```text
Evitar realizar el trayecto durante la madrugada.
```

#### Regla de zona industrial durante la noche

```text
SI la hora es igual o posterior a las 19:00
Y la ruta pasa por una zona industrial,
ENTONCES el recorrido se clasifica como riesgo alto.
```

Recomendación:

```text
Evitar la zona industrial durante la noche.
```

#### Regla de lluvia y caminata

```text
SI está lloviendo
Y la persona debe caminar antes o después del transporte,
ENTONCES se registra una condición de precaución.
```

Recomendación:

```text
Reducir el tiempo caminando debido a la lluvia.
```

#### Regla de disponibilidad del Metro

```text
SI el medio seleccionado es Metro
Y la hora está entre las 04:00 y las 23:00,
ENTONCES el Metro se considera disponible.
```

```text
SI el medio seleccionado es Metro
Y la hora está fuera del horario definido,
ENTONCES se registra una condición de riesgo alto.
```

Recomendación:

```text
Utilizar otro medio de transporte.
```

#### Regla de caminata antes del transporte

```text
SI la persona debe caminar más de 10 minutos antes del transporte,
ENTONCES se registra una condición de riesgo alto.
```

Recomendación:

```text
Buscar un punto de transporte más cercano.
```

#### Regla de caminata después del transporte

```text
SI la persona debe caminar más de 10 minutos después del transporte,
ENTONCES se registra una condición de riesgo alto.
```

Recomendación:

```text
Buscar un transporte que deje más cerca del destino.
```

#### Regla de clasificación final

```text
SI se activa al menos una regla de riesgo alto,
ENTONCES el nivel es RIESGO ALTO.
```

```text
SI existen condiciones identificadas,
PERO ninguna activa un riesgo alto,
ENTONCES el nivel es PRECAUCIÓN.
```

```text
SI no se identifican condiciones de riesgo,
ENTONCES el nivel es CONDICIONES FAVORABLES.
```



---

## 7. Integrantes

| Integrante | Aporte realizado |
|---|---|
| Daniela Camacho Grueso | Desarrollo y documentación del sistema inteligente de rutas del Metro de Medellín mediante el algoritmo A*. |
| Dayana Monsalve | Desarrollo y documentación del SI – Condiciones de ruta y seguridad basado en reglas lógicas. |

