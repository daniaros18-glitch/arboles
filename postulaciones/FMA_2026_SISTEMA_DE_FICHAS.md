# Sistema de fichas de ciencia ciudadana

**Proyecto:** Observatorio Ciudadano del Arbolado Urbano de Temuco · Fondo FMA 2026-2027
**Fecha:** 16 de agosto de 2026
**Base:** [`FMA_2026_PILOTO.md`](FMA_2026_PILOTO.md) §3 (ficha v1) · [`FMA_2026_DISENO_CIENTIFICO.md`](FMA_2026_DISENO_CIENTIFICO.md) §5 · [`FMA_2026_SERVICIOS_LINEA_BASE_Y_MONITOREO.md`](FMA_2026_SERVICIOS_LINEA_BASE_Y_MONITOREO.md) §7 · [`FMA_2026_ESCUELAS_E_INCLUSION.md`](FMA_2026_ESCUELAS_E_INCLUSION.md) §4

---

## 0. Las cuatro conclusiones, antes del detalle

Trabajé sobre tus seis categorías. Cuatro cosas cambiaron y conviene decirlas de entrada.

**1. La "ficha de vida del árbol" no es una ficha de terreno, y por eso es la más importante.**
En nueve meses cada árbol se observa **una vez**. Una biografía con una sola entrada no es una biografía. Lo que estás describiendo tiene en realidad dos formas distintas: una **página pública del árbol** en el observatorio, que es una **salida** del sistema, y una **ficha de revisita** que se usará desde 2030, que es una **entrada**. Diseñar hoy la de 2030 es exactamente lo correcto, pero no como un formulario que los niños llenen ahora, sino como la **especificación que obliga a la ficha de hoy**. Lo desarrollo en §5, y es la parte que más le sirve a la postulación.

**2. Los tres niveles no pueden recoger variables distintas.**
Si la ficha exploradora, la investigadora y la técnica levantan cosas diferentes, terminamos con tres conjuntos de datos que no se pueden juntar, y el análisis se cae. La arquitectura correcta es **un núcleo común idéntico para todos** más capas que se agregan según el nivel. Un dato levantado por un niño de siete años tiene que ser **el mismo dato** que levanta uno de trece, no una versión aguada. Lo que cambia es **cuántas variables cubre cada nivel**, no **con qué calidad**.

**3. Hay que reducir el número de hojas, no aumentarlo.**
Tu lista, tomada literalmente, son seis papeles por árbol. En terreno eso significa seis oportunidades de que el código se escriba mal, de que una hoja se separe de las otras y de que el equipo pase más tiempo administrando papeles que mirando el árbol. Propongo **dos fichas físicas** en vez de seis, organizadas en bloques que corresponden a los niveles. Y una de ellas, la del tramo, **ahorra tiempo** respecto de la ficha actual.

**4. El presupuesto real de este sistema no es plata: son minutos.**
La hipótesis de trabajo es de 12 a 15 minutos por árbol. Tu lista completa, aplicada a cada árbol, da alrededor de 35. Con 180 árboles, esa diferencia es la que decide si el proyecto cabe en marzo y abril o no cabe. Por eso cada sección de este documento trae su costo en minutos, y hay una tabla de recortes en §8.

---

## 1. El principio que ordena todo: la ficha se diseña desde 2030 hacia atrás

La pregunta que ordena el diseño no es *"¿qué queremos saber de este árbol?"*. Es:

> **¿Qué necesita saber alguien que en 2030 vuelva a este árbol y quiera comparar?**

Esa persona no va a estar. Nosotros tampoco necesariamente. Va a tener el registro y nada más. Y de ahí salen tres exigencias que la ficha de hoy tiene que cumplir sí o sí, y que no son obvias:

| Exigencia de 2030 | Qué obliga hoy |
|---|---|
| **Encontrar el mismo árbol** | Código, GPS, referencia postal y foto con contexto. Ya está en el diseño y es lo que la prueba de relocalización verifica |
| **Medir en el mismo punto exacto** | 🔑 **Marcar y registrar la altura y la cara del tronco donde se midió.** Si en 2030 se mide 10 cm más arriba, el "crecimiento" medido es un artefacto |
| **Saber cuánto error tenía la medición de origen** | Registrar quién midió, con qué, y que el 15% pasó por control ciego |

La segunda es la que faltaba y es barata: agregar a la ficha **"altura de medición: 1,30 m"** como dato registrado, no supuesto, y **la cara del tronco** donde se apoyó la grilla de líquenes. Dos casillas hoy, y sin ellas la remedición de 2030 no es comparable.

**Esto es lo que separa una línea base de un inventario.** Un inventario dice qué hay. Una línea base está diseñada para ser comparada consigo misma.

---

## 2. La arquitectura: dos fichas de terreno, no seis

```
POR SALIDA, POR EQUIPO                    POR ÁRBOL
┌──────────────────────────┐             ┌────────────────────────────────┐
│  F2 · FICHA DEL TRAMO    │             │  F1 · FICHA DEL ÁRBOL          │
│  (una por equipo/salida) │             │  (una por árbol, anverso y     │
│                          │             │   reverso)                     │
│  fecha, clima, equipo    │──contexto──▶│                                │
│  tramo recorrido         │             │  ANVERSO                       │
│  árboles no accesibles   │             │   A · Identificación           │
│  percepción térmica      │             │   B · Medición                 │
│  conteo de aves          │             │   C · Entorno inmediato        │
└──────────────────────────┘             │                                │
                                         │  REVERSO                       │
                                         │   D · Líquenes (grilla)        │
                                         │   E · Otros seres vivos        │
                                         │   F · Lo que nos llamó         │
                                         └────────────────────────────────┘
```

**Por qué esto en vez de tus seis fichas:**

**La ficha del tramo (F2) es un hallazgo, no una simplificación.** Hoy la ficha v1 pide fecha, clima y nombres del equipo **en cada árbol**. Con 70 árboles por escuela eso es escribir 70 veces lo mismo. Esos datos no son del árbol: son de **la salida**. Moverlos a una sola hoja por equipo ahorra alrededor de **1 minuto por árbol**, o sea unas tres horas de terreno en todo el proyecto, y elimina la inconsistencia de que el mismo equipo anote climas distintos en árboles medidos con diez minutos de diferencia.

Además, F2 es el lugar natural para tres cosas que **no son por árbol y hoy no tienen dónde ir**: los árboles que tocaba medir y no se pudieron (dato clave contra el sesgo de selección), el conteo de aves (que es de sitio, no de árbol) y la percepción térmica.

**Tus categorías 1, 2 y 5 van en una sola hoja** porque son el mismo árbol en el mismo momento. Separarlas duplica el código escrito a mano, que es la principal fuente de registros huérfanos.

**Tu categoría 3 va al reverso** de la misma hoja, no en papel aparte, por lo mismo.

**Tu categoría 4 no es una ficha de terreno.** Ver §5.

**Tu categoría 6 no es una ficha más: es cómo se imprime F1.** Ver §4.

---

## 3. Qué entra en cada bloque, y qué dejé fuera

### Bloque A · Identificación

| Variable | Nivel mínimo | Justificación |
|---|---|---|
| **Código del árbol** | Explorador | Preimpreso en la ficha, no se escribe |
| **Hora de inicio y de término** | Explorador | 🔑 Variable de control más importante del diseño |
| **Calle y número más cercano** | Investigador | Redundancia de ubicación para 2030 |
| **Referencia**: "3er árbol hacia el norte desde ese número" | Investigador | Lo que realmente permite reencontrarlo |
| **GPS y precisión declarada** | Investigador | Precisión, no solo coordenada: sin ella no sabemos cuánto confiar |
| **"Lo llamamos ______"** | Explorador | **No se pide la especie.** Pedirla induce a inventar. Este campo además es dato etnobotánico real |
| **Nombre en mapuzugun u otra lengua** | Explorador | Nuevo. Es el aporte propio de Los Trigales y cuesta una línea |
| **Tres fotos**: árbol entero, corteza con escala, hoja | Explorador | La identificación vive acá, no en el criterio del estudiante |

❌ **Fuera: "especie o identificación preliminar".** Está en tu lista y el diseño científico ya lo había descartado con razón. Un estudiante que escribe "creo que es un roble" contamina el dato: después alguien lo lee como determinación. La especie la pone la especialista desde las fotos, y ese campo se llena en gabinete, no en terreno.

❌ **Fuera: "características visibles"** como campo suelto. Es demasiado vago para producir un dato comparable y se superpone con el bloque B. Lo que quedaba de útil ahí está en el campo libre F.

### Bloque B · Medición

| Variable | Nivel mínimo | Justificación |
|---|---|---|
| **Perímetro a 1,30 m** | Investigador | El predictor principal de H1. Se registra perímetro, no DAP: dividir por π es cálculo, no dato de terreno |
| **Altura de medición registrada (1,30 m)** | Investigador | 🔑 Nuevo, por §1. Sin esto la remedición no es comparable |
| **Número de fustes** | Investigador | Un multifuste rompe las ecuaciones alométricas si no se registra |
| **Altura total**, y **con qué se midió**: ☐ clinómetro ☐ app ☐ a ojo | Investigador | Entra en biomasa. 🔑 Sin saber el método no sabemos qué confianza tiene el dato: el clinómetro casero da 10-15% de error y la estimación a ojo, 30-50%. Ver [`FMA_2026_EQUIPAMIENTO_INCLUSIVO.md`](FMA_2026_EQUIPAMIENTO_INCLUSIVO.md) §3.2 |
| **Copa en dos ejes** (N-S, E-O) | Técnico | De acá sale el área de sombra, que es el único servicio que se calcula sin modelos |
| **Estado sanitario en 5 clases** | Técnico | Las clases de la Ordenanza: sano, leve, mediana, fuerte, muerto. Cada una con su descripción escrita |
| **Estado sanitario en 3 clases** | Explorador | 🔑 Ver abajo |
| **Daños visibles** (casillas) | Explorador | Explica el estado y documenta la poda severa |
| **Floración o fructificación** (casilla) | Explorador | Nuevo, y lo agrego por tu propuesta. Cuesta un tic y es **fenología**, que es justamente lo que gana valor con la revisita |

🔑 **La solución al problema de las 5 clases.** La Ordenanza necesita cinco categorías para el factor `fd` del Art. 32, pero más clases significa menos concordancia entre observadores, y con estudiantes pequeños eso se desploma. La salida es que **las dos escalas convivan en la misma ficha, anidadas**:

```
ESTADO DEL ÁRBOL
  ☐ SANO      copa completa, sin heridas grandes            → fd 100%
  ☐ REGULAR ──┬─ ☐ daño leve: algunas ramas secas           → fd 70%
              └─ ☐ daño mediano: bastantes ramas secas      → fd 50%
  ☐ MALO    ──┬─ ☐ daño fuerte: tronco hueco o herido       → fd 40%
              └─ ☐ está muerto                              → fd 0%
```

El nivel Explorador marca solo la columna de la izquierda. El Investigador y el Técnico marcan también la de la derecha. **Ambos producen el mismo dato en tres clases**, que es el que se usa para analizar biodiversidad, y solo los niveles altos producen el de cinco, que es el que alimenta la fórmula del valor económico. Nadie levanta un dato peor: unos levantan menos.

### Bloque C · Entorno inmediato

Acá está el recorte más grande respecto de tu lista, y la razón es simple: **la mitad de lo que propones ya lo tenemos desde el satélite, mejor y gratis.**

| Tu variable | Veredicto |
|---|---|
| Tipo de superficie alrededor del árbol | ✅ **Entra.** Es lo que el satélite **no** ve: si el árbol tiene tierra, pasto o cemento hasta el tronco. Determina infiltración de agua y estrés hídrico, y es invisible a 30 m. Cuatro casillas |
| Presencia de áreas verdes | ❌ **Fuera.** Es la cobertura vegetal a 100 m, que el observatorio aporta por cruce espacial con más precisión que una apreciación a ojo |
| Sombra | ❌ **Fuera del terreno.** Se **calcula** con los dos ejes de copa del bloque B. Medirla además sería levantar dos veces el mismo dato |
| Proximidad a edificios o calles | 🟡 **Entra en versión mínima:** distancia a la calzada en pasos, y si hay cables sobre el árbol. Los cables explican el desmoche, que es el daño más común en Temuco |
| Otros árboles cercanos | 🟡 **Entra solo en nivel Investigador:** cuántos árboles hay a menos de diez pasos. Captura la vecindad inmediata, que a 30 m de resolución el satélite promedia y pierde |
| Presencia de infraestructura | ❌ **Fuera.** Se superpone con lo anterior y es demasiado abierto |
| Posibles amenazas | ✅ **Entra**, pero como casillas cerradas, no como texto: obra en construcción, sitio en venta, poda reciente, tocón vecino. **El tocón vecino es el dato más valioso de todo el bloque**: es evidencia directa de tala reciente en el mismo tramo |
| **Percepción de temperatura o confort** | 🟡 **Sí, con metodología, pero en F2 y no por árbol.** Ver abajo |

**Sobre la percepción térmica, porque preguntaste si existe una metodología apropiada.** Sí existe: las escalas de sensación térmica de siete puntos, del tipo mucho frío / frío / algo de frío / neutro / algo de calor / calor / mucho calor, son estándar en estudios de confort urbano. Son subjetivas por definición y esa es su gracia: registran lo que la persona siente, no lo que marca un instrumento.

Mi recomendación es incorporarla **una vez por tramo y por equipo, en F2**, en dos puntos contrastantes de la misma salida: uno bajo copa y uno al sol. No por árbol, porque multiplicaría el tiempo sin agregar información.

Y tiene un valor pedagógico que va más allá del dato: permite contrastar **lo que yo siento** con **lo que el satélite dice** sobre ese mismo punto, y conversar por qué no siempre coinciden. Eso es alfabetización científica de la buena, y encaja con el sello del proyecto. Se declara como percepción, nunca como medición de temperatura.

❌ **Y sigue fuera el termómetro de mano**, que ya estaba descartado en el diseño: varía con el sol, la hora y el viento, y produce ruido con apariencia de precisión.

### Bloques D y E · Biodiversidad asociada

Aquí no cambia casi nada respecto de lo ya diseñado, porque ya estaba resuelto. Tu pregunta sobre fotografías y vínculo con iNaturalist tiene respuesta afirmativa y verificada en el diseño: cada foto se sube con el **código del árbol en el campo del proyecto y además en las notas**, por redundancia, y el piloto lo prueba con diez observaciones reales antes de comprometerlo.

Lo que agrego:

| Variable | Nivel | Nota |
|---|---|---|
| **Cara del tronco donde se apoyó la grilla** | Investigador | 🔑 Nuevo, por §1. En 2030 hay que medir la misma cara |
| Celdas con liquen, de 100 | Investigador | Cobertura |
| Tipos distintos de liquen | Explorador | **Morfotipos, no especies.** "Gris en costra", "verde con hojitas" |
| 5 minutos cronometrados de otros seres vivos | Explorador | El cronómetro lo lleva un rol propio del equipo |
| Casillas de grupos: insectos, arañas, caracoles, musgo, enredadera, **hongos**, nido, agallas, hojas comidas | Explorador | Los hongos suben de prioridad por el perfil de la especialista |
| **"No vimos nada"** | Explorador | 🔑 Obligatoria. Sin ella, la ausencia se confunde con la falta de observación, y para un análisis de riqueza esa diferencia lo es todo |
| 🆕 **Cavidad visible: sí / no** | Explorador | **Indicador de estructura de hábitat, no de daño.** Ver nota abajo |
| Fotos subidas a iNaturalist con el código | Investigador | Casilla de verificación |

🆕 **Sobre la cavidad visible (agregado el 25-08-2026).** Hasta ahora un tronco hueco entraba al
sistema **solo** por el bloque B, como *"daño fuerte: tronco hueco o herido → fd 40%"*, es decir como
deterioro que baja el valor del ejemplar en la fórmula del Art. 32. Eso es correcto para valoración
económica y **es insuficiente para biodiversidad**: la literatura describe las cavidades como
vivienda escasa en ciudad, por la que las especies compiten (Davis et al. 2013,
[10.1371/journal.pone.0059332](https://doi.org/10.1371/journal.pone.0059332)).

El mismo rasgo tiene entonces dos lecturas legítimas y opuestas, y el instrumento debe poder
registrar ambas sin confundirlas:

| Dónde | Qué registra | Para qué |
|---|---|---|
| Bloque B, estado sanitario | Tronco hueco como **daño** | Estado del árbol, factor `fd` del Art. 32 |
| Bloque D-E, cavidad visible | Cavidad como **estructura de hábitat** | Indicador de vida asociada |

🔴 **Solo se registra que la cavidad existe y es visible. No se registra si está ocupada.** Saber
quién la usa exige observación repetida o cámara, y no es algo que una salida escolar resuelva.
Prometer ocupación sería inventar un dato.

❌ **Fuera: contar individuos de insectos.** Se registran morfotipos presentes, no abundancias. Contar es inviable y produce números inventados.

### Bloque F · Campo libre

Se mantiene tal cual. Es donde aparece lo que no anticipamos y es lo que mantiene despierto al estudiante.

---

## 4. Los tres niveles, con fundamento pedagógico

Pediste que no fueran arbitrarios. Los anclé en dos cosas verificables: **qué sabe hacer un estudiante según el currículum nacional** y **qué exige cada variable**.

### 4.1 El corte lo pone la medición, no la edad

La variable que parte el sistema en dos es **medir una longitud con una unidad estandarizada y anotar el número con un decimal**. En el currículum chileno, la medición de longitud con unidades estandarizadas (centímetros y metros) aparece en Matemática de **tercero básico**. Antes de eso, un estudiante puede comparar, ordenar y contar, pero no producir una medida numérica confiable.

Ese es el corte real, y no lo elegí yo: lo pone lo que el estudiante ya trabaja en clases.

| Nivel | Curso | Qué puede hacer | Qué bloques cubre |
|---|---|---|---|
| **Explorador** | NT1 a 2° básico (4 a 7 años) | Contar, comparar, marcar casillas, fotografiar, dibujar, reconocer y nombrar. **No producir medidas numéricas** | A parcial, B solo casillas, D tipos, E completo, F por dibujo |
| **Investigador** | 3° a 6° básico (8 a 11 años) | Medir con huincha y anotar, contar celdas en grilla, leer un GPS, registrar hora | A, B casi completo, C, D, E, F |
| **Técnico** | 7° y 8° básico (12 a 13 años) y equipo | Todo lo anterior, más copa en dos ejes, estado en cinco clases, y **convertir perímetro en diámetro** dividiendo por π | Todo |

💡 **La conversión de perímetro a diámetro es contenido de séptimo y octavo** (circunferencia, π, área del círculo). Que los estudiantes de ese nivel hagan el cálculo con datos que ellos mismos midieron no es una actividad extra: es la unidad de Matemática hecha con el barrio.

### 4.2 Los niveles se combinan dentro del mismo equipo, no se separan por escuela

Esto es lo que hace que el sistema funcione y conecta con lo que ya habíamos diseñado para inclusión. **Un equipo de cuatro cubre la ficha completa aunque sus integrantes tengan capacidades distintas**, porque los cuatro roles llenan bloques distintos de la misma hoja:

| Rol | Bloques que llena | Nivel que exige |
|---|---|---|
| **Quien mide** | B | Investigador |
| **Quien anota** | A, C | Investigador, o **nota de voz** si no puede escribir |
| **Quien fotografía** | A fotos, D fotos, E fotos | **Explorador** |
| **Quien observa y cronometra** | D conteo, E, hora de inicio y término | **Explorador** |
| **Quien georreferencia** | A, GPS y referencia postal | **Explorador** |

> **Actualización del 16-08-2026.** Los roles de terreno pasan de cuatro a **cinco** al separar
> georreferenciar de anotar. Y hay **dos roles más que ocurren en otros momentos del ciclo**:
> **identificar**, en aula y gabinete después de la salida, e **integrar y comunicar**, en la
> devolución final. 🔑 **Eso significa que un curso completo participa aunque solo una parte salga a
> terreno cada día**, lo que resuelve un problema logístico real en Campos Deportivos. Detalle en
> [`FMA_2026_EQUIPAMIENTO_INCLUSIVO.md`](FMA_2026_EQUIPAMIENTO_INCLUSIVO.md) §2.

🔑 **Dos de los cuatro roles son de nivel Explorador y ninguno es prescindible.** Sin la foto no hay identificación, y sin el cronómetro los datos de todos los equipos dejan de ser comparables. Un estudiante de siete años, o uno con dificultades de lectoescritura, ocupa un rol del que depende todo el resto. **No es una adaptación compasiva: es cómo trabajan las cuadrillas de terreno reales.**

En cursos donde todos son pequeños, el equipo se arma con **un adulto en el rol de quien anota** y los cuatro estudiantes reparten los demás.

### 4.3 Cómo queda en cada una de las tres escuelas

| Escuela | Niveles | Cómo se organiza |
|---|---|---|
| **Los Trigales** (NT1 a 8°) | Investigador y Técnico, si participan 7° y 8° | La escuela cubre todo el rango. Es la candidata natural para el piloto y para probar los tres niveles a la vez. Suma la línea de nombres en mapuzugun, que puede levantarse con los cursos pequeños que ya lo estudian |
| **Campos Deportivos** (NT1 a 8°) | Investigador y Técnico | Igual cobertura. Con matrícula grande, conviene un curso de séptimo u octavo que produzca la ficha completa |
| **Hablaarte** | ⚠️ **Depende de un dato que no tenemos** | Ver abajo |

### 4.4 🔴 El dato que falta y que puede cambiar todo el diseño de Hablaarte

Las escuelas de lenguaje en Chile atienden principalmente a estudiantes de **educación parvularia**, en torno a los 3 a 6 años, con trastorno específico del lenguaje. Nuestras fuentes son contradictorias: un directorio la menciona como "Lenguaje y Educación Básica" y en el registro figura como "Escuela Especial Hablaarte". **No lo sabemos y no lo voy a suponer.**

La diferencia no es menor:

| Si Hablaarte es… | Consecuencia para el sistema de fichas |
|---|---|
| **Solo parvularia (3 a 6 años)** | Ningún estudiante puede producir medidas numéricas. Trabajan **íntegramente en nivel Explorador**: fotografían, cronometran, cuentan tipos de liquen, dibujan y nombran. **El bloque B lo levantan los docentes y el equipo**, con los niños presentes y participando de la observación. La escuela aporta menos árboles al inventario dendrométrico y aporta, en cambio, el registro de biodiversidad y el trabajo de vocabulario |
| **Lenguaje y básica** | Funciona igual que las otras dos, con la ficha pictográfica como versión principal |

⬜ **Es la pregunta número uno que hay que hacerle a la escuela**, y va en el mismo correo donde se pide la carta de apoyo. De la respuesta depende cuántos árboles compromete Hablaarte y qué versión de la ficha se imprime.

💡 Y una cosa que conviene decir con claridad: **la primera opción no es un problema, siempre que se declare.** Un proyecto que dice "en esta escuela los niños de cinco años registran biodiversidad y nombran, y los adultos miden" es honesto y es replicable. Uno que finge que un niño de cinco años produce datos dendrométricos confiables se cae al primer control de calidad.

> ## 🔴 DECISIÓN DEL 23-08-2026: la metodología de Hablaarte queda abierta
>
> **Este documento propone una metodología para la ficha pictográfica. No hay que presentarla como
> cerrada, ni en la postulación ni ante la escuela.**
>
> La búsqueda bibliográfica que hicimos ([`FICHAS_INCLUSIVAS_EVIDENCIA.md`](../investigacion/FICHAS_INCLUSIVAS_EVIDENCIA.md))
> encontró que **no existe literatura sobre niñas y niños con trastorno del desarrollo del lenguaje
> generando datos de biodiversidad**, y que la evidencia sólida de apoyos visuales es casi toda de
> autismo. De las ocho formas alternativas de respuesta que consideramos, dos tienen respaldo fuerte,
> cuatro parcial y dos son ideas nuestras.
>
> A eso se suma una razón que no es de evidencia sino de pertinencia: **definir desde fuera cuál es la
> vía comunicativa adecuada para los estudiantes de esa escuela no nos corresponde.**
>
> **Lo que se compromete es un proceso, no un método:**
>
> | Se compromete | No se compromete |
> |---|---|
> | **Co-diseñar** los instrumentos con fonoaudiólogas, educadoras y equipo de apoyo | Que la ficha pictográfica sea de tal o cual forma |
> | **Pilotear** la versión co-diseñada antes del levantamiento | Que las ocho formas de respuesta funcionen |
> | **Ajustar** según lo que muestre el piloto | Un método validado para esta población |
> | **Mantener fijos el objetivo científico y las variables** | La vía concreta de acceder a cada variable |
>
> 🔑 **La frase que ordena todo esto:** *no bajamos el nivel de la actividad científica, buscamos vías
> distintas de acceder a ella.* Las variables que hay que observar son las mismas en las tres escuelas;
> lo que se adapta es cómo se accede a ellas y cómo se registran.
>
> 💡 **Y hay una ventaja estratégica en decirlo así.** Comprometer un proceso es verificable: se hizo el
> co-diseño o no se hizo. Comprometer un método validado es refutable, y con esta población, falso.
>
> **Todo lo que sigue en esta sección son, entonces, propuestas para llevar a esa mesa.**

### 4.5 La versión pictográfica no es un nivel: es un formato

Tu categoría 6 pide lenguaje sencillo, pictogramas, marcar en vez de escribir y espacio para dibujar. Todo eso es correcto, pero **no define un cuarto nivel**: define **cómo se imprime** la ficha.

La misma ficha F1 se imprime en tres formatos, con **exactamente las mismas variables y los mismos códigos de campo**:

| Formato | Para quién | Qué cambia |
|---|---|---|
| **Pictográfica** | Explorador, y versión principal en Hablaarte | 🔑 **Pictograma junto a la palabra, nunca en vez de la palabra.** Casillas grandes, instrucción en secuencia de imágenes, recuadro para dibujar. Ver el recuadro de abajo |
| **Estándar** | Investigador | La ficha v1 corregida, con descripciones escritas en cada opción |
| **Técnica** | Técnico y equipo | Misma información, disposición densa, campos de cálculo al margen. **Es también la hoja de la submuestra de control ciega** |

🔑 **Que la versión técnica y la de control sean la misma hoja no es economía: es diseño.** El técnico que remide el 15% de los árboles a ciegas tiene que registrar exactamente las mismas variables, en el mismo orden, para que la comparación sea válida. Ahí es donde tu idea de "una versión técnica para el equipo" encuentra su función real dentro del control de calidad.

> ### 🔴 Corrección del 23-08-2026: en Hablaarte el lenguaje no se rodea, se produce
>
> Este documento venía diseñando la participación de Hablaarte como *"registrar sin depender de leer
> y escribir"*. **Eso está mal orientado.** Una escuela de lenguaje existe justamente para que sus
> estudiantes hablen y escriban: un instrumento que evita el lenguaje trabaja contra el objetivo de
> la escuela que lo va a usar.
>
> **El encuadre correcto:** el pictograma es andamio, no reemplazo. El proyecto tiene que ser una
> **ocasión de producir lenguaje**, y el árbol es un referente inmejorable para eso, porque es real,
> concreto y **se puede volver a visitar**: la misma palabra se reactiva sobre el mismo objeto durante
> semanas, cosa que una lámina no permite.
>
> **Lo que cambia en el material:** en la versión pictográfica, cada campo lleva **símbolo y palabra
> juntos**, siempre. Es un cambio menor de diseño y cambia el sentido completo del instrumento.
>
> **Formas metodológicas para llevar al co-diseño con las fonoaudiólogas:**
>
> | En lo oral | Cómo entra en el protocolo |
> |---|---|
> | **Campo semántico cerrado y repetido** | 20 a 30 palabras que vuelven en cada árbol: tronco, corteza, rama, hoja, copa, raíz, liquen, musgo, hongo, rugosa, lisa, gruesa, delgada |
> | **Progresión nombrar, describir, contar** | De la palabra ("corteza") al atributo ("corteza rugosa") al enunciado ("encontramos un liquen gris en la corteza") |
> | **Conciencia fonológica** | Separar sílabas de *cor-te-za*, sonido inicial de *liquen*. Se hace caminando entre un árbol y otro, sin material extra |
> | **Comunicación funcional entre pares** | Quien mide dice el número en voz alta y quien anota lo repite para confirmar. Si no se articula claro, el dato sale malo: hay una razón real para hablar bien |
> | **Grabación de la propia observación** | El estudiante graba y después se escucha. Sirve para el automonitoreo y de paso nos deja el registro |
>
> | En lo escrito | Cómo entra en el protocolo |
> |---|---|
> | **Escritura funcional muy corta** | El código en la etiqueta, el nombre en la ficha, el propio nombre como observador. `TRI-014` es reconocimiento de letras y números con una función verdadera |
> | **Dictado al adulto y copia parcial** | El estudiante dicta, el adulto escribe, se le lee de vuelta y copia una palabra o una frase |
> | **El dibujo como puente a la palabra** | Dibujar, nombrar lo dibujado, rotular el dibujo. En ese orden. Es el herbario ilustrado cumpliendo dos funciones |
> | **Un producto con destinatario real** | *El libro de nuestros árboles*: una página por estudiante, con su dibujo, el nombre del árbol y tres palabras suyas |
>
> ⚠️ **El límite, dicho claro.** Nada de esto lo decide el equipo del proyecto. Son propuestas para
> poner sobre la mesa; **quiénes deciden qué sirve para sus estudiantes y en qué nivel son las
> profesionales de Hablaarte**. Eso ya estaba comprometido como co-diseño en la actividad 1.3, y ahora
> tiene contenido concreto que llevarles a esa reunión.

**El recuadro de dibujo merece una nota.** No es relleno para los más chicos. El dibujo de observación obliga a mirar detenido, que es la destreza que el protocolo entero necesita, y es además el punto de partida del **herbario ilustrado**, que es el componente artístico obligatorio del formulario. O sea que ese recuadro conecta la ficha con un producto comprometido del proyecto.

---

## 5. La historia del árbol: lo que en realidad pediste

Esta es la parte que más me interesó de tu planteamiento, y creo que vale más de lo que parece a primera vista. Pero hay que separarla en tres objetos distintos, porque hoy están mezclados en uno.

### 5.1 Los tres objetos

**a) La página del árbol.** Es una **salida**, no una ficha. Una página pública en el observatorio, por código, que se arma sola con lo que ya está en la base de datos:

```
TRI-014 · "el árbol de la esquina"
Los Trigales · Ignacio Carrera Pinto con [calle]
─────────────────────────────────────────────
Especie        Acer negundo (confirmada por especialista)
Lo llamamos    "arce" · mapuzugun: [pendiente]
DAP            34,4 cm   ·   Altura ~9 m   ·   Copa 6,2 × 5,8 m
Estado         Regular, daño mediano
Sombra         28 m²
Carbono        estimado, rango declarado
Valor Art. 32  entre X e Y UTM
Vida asociada  4 morfotipos de liquen · 3 de artrópodos · 1 hongo
Medido por     equipo 3, 8° básico, 24 de marzo de 2027
─────────────────────────────────────────────
LÍNEA DE TIEMPO
2027 ●  primera medición
2030 ○  próxima revisita programada
```

Con una sola observación esa línea de tiempo tiene un punto. **Y eso está bien, porque muestra el punto cero.** Un árbol con un solo punto y una revisita programada comunica mejor la idea de monitoreo que cualquier explicación.

**b) La ficha de revisita (F3).** Es la **entrada** de 2030 y es la que hay que diseñar ahora aunque se use en tres años. No es igual a F1: una revisita registra **cambios**, no estado absoluto, y por eso muestra el dato anterior impreso al lado del campo vacío:

```
┌──────────────────────────────────────────────────────────────┐
│ FICHA DE REVISITA · TRI-014                    Visita nº __  │
│ Medición anterior: 24-03-2027                                │
├──────────────────────────────────────────────────────────────┤
│ ¿El árbol sigue ahí?                                         │
│   ☐ sí   ☐ NO → ☐ talado  ☐ caído  ☐ no lo encontramos      │
│   (si no está: foto del lugar y fecha. ESTE ES EL DATO       │
│    MÁS IMPORTANTE QUE PUEDE PRODUCIR UNA REVISITA)           │
├──────────────────────────────────────────────────────────────┤
│ Perímetro a 1,30 m     antes: 108,0 cm    ahora: _____ cm    │
│ Estado                 antes: REGULAR     ahora: ________    │
│ Copa N-S               antes: 6,2 m       ahora: _____ m     │
│ Celdas con liquen      antes: 34 de 100   ahora: ____        │
├──────────────────────────────────────────────────────────────┤
│ ¿Qué cambió? ☐ lo podaron  ☐ hay obra nueva al lado          │
│   ☐ cambió la vereda  ☐ tiene cables nuevos  ☐ nada visible  │
├──────────────────────────────────────────────────────────────┤
│ Foto desde el MISMO punto que la foto de 2027 (va impresa    │
│ al reverso de esta ficha para poder repetir el encuadre)     │
└──────────────────────────────────────────────────────────────┘
```

🔑 **Ese último detalle, la foto anterior impresa al reverso para repetir el encuadre, es lo que convierte una serie de fotos sueltas en una secuencia comparable.** Cuesta imprimir una foto y es la diferencia entre un archivo y una serie temporal.
**c) La biografía narrativa.** Es lo que tú describiste con más cariño y es lo que las escuelas van a querer: el árbol contado, no tabulado. *"Este árbol lo midió el 8° B en 2027. En 2029 lo podaron. En 2030 volvió el mismo curso, ya en la media, y estaba 3 cm más grueso."* Se construye sola con los datos de arriba, pero es un **producto de comunicación**, no un formulario. Va en la página pública y en el cuadernillo.

### 5.2 Por qué esto es lo más fuerte de la postulación

Porque es la única parte del proyecto que **no puede existir sin haber empezado**. Todo lo demás alguien podría hacerlo mejor con más plata y más tiempo. Una serie temporal, no: o se empieza en 2027 o el punto cero de 2027 no existe nunca.

Y dicho como corresponde en el formulario: **la continuidad deja de ser una intención declarada y pasa a ser una consecuencia metodológica.** La línea base no sirve de nada sin la segunda medición, y por eso el proyecto está diseñado para que la segunda medición sea posible sin nosotros.

### 5.3 Lo que hay que comprometer ahora

| Producto | Cuándo | Estado |
|---|---|---|
| Página del árbol en el observatorio | Etapa 4, semanas 31 a 34 | Ya está la actividad 4.3 |
| **Ficha de revisita F3, diseñada e impresa** | Etapa 4, junto al cuadernillo | 🔑 **Agregar a la actividad 4.1** |
| Fotos con punto de toma registrado | Desde la primera salida | Agregar a F1 |
| Revisita programada y escrita en el cuadernillo | Etapa 4 | Ya está |

---

## 6. La cadena completa, campo por campo

Pediste diseñar las fichas considerando toda la cadena. Esta es, con los responsables y el punto donde cada dato puede perderse.

```
FICHA EN TERRENO ──▶ DIGITACIÓN ──▶ VALIDACIÓN ──▶ BASE DE DATOS ──▶ MAPA ──▶ ANÁLISIS ──▶ PÁGINA DEL ÁRBOL ──▶ REVISITA
   estudiantes         estudiantes    especialista    análisis       observatorio  análisis      observatorio      2030
   + docentes          + docentes                     y datos                                                      escuela
```

| Etapa | Quién | Riesgo principal | Defensa |
|---|---|---|---|
| **Ficha en terreno** | Estudiantes | Campo mal llenado o vacío | Casillas cerradas, descripciones escritas, práctica en el patio antes de salir |
| **Digitación** | Estudiantes y docentes, en aula | 🔴 **El cuello de botella real.** 180 fichas de papel a planilla | Ver §7 |
| **Validación** | Especialista | Identificación errada | Fotos obligatorias; la especie se pone acá, no en terreno |
| **Base de datos** | Análisis y datos | Registros huérfanos sin código | Código en ficha, en nombre de archivo de foto, en campo de iNaturalist y en notas. Cuádruple redundancia |
| **Mapa** | Observatorio | GPS impreciso | Precisión declarada por cada punto; los de más de 10 m se marcan |
| **Análisis** | Análisis y datos | Datos no comparables por esfuerzo distinto | Hora de inicio y término en cada ficha; rarefacción |
| **Página del árbol** | Observatorio | Que quede desactualizada | Se genera desde la base, no se escribe a mano |
| **Revisita** | La escuela, 2030 | No encontrar el árbol | Prueba de relocalización a ciegas en 2027, que verifica que el sistema funciona |

### 6.1 El diccionario de variables

Cada variable, con su ficha, su nivel mínimo, su destino y para qué sirve. Es lo que evita que entre un dato "por si acaso".

| Variable | Ficha | Nivel | Destino | Para qué |
|---|---|---|---|---|
| Código | F1-A | Explorador | Clave primaria | Todo |
| Hora inicio y fin | F1-A | Explorador | Control | 🔑 Esfuerzo de muestreo |
| Fecha, clima, equipo | **F2** | Explorador | Control | Detectabilidad, efecto observador |
| GPS y precisión | F1-A | Investigador | Mapa | Relocalización |
| Calle y referencia | F1-A | Investigador | Mapa | Relocalización |
| "Lo llamamos" | F1-A | Explorador | Base | Etnobotánica |
| Nombre en mapuzugun | F1-A | Explorador | Base | Saberes territoriales, campo obligatorio del formulario |
| Fotos (3) | F1-A | Explorador | Validación | Especie |
| Perímetro a 1,30 m | F1-B | Investigador | Base → DAP | **H1**, carbono, Art. 32 |
| Altura de medición | F1-B | Investigador | Metadato | 🔑 Revisita 2030 |
| Nº de fustes | F1-B | Investigador | Base | Alometría |
| Altura total | F1-B | Investigador | Base | Biomasa |
| Copa en 2 ejes | F1-B | Técnico | Base | **Sombra**, área foliar |
| Estado 3 clases | F1-B | Explorador | Base | **H4**, análisis de biodiversidad |
| Estado 5 clases | F1-B | Técnico | Base | Factor `fd` del Art. 32 |
| Daños visibles | F1-B | Explorador | Base | Explica estado, documenta desmoche |
| Floración o fruto | F1-B | Explorador | Base | Fenología, gana valor en la revisita |
| Superficie al pie | F1-C | Explorador | Base | Lo que el satélite no ve |
| Distancia a calzada | F1-C | Investigador | Control | Exposición |
| Cables sobre el árbol | F1-C | Explorador | Base | Explica el desmoche |
| Árboles a menos de 10 pasos | F1-C | Investigador | Base | **H2** a escala fina |
| Amenazas (casillas) | F1-C | Explorador | Base | 🔑 Tocón vecino = tala reciente |
| Cara del tronco de la grilla | F1-D | Investigador | Metadato | 🔑 Revisita 2030 |
| Celdas con liquen | F1-D | Investigador | Base | **H3**, cobertura |
| Morfotipos de liquen | F1-D | Explorador | Base | **H3**, riqueza |
| Grupos observados | F1-E | Explorador | Base | **H1, H2, H4** |
| "No vimos nada" | F1-E | Explorador | Base | 🔑 Ausencia real |
| Fotos a iNaturalist | F1-E | Investigador | GBIF | Identificación y aporte global |
| Campo libre | F1-F | Explorador | Cualitativo | Lo no anticipado |
| Árboles no accesibles | **F2** | Investigador | Control | 🔑 Sesgo de selección |
| Percepción térmica | **F2** | Explorador | Complementario | Educativo, contraste con satélite |
| Conteo de aves | **F2** | Técnico | Base, nivel sitio | H2, complementario |
| Cobertura vegetal 100 m | — | — | Cruce satelital | **H2** |
| Temperatura de superficie | — | — | Cruce satelital | Contexto |
| Unidad vecinal e índice | — | — | Cruce satelital | Justicia ambiental |
| **Especie** | — | Especialista | Base | **H1** nativo o exótico |

**Las cuatro últimas no las levanta nadie en terreno.** Tres las aporta el observatorio por cruce espacial y la cuarta la pone la especialista. Vale la pena que esto quede visible en el cuadernillo: los estudiantes ven que su dato se junta con otros que vienen de un satélite y de una especialista, y que el resultado es de los tres.

---

## 7. 🔴 El cuello de botella que nadie ha mirado: la digitación

Ciento ochenta fichas de papel tienen que llegar a una planilla. **Eso no está en el plan de actividades ni en el presupuesto, y es una tarea real.**

A dos o tres minutos por ficha son entre seis y nueve horas de digitación, más la revisión. Si se acumula para el final, se hace mal y tarde.

**Propuesta: la digitación es parte del taller, no trabajo administrativo posterior.** Se hace en aula, en la sesión siguiente a cada salida, con los propios estudiantes ingresando sus fichas en un formulario en línea sencillo. Tiene tres ventajas y ninguna desventaja:

1. Los datos entran **frescos**, cuando el equipo todavía recuerda qué quiso decir con una letra ilegible.
2. **Ingresar datos es contenido**, no trámite: es la parte de la indagación científica que casi nunca se enseña, y aparece en los objetivos de aprendizaje de registro y organización de información.
3. **El error se detecta cuando todavía se puede volver al árbol**, no en junio.

⬜ **Hay que agregarlo como actividad explícita** en la etapa 2 del plan, y contemplar en el presupuesto el tiempo de un adulto acompañando esas sesiones.

---

## 8. El presupuesto de minutos, que es la restricción real

| Bloque | Minutos por árbol | Nivel |
|---|---|---|
| A · Identificación y fotos | 3 | Explorador |
| B · Medición | 4 | Investigador |
| C · Entorno | 1 | Explorador |
| D · Grilla de líquenes | 4 | Investigador |
| E · Cinco minutos de observación | 5 | Explorador |
| F · Campo libre | 1 | Explorador |
| Traslado al siguiente árbol | 2 | — |
| **Total** | **20** | |

**Veinte minutos por árbol contra una hipótesis de trabajo de 12 a 15.** Con 20 minutos, un equipo hace 6 árboles en una salida de dos horas útiles; con 5 equipos, 30 árboles por salida; y 180 árboles son **6 salidas**, más las repeticiones. Cabe en marzo y abril, pero justo.

**Si el piloto arroja más de 20 minutos, este es el orden de recorte**, decidido ahora y no en terreno:

| Orden | Qué se recorta | Cuánto ahorra | Qué se pierde |
|---|---|---|---|
| 1° | Bloque C completo, salvo superficie al pie y amenazas | 0,5 min | Poco: casi todo lo cubre el satélite |
| 2° | Copa en un solo eje en vez de dos | 1 min | La sombra pasa a círculo en vez de elipse, menos precisa |
| 3° | Grilla de líquenes de 100 a 25 celdas | 2 min | Menos resolución en cobertura, se mantiene la riqueza |
| 4° | Observación de 5 a 3 minutos | 2 min | Menos detección de artrópodos. **Hay que aplicarlo a todos los árboles o los datos no se comparan** |
| 5° | Bajar la meta de 210 a 180 y de 180 a 150 | — | Poder estadístico |

⚠️ **Lo que no se recorta nunca:** la hora de inicio y término, el "no vimos nada", el código, y las fotos. Sin esos cuatro, los datos dejan de servir aunque se levanten todos los demás.

---

## 9. El kit de ciencia ciudadana del Observatorio

Preguntaste si esto puede convertirse después en un kit que Ekuwün siga usando con otras escuelas. **Sí, y creo que es la mejor idea de tu planteamiento**, por una razón que va más allá de lo práctico: **convierte el segundo producto del proyecto en un objeto que se puede entregar, mostrar y contar.** Hoy "queda instalado un sistema de monitoreo" es una frase; un kit es una caja.

### 9.1 Qué contiene

| Componente | Estado al terminar el proyecto |
|---|---|
| Fichas F1 en sus tres formatos, en PDF imprimible y editable | Producidas y probadas en tres escuelas |
| Ficha del tramo F2 | Ídem |
| **Ficha de revisita F3** | Producida, sin usar todavía |
| Protocolo de una plana, plastificable | Producido |
| Cuadernillo docente con la secuencia didáctica | Comprometido en la actividad 4.1 |
| Instructivo del circuito iNaturalist | Producido |
| Grilla de acetato de 10×10 cm, plantilla para reproducir | Producida |
| Lista de materiales con costos reales | Del presupuesto ejecutado |
| Planilla de datos y diccionario de variables | §6.1 de este documento |
| Guía de errores frecuentes | **Del control de calidad**, con los errores reales medidos |

🔑 **Esa última línea es la que ningún otro kit tiene.** No dice "cuidado, midan bien": dice **cuánto se equivocan realmente los estudiantes al medir, en qué dirección y en qué campos**, medido con la submuestra de control ciega de este proyecto. Un kit que trae su propio margen de error medido es un instrumento, no un folleto.

### 9.2 Por qué encaja con lo que el fondo busca

FMA dijo explícitamente que busca *replicar y escalar*, y advirtió que los talleres escolares que solo se repiten cada año con financiamiento nuevo se leen como poca proyección. **El kit es la respuesta exacta a esa advertencia:** lo que queda no es la voluntad de repetir, es el instrumento que permite repetir sin nosotros y sin plata nueva.

Y tiene la ventaja de que **es un subproducto, no un costo adicional**. Todo lo que contiene hay que producirlo igual para ejecutar el proyecto. Lo único que agrega es el trabajo de ordenarlo, documentarlo y publicarlo bajo licencia abierta, que es cuestión de días de la coordinación pedagógica, no de una partida nueva.

⚠️ **Una precaución.** No conviene presentar el kit como **el** producto del proyecto. El producto es la línea base y el sistema de monitoreo; el kit es la forma que toma el segundo. Presentarlo como producto principal correría el riesgo de que se lea como material educativo, y el fondo financia conservación, no producción de materiales.

### 9.3 Y una posibilidad que dejo planteada, no comprometida

Si el kit funciona en tres escuelas tan distintas como las nuestras, **queda demostrado empíricamente que es replicable**, y eso es un resultado, no una promesa. Ese es el argumento con el que Ekuwün puede llegar al DAEM a proponer que se use en más establecimientos, o postular a otro fondo para escalarlo.

⬜ No lo comprometería en esta postulación. Es lo que viene después, y conviene que aparezca como horizonte y no como meta de nueve meses.

---

## 10. Qué hay que cambiar en los documentos que ya están escritos

| Documento | Cambio |
|---|---|
| `FMA_2026_PILOTO.md` §3 | La ficha v1 pasa a ser **F1 estándar**. Sacar de ella fecha, clima y equipo, que se van a F2. Agregar: altura de medición registrada, cara del tronco, floración o fruto, bloque C, estado anidado en 3 y 5 clases |
| `FMA_2026_ACTIVIDADES.md` 1.3 | Ampliar: no es "ficha v2", son **F1 en tres formatos, F2 y F3** |
| `FMA_2026_ACTIVIDADES.md` etapa 2 | 🔑 **Agregar actividad de digitación en aula**, que hoy no existe |
| `FMA_2026_ACTIVIDADES.md` 4.1 | Agregar la **ficha de revisita F3** y el **kit** como entregables |
| `FMA_2026_ACTIVIDADES.md` §8 | Ítem 3 del presupuesto: diseño gráfico e impresión de **tres formatos**, no uno |
| `FMA_2026_DISENO_CIENTIFICO.md` §5 | Reemplazar la ficha por referencia a este documento |
| Presupuesto (paso 7) | El diseño gráfico de la ficha pictográfica es una **partida real**: no la puede hacer cualquiera y es lo que hace posible la participación en Hablaarte |

---

## 11. Lo que necesito para cerrar este diseño

| # | Pregunta | Por qué bloquea |
|---|---|---|
| 1 | 🔴 **¿Hablaarte es solo parvularia o también básica?** | Define si esa escuela produce datos dendrométricos o solo de biodiversidad, y cuántos árboles compromete |
| 2 | **Qué cursos exactos participan en cada escuela** | Define qué formato de ficha se imprime y en qué cantidad |
| 3 | ¿Hay alguien que pueda hacer el **diseño gráfico** de la versión pictográfica? | Es una partida del presupuesto y una competencia específica |
| 4 | ¿Las fonoaudiólogas de Hablaarte pueden revisar la ficha pictográfica? | Ya está ofrecido en la carta de apoyo. Es la validación que le da legitimidad |
| 5 | ¿Confirmas la percepción térmica como componente complementario? | Es la única variable de tu lista que agrego sin que estuviera en el diseño previo |
