# Medición, estimación y monitoreo: qué puede decir el Observatorio sobre servicios ecosistémicos

**Fecha:** 13 de agosto de 2026
**Corrige y reemplaza** lo dicho sobre carbono en [`FMA_2026_DISENO_CIENTIFICO.md`](FMA_2026_DISENO_CIENTIFICO.md) §9.
**Base:** [`SERVICIOS_ECOSISTEMICOS_E_INDICE.md`](../investigacion/SERVICIOS_ECOSISTEMICOS_E_INDICE.md) · Ordenanza 004/2021 Art. 32 · documentación oficial de i-Tree Eco v6.

---

## 1. Mi error, dicho derecho

Escribí que el secuestro anual de CO₂ **no se puede estimar** porque *"requiere medir crecimiento, o sea dos mediciones separadas en el tiempo"*.

**Eso es falso como lo dije.** Es cierto para el crecimiento **medido**, y falso para el secuestro **estimado**. Confundí dos cosas distintas, y tu objeción es correcta.

La prueba está en la documentación oficial de i-Tree Eco que archivamos. Para el **secuestro bruto de carbono**, el modelo usa:

> Especie · DAP · Altura total · Uso de suelo · **Estado sanitario — para ajustar las tasas de crecimiento** · **Exposición a la luz de la copa — para ajustar las tasas de crecimiento**

Es decir: **i-Tree estima el secuestro anual a partir de un solo inventario**, aplicando tasas de crecimiento por especie corregidas por la salud del árbol, su exposición a la luz y su emplazamiento. No necesita volver a medir.

Lo que **sí** requiere remedición es *comprobar* si ese crecimiento estimado fue el real. Eso es validación, no estimación — y es justamente el segundo producto del Observatorio.

**Conclusión: el carbono vuelve al proyecto**, con método declarado y límites explícitos.

---

## 2. Las tres categorías

### Categoría 1 — LO QUE SE MIDE en terreno

Dato tomado por una persona parada junto al árbol. Sin modelos de por medio.

| Variable | Quién | Instrumento |
|---|---|---|
| Ubicación (coordenadas y referencia postal) | estudiante | celular |
| Especie *(propuesta en terreno, confirmada por especialista)* | estudiante + especialista | fotos |
| **Perímetro del tronco a 1,30 m** → DAP | estudiante | huincha |
| Nº de fustes | estudiante | — |
| Altura total *(estimada)* | estudiante | app o vara de referencia |
| Diámetro de copa en dos ejes | estudiante | pasos o huincha |
| Altura a la base de la copa | estudiante | estimación |
| **Estado sanitario** | estudiante | protocolo visual (ver §5) |
| Daños visibles (desmoche, heridas, cables) | estudiante | — |
| **Emplazamiento** (plaza / calle / bandejón / patio) | estudiante | — |
| Riqueza y cobertura de **líquenes** (morfotipos) | estudiante | grilla de 10×10 cm |
| Presencia de **hongos**, artrópodos, epífitas | estudiante | foto → iNaturalist |
| **Aves** por punto de conteo (nivel sitio) | estudiante + especialista | 10 min, radio fijo |
| Esfuerzo de muestreo (minutos) | estudiante | cronómetro |

### Categoría 2 — LO QUE SE ESTIMA con modelos, desde una sola medición

Todo esto **sí entra en los nueve meses**, con la metodología y su incertidumbre declaradas.

| Indicador | Cómo se obtiene | Respaldo | Confianza |
|---|---|---|---|
| **Área basal** | π·(DAP/2)² | aritmética | ✅ Alta |
| **Área de copa y sombra proyectada** | elipse a partir de los dos diámetros | geometría | ✅ Alta |
| **Biomasa aérea** | ecuaciones alométricas | **Dobbs, Hernández & Escobedo 2011** (11 especies urbanas de Chile central) + genéricas con **factor urbano 0,8** | 🟡 Media |
| **Biomasa total** | aérea × (1 + 0,26 raíz/tallo) | i-Tree / Nowak | 🟡 Media |
| **Carbono almacenado** | biomasa seca × **0,47** | fracción IPCC | 🟡 Media |
| **CO₂ equivalente almacenado** | carbono × **3,67** | estequiometría | 🟡 Media (hereda la anterior) |
| **Secuestro bruto anual** | tasas de crecimiento por especie **ajustadas por estado sanitario, exposición a la luz y uso de suelo** | **i-Tree Eco v6** | 🟠 Media-baja |
| **Secuestro neto anual** | bruto − mortalidad y descomposición modeladas | i-Tree Eco v6 | 🟠 Media-baja |
| **🔑 Valor económico del árbol** | **Vt = Vb · fd · fu · fs** | **Ordenanza 004/2021, Art. 32** | ✅ **Alta** — ver §3 |
| Área foliar e índice de área foliar | de copa + especie | i-Tree | 🟡 Media |
| Escorrentía evitada | LAI + precipitación horaria | i-Tree Hydro | 🟠 requiere datos horarios |
| Remoción de contaminantes | LAI + contaminación horaria | i-Tree | 🔴 ver §6 |
| Producción de O₂ | secuestro × 2,67 | estequiometría | ⚫ ver §5 |

### Categoría 3 — LO QUE SOLO SE SABE VOLVIENDO A MEDIR

Requiere dos o más mediciones de **los mismos árboles**, separadas por años. **Es el segundo producto del Observatorio, no una promesa de esta etapa.**

| Indicador | Cada cuánto |
|---|---|
| **Crecimiento diamétrico real** | 3-5 años |
| **Secuestro medido** (no estimado) | 3-5 años |
| **Validación local de los modelos**: ¿acertó i-Tree en Temuco? | 3-5 años |
| **🔑 Calibración de ecuaciones alométricas para especies del sur** | 5-10 años |
| Tasa real de mortalidad y de reposición | 3-5 años |
| Pérdida de arbolado por tala | continuo (satélite + denuncias) |
| Cambio en la biodiversidad asociada | 3-5 años |
| Efecto de intervenciones (podas, plantaciones) | según el caso |

💡 **La calibración de ecuaciones para especies nativas del sur es un vacío real de la literatura chilena** —lo detectamos en la investigación previa— y una línea base marcada hoy es el único camino para llenarlo. Es el argumento de largo plazo más fuerte que tiene el proyecto: no es "queremos seguir", es "esto solo se puede resolver empezando ahora".

---

## 3. 🔑 El hallazgo: la propia Ordenanza tiene su fórmula de valoración

El **Art. 32 de la Ordenanza 004/2021** establece cómo se calculan los derechos municipales por daño o destrucción de un árbol:

> **Vt = Vb · fd · fu · fs**

| Factor | Qué es | Valores |
|---|---|---|
| **Vb** | Valor base en UTM, por **grupo de especie** y **edad** | de 1,0 UTM (Grupo 1, 1-4 años) hasta ~30 UTM (Grupo 3, 41-45 años) |
| **fd** | **Sanidad** | Sano 100% · Leve 70% · Mediana 50% · Fuerte 40% · **Muerto 0%** |
| **fu** | **Ubicación** | Plazas y parques **200%** · Calle alta visibilidad **150%** · Media **80%** · Baja **50%** |
| **fs** | **Singularidad** | Patrimonial **500%** · Alto valor de conservación **400%** · Monumento natural **700%** |

Los grupos de especie: **Grupo 1** exóticas comunes de crecimiento rápido (acacias, acer negundo, liquidámbar, álamo, sauce…), **Grupo 2** ornamentales y coníferas (ginkgo, plátano oriental, roble europeo, tilo…), **Grupo 3** **nativas de alto valor** (araucaria, nothofagus, quillay, boldo, lingue, canelo, avellano, maitén, luma…).

### Por qué esto es mejor que cualquier cifra de carbono importada

1. **Todas sus variables son las que ya medimos**: especie, sanidad, emplazamiento y singularidad.
2. **Es derecho vigente en Temuco**, no un modelo estadounidense. Nadie puede discutir la metodología: la escribió el municipio.
3. **Está en UTM**, o sea que se actualiza sola.
4. **Es directamente accionable**: cuando alguien tala un árbol, ese número es lo que el municipio debería cobrar. Un catastro ciudadano que dice *"este árbol vale X UTM según su propia ordenanza"* es un instrumento de protección, no un dato de divulgación.
5. **Le da peso normativo a H1**: la Ordenanza ya valora más a las nativas (Grupo 3). Si nuestros datos muestran que **el tamaño sostiene más biodiversidad que el origen**, eso interpela directamente a la fórmula municipal — y esa tensión es un resultado publicable.

### ⚠️ El problema que hay que resolver: Vb depende de la EDAD

La tabla de valor base está construida por **rangos de edad**, y la edad **no se mide** (habría que barrenar el tronco). Tres salidas posibles:

| Opción | Qué implica |
|---|---|
| **a) Convertir DAP a edad** con curvas de crecimiento por especie | Introduce un supuesto fuerte y no hay curvas locales para muchas especies |
| **b) Reportar rangos**: "entre X e Y UTM según el rango de edad" | Honesto, defendible, y es lo que recomiendo |
| **c) Consultar a la DMAO** cómo aplican la tabla en la práctica | **La mejor**: si el municipio ya tiene un criterio DAP→edad, lo adoptamos y quedamos alineados con quien cobra |

💡 Y esto conecta con la Categoría 3: **la remedición a 3-5 años entrega crecimiento diamétrico real por especie en Temuco**, que es exactamente lo que hace falta para convertir DAP en edad con base local. **El sistema de monitoreo resuelve la limitación de la línea base.** Es el mejor argumento de continuidad que tiene el proyecto.

---

## 4. Los dos productos, como pediste

### Producto 1 — Línea base ciudadana (los 9 meses)

> **¿Qué árboles tenemos hoy, cómo son, qué vida sostienen y cuánto valen?**

- Catastro de 200-350 árboles con ficha completa y código permanente.
- Biodiversidad asociada a cada individuo, validada vía iNaturalist y por la especialista.
- **Servicios ecosistémicos estimados**: sombra, carbono almacenado, secuestro anual y **valor según Art. 32**, todos con método e incertidumbre declarados.
- Contraste del error de los datos ciudadanos (submuestra de control).
- Respuesta a las hipótesis H1, H2 y H4.

### Producto 2 — Sistema de monitoreo (queda instalado)

> **¿Cómo volvemos a medir estos mismos árboles dentro de tres años?**

- **Protocolo** replicable, probado en tres comunidades distintas.
- **Árboles georreferenciados con código único**, más la prueba de relocalización a ciegas que verifica que se pueden reencontrar.
- **Docentes formados** capaces de repetir el ciclo sin nosotros.
- **Datos abiertos** en el observatorio, que ya existe y no cuesta operar.
- **Agenda científica explícita** de lo que la remedición permitirá: crecimiento real, validación de modelos y calibración de ecuaciones locales.

**Esta estructura de dos productos es, además, la mejor respuesta al requisito del fondo** de *"generar acciones que puedan impulsar mayores acciones a largo plazo"*: la continuidad no es una intención declarada, es una **consecuencia metodológica**. La línea base no sirve de nada sin la segunda medición, y por eso el proyecto está diseñado para que exista.

---

## 5. Oxígeno: veredicto científico

Me pediste evaluarlo. Mi conclusión no cambia, y ahora la fundamento mejor:

1. **No es una medición ni una estimación independiente.** Se deriva del secuestro neto de carbono multiplicando por **2,67** (relación 32/12). Es el mismo dato con otra unidad: **cero información nueva**.
2. **Sus propios autores lo descartan.** Nowak, Hoehn & Crane (2007) concluyen que el beneficio es *"relativamente insignificante"* y de valor prácticamente nulo, porque la reserva atmosférica de oxígeno es enorme y ningún arbolado urbano la condiciona.
3. **Hereda toda la incertidumbre** del secuestro, que es nuestro indicador menos confiable.

> **Veredicto: fuera de los indicadores. Dentro como contenido educativo.**

Y como contenido educativo es **excelente**, porque enseña dos cosas a la vez: cómo funciona la fotosíntesis, y **por qué una cifra que suena impresionante puede no significar nada**. Esa segunda lección —aprender a preguntarle a un número de dónde salió— es alfabetización científica de la buena, y encaja con el sello del proyecto.

---

## 6. Contaminación del aire: veredicto

Me pediste evaluar si hay metodología rigurosa aplicable. La hay, y **no es viable para nosotros ahora**, por tres razones acumulativas:

1. **Requiere datos horarios** de contaminación y meteorología cargados al sistema i-Tree. Es factible —el SINCA tiene estación en Temuco por el problema de la leña— pero es un pipeline de datos completo, no un cálculo.
2. **El módulo de efectos en salud es exclusivo de EE.UU.** y no está disponible para proyectos internacionales. O sea que ni siquiera podríamos traducirlo a lo que la gente quiere saber.
3. **La magnitud real es pequeña** (del orden del 1% de la concentración ambiente) y **en cañón de calle el arbolado puede empeorar la calidad del aire** al reducir la ventilación.

> **Veredicto: fuera de los indicadores principales.**

**Pero el tema no se abandona: se aborda por la vía correcta.** Los **líquenes son bioindicadores de calidad del aire** — no la limpian, la *registran*. Nuestra hipótesis H3 usa su riqueza y cobertura como señal del gradiente de contaminación por leña. Es una aproximación:

- **medible por estudiantes** con una grilla de acetato,
- **científicamente establecida** como método de biomonitoreo,
- y **honesta**, porque no afirma que los árboles limpien nada.

Es el mismo tema tratado con rigor en vez de con una cifra inventada.

---

## 7. Qué cambia en la ficha de terreno

El Art. 32 obliga a dos ajustes concretos, y ambos **mejoran** la ficha:

**a) El estado sanitario pasa de 3 a 5 clases.** La Ordenanza usa: **Sano (100%) · Leve (70%) · Mediana (50%) · Fuerte (40%) · Muerto (0%)**. Si registramos en esas cinco categorías, el factor `fd` sale directo del dato de terreno.

⚠️ **Contrapartida honesta:** más clases significa **menor concordancia entre observadores** — es exactamente el problema que el control de calidad mide con el índice kappa. **Propuesta:** registrar en las 5 clases de la Ordenanza pero **analizar la biodiversidad agrupando en 3** (sano / intermedio / malo). Así el dato normativo y el dato ecológico conviven sin sacrificar ninguno. El piloto dirá si los estudiantes distinguen cinco niveles de forma consistente.

**b) El emplazamiento se alinea con el factor `fu`.** Cambiar las categorías actuales por las de la Ordenanza: **plaza o parque · calle de alta visibilidad · calle de visibilidad media · calle de baja visibilidad**, agregando *patio escolar* como categoría propia.

Y una tercera, opcional: un campo de **singularidad** (`fs`) que se llena solo si el árbol es candidato a patrimonial — lo que enlaza directamente con los expedientes del Art. 9.

---

## 8. Cómo se declara esto en la postulación

La redacción tiene que sostener la distinción con precisión. Propuesta de fórmula:

> *"El proyecto levanta una línea base ciudadana del arbolado urbano de Temuco. Sobre las variables medidas en terreno —especie, diámetro, altura, copa, estado sanitario y emplazamiento— se **estiman**, mediante ecuaciones alométricas y modelos validados internacionalmente, el carbono almacenado y el secuestro anual de carbono, así como el **valor económico de cada ejemplar según la fórmula del Art. 32 de la Ordenanza Municipal 004/2021**. Todas las estimaciones se publican con su metodología, sus supuestos y su rango de incertidumbre. El proyecto **no afirma haber medido** el carbono capturado durante su ejecución: la verificación de las estimaciones requiere volver a medir los mismos árboles, y para eso queda instalado el sistema de monitoreo."*

Esa última frase es la que separa esta propuesta de las que prometen de más — y es la que un evaluador con formación científica va a agradecer.

---

## 9. Resumen de la corrección

| Antes decía | Ahora dice |
|---|---|
| Carbono almacenado: "estimable, pero fuera" | ✅ **Dentro**, como estimación con rango declarado |
| Secuestro anual: "físicamente imposible" | ✅ **Dentro como estimación** (i-Tree lo hace desde un solo inventario). Lo imposible es **medirlo** en 9 meses |
| Oxígeno: fuera | ⚫ **Fuera de indicadores, dentro como contenido educativo** — sin cambios, ahora fundamentado |
| Contaminación: fuera | 🔴 **Fuera de indicadores principales**; el tema se aborda vía **líquenes como bioindicadores** |
| Valor económico | 🔑 **Nuevo: la fórmula del Art. 32 de la propia Ordenanza** |
| Un solo producto | **Dos**: línea base y sistema de monitoreo |
