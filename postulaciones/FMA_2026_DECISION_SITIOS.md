# Decisión sobre los sitios: cada escuela estudia su propio territorio

**Fecha:** 13 de agosto de 2026
**Sustituye** la propuesta de "sitio de referencia externo en Cerro Ñielol" de [`FMA_2026_PLANTILLAS_Y_SITIOS.md`](FMA_2026_PLANTILLAS_Y_SITIOS.md) §1.

---

## 1. Por qué mi propuesta era peor que tu intuición

Propuse un sitio de referencia en el Cerro Ñielol para recuperar el contraste de cobertura que se había perdido al quedar las tres escuelas en el mismo estrato. **Resolvía el problema estadístico y rompía el proyecto.**

Lo que rompía: el principio de que **cada comunidad estudia el arbolado de su propio barrio**. Ñielol no es el territorio de ninguna de las tres escuelas. Llevarlas ahí las convierte en visitantes de un lugar ajeno, y convierte el proyecto en una salida educativa más — justo el tipo de actividad que el fondo advirtió que no busca.

Tu propuesta —que Hablaarte se relacione con el río Cautín y el humedal Antumalén, que están en su sector— **resuelve el mismo problema sin romper nada**. Y además, como muestro abajo, lo resuelve **mejor estadísticamente**.

---

## 2. Lo que verifiqué

### 2.1 Distancia de cada escuela al río Cautín

Medida contra la geometría del río en OpenStreetMap (1.273 nodos):

| Escuela | Distancia al Cautín |
|---|---|
| **Hablaarte** | **451 m** |
| Los Trigales | 2.828 m |
| Campos Deportivos | 3.338 m |

🔑 **Hablaarte está a 451 metros del río: el corredor ribereño cae dentro de su propio radio de 500 m.** No hay que sacar a nadie de su barrio. Las otras dos están a casi 3 km — sus sectores son urbanos puros.

### 2.2 El humedal existe y está protegido por ley

| Dato | Fuente |
|---|---|
| Registrado como **"Humedal Urbano Río Cautín-Sector Antumalén"**, categoría reserva natural | OpenStreetMap (-38,72124 · -72,54830) |
| **Declarado humedal urbano bajo la Ley 21.202**, entre los primeros cuatro de La Araucanía | 🟢 prensa regional + [Portal de Humedales del MMA](https://sistemahumedales.mma.gob.cl/HumedalesUrbanos/DetailsPublico/11) |
| Compartido entre las comunas de **Temuco y Padre Las Casas** | 🟢 |
| Temuco suma **401,2 ha de humedales urbanos protegidos** y 6 humedales reconocidos bajo esa ley | 🟢 |
| El municipio mantiene una **mesa de fiscalización de humedales** | 🟢 Municipalidad de Temuco |
| Tiene sitio propio: hantumalen.cl | 🟢 |

⚠️ **Antes de citarlo en la postulación** conviene abrir la ficha del portal del MMA y anotar el **número y fecha de la resolución** de declaración. La prensa es suficiente para decidir; no lo es para citar.

**Distancia de Hablaarte al sector Antumalén: ~2 km.** Está fuera del radio de 500 m del muestreo, pero es **el mismo sistema ribereño** que pasa a 451 m de la escuela, y es perfectamente alcanzable para una salida.

---

## 3. El diseño corregido: gradiente dentro de cada sector

**Principio: nadie sale de su territorio. El contraste se busca dentro de cada barrio, no entre barrios.**

| Escuela | Su gradiente propio | Extremo alto de vegetación | Extremo bajo |
|---|---|---|---|
| **Hablaarte** | **calle ↔ ribera del Cautín** | Corredor ribereño (a 451 m) y humedal urbano protegido | Barrio con 3,3% de dosel |
| **Los Trigales** | **calle ↔ plaza / bandejón / patio escolar** | Los puntos más arbolados de su sector | UV más caliente de Temuco: **33,0 °C** |
| **Campos Deportivos** | **calle ↔ plaza / bandejón / patio escolar** | Ídem | 3,1% de dosel · IVE 90% |

### 3.1 Por qué esto es mejor y no un consuelo

Un gradiente **dentro** de cada sitio es estadísticamente **superior** a uno entre sitios distintos:

- Al comparar barrios diferentes, el efecto de la cobertura arbórea **se confunde** con todo lo demás que también cambia entre ellos: nivel socioeconómico, tipo de construcción, edad del barrio, quién midió.
- Al comparar **dentro del mismo barrio y con el mismo equipo de estudiantes**, esas variables quedan **controladas**. Lo que varía es la vegetación del entorno, que es justo lo que H2 quiere aislar.

En términos del diseño: la escuela pasa de ser un factor de ruido a ser un **factor aleatorio bien poblado**, y el efecto de interés se estima **dentro** de cada nivel. Es exactamente para lo que sirven los modelos mixtos que ya estaban previstos.

### 3.2 La limitación honesta

**El extremo alto del gradiente solo está bien representado en Hablaarte.** Los otros dos sectores no tienen río ni bosque: su punto más verde es una plaza o un bandejón arbolado, que está lejos de un 50% de cobertura.

Consecuencia: **el rango superior del predictor descansa principalmente en los datos de Hablaarte.** Hay que declararlo, y hay una mitigación barata: en Los Trigales y Campos Deportivos **incluir deliberadamente en el muestreo los puntos más arbolados disponibles** —plaza, bandejón, patio— para estirar el rango local todo lo que dé. Sigue siendo su propio sector.

---

## 4. Lo que gana el proyecto con este cambio

1. **Coherencia con la idea central.** Cada comunidad investiga el arbolado que camina todos los días. Eso es lo que hace que el conocimiento sea apropiable y que el proyecto no dependa de nosotros para repetirse.
2. **Un área protegida oficial, en el barrio de una de las escuelas.** Las bases valoran *"vincular el proyecto a áreas protegidas/espacios de cuidado"*. Con Ñielol lo cumplíamos de prestado; con el humedal Antumalén lo cumplimos **desde el territorio de la propia comunidad escolar**.
3. **Un anclaje de política pública adicional**: la Ley 21.202 de Humedales Urbanos, el portal del MMA y la mesa municipal de fiscalización. Se suma al Art. 28 de la Ordenanza y al diagnóstico regional de biodiversidad.
4. **Identidad propia para cada escuela**, que es lo que las convierte en tres comunidades y no en tres puntos de muestreo:
   - **Hablaarte** → escuela de lenguaje, río y humedal. **Y las aves de ribera**, que en un humedal son abundantes y visibles — con 1.602 identificaciones de aves en el equipo, es la combinación más potente de las tres.
   - **Los Trigales** → multiculturalidad, mapuzugun, y el **extremo de calor urbano** de toda la comuna.
   - **Campos Deportivos** → escala y justicia ambiental (IVE 90%).
5. **Se ahorra una salida de terreno** respecto de la propuesta anterior.

---

## 5. Lo que hay que verificar antes de comprometerlo

| # | Qué | A quién |
|---|---|---|
| 1 | **Resolución de declaración** del humedal: número y fecha | Portal de Humedales del MMA (ficha 11) |
| 2 | **¿Se requiere alguna coordinación** para actividades educativas y de registro dentro del humedal? | Municipalidad de Temuco — existe una mesa de fiscalización de humedales |
| 3 | **Seguridad de la ribera** para un grupo escolar: accesos, crecidas, ruta | Terreno, con la escuela |
| 4 | ¿El sector ribereño cercano a Hablaarte tiene **arbolado medible**, o es matorral y pastizal? | 🔑 **Ver en terreno o en la imagen satelital** — si no hay árboles medibles, el gradiente se apoya en las calles arboladas del sector y no en la ribera |

⚠️ **El punto 4 es el único que puede echar abajo la idea**, y es fácil de resolver: mirar el sector en el mapa satelital del propio observatorio antes de decidir. Un humedal ribereño puede ser espectacular en biodiversidad y tener pocos **árboles** en el sentido dendrométrico.

💡 Y si ese fuera el caso, no se pierde: el humedal entra igual como **sitio de biodiversidad asociada** —aves, hongos, líquenes sobre los árboles que haya— aunque no aporte muchos individuos al inventario dendrométrico. La coordinación con la mesa municipal de humedales sigue siendo un activo.

---

## 6. Decisión propuesta

> **Se descarta el sitio de referencia externo.** Cada escuela muestrea en su propio radio de 500 m, y el contraste de vegetación se busca **dentro** de cada sector. En Hablaarte, ese contraste lo aporta el corredor ribereño del Cautín, a 451 m, vinculado al **Humedal Urbano Río Cautín-Sector Antumalén**, declarado bajo la Ley 21.202.

Queda pendiente **tu confirmación** y la verificación del punto 4.
