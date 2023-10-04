# Tarea 1 - Analisis de datos sobre partidas de League of Legends

La tarea consiste en realizar un analisis de datos sobre partidas de league of legends en un **periodo de 10 minutos**, para ello se utilizara el dataset correspondiene, de un total de 10 mil partidas, se tomara una muestra de 400 partidas para realizar el analisis.

Cada partida tendra información de la partida en particular tanto del equipo rojo como azul, como por ejemplo:

- Victorias ganadas y perdidas
- Wards colocados y destruidos
- Kills, muertes y asistencias
- Oro ganado

Puede importar las librerias que crea necesarias para realizar el analisis, pero se recomienda utilizar las siguientes:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

**RECORDAR:** Para que las librerias funcionen correctamente se debe instalarlas, para ello se puede utilizar el siguiente comando en la terminal:

```bash
pip install pandas numpy matplotlib
```

## Objetivos

El objetivo prinicipal es identificar las características que pueden actuar como "señales" o indicadores de una **victoria del equipo azul**, así como las características de las pertida dónde el mismo equipo perdió.

### ✅ 1. Analisis preliminar

1.1 Examinar los datos para familiarizarse con las columnas correspondientes.

1.2 Estadisticas descripitivas básicas

- ✅ **Media:** Es el promedio de los datos, se calcula sumando todos los datos y dividiendolos por la cantidad de datos.
- ✅ **Mediana:** Es el valor que se encuentra en el centro de los datos, es decir, la mitad de los datos son menores a la mediana y la otra mitad son mayores.
- ✅ **Moda:** Es el valor que mas se repite en los datos.
- ✅ **Varianza:** Es una medida de dispersión de los datos, es decir, que tan alejados estan los datos de la media, pero al cuadrado.
- ✅ **Desviación estandar:** Es una medida de dispersión de los datos, es decir, que tan alejados estan los datos de la media.
- ✅ **Valor máximo:** Es el valor mas alto de los datos.
- ✅ **Valor mínimo:** Es el valor mas bajo de los datos.
- ✅ **Rango:** Es la diferencia entre el valor mayor y el valor menor de los datos.

### 2. Visualización de los datos

2.1 Utilizar histogramas para visualizar la distribución de características clave:

- La diferencia de oro `blueGoldDiff`
- La diferencia de experiencia `blueExperienceDiff`
- Los asesinatos del equipo azul `blueKills`
- La cantidad de muertes `blueDeaths`
- La cantidad de asistencias `blueAssists`
- La cantidad de monstruos epicos asesinados `blueEliteMonsters`
- La cantidad de torres destruidas `blueTowersDestroyed`
- El promedio de nivel en la partida `blueAvgLevel`

**¿Qué se puede decir de la distribución de los datos?**

2.2 Realizar gráficos de barra para comparar las medias características anteriores **entre las victorias y derrotas** del equipo azul ¿Hay alguna diferencia significativa?

2.3 Utilizar diagramas de caja (**bloxplots**) para visualizar la variabilidad y distribución de las características mencionadas, segmentadas por victoria o derrota del equipo azul. Identifique y analice cualquier dato atípico, ya sea con la **distancia de mahalanobis** o cualquier técnica de disviación estándar o con la del rango intercuartil.

2.4 Se puede explora y visualizar otras características que considere relevantes para el análisis.

2.5 (**PUNTO EXTRA**) Comparar gráficamente los resultados del subconjunto, ya sea victorias o derrotas con el global de victorias y derrotas (en ambos casos rondan las 5000 filas). Mencione si en base a su criterio experto los resultados son similares.

### 3. Análisis y conclusiones

3.1 Basándose en sus visualizaciones, identifique las características que cree que son indicadores clave de una victoria del equipo azul. Justifique sus elecciones.

3.2 ¿Hay características que parezcan no influir mucho en el resultado de la partida? Explique.

3.3 Proporcione una breve conclusión de sus hallazgos y discuta cómo se podrían utilizar estos insights en el contexto del juego.

## Instrucciones

1. Del archivo `'puntos high_diamond_ranked_10min.xlsx'` debe tomar una muestra de **400 partidas** en base a lo que se le asignó, para ello se puede utilizar la siguiente instrucción:

    ```python
    import pandas as pd

    df = pd.read_excel('data/puntos high_diamond_ranked_10min.xlsx', sheet_name='high_diamond_ranked_10min')
    df = df.sample(n=400, random_state=1)
    ```

2. Puede comenzar a usar el archivo `main.ipynb` para realizar el análisis de datos.

3. Para cargar el **dataset** presente en el archivo dentro de la carpeta `./data` se puede utilizar la siguiente instrucción:

    ```python
    df = pd.read_excel('data/data_example_lol.excel')
    ```

4. Para guardar el **dataset** resultante en un archivo dentro de la carpeta `./data` se puede utilizar la siguiente instrucción:

    ```python
    df.to_excel('data/data_example_lol.excel')
    ```

## Formato de entrega

- Incluir tanto los gráficos como las interpretaciones en un informe bien estructurado.
- Asegúrese de que todos los gráficos estén claramente etiquetados y sean fácilmente interpretables.
- Cite cualquier recurso externo o referencia que haya utilizado para su análisis.
