# Piloto metodológico — Paso 2

**Proyecto:** Observatorio Ciudadano del Arbolado Urbano de Temuco · Fondo FMA 2026-2027
**Escuelas vinculadas vía Ekuwün:** Escuela Campos Deportivos · Escuela Los Trigales · HablArte
**Objetivo del piloto:** **encontrar los problemas del método**, no producir resultados.
**Fecha:** 11 de agosto de 2026
**Base:** [`FMA_2026_DISENO_CIENTIFICO.md`](FMA_2026_DISENO_CIENTIFICO.md)

---

## 0. Lo primero: el vínculo con las escuelas cambia la postulación

Tener tres escuelas ya vinculadas por Ekuwün **no es un detalle logístico: es la evidencia que nos faltaba.**

Las bases del Fondo FMA excluyen "proyectos en etapa de ideas" y exigen "trayectoria previa en el territorio **y/o** con comunidades locales". Hasta ayer nuestra respuesta era trayectoria territorial (el análisis satelital) y **cero** trayectoria con comunidades escolares. Con Ekuwün, la respuesta pasa a ser **ambas**, que es lo que el evaluador quiere leer.

> ⚠️ **Corrección del 12-08-2026, tras la Jornada de Orientación.**
> Escribí más abajo que ejecutar el piloto antes del 24 de agosto era casi condición para acreditar
> trayectoria. **No es así.** La **Q4** define "etapa de ideas" como un proyecto *sin ningún grado de
> desarrollo o validación previa —sin piloto, sin trabajo previo con la comunidad, sin antecedentes de
> factibilidad—*, y la **Q9** aclara que **no se exige que el proyecto esté en ejecución**. Los criterios
> son **alternativos**, y ya cumplimos dos por vías independientes.
> **El piloto sigue siendo necesario metodológicamente** (sin el tiempo por árbol no sabemos si el
> proyecto cabe en 240 árboles), pero puede ejecutarse como primera actividad del proyecto adjudicado,
> en diciembre de 2026. Ver [`FMA_2026_REVISION_TRAS_JORNADA.md`](FMA_2026_REVISION_TRAS_JORNADA.md) §4.

---

## 1. Qué escuela elegir para el piloto (y por qué no la más fácil)

**Criterio contraintuitivo pero correcto: el piloto va en el sitio más difícil, no en el más cómodo.**

Un protocolo que funciona donde sobran árboles grandes y sanos no prueba nada. Uno que funciona donde hay pocos árboles, chicos y maltratados, funciona en cualquier parte. Además, el estrato de baja cobertura es donde el proyecto definitivo tendrá la mitad de sus sitios: conviene descubrir ahí los problemas.

### Cómo decidir con datos propios

Ubicar cada escuela en su unidad vecinal y leer su cobertura arbórea en nuestra propia capa:

| Unidad vecinal | Sector | Dosel % | LST (°C) | Prioridad |
|---|---|---|---|---|
| ESTACIÓN | urbano | 3,0 | 32,6 | 81,7 |
| JAVIERA CARRERA ORIENTE | urbano | 3,1 | 31,1 | 80,0 |
| ALEMANIA | urbano | 3,6 | 32,4 | 80,0 |
| PRIETO SUR | urbano | 3,1 | 32,4 | 79,8 |
| MUSEO FERROVIARIO | urbano | 3,2 | 31,7 | 79,8 |
| AQUELARRE | urbano | 3,5 | 31,7 | 79,6 |
| ESTADIO | urbano | 4,2 | 32,2 | 79,4 |
| SAN ANTONIO | urbano | 4,1 | 30,9 | 78,7 |
| RECABARREN | urbano | 4,2 | 32,0 | 78,7 |
| 5 SUR | urbano | 3,8 | 31,0 | 78,4 |
| VILLA ALEGRE | urbano | 5,3 | 31,1 | 78,2 |
| VALPARAÍSO | urbano | 3,3 | 30,4 | 77,5 |
| ALTO DEL BOSQUE | urbano | 5,9 | 31,2 | 77,5 |
| CERRO MARIPOSA | urbano | 6,8 | 30,5 | 76,8 |
| JAVIERA CARRERA PONIENTE | urbano | 5,8 | 31,0 | 76,7 |
| CAUPOLICÁN | urbano | 4,8 | 31,8 | 76,5 |
| LAS ENCINAS | urbano | 7,4 | **33,0** | 76,5 |
| AMANECER | urbano | 5,0 | 30,7 | 75,5 |
| INDUSTRIAL | urbano | 8,1 | 32,1 | 75,2 |
| NAHUELBUTA | urbano | 7,8 | 30,7 | 74,5 |
| BORDE RÍO | urbano | 7,0 | 30,3 | 74,2 |
| LABRANZA ALTO | urbano | 12,2 | 30,7 | 72,3 |
| RALUNCOYÁN | urbano | 15,6 | 30,6 | 72,1 |
| COIHUECO | urbano | 16,4 | 30,4 | 71,9 |
| LABRANZA UNO NORTE | urbano | 13,5 | 29,8 | 69,2 |
| CREADORES | urbano | 19,2 | 31,0 | 65,1 |
| SECTOR RIBEREÑO | urbano | 17,2 | 30,7 | 61,9 |
| BOTROLHUE | urbano | 15,9 | 29,7 | 59,6 |
| LOS RÍOS | urbano | 17,2 | 28,3 | 59,1 |
| ACCESO NORTE | urbano | 22,5 | 28,6 | 56,2 |
| COSTANERA | urbano | 21,8 | 29,4 | 48,0 |
| ÑIELOL | urbano | **52,1** | **24,4** | 7,6 |
| TROMEN MOLLULCO · BOYECO · LA SERENA · MONTE VERDE | rural | 18–55 | 23–31 | — |

**Regla de decisión (aplicar con las direcciones de las tres escuelas):**

1. Ubicar cada escuela en su UV → leer su `dosel %`.
2. **Estrato bajo:** dosel < 8%. **Estrato alto:** dosel > 12%.
3. **Elegir para el piloto la escuela del estrato bajo** que tenga mejor disponibilidad de curso y docente.
4. Si las tres caen en el mismo estrato, elegir por variedad de arbolado en el buffer de 500 m — hay que ir a mirar una vez antes de decidir.

> ⚠️ **No sé dónde están las tres escuelas** y no lo voy a suponer. Pásame las direcciones y las ubico en la capa de unidades vecinales en cinco minutos, con su dosel, su temperatura y su índice — eso además queda como anexo de la postulación.

**Reserva las otras dos.** El piloto usa **una sola** escuela. Las otras dos entran al proyecto definitivo sin haber sido "gastadas" en pruebas, y con un protocolo ya corregido — que es una mejor primera experiencia para ellas.

---

## 2. Sistema de identificación de árboles

### 2.1 Estructura del código

```
XXX - NNN
 │     └── correlativo de 3 dígitos dentro de la escuela (001–999)
 └──────── prefijo de 3 letras del sitio
```

| Sitio | Prefijo | Ejemplo |
|---|---|---|
| Escuela Los Trigales | **TRI** | `TRI-001` |
| Escuela Campos Deportivos | **CDE** | `CDE-001` |
| HablArte | **HAB** | `HAB-001` |
| Submuestra de control | se usa **el mismo código** del árbol, en planilla aparte | `TRI-014` |

**Reglas:**
- El código **no se reutiliza jamás**, ni siquiera si el árbol se tala. Un árbol talado queda como `TRI-023 · estado: eliminado` con su fecha. **Esa es, literalmente, la evidencia de pérdida de arbolado**, y es uno de los datos más valiosos que puede producir el proyecto.
- Los códigos se **preimprimen** en las fichas antes de salir (tira de 60 códigos por equipo). Evita duplicados y errores de tipeo en terreno.
- Formato fijo: 3 letras, guion, 3 dígitos con ceros a la izquierda. `TRI-007`, nunca `TRI-7`.

### 2.2 Qué cadena de datos amarra el código

```
TRI-014
  ├── Ficha de terreno       → especie, perímetro, altura, copa, estado, emplazamiento
  ├── Fotos                  → nombre de archivo: TRI-014_arbol.jpg, TRI-014_corteza.jpg, TRI-014_hoja.jpg
  ├── Coordenadas GPS        → lat, lon + precisión declarada por el celular
  ├── Observaciones iNaturalist → campo Arbol_OCAU = "TRI-014" + código en notas
  ├── Grilla de líquenes     → nº de morfotipos, celdas ocupadas
  └── Datos ambientales      → los agrega el Observatorio por cruce espacial:
                               cobertura arbórea 100 m, LST, unidad vecinal, índice de prioridad
```

Los estudiantes levantan las cinco primeras filas. **La sexta la aporta el Observatorio automáticamente** desde las capas satelitales ya operativas: nadie mide temperatura en terreno.

### 2.3 Marcado físico: la decisión que hay que probar, no asumir

El problema real: **¿cómo encontramos el mismo árbol dentro de 3 años para remedirlo?** De eso depende toda la promesa de línea base.

| Opción | A favor | En contra | Veredicto piloto |
|---|---|---|---|
| **Sin marca física** (GPS + foto + referencia de dirección) | No interviene el árbol; no requiere permiso | El GPS de celular tiene error de 3-10 m; en una vereda con árboles cada 6 m, eso es ambiguo | ✅ **Probar en el piloto** |
| Placa de aluminio con clavo | Estándar forestal, duradero | En arbolado público **requiere autorización municipal**, y visualmente se lee como daño. Mal mensaje para un proyecto que denuncia la agresión al arbolado | ❌ No en el piloto |
| Tiza o marcador temporal | Inmediato, inofensivo | Dura días | 🟡 Solo para la jornada |
| Referencia a dirección postal + posición | Barato y robusto: *"frente a Prieto Norte 1245, 2º árbol hacia el norte"* | Requiere disciplina al anotar | ✅ **Obligatorio, junto al GPS** |

**Decisión: sin marca permanente**, con triple redundancia (GPS + foto del árbol con contexto + referencia a dirección). Y el piloto **prueba si eso alcanza** — ver la prueba de relocalización en §5.

---

## 3. Ficha de terreno piloto

Una hoja por árbol, tamaño carta, impresa y plastificada o en carpeta con clip. **En el piloto se usa papel, no aplicación.** Si el papel funciona, después se digitaliza; si se parte por la app, los problemas del método se confunden con problemas del software.

```
┌───────────────────────────────────────────────────────────────────────────┐
│ OBSERVATORIO DEL ARBOLADO URBANO DE TEMUCO · FICHA DE ÁRBOL   [PILOTO v1] │
├───────────────────────────────────────────────────────────────────────────┤
│ CÓDIGO: ___-___     Fecha: __/__/____   Hora inicio: __:__  Fin: __:__    │
│ Equipo (nombres): ______________________________________________________  │
│ Clima:  ☐ despejado   ☐ nublado   ☐ llovizna     (con lluvia NO se sale)  │
├───────────────────────────────────────────────────────────────────────────┤
│ 1. DÓNDE ESTÁ                                                             │
│    Calle y número más cercano: _________________________________________  │
│    Referencia: "____º árbol hacia el ☐N ☐S ☐E ☐O desde ese número"       │
│    GPS   lat: -38.______   lon: -72.______   precisión: ____ m            │
│    Está en: ☐ vereda  ☐ bandejón central  ☐ plaza  ☐ patio escuela        │
├───────────────────────────────────────────────────────────────────────────┤
│ 2. CÓMO ES                                                                │
│    Perímetro del tronco a 1,30 m del suelo: _______ , ___ cm              │
│       ¿Tiene más de un fuste?  ☐ no   ☐ sí → nº de fustes: ___            │
│       (si son varios, medir cada uno y anotar al reverso)                 │
│    Altura aproximada: _____ m     ☐ estimada a ojo  ☐ con app             │
│    Ancho de copa:  norte-sur _____ m     este-oeste _____ m               │
│    Estado del árbol (marcar UNA):                                         │
│       ☐ BUENO    copa completa, sin heridas grandes, ramas vivas          │
│       ☐ REGULAR  algunas ramas secas, heridas o poda fuerte antigua       │
│       ☐ MALO     muchas ramas secas, tronco dañado o hueco, se ve enfermo │
│    Daños visibles: ☐ desmoche  ☐ heridas  ☐ cables  ☐ clavos/carteles     │
│                    ☐ raíces levantando vereda  ☐ ninguno                  │
├───────────────────────────────────────────────────────────────────────────┤
│ 3. QUÉ ÁRBOL ES                                                           │
│    Lo llamamos: ________________________  (nombre común o "no sabemos")   │
│    ☐ Foto del árbol completo   ☐ Foto de la corteza   ☐ Foto de la hoja   │
│    (NO adivinar la especie: la confirma el especialista con las fotos)    │
├───────────────────────────────────────────────────────────────────────────┤
│ 4. QUÉ VIVE EN ÉL                                                         │
│    LÍQUENES — grilla de 10×10 cm sobre el tronco, cara ____ (N/S/E/O),    │
│    entre 1,0 y 1,5 m de altura:                                           │
│       Celdas con liquen (de 100): _____                                   │
│       Tipos distintos que vemos:  ☐1 ☐2 ☐3 ☐4 ☐5 ☐+     Fotos: ____      │
│    OTROS SERES VIVOS — 5 minutos exactos mirando tronco y ramas bajas:    │
│       ☐ insectos (¿cuántos tipos distintos? ___)  Fotos: ____             │
│       ☐ arañas   ☐ caracoles   ☐ musgo   ☐ enredadera   ☐ hongos          │
│       ☐ nido     ☐ agallas     ☐ hojas comidas   ☐ no vimos nada          │
│    ¿Subí las fotos a iNaturalist con el código del árbol?  ☐ sí  ☐ no     │
├───────────────────────────────────────────────────────────────────────────┤
│ 5. LO QUE NOS LLAMÓ LA ATENCIÓN (escribir libremente)                     │
│ ________________________________________________________________________  │
│ ________________________________________________________________________  │
└───────────────────────────────────────────────────────────────────────────┘
```

**Decisiones de diseño de la ficha, explicadas:**

- **"Lo llamamos ___" en vez de "Especie".** Pedir el nombre científico induce a inventar. Pedir cómo lo llaman ellos es honesto, es dato etnobotánico real, y la identificación queda donde corresponde.
- **Hora de inicio y fin.** Es la variable de control más importante del diseño y la más fácil de olvidar. Va arriba, no al final.
- **Estado sanitario en 3 clases con descripción escrita en cada opción.** Sin la descripción, cada equipo usa su propio criterio y la concordancia se desploma.
- **La casilla "no vimos nada" es obligatoria.** Sin ella, la ausencia se confunde con "no miramos", y para un análisis de riqueza esa diferencia lo es todo.
- **Campo 5, libre.** Es donde aparecen los hallazgos que no anticipamos, y es lo que mantiene despierto al estudiante.

---

## 4. Protocolo paso a paso para estudiantes

> Escrito para leerse tal cual en el taller. Lenguaje directo, sin tecnicismos innecesarios.

### Antes de salir (en la sala, 60 min)

1. **Un árbol es una casa.** Vemos fotos: un liquen, un insecto en la corteza, un nido, musgo. Pregunta abierta: *¿qué creen que vive en el árbol de la esquina de la escuela?*
2. **Por qué medimos.** Sin medir, "el árbol es grande" es una opinión. Con el perímetro, es un dato que otra persona puede comprobar dentro de diez años.
3. **Práctica en el patio.** Cada equipo mide el **mismo** árbol del patio. Se comparan los resultados en la pizarra. **Casi nunca coinciden** — y de ahí sale la conversación más importante del taller: *¿por qué nos dio distinto? ¿a qué altura mediste? ¿apretaste la huincha?* Esta actividad hace más por la calidad de los datos que cualquier instructivo.
4. **La regla de oro:** *el árbol feo también entra*. Si el protocolo dice que toca el tercer árbol y ese está enfermo y chico, **ese se mide**. Elegir solo los bonitos arruinaría el estudio, porque justamente queremos saber si los árboles grandes tienen más vida que los chicos — y para eso necesitamos chicos.
5. **Cómo se llama cada árbol:** con su código. Repartir la tira de códigos preimpresos.

### En terreno (2–3 horas)

**Paso 1 — Elegir el árbol sin hacer trampa.**
Caminamos por la vereda que nos tocó. Medimos **el primer árbol y después cada tercer árbol**, sin mirar cuál es. Si el que toca está detrás de un auto o en un antejardín cerrado, se anota "no accesible" y se pasa al siguiente — **pero se anota**.

**Paso 2 — Escribir el código y la dirección.** Antes de tocar nada. Anotar hora de inicio.

**Paso 3 — Las tres fotos.** Árbol completo (que se vea entero y su entorno), corteza de cerca (con una mano o una regla al lado, para escala) y una hoja. **Renombrar después: `TRI-014_arbol.jpg`.**

**Paso 4 — Medir el tronco.**
Rodear el tronco con la huincha **a la altura del pecho (1,30 m)**, ajustada sin apretar, horizontal, sin torcerse. Anotar en centímetros con un decimal.
*Si el árbol se divide en dos antes de 1,30 m*, se miden los dos y se anota que son dos.

**Paso 5 — Estimar la altura y la copa.** Con la app, o comparando con algo conocido (un poste de alumbrado ≈ 8-9 m). Se anota que es **estimada** — no es lo mismo que medida y no pasa nada.

**Paso 6 — Mirar el estado.** Leer las tres descripciones de la ficha y elegir. Si el equipo duda entre dos, marcar la peor y anotar la duda en el campo 5.

**Paso 7 — La grilla de líquenes.** Apoyar la grilla en el tronco entre 1,0 y 1,5 m, siempre en la **misma cara** (anotar cuál). Contar cuántos cuadraditos tienen liquen. Contar **cuántos tipos distintos** se ven —por forma y color, no por nombre—. Fotografiar cada tipo.

**Paso 8 — Cinco minutos de observación.** Cronómetro. Mirar tronco, ramas bajas y hojas. Fotografiar todo bicho que aparezca. **Si no aparece nada, marcar "no vimos nada"** — eso también es un dato.

**Paso 9 — Subir a iNaturalist.** Cada foto de un ser vivo se sube con el código del árbol **en las notas** y en el campo del proyecto.

**Paso 10 — Anotar hora de término** y pasar al siguiente.

### De vuelta (45 min)

11. **Cada equipo cuenta un hallazgo.** Uno solo, el que más le llamó la atención.
12. **Se cuentan los tiempos:** ¿cuánto demoramos por árbol? ¿qué fue lo más lento?
13. **Qué salió mal.** Explícitamente: *¿qué casilla no supieron llenar?* Esta pregunta es el producto principal del piloto.

---

## 5. Las 12 pruebas del piloto

Cada punto que planteaste, convertido en una medición con un número de salida y una regla de decisión.

| # | Qué se prueba | Cómo se mide en el piloto | Qué número sale | Decisión que gatilla |
|---|---|---|---|---|
| 1 | **Tiempo por árbol** | Hora inicio/fin en cada ficha | mediana y rango de minutos | Si > 20 min → recortar ficha. Define cuántos árboles por sitio son viables |
| 2 | **Qué pueden levantar** | % de casillas completas y correctas por campo | tasa de llenado por variable | Campo con < 80% de llenado → se simplifica o se elimina |
| 3 | **Instrumentos** | Registro de qué faltó o falló | lista | Define la compra definitiva |
| 4 | **Errores de medición** | 5 árboles remedidos por un técnico, **a ciegas** | RMSE y sesgo del perímetro | RMSE > 5 cm → reforzar capacitación en el punto de medición |
| 5 | **Sesgo de selección** | Comparar la distribución de perímetros medidos vs. **todos** los árboles del tramo (censo rápido del técnico) | ¿se saltaron los chicos? | Si hay sesgo → regla más estricta y supervisión |
| 6 | **Registro de biodiversidad** | Nº de registros por árbol y por grupo | promedio de morfotipos/árbol | Si es ~0 → el método no detecta y hay que cambiarlo |
| 7 | **Vínculo iNaturalist** | Prueba dedicada (§6) | % de observaciones correctamente vinculadas | < 90% → agregar redundancia o cambiar mecanismo |
| 8 | **Grupos viables** | Comparar rendimiento entre líquenes, artrópodos, aves | registros útiles por grupo | Grupo con rendimiento nulo sale del proyecto definitivo |
| 9 | **Carga del especialista** | Cronometrar la validación de todo el material del piloto | minutos por árbol validado | Se extrapola: horas de especialista para 240 árboles |
| 10 | **Submuestra de control** | Ejecutar el 20% en el piloto (5 de 25) | viabilidad operativa | Define si el 15% del proyecto es realista |
| 11 | **Variables a eliminar** | Cruce de #1, #2 y #4 | lista de campos a borrar | **Se espera eliminar 2-4 campos.** Si no se elimina ninguno, sospechar del piloto |
| 12 | **Costo del levantamiento completo** | Se calcula con el tiempo real de #1 y #9 | ver §8 | Insumo directo del presupuesto (paso 7) |

### Prueba adicional que propongo: **relocalización**

No estaba en tu lista y es la que sostiene la promesa de "línea base para remedición".

**Cómo:** al día siguiente, un equipo distinto recibe **solo el registro** (código, GPS, foto, referencia de dirección) de **5 árboles** y tiene que encontrarlos.
**Métrica:** cuántos de 5 encuentran, y en cuántos minutos.
**Regla:** si encuentran menos de 4 de 5, el registro de ubicación es insuficiente y hay que reforzarlo antes del proyecto definitivo.

Sin esta prueba, "dejamos la línea base para remedir en 3 años" es una frase; con ella, es una capacidad verificada.

---

## 6. Prueba específica del vínculo con iNaturalist

**Se hace una semana antes de la salida, en gabinete, con material propio.** No se puede descubrir en terreno, con 20 estudiantes esperando, que el mecanismo no funciona.

### Preparación (una tarde)

1. Crear el **Proyecto Tradicional** "Arbolado Urbano de Temuco (piloto)".
   ⚠️ Debe ser **tradicional**, no de colección: los campos de observación solo funcionan en los tradicionales.
2. Crear el campo de observación **`Arbol_OCAU`**, tipo **texto**.
3. Agregar el campo al proyecto y marcarlo **obligatorio**.

### Ejecución (10 observaciones de prueba)

4. Salir a cualquier calle y registrar **10 observaciones reales** —líquenes, insectos, musgo— sobre **3 árboles** identificados como `TST-001`, `TST-002`, `TST-003`.
5. En cada observación: llenar el campo `Arbol_OCAU` **y** escribir el código al inicio de las notas: `TRI-014 | ...`.
6. **Casos de prueba deliberados** (esto es lo importante):
   - 2 observaciones **sin** el campo, solo con el código en notas → ¿se recuperan igual?
   - 1 observación con el código **mal escrito** (`TST 001` con espacio) → ¿la detecta el cruce?
   - 1 observación de un taxón **sensible**, si aparece → ¿se oscurecen las coordenadas y afecta el vínculo?
   - 1 observación cargada **desde el celular** de un estudiante, no desde el nuestro → ¿puede llenar el campo desde la app móvil, o solo desde el sitio web?

**Ese último caso es el más crítico y el que más probablemente falle.** Si el campo de observación no se puede llenar cómodamente desde la app en terreno, todo el mecanismo se cae y hay que apoyarse en las notas.

### Verificación

7. Exportar el proyecto a CSV y comprobar que las columnas del campo y de las notas llegan completas.
8. Cruzar por código contra la tabla de árboles y contar aciertos.

### Criterios

| Resultado | Lectura |
|---|---|
| ≥ 9 de 10 vinculadas por el campo | ✅ Mecanismo principal aprobado |
| El campo falla pero las notas rescatan ≥ 9 | 🟡 Se usan las notas como principal y el campo como respaldo |
| < 9 por ambas vías | ❌ Rediseñar: código en el **nombre del archivo** de la foto y planilla propia paralela |
| No se puede llenar el campo desde la app móvil | 🟡 El código va en notas y se enseña como paso 9 del protocolo |

**Nota verificada:** la documentación de iNaturalist advierte que los campos de observación **"no están estrictamente regulados"** (hay campos redundantes) y existen reportes históricos de fallas en la exportación. Por eso la redundancia en notas no es paranoia: es diseño.

---

## 7. Permisos, seguridad y consentimiento

No es burocracia: si esto falla, el proyecto no se ejecuta, y un comité evaluador lo va a preguntar.

| Asunto | Qué se necesita | Cuándo |
|---|---|---|
| **Autorización del establecimiento** | Carta de dirección autorizando la salida y el uso pedagógico | Antes del piloto |
| **Consentimiento de apoderados** | Autorización de salida + **autorización de uso de imagen** (hay registro audiovisual comprometido con FMA) | Antes del piloto |
| **Seguridad vial** | Trabajo en veredas con tráfico: chalecos reflectantes, ratio adulto/estudiante ≤ 1:8, evitar avenidas principales | Diseño del recorrido |
| **Medición de árboles públicos** | Medir con huincha no interviene el árbol ni requiere permiso municipal. **Sí lo requeriría** colocar placas → una razón más para no marcarlos | — |
| **Datos de menores** | Los datos publicados son de **árboles**, no de personas. Ningún nombre de estudiante en el conjunto de datos público | Diseño de la base |
| **Cuentas de iNaturalist** | Los menores de 13 años **no pueden** tener cuenta propia. Se usa una **cuenta institucional del proyecto** operada por el docente | Antes del piloto |

⚠️ **El punto de las cuentas de iNaturalist es una restricción real** que puede afectar el diseño según la edad del curso. Conviene verificarlo con la escuela antes de comprometer el mecanismo — si el curso es de básica, todo el registro pasa por cuenta institucional.

---

## 8. Cuánto costaría el levantamiento completo (método, no cifra inventada)

No se puede estimar antes del piloto: **depende del tiempo por árbol, que es justamente lo que el piloto mide.** Lo que sí se puede dejar es la fórmula, para llenarla con datos reales:

```
Jornadas de terreno = (nº de árboles × minutos por árbol) ÷ (minutos útiles por salida × equipos por salida)
Horas de especialista = nº de árboles × minutos de validación por árbol
Costo ≈ (jornadas × costo de jornada) + horas de especialista + materiales + movilización
```

**Envolvente preliminar, con supuestos explícitos y sujeta a corrección por el piloto:**

| Supuesto | Valor tentativo |
|---|---|
| Árboles totales (4 sitios × 60) | 240 |
| Minutos por árbol | **por medir** — hipótesis de trabajo: 12-15 |
| Equipos simultáneos por salida | 5 (de 3-4 estudiantes) |
| Minutos útiles por salida | 120 |
| Árboles por salida | ≈ 40-50 |
| **Salidas de terreno necesarias** | **5-6** (más 1 de repetición por sitio) |
| Validación taxonómica | **por medir** — hipótesis: 3-5 min/árbol → 12-20 h |
| Materiales de medición | huinchas, grillas, impresión, chalecos |

**Si el piloto arroja 25 minutos por árbol en vez de 12, el proyecto no cabe en 240 árboles** y hay que bajar a 160 o recortar la ficha. Descubrir eso ahora cuesta una tarde; descubrirlo en marzo cuesta el proyecto.

---

## 9. Criterios de éxito y fracaso

### 9.1 El criterio principal

> **El piloto es exitoso si detecta al menos TRES problemas metodológicos concretos y genera tres correcciones específicas al protocolo.**

Un piloto donde "todo salió bien" es un piloto mal observado. Si nadie se equivocó, es que no miramos.

### 9.2 Criterios cuantitativos

| Indicador | ✅ Éxito | 🟡 Corregir | ❌ Rediseñar |
|---|---|---|---|
| Tiempo por árbol | ≤ 15 min | 15-25 min | > 25 min |
| Fichas completas (sin campos vacíos críticos) | ≥ 90% | 70-90% | < 70% |
| RMSE del perímetro vs. técnico | ≤ 5 cm | 5-10 cm | > 10 cm |
| Concordancia en estado sanitario (κ) | ≥ 0,6 | 0,4-0,6 | < 0,4 |
| Observaciones vinculadas en iNaturalist | ≥ 90% | 70-90% | < 70% |
| Relocalización de árboles (de 5) | 5 | 4 | ≤ 3 |
| Morfotipos de líquenes por árbol | ≥ 2 | 1 | 0 |
| Árboles con ≥ 1 registro de biodiversidad | ≥ 80% | 50-80% | < 50% |
| Sesgo en selección (perímetro medio muestreado vs. censo) | sin diferencia | leve | los chicos se saltan sistemáticamente |

### 9.3 Qué significa cada resultado

- **Todo verde** → sospechar. Revisar si la submuestra de control se hizo realmente a ciegas y si el técnico fue suficientemente estricto.
- **Amarillos** → lo normal y lo deseable. Cada amarillo es una corrección concreta al protocolo.
- **Un rojo** → se corrige ese componente y se repite solo esa parte, no todo el piloto.
- **Tres o más rojos** → el diseño es demasiado ambicioso para el contexto escolar. Se recorta: menos variables, menos grupos de biodiversidad, más tiempo por árbol.

### 9.4 Qué produce el piloto (entregables)

1. **Ficha v2**, corregida, con los campos eliminados marcados y justificados.
2. **Protocolo v2** para estudiantes.
3. **Tabla de errores medidos** (RMSE, sesgo, κ) — primer dato duro del control de calidad, y material publicable.
4. **Veredicto sobre iNaturalist**, con el mecanismo definitivo escrito.
5. **Tiempo real por árbol**, que dimensiona todo el proyecto.
6. **Lista de materiales definitiva** con cantidades.
7. **20-25 árboles reales** ya caracterizados: el inicio del catastro, no un ensayo desechable.
8. **Registro fotográfico** de la actividad → evidencia de trabajo con comunidades para la postulación **y** el registro audiovisual que FMA pide como compromiso.

---

## 10. Lo que necesito de ti para cerrar este paso

1. **Direcciones de las tres escuelas** → las ubico en la capa de unidades vecinales y decidimos el estrato con datos, no por intuición.
2. **Qué curso y de qué edad.** Cambia el lenguaje del protocolo y define lo de las cuentas de iNaturalist (menores de 13 no pueden tener cuenta propia).
3. **¿Hay alguien que pueda hacer la validación taxonómica** y la submuestra de control? Sin esa persona, las pruebas 4, 9 y 10 no se pueden ejecutar.
4. **Fecha tentativa de la salida.** De ahí sale si alcanza antes del 24 de agosto.
5. **Qué es Ekuwün y qué relación tiene con las escuelas.** Lo necesito para escribir bien la sección de trayectoria de la postulación, y no quiero suponerlo.
