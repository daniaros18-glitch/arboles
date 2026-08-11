# Servicios ecosistémicos del arbolado e Índice de Habitabilidad Ecológica

**Informe de factibilidad para el Observatorio Ciudadano del Arbolado Urbano de Temuco**
Fecha: 10 de agosto de 2026 · Estado: investigación previa, ninguna cifra publicada aún en el sitio.

> **Cómo leer este documento.** No es una propuesta de venta: es una evaluación de qué se puede
> medir con rigor, qué solo se puede modelar, y qué directamente no deberíamos afirmar. Las dos
> líneas son viables, pero **ninguna de las dos lo es en la forma en que suelen presentarse**.
> Las secciones críticas (§3.6, §6, §8) son las más importantes del informe.

---

## Resumen ejecutivo

**Línea 1 — Servicios ecosistémicos.** Sí es posible, con una distinción que hay que sostener en
todo el proyecto: **casi nada de esto se mide; casi todo se modela.** Lo único que se mide en
terreno son dimensiones del árbol (especie, diámetro, altura, copa). Carbono, contaminantes, agua
y enfriamiento son **salidas de modelos** alimentados por esas dimensiones. El marco de referencia
mundial es **i-Tree Eco** (USDA Forest Service), que exige solo dos variables obligatorias —especie
y DAP— pero cuya calidad depende de ocho variables adicionales altamente recomendadas.

Hay una buena noticia específica para Chile: **Dobbs, Hernández & Escobedo (2011)** publicaron
ecuaciones alométricas no destructivas para 11 especies del arbolado urbano de Santiago, ocho de
ellas exóticas que también son comunes en Temuco.

Y hay dos advertencias que conviene incorporar desde el día uno: **la producción de oxígeno es
irrelevante como argumento** (lo dice el propio autor del método), y **"los árboles limpian el
aire" es falso en cañón de calle con tráfico**, donde pueden empeorar la concentración.

**Línea 2 — Índice de habitabilidad ecológica.** Es viable y es probablemente el aporte más
valioso que el Observatorio puede hacer, **pero solo si se construye como un tablero de subíndices
transparentes y no como un número único**. La literatura de indicadores compuestos (Manual
OECD/JRC) es explícita: la ponderación es un juicio de valor, no un resultado del dato, y un
índice agregado permite que un buen puntaje en una dimensión tape un déficit grave en otra.
Recomiendo **publicar 4 subíndices + un índice compuesto claramente marcado como resumen
comunicacional**, con la fórmula, los pesos y el análisis de sensibilidad a la vista.

---

# PARTE 1 — Servicios ecosistémicos del arbolado

## 1. La distinción que hay que sostener: medido vs. modelado

Esta es la fuente número uno de greenwashing involuntario en observatorios de arbolado. La cadena
real es:

```
SE MIDE           →   SE DERIVA          →   SE MODELA
(en terreno)          (por ecuación)         (por modelo + datos externos)

especie               área foliar            carbono almacenado
diámetro (DAP)        biomasa foliar         secuestro anual de CO2
altura total                                 remoción de contaminantes
altura de copa                               escorrentía evitada
ancho de copa                                transpiración
% de copa faltante                           efecto en temperatura
estado sanitario                             emisión de COV
exposición a la luz                          valor compensatorio
uso de suelo                                 hábitat para fauna
```

**Ninguno de los servicios de la tercera columna se mide.** Todos son estimaciones. Decir "este
árbol captura X kg de CO2" es, estrictamente, "un modelo calibrado en otro país estima que un
árbol de esta especie, diámetro y estado sanitario capturaría X kg de CO2 al año".

### 1.1 Los cuatro conceptos de carbono que se confunden (y no son lo mismo)

| Concepto | Qué es | Unidad | Naturaleza |
|---|---|---|---|
| **Carbono almacenado** (*storage*) | El carbono acumulado en la madera a lo largo de toda la vida del árbol. Es un **stock**. | kg C (o t C) | Se estima de la biomasa vía alometría |
| **Secuestro bruto** (*gross sequestration*) | Cuánto carbono nuevo fija el árbol en **un año**. Es un **flujo**. | kg C/año | Se estima del crecimiento anual modelado |
| **Secuestro neto** (*net sequestration*) | El bruto **menos** las emisiones por mortalidad y descomposición del arbolado que muere. | kg C/año | Puede ser negativo si muere mucho arbolado maduro |
| **CO₂ equivalente** | El carbono expresado como dióxido de carbono: **× 3,67** (44/12). | kg CO₂ | Conversión estequiométrica |

**Errores frecuentes que debemos evitar:**

- Presentar el **stock** como si fuera un flujo anual ("este árbol captura 800 kg de CO₂" cuando
  esos 800 kg son lo acumulado en 60 años).
- Publicar el **bruto** y no el **neto**. En una ciudad que pierde arbolado maduro —como Temuco,
  donde medimos 139 ha perdidas— el neto puede ser mucho menor, o negativo. El neto es la cifra
  honesta y, en nuestro caso, además es la **cifra políticamente más fuerte**.
- Mezclar kg C y kg CO₂ (difieren en un factor 3,67 — es el error de redondeo más caro del rubro).

### 1.2 Oxígeno: la métrica que hay que dejar fuera

La producción de O₂ **no se mide ni se modela aparte**: se deriva estequiométricamente del
secuestro neto de carbono. Por cada gramo de carbono fijado se liberan **2,67 g de O₂** (32/12).

Es decir, **no aporta información nueva**: es el mismo dato multiplicado por una constante.

Y hay algo más importante. Nowak, Hoehn & Crane (2007), los autores del método, concluyen que
**este beneficio es "relativamente insignificante" y de valor prácticamente nulo**, porque la
atmósfera tiene una reserva de oxígeno enorme y no existe escenario en que el arbolado urbano la
condicione. Los árboles urbanos de EE.UU. producen O₂ para dos tercios de la población, y aun así
los autores lo descartan como argumento.

**Recomendación:** no publicar cifras de oxígeno como beneficio. Si se menciona, mencionarlo
explicando por qué **no** es un buen argumento. Es exactamente el tipo de cifra impresionante y
vacía que el criterio editorial de este proyecto rechaza — y desmontarla nos da credibilidad.

---

## 2. Qué variables registrar por árbol (fuente autoritativa)

Esta tabla está tomada directamente de la documentación oficial de i-Tree Eco v6
(*Use of Direct Measures by i-Tree Eco*, 18-01-2018). **D** = usada directamente ·
**I** = indirectamente (vía área foliar) · **C** = condicional (perennes y palmas).

| Variable de terreno | C. almacenado | Secuestro | Contaminantes | Escorrentía | Energía | Valor comp. | Fauna |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **Especie** | D | D | I | I | D | D | |
| **DAP** (diámetro a 1,3 m) | D | D | | | | D | D |
| **Altura total** | D | D | I | I | D | | D |
| Altura a la base de copa | C | | I | I | | | |
| Ancho de copa | C | | I | I | | | |
| % de copa faltante | C | | I | I | D | | |
| Estado sanitario (*dieback*) | | D | | | | D | D |
| Exposición a la luz (CLE) | | D | | | | | |
| Uso de suelo | D | D | | | | D | D |
| Distancia y orientación al edificio | | | | | D | | |
| % cobertura arbórea del sector | | | D | D | D | | D |

### 2.1 El mínimo, el recomendado y qué pasa si falta

**Obligatorio (i-Tree corre con esto):** especie + DAP. Nada más.

**Altamente recomendado** (ocho variables): uso de suelo, altura total, altura de copa viva,
altura a la base de copa, ancho de copa, % de copa faltante, estado sanitario y exposición a la luz.

**Si no se recogen, el modelo las inventa** — y así lo dice la documentación oficial:

| Variable ausente | Qué hace el modelo | Riesgo |
|---|---|---|
| Uso de suelo | asume "residencial" | sesgo en factor de ajuste de biomasa |
| Altura total | la predice por regresión desde el DAP | **tiende al promedio**: subestima árboles altos, sobreestima bajos |
| Altura a base de copa / ancho de copa | regresión desde DAP | ídem |
| % de copa faltante | asume 13% | — |
| **Estado sanitario** | **asume 13% de muerte regresiva (87% de condición)** | **clasifica árboles muertos o moribundos como sanos y en crecimiento → sobreestima el secuestro** |
| Exposición a la luz | asume clase 2-3 | sesgo en tasa de crecimiento |

Ese penúltimo punto es crítico para nosotros: **si no registramos estado sanitario, el modelo
sobreestima sistemáticamente la captura**, justo en la dirección que nos conviene. Es una trampa
de confirmación y hay que evitarla registrando la variable.

> ⚠️ **Sesgo de regresión al promedio.** La documentación advierte que predecir altura desde DAP
> "tiende a predecir hacia el promedio". Esto importa poco para totales de población grande (los
> errores se compensan) pero **invalida la ficha de un árbol individual**. Consecuencia directa
> para nosotros: **no publicar cifras de servicio por árbol individual** salvo que se hayan medido
> sus ocho variables.

### 2.2 Protocolo propuesto en tres niveles

| Nivel | Quién | Qué registra | Rinde |
|---|---|---|---|
| **N1 — Ciudadano** | Cualquier vecino, con el formulario del sitio | Especie (o foto para identificar), foto del tronco con referencia de escala, ubicación GPS | Presencia, especie, ubicación. **No sirve para carbono** |
| **N2 — Voluntario entrenado** | Brigada con cinta métrica y una tarde de capacitación | + **perímetro del tronco a 1,3 m** (→ DAP = perímetro/π), altura estimada con vara/app, ancho de copa por pasos, estado sanitario en 3 clases, uso de suelo | **Suficiente para i-Tree Eco con calidad razonable** |
| **N3 — Técnico** | Estudiantes de la UFRO, tesistas | + altura con clinómetro/telémetro, altura a base de copa, % copa faltante, exposición a la luz, distancia y orientación a edificios | Calidad publicable |

El salto de valor está en **N2**: con perímetro de tronco medido con una huincha de $2.000 y un
protocolo de estado sanitario de tres clases, el Observatorio pasa de "no puede estimar carbono"
a "puede estimarlo con la calidad que el propio USDA considera aceptable".

---

## 3. Metodologías disponibles

### 3.1 i-Tree Eco — el estándar de facto

Software libre del USDA Forest Service, es el marco usado internacionalmente y el que respalda
la literatura de referencia (Nowak & Crane 2002; Nowak et al. 2013).

**Para Chile hay una fricción concreta:** i-Tree Eco tiene modo internacional adaptado para
Australia, Canadá, México, Colombia, Corea del Sur y la mayoría de Europa. **Chile no está en esa
lista.** Se puede usar igual, pero exige cargar al sistema *i-Tree Database* datos horarios de
contaminación y precipitación de Temuco. Eso es factible —el SINCA del MMA tiene estación en
Temuco por el problema de leña, y la DMC tiene datos meteorológicos— pero es trabajo real, no un
clic.

**Además**: el módulo de **impactos en salud humana** de la remoción de contaminantes se basa en
un modelo de la EPA de EE.UU. y **no está disponible para proyectos internacionales**. Cualquier
cifra de "muertes evitadas" o "costos de salud ahorrados" está fuera de nuestro alcance.

### 3.2 i-Tree Canopy — la vía barata e inmediata

Herramienta web que estima cobertura arbórea por **fotointerpretación de puntos aleatorios** sobre
imagen satelital, y de ahí deriva estimaciones gruesas de carbono y contaminantes por unidad de
superficie. No requiere terreno, no requiere programación, corre en el navegador.

**Es el primer paso lógico para el Observatorio**: da una línea base de cobertura por barrio con
intervalo de confianza estadístico explícito, y se puede hacer en una tarde. Su debilidad es que
**no distingue especies ni estructura** — trata todo el dosel como un promedio.

### 3.3 Alometría propia: la buena noticia chilena

**Dobbs, Hernández & Escobedo (2011)**, *Bosque* 32(3) — DOI `10.4067/s0717-92002011000300010`
(verificado en Crossref) — desarrollaron ecuaciones de **biomasa aérea y área foliar por métodos
no destructivos** para árboles urbanos de dos comunas de Santiago (Lo Barnechea y La Reina).

- **11 especies**: 8 exóticas (*Ailanthus altissima, Robinia pseudoacacia, Prunus cerasifera,
  Acacia melanoxylon, Acacia dealbata, Acer negundo, Liquidambar styraciflua, Platanus × acerifolia*)
  y 3 nativas (*Schinus molle, Quillaja saponaria, Maytenus boaria*).
- **Predictores**: DAP y altura total — exactamente lo que un voluntario N2 puede medir.
- **Muestra**: 10 árboles por especie (biomasa), 5 (área foliar). **Es una muestra pequeña.**
- **Ajuste**: R² > 0,60 en solo 3 de las especies para biomasa de ramas; 0,40–0,60 en otras cuatro.

**Qué significa esto para Temuco.** Varias de esas especies —plátano oriental, liquidámbar, acer
negundo, robinia, acacias— son abundantes en el arbolado de Temuco, así que las ecuaciones son
**más pertinentes que las genéricas de EE.UU.** Pero hay que decir tres cosas:

1. Santiago es clima mediterráneo semiárido; Temuco es templado lluvioso. **El crecimiento no es
   el mismo**, y las ecuaciones no fueron validadas fuera de su zona.
2. Los R² son modestos. Para totales de barrio sirven; para un árbol, no.
3. **Faltan las especies nativas del sur** que importan acá (roble, laurel, ulmo, avellano). Ese
   es un vacío real y una oportunidad de investigación con la UFRO.

**Factor de corrección urbano.** La literatura establece que las ecuaciones desarrolladas para
árboles de bosque **sobreestiman** la biomasa de árboles urbanos (que crecen más abiertos, con más
copa y menos fuste), y por eso i-Tree aplica un **factor de 0,8**. Si usamos ecuaciones forestales
chilenas (que las hay, de INFOR) hay que aplicar esa corrección o estaremos inflando el resultado.

### 3.4 Fracción de carbono

Convención IPCC: la biomasa seca es **47% carbono**. Y biomasa total = biomasa aérea ×
(1 + relación raíz/tallo); i-Tree usa **0,26** para árboles urbanos.

### 3.5 Enfriamiento — lo que ya tenemos y no necesita modelo

Esta es la excepción feliz: **el enfriamiento sí lo estamos midiendo**, no modelando. La
comparación por grupos que ya publica el sitio (29,3 °C donde el dosel se mantuvo · 30,8 °C donde
se perdió · 31,6 °C donde nunca hubo) es **observación satelital directa de temperatura de
superficie**, no una salida de i-Tree.

Es, con diferencia, nuestro dato más sólido y el que menos supuestos arrastra. Conviene apoyarse
en él antes que en el carbono.

### 3.6 ⚠️ Remoción de contaminantes: el servicio que NO deberíamos publicar todavía

Es el más pedido y el más riesgoso. Dos problemas independientes:

**(a) La magnitud real es pequeña.** Los porcentajes de remoción que reporta la literatura para
material particulado a escala urbana son de orden de **1%** de la concentración ambiente. Es
positivo pero no es una solución a la contaminación por leña de Temuco, y presentarlo como tal
sería deshonesto.

**(b) En cañón de calle, los árboles pueden EMPEORAR la calidad del aire.** Es la llamada *green
paradox*: la copa **reduce la ventilación** del cañón y atrapa lo que se emite dentro (los autos).
Estudios de modelación reportan **aumentos** de concentración a nivel peatonal por presencia de
arbolado —hasta ~13% en un caso, +8% de carbono elemental en otro—, especialmente en el lado de
sotavento. El efecto depende críticamente de **dónde se origina el contaminante**: si viene de
fuera del cañón, el árbol ayuda; si se emite dentro (tráfico), puede atrapar.

**Recomendación firme:** no publicar cifras de "toneladas de contaminantes removidas". Si se
aborda el tema, hacerlo como **contenido educativo sobre el matiz**, que además es un contenido
diferenciador: casi ningún observatorio lo dice.

### 3.7 Escorrentía evitada, transpiración, biodiversidad

- **Escorrentía evitada**: i-Tree la estima solo desde **% de cobertura arbórea** y área foliar.
  No requiere datos de terreno adicionales, pero sí precipitación horaria local. Viable en fase 2.
- **Transpiración**: la documentación oficial dice literalmente **"NO DIRECT MEASURES"** — es
  íntegramente modelada. Baja prioridad.
- **Biodiversidad**: i-Tree tiene un módulo de idoneidad de hábitat para aves, **calibrado con
  especies de EE.UU.** — inservible acá. La vía realista en Chile es distinta y mejor:
  **ciencia ciudadana con eBird/iNaturalist** cruzada con nuestra capa de dosel. Ahí sí hay
  observación real y hay comunidad activa.

---

## 4. Qué aporta cada tecnología de observación

| Plataforma | Qué entrega de verdad | Resolución | Costo | Estado en el proyecto |
|---|---|---|---|---|
| **Landsat (30 m)** | Cobertura verde, cambio multitemporal, **temperatura de superficie** | Barrio | Gratis | ✅ **Operativo** |
| **Sentinel-2 (10 m)** | Cobertura, índices de vegetación | Manzana | Gratis | ✅ Operativo |
| **Google Dynamic World (10 m)** | Separa árbol de pasto/cultivo | Manzana | Gratis | ✅ Operativo |
| **Canopy Height Meta/WRI (~1 m)** | **Altura de dosel** — la única vía masiva a estructura vertical | Árbol grande / grupo | Gratis | ✅ Operativo (una sola época, ~2020) |
| **Ortofoto / fotografía aérea** | Delimitación de copas individuales, % cobertura | Árbol | Variable | ⬜ Ver IDE Municipal |
| **Google Street View** | **Green View Index** (verde percibido desde la vereda), especie a veces identificable | Calle | Gratis (API con cuota) | ⬜ Alto potencial |
| **Dron (fotogrametría SfM)** | Altura, ancho de copa, modelo 3D del corredor | Árbol individual | Bajo-medio | ⬜ Ideal para el corredor piloto |
| **LiDAR móvil de bajo costo** | **DAP con RMSE ~5 cm**, altura, estructura | Árbol individual | Medio | ⬜ Vía tesis UFRO |
| **Terreno (huincha)** | DAP real, especie confirmada, **estado sanitario** | Árbol individual | Casi cero | ⬜ **La pieza que falta** |

**Lo que ninguna imagen puede darnos:** el **DAP** y el **estado sanitario**. El DAP es la variable
que manda en toda la alometría de carbono, y la salud de la copa es la que evita sobreestimar el
secuestro. Ambas requieren a alguien parado junto al árbol.

Ese es el argumento técnico —no sentimental— de por qué el Observatorio necesita ciencia ciudadana
y no solo satélite: **el satélite localiza y prioriza; la vereda mide lo que decide el resultado.**

---

# PARTE 2 — Índice de Habitabilidad Ecológica Urbana

## 5. Qué existe ya (no hay que inventar desde cero, pero tampoco copiar)

| Marco | Qué es | Qué tomar | Qué no |
|---|---|---|---|
| **Regla 3-30-300** (Konijnendijk 2022, *J. Forestry Research*, DOI `10.1007/s11676-022-01523-z`) | 3 árboles visibles desde cada casa · 30% de dosel por barrio · 300 m a un área verde de calidad | **Umbrales concretos, comunicables y verificables.** Es lo más útil que existe para nuestro caso | Es una *regla de oro*, no un índice validado; sus umbrales son razonables pero no derivados de un modelo dosis-respuesta |
| **Índice de Singapur / City Biodiversity Index** (CBD) | 23 indicadores en 3 componentes: biodiversidad nativa, servicios ecosistémicos, gobernanza | La **estructura de tres componentes** y la idea de autoevaluación contra la propia línea base | Es de **autoevaluación municipal**, diseñado para que una ciudad se compare consigo misma. No sirve para rankear barrios |
| **Green View Index** (MIT Senseable City / Treepedia) | % de verde visible desde la calle, por visión computacional sobre Street View | **Directamente aplicable y gratis.** Mide el verde *percibido*, que es lo que la gente vive | Depende de cobertura y fecha de Street View; confunde arbolado con muro verde o pasto alto |
| **Manual OECD/JRC de Indicadores Compuestos** (2008) | El manual metodológico de referencia: 10 pasos, normalización, ponderación, agregación, robustez | **La disciplina metodológica completa.** Es la referencia que nos obliga a hacerlo bien | No es un índice: es cómo construir uno |
| **Índice de Gini aplicado a verde urbano** | Mide desigualdad en la distribución del verde entre unidades | Excelente para **equidad**: un número interpretable y comparable entre ciudades | **No informa cantidad**: una ciudad puede ser perfectamente equitativa en la miseria. Nunca usarlo solo |
| **Estándar SIEDU / 10 m² por habitante** | Referencia nacional de área verde por habitante | Comparabilidad con política pública chilena | El famoso "9 m²/hab de la OMS" **es discutido**: no corresponde a un estándar formal vigente de la OMS. Usarlo con cuidado |

**Conclusión de la revisión:** no existe un índice consolidado de "habitabilidad ecológica" que
podamos adoptar tal cual. Lo que existe son **piezas sólidas** (umbrales del 3-30-300, estructura
del CBI, Gini para equidad, GVI para verde percibido) y un **manual metodológico** que dice cómo
combinarlas sin hacer el ridículo. Construir uno propio está justificado — con condiciones.

---

## 6. Evaluación crítica indicador por indicador

Criterio: ¿tiene respaldo científico? ¿lo podemos medir **nosotros**, con datos gratuitos? ¿a qué
escala? Marco con ✅ lo que entra en un piloto, 🟡 lo que entra en fase 2, ❌ lo que no debería
entrar.

| Indicador | Respaldo | ¿Podemos medirlo? | Escala | Veredicto |
|---|---|---|---|---|
| **% de cobertura arbórea** | Muy alto. Es la variable estructural central del arbolado urbano | **Sí, ya lo hacemos** (Landsat/Sentinel + Dynamic World) | Barrio | ✅ **Núcleo** |
| **Temperatura de superficie / isla de calor** | Muy alto | **Sí, ya lo hacemos** (Landsat térmico) | Barrio | ✅ **Núcleo** |
| **Área verde por habitante** | Alto como indicador de política; el umbral concreto es débil | Sí (catastro INE 2024 + Censo 2024) | Barrio | ✅ **Núcleo** |
| **Distancia a área verde (300 m)** | Alto — es la métrica de acceso que la evidencia respalda mejor | Sí (SIG: red de calles + polígonos de áreas verdes) | Manzana | ✅ **Núcleo** — y es mejor que m²/hab |
| **Equidad distributiva (Gini del dosel)** | Alto | Sí, se calcula de lo que ya tenemos | Ciudad | ✅ **Núcleo** |
| **Vulnerabilidad social** | Alto en justicia ambiental | Sí (Censo 2024) | Barrio | ✅ Como **modulador**, no como componente ecológico |
| **Verde percibido (GVI)** | Medio-alto y creciente | Sí, Street View + visión computacional | Calle | 🟡 Fase 2 — alto valor comunicacional |
| **Altura/estructura del dosel** | Alto (un dosel alto no equivale a arbustos) | Sí (Canopy Height Meta/WRI) | Barrio | 🟡 Fase 2 |
| **Carbono almacenado** | Alto en método, **débil en dato local** | Solo con terreno N2 + alometría chilena | Barrio | 🟡 Fase 2, y **como estimación con rango** |
| **Especies nativas (%)** | Alto conceptualmente | Solo con inventario en terreno. **No se puede desde satélite** | Árbol → barrio | 🟡 Fase 2, empezando por corredor piloto |
| **Conectividad ecológica** | Alto en ecología del paisaje | Parcialmente: métricas de fragmentación sobre nuestra capa de dosel | Ciudad | 🟡 Fase 2 — cuidado con la sofisticación aparente |
| **Biodiversidad (aves, fauna)** | Alto | Solo vía eBird/iNaturalist. Sesgo de muestreo fuerte (se observa donde va la gente) | Barrio | 🟡 Fase 2, **declarando el sesgo** |
| **Regulación hídrica / infiltración** | Alto en teoría | Modelable, no medible por nosotros. Requiere precipitación horaria y suelos | Barrio | ❌ Fuera del piloto |
| **Calidad del aire** | Alto | **Solo 1-2 estaciones SINCA en Temuco** → no hay resolución de barrio. Y el efecto del arbolado es ambiguo (§3.6) | Ciudad | ❌ Fuera del índice. Como contexto, sí |
| **Proximidad a espacios naturales** | Medio | Sí, pero se solapa con "distancia a área verde" | Barrio | ❌ Redundante |
| **Producción de oxígeno** | **Nulo como argumento** (§1.2) | Trivial de calcular, irrelevante | — | ❌ **Excluir** |

**Regla que se desprende:** el índice piloto debe construirse **solo con lo que ya medimos o
podemos medir sin depender de nadie**. Cada indicador que exija un dato que no controlamos es un
punto de falla que dejará el índice desactualizado en un año.

---

## 7. Estructura propuesta

### 7.1 Cuatro subíndices, no uno

```
ÍNDICE DE HABITABILIDAD ECOLÓGICA (IHE) — barrio (unidad vecinal)
│
├── A. INFRAESTRUCTURA VERDE          ¿cuánto verde hay?
│      · % de cobertura arbórea
│      · m² de área verde por habitante
│      · altura media del dosel (fase 2)
│
├── B. CONFORT CLIMÁTICO              ¿qué tan habitable es en verano?
│      · temperatura de superficie relativa al promedio de la ciudad
│      · diferencia térmica con el barrio más fresco
│
├── C. ACCESO                         ¿le llega a la gente?
│      · % de población a menos de 300 m de un área verde
│      · verde percibido desde la calle (GVI, fase 2)
│
└── D. EQUIDAD                        ¿está bien repartido?
       · posición del barrio en la distribución comunal (Gini)
       · cruce con vulnerabilidad social del Censo 2024
```

**Por qué cuatro y no seis.** Descarté "regulación hídrica" y "calidad ambiental" como subíndices
porque no tenemos datos propios para sostenerlos a escala de barrio. Un subíndice alimentado por
un solo indicador débil da la **apariencia** de completitud y en realidad agrega ruido. Es
preferible un tablero de cuatro dimensiones sólidas que uno de seis con dos huecos.

### 7.2 Normalización

**Recomendación: min–max contra referencias explícitas**, no contra el propio rango observado.

| Método | Ventaja | Por qué sí/no |
|---|---|---|
| **Min–max con anclas fijas** | Interpretable; comparable en el tiempo y con otras ciudades | ✅ **Elegido.** Ej.: dosel 0% → 0 puntos, **30% → 100 puntos** (ancla del 3-30-300) |
| Min–max contra el rango observado | Simple | ❌ **El mejor barrio siempre saca 100**, aunque toda la ciudad esté mal. Y el índice cambia cada año aunque nada cambie |
| Puntaje z | Estadísticamente correcto | ❌ Ininterpretable para un vecino, y también es relativo |
| Percentiles | Robusto a extremos | 🟡 Útil como vista secundaria |

Anclar en el 3-30-300 tiene una ventaja política enorme: **el 100 significa algo** ("este barrio
alcanza el estándar internacional"), no "este barrio es el mejor de Temuco".

### 7.3 ¿Tiene sentido un 0–100?

**Sí, con dos condiciones.** Es la escala que la gente entiende y la que hace que un dirigente
vecinal pueda pararse en el municipio a decir "mi barrio saca 38". Pero:

1. **El número compuesto nunca debe presentarse solo.** Siempre junto a los cuatro subíndices.
2. **Debe poder desarmarse.** Un clic desde el 38 debe llevar a "porque el dosel es 3% y la
   temperatura es 32,4 °C".

### 7.4 Ponderación: dígase que es una decisión, no un hallazgo

El Manual OECD/JRC es explícito: los pesos son **juicios de valor**, y hay que someterlos a
análisis de robustez. Propuesta de partida:

| Subíndice | Peso | Justificación |
|---|---|---|
| A. Infraestructura verde | 30% | Es la variable que el municipio **puede modificar plantando** |
| B. Confort climático | 25% | Es el impacto medido con mayor solidez en nuestros datos |
| C. Acceso | 25% | La evidencia de salud se asocia al acceso, no a la cantidad total |
| D. Equidad | 20% | Es el propósito declarado del Observatorio |

**Obligación metodológica que asumimos:** publicar el índice con **al menos tres esquemas de
peso** (el propuesto, uno equiponderado 25/25/25/25, y uno que priorice equidad) y mostrar cuánto
cambia el ranking. Si el orden de los barrios prioritarios **no cambia**, el resultado es robusto y
eso vale más que cualquier defensa retórica de los pesos. Si cambia mucho, el índice no está
maduro para publicarse como ranking.

### 7.5 Agregación: evitar que un puntaje tape otro

La suma ponderada es **totalmente compensatoria**: 30% de dosel compensa un calor extremo. Para
evitarlo, dos opciones:

- **Media geométrica** en vez de aritmética: penaliza los desequilibrios, un cero en cualquier
  dimensión arrastra el total. Es lo que usa el **Índice de Desarrollo Humano** desde 2010,
  precisamente por esta razón.
- **Regla de bandera**: mantener la suma ponderada pero marcar con alerta visible cualquier barrio
  que esté bajo un umbral crítico en **cualquier** dimensión, sin importar su puntaje total.

**Recomendación: media geométrica + regla de bandera.**

---

## 8. Debilidades, riesgos y objeciones (la sección que importa)

Es la parte que pediste explícitamente, y es donde el proyecto se juega la credibilidad.

**1. Los pesos no salen del dato — salen de nosotros.** Cualquiera puede reordenar la lista de
barrios prioritarios cambiando los pesos. Mitigación: publicar el análisis de sensibilidad y no
presentar el ranking como verdad objetiva.

**2. La falacia ecológica.** Un índice de unidad vecinal **no dice nada de tu cuadra**. Dentro de
un mismo barrio hay calles arboladas y calles peladas. Riesgo concreto: que se use para negarle
prioridad a una manzana en un barrio "bien evaluado". Mitigación: declararlo en cada visualización
y bajar a manzana donde los datos lo permitan.

**3. Resolución de 30 m sobre trama urbana fina.** Nuestro dato de dosel viene de píxeles de 30 m.
Un bandejón arbolado de 10 m de ancho **desaparece** en ese píxel. El índice tiende a subestimar
sistemáticamente el arbolado lineal de calle — que es justamente el que más se pierde por tala.

**4. Precisión aparente.** Publicar "78,4 puntos" sugiere una exactitud que no existe. Mitigación:
**publicar en tramos** (muy alto / alto / medio / bajo) o con banda de incertidumbre. Un decimal
en este índice es una mentira tipográfica.

**5. El índice puede ser usado en contra.** Una inmobiliaria puede citar "barrio con alta
habitabilidad ecológica" como argumento de venta del loteo que está talando. Un municipio puede
mostrar el promedio comunal para decir que está todo bien. No hay defensa técnica: hay que
anticiparlo en la comunicación.

**6. Correlación entre indicadores = doble conteo.** Dosel y temperatura están correlacionados por
construcción: al sumar ambos estamos contando el mismo fenómeno dos veces y dándole peso
excesivo. Mitigación: reportar la matriz de correlación y considerar componentes principales como
chequeo (no como el índice publicado — sería ininterpretable).

**7. Actualizabilidad.** Un índice que no se puede recalcular cada año es un informe, no un
observatorio. Todo indicador que dependa de un dato que no controlamos es deuda futura.

**8. El riesgo de fondo: sofisticación sin sustancia.** Es perfectamente posible construir un
índice elegante, con seis subíndices y media geométrica, alimentado por datos malos. **Sería peor
que no tener índice**, porque le daría autoridad numérica a una impresión. La prueba a la que hay
que someter cada indicador es: *si este número resultara incómodo para nuestra propia tesis,
¿lo publicaríamos igual?*

---

# PARTE 3 — Metodología piloto para Temuco

## 9. Qué haría, en este orden

### Fase 0 — Con lo que ya tenemos (semanas, costo cero)

1. **Recalcular el índice de equidad actual como IHE v0.1** con los cuatro subíndices y anclas del
   3-30-300, en vez de la fórmula actual de 4 términos.
2. **Calcular el Gini del dosel** entre las 36 unidades vecinales: un número, comparable con otras
   ciudades del mundo, que resume la desigualdad de Temuco en una cifra.
3. **Calcular el indicador "300 m"**: % de población de cada unidad vecinal a menos de 300 m de un
   área verde, con la capa de áreas verdes que ya está en `investigacion/geodata/`. Es SIG puro y
   probablemente el indicador más potente y menos discutible de todos.
4. **Análisis de sensibilidad de pesos** y publicación de los tres escenarios.

### Fase 1 — El corredor piloto (un semestre, costo bajo)

5. **i-Tree Canopy** sobre Temuco para tener línea base de cobertura con intervalo de confianza,
   independiente de nuestra propia estimación satelital. Sirve de **validación cruzada**.
6. **Inventario N2 del corredor piloto** (la guía de conteo manual ya está escrita): especie,
   perímetro de tronco, altura estimada, estado sanitario en 3 clases, uso de suelo.
7. **Estimar carbono con las ecuaciones de Dobbs 2011** para las especies que coincidan, y con
   ecuaciones genéricas + factor 0,8 para el resto. **Publicar como rango, no como cifra.**
8. **Contrastar** el resultado de terreno contra lo que estimaba el satélite en el mismo corredor.
   Ese contraste —cuánto se equivoca el satélite— es un resultado publicable por sí solo.

### Fase 2 — Ampliación (año 2)

9. Green View Index sobre Street View para todo Temuco.
10. Cruce con eBird/iNaturalist para el subíndice de biodiversidad.
11. Gestión con la UFRO de ecuaciones alométricas para especies nativas del sur — el vacío real.

## 10. Herramientas, todas gratuitas

| Necesidad | Herramienta | Costo |
|---|---|---|
| Análisis satelital | Google Earth Engine | Gratis (ya autorizado) |
| Cobertura por fotointerpretación | i-Tree Canopy | Gratis, navegador |
| Servicios ecosistémicos | i-Tree Eco (requiere cargar datos de Temuco) | Gratis |
| SIG de escritorio | QGIS | Gratis |
| Distancias en red de calles | QGIS + OpenStreetMap | Gratis |
| Verde percibido | Treepedia (código abierto, MIT) + Street View API | Gratis con cuota |
| Biodiversidad | eBird / iNaturalist | Gratis |
| Datos de población | Censo 2024 (INE) | Gratis |
| Contaminación | SINCA (MMA) | Gratis |
| Terreno | Huincha métrica, app de altura, planilla | ~$20.000 total |

---

## 11. Respuestas directas a las 8 preguntas

1. **Indicadores científicamente sólidos:** cobertura arbórea, temperatura de superficie, acceso a
   300 m, área verde por habitante, Gini de distribución. Con reservas: GVI, altura de dosel,
   carbono. Fuera: oxígeno, calidad del aire a escala de barrio, regulación hídrica.
2. **Datos necesarios:** los tres primeros ya los tenemos; acceso a 300 m requiere solo SIG sobre
   capas que ya están descargadas; carbono requiere terreno.
3. **Cómo medirlos:** §4 y §9.
4. **Escala adecuada:** **unidad vecinal** para el índice (hay 36, coinciden con el Censo y con la
   organización social real); **manzana** para el indicador de acceso; **árbol** solo para el
   corredor piloto y el registro patrimonial.
5. **Normalización:** min–max con anclas fijas externas (30% de dosel = 100), no contra el rango
   observado.
6. **¿0–100?** Sí, pero acompañado siempre de los subíndices, publicado en tramos y no en decimales.
7. **Ponderación:** 30/25/25/20 como punto de partida, **declarada como decisión** y publicada con
   análisis de sensibilidad de al menos tres esquemas.
8. **Limitaciones:** §8 completa. Las tres mayores: los pesos son nuestros, el píxel de 30 m no ve
   el arbolado de calle, y un índice de barrio no dice nada de una manzana.

---

## 12. Referencias verificadas

Todas las citas siguientes fueron **verificadas contra Crossref** (título, autores, año y DOI
coincidentes) el 10-08-2026.

- **Dobbs, C., Hernández, J. & Escobedo, F. (2011).** *Above ground biomass and leaf area models
  based on a non destructive method for urban trees of two communes in Central Chile.*
  **Bosque** 32(3). DOI: [10.4067/s0717-92002011000300010](https://doi.org/10.4067/s0717-92002011000300010)
- **Nowak, D.J. & Crane, D.E. (2002).** *Carbon storage and sequestration by urban trees in the USA.*
  **Environmental Pollution** 116(3). DOI: [10.1016/s0269-7491(01)00214-7](https://doi.org/10.1016/s0269-7491(01)00214-7)
- **Nowak, D.J., Hoehn, R. & Crane, D.E. (2007).** *Oxygen Production by Urban Trees in the United States.*
  **Arboriculture & Urban Forestry** 33(3). DOI: [10.48044/jauf.2007.026](https://doi.org/10.48044/jauf.2007.026)
- **Nowak, D.J., Greenfield, E.J., Hoehn, R.E. & Lapoint, E. (2013).** *Carbon storage and
  sequestration by trees in urban and community areas of the United States.*
  **Environmental Pollution** 178. DOI: [10.1016/j.envpol.2013.03.019](https://doi.org/10.1016/j.envpol.2013.03.019)
- **Konijnendijk, C.C. (2022).** *Evidence-based guidelines for greener, healthier, more resilient
  neighbourhoods: Introducing the 3-30-300 rule.* **Journal of Forestry Research** 34.
  DOI: [10.1007/s11676-022-01523-z](https://doi.org/10.1007/s11676-022-01523-z)
  — ⚠️ Se cita frecuentemente como "2021": el artículo revisado por pares es **2022**.

**Documentación técnica** (descargada y verificada, en `investigacion/papers/itree/`):

- USDA Forest Service — *Use of Direct Measures by i-Tree Eco (v6.0)*, 18-01-2018.
  [itreetools.org](https://www.itreetools.org/documents/81/Ecov6_data_variables_ES_relationships.pdf)
- USDA Forest Service — *Eco Guide to Data Limitations*, 15-07-2020.
  [itreetools.org](https://www.itreetools.org/resources/manuals/Ecov6_ManualsGuides/Ecov6Guide_DataLimitations.pdf)
- OECD/JRC (2008) — *Handbook on Constructing Composite Indicators: Methodology and User Guide.*
  [oecd.org](https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/08/handbook-on-constructing-composite-indicators-methodology-and-user-guide_g1gh9301/9789264043466-en.pdf)
- CBD / NParks Singapore — *The City Biodiversity Index (Singapore Index).*
  [cbd.int](https://www.cbd.int/doc/meetings/cop/cop-11/information/cop-11-inf-45-en.pdf)
- MIT Senseable City Lab — *Treepedia / Green View Index* (código abierto).
  [senseable.mit.edu/treepedia](https://senseable.mit.edu/treepedia) ·
  [github.com/mittrees/Treepedia_Public](https://github.com/mittrees/Treepedia_Public)

**Referencias consultadas sin verificación individual de DOI** (usadas para contexto, no como
autoridad numérica): literatura sobre el *green paradox* en cañones de calle (Gromke & Blocken y
estudios de Rotterdam), revisión sistemática del uso del índice de Gini en desigualdad de verde
urbano (*Landscape and Urban Planning*, 2025), y literatura de LiDAR móvil de bajo costo para
inventario urbano. **Antes de citar cualquiera de estas en material público, verificar el DOI.**
