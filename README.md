# Sistema inteligente de rutas del Metro de Medellín

## 1. Descripción

Este proyecto presenta un sistema inteligente desarrollado en Python para determinar la mejor ruta entre una estación de inicio y una estación de destino dentro de las líneas A y B del Metro de Medellín.

El sistema utiliza una base de conocimiento compuesta por las estaciones y sus conexiones, un conjunto de reglas lógicas para validar los recorridos y el algoritmo de búsqueda heurística A* para encontrar la ruta disponible con la menor cantidad de tramos.

Las estaciones se encuentran organizadas de acuerdo con su orden dentro de cada línea. La estación San Antonio se utiliza como punto de transferencia entre las líneas A y B.

> **Nota:** este programa corresponde a una simulación académica. No consulta horarios, tarifas, distancias reales ni el estado operativo del Metro de Medellín en tiempo real.

---

## 2. Objetivo

Desarrollar un sistema inteligente basado en conocimiento que represente las estaciones y conexiones de las líneas A y B del Metro de Medellín, aplique reglas lógicas y utilice el algoritmo A* para calcular la mejor ruta entre un inicio y un destino seleccionados por el usuario.

Para este proyecto, la mejor ruta se define como el recorrido disponible con la menor cantidad de tramos entre estaciones.

---

## 3. Librería utilizada

El programa utiliza únicamente la siguiente librería:

```python
import heapq
```

`heapq` pertenece a la biblioteca estándar de Python y permite implementar una cola de prioridad. Esta estructura es utilizada por el algoritmo A* para revisar primero las alternativas con el menor costo estimado.

No es necesario instalar paquetes o dependencias externas para ejecutar el programa.

---

## 4. Instrucciones para ejecutarlo en Google Colab

### Paso 1. Descargar el código

Descargue desde este repositorio el archivo:

```text
sistema_inteligente_rutas_medellin.py
```

### Paso 2. Abrir Google Colab

Ingrese a [Google Colab](https://colab.research.google.com/) e inicie sesión con una cuenta de Google.

### Paso 3. Crear un cuaderno

Seleccione la opción:

```text
Archivo → Nuevo cuaderno
```

### Paso 4. Subir el archivo de Python

En el panel izquierdo de Google Colab:

1. Seleccione el icono de carpeta.
2. Presione la opción **Subir al almacenamiento de la sesión**.
3. Seleccione el archivo `sistema_inteligente_rutas_medellin.py`.

También puede subirlo ejecutando la siguiente instrucción en una celda:

```python
from google.colab import files
files.upload()
```

### Paso 5. Ejecutar el programa

En una nueva celda escriba:

```python
%run sistema_inteligente_rutas_medellin.py
```

Ejecute la celda con el botón de reproducción.

### Paso 6. Seleccionar el recorrido

El programa mostrará un menú numerado con las estaciones disponibles y solicitará:

```text
INICIO DEL RECORRIDO
```

Escriba el número correspondiente a la estación de inicio y presione `Enter`.

Después solicitará:

```text
DESTINO DEL RECORRIDO
```

Escriba el número correspondiente a la estación de destino y presione `Enter`.

El sistema mostrará:

- Inicio del recorrido.
- Destino del recorrido.
- Mejor ruta encontrada.
- Cantidad total de tramos.
- Estación de transferencia, cuando corresponda.
- Explicación resumida del resultado.

---

## 5. Reglas lógicas del sistema

El sistema aplica las siguientes reglas:

### Regla 1. Conexión entre estaciones

Dos estaciones pueden conectarse cuando son consecutivas dentro de la misma línea.

```text
SI dos estaciones son consecutivas en una línea
ENTONCES existe una conexión válida entre ellas.
```

### Regla 2. Disponibilidad del tramo

Una conexión solo puede utilizarse cuando el tramo no se encuentra registrado como cerrado.

```text
SI un tramo no está cerrado
ENTONCES puede utilizarse durante la búsqueda.
```

### Regla 3. Transferencia entre líneas

El cambio entre las líneas A y B solamente está permitido en la estación San Antonio.

```text
SI el recorrido cambia de la Línea A a la Línea B,
o de la Línea B a la Línea A,
ENTONCES la transferencia debe realizarse en San Antonio.
```

### Regla 4. Validación del inicio y el destino

Si la estación de inicio y la estación de destino son iguales, el sistema informa que no se requiere realizar ningún recorrido.

```text
SI el inicio es igual al destino
ENTONCES no se requiere desplazamiento.
```

### Regla 5. Validación de la entrada

El sistema solo acepta números que correspondan a las estaciones mostradas en el menú.

```text
SI la opción no corresponde a una estación
ENTONCES se solicita nuevamente la información.
```

---

## 6. Heurística y algoritmo A*

### Heurística

La heurística estima la cantidad de tramos que faltan para llegar desde una estación hasta el destino.

- Si las estaciones pertenecen a la misma línea, calcula la diferencia entre sus posiciones.
- Si pertenecen a líneas diferentes, estima el recorrido pasando por la estación San Antonio.

La heurística orienta al algoritmo hacia las estaciones que parecen encontrarse más cerca del destino.

### Algoritmo A*

El sistema utiliza el algoritmo A* para encontrar la ruta con la menor cantidad de tramos. Su función de evaluación es:

```text
f(n) = g(n) + h(n)
```

Donde:

- `g(n)` representa el costo real acumulado desde el inicio hasta la estación actual.
- `h(n)` representa la cantidad estimada de tramos desde la estación actual hasta el destino.
- `f(n)` representa el costo total estimado de la alternativa.

A* utiliza una cola de prioridad para seleccionar primero la estación que tenga el menor valor de `f(n)`. Cuando alcanza el destino, presenta la secuencia de estaciones, la cantidad de tramos y la transferencia necesaria.

---

## 7. Integrantes

| Integrante |
|---|
| Daniela Camacho Grueso] |
| Dayana Monsalve] | 

El historial de commits del repositorio evidencia los aportes realizados por cada integrante.

---

## 8. Video explicativo

El video presenta el objetivo del proyecto, la base de conocimiento, las reglas lógicas, la heurística, el algoritmo A*, los comandos ejecutados en Google Colab y los resultados obtenidos durante las pruebas.

[Ver video explicativo](REEMPLAZAR_CON_EL_ENLACE_DEL_VIDEO)

---

## 9. Documento de pruebas funcionales

El documento contiene los casos de prueba, las entradas utilizadas, los resultados esperados, los resultados obtenidos y las evidencias de ejecución del sistema.

[Consultar documento PDF de pruebas](./documentos/pruebas_sistema_rutas.pdf)

> Si el archivo PDF se guarda en otra carpeta o con otro nombre, se debe actualizar la ruta anterior.

---

## Archivo principal

El código fuente del proyecto se encuentra en:

[`sistema_inteligente_rutas_medellin.py`](./sistema_inteligente_rutas_medellin.py)

---

## Estado del proyecto

El sistema fue ejecutado en Google Colab y validado mediante pruebas funcionales relacionadas con:

- Recorrido directo en una misma línea.
- Recorrido con transferencia entre las líneas A y B.
- Recorrido en sentido contrario.
- Inicio y destino iguales.
- Ingreso de una opción inválida.
- Aplicación de la regla de tramo cerrado.

