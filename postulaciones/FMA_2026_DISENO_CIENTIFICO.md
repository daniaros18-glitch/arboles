# Diseño científico — El árbol urbano como hábitat

**Proyecto:** Observatorio Ciudadano del Arbolado Urbano de Temuco · Fondo FMA 2026-2027
**Documento:** diseño científico completo, previo a presupuesto y redacción
**Fecha:** 11 de agosto de 2026
**Base previa:** [`FMA_2026_ESTRUCTURA_CONCEPTUAL.md`](FMA_2026_ESTRUCTURA_CONCEPTUAL.md) · [`SERVICIOS_ECOSISTEMICOS_E_INDICE.md`](../investigacion/SERVICIOS_ECOSISTEMICOS_E_INDICE.md)

---

## 1. Pregunta científica

### Las tres alternativas

**Opción A — Estructura del arbolado y biodiversidad asociada**
> ¿Qué atributos del arbolado urbano de Temuco —tamaño del ejemplar, origen nativo o exótico, estado sanitario y cobertura arbórea circundante— explican mejor la riqueza y composición de la biodiversidad que sostiene?

- **Falsable:** sí. Puede resultar que ningún atributo explique nada, o que el origen no importe.
- **Objeto:** el arbolado y su biodiversidad. La ciencia ciudadana es método, no tema.
- **Consecuencia práctica:** define qué ejemplares priorizar para protección y qué especies plantar.
- **Riesgo:** requiere suficiente rango de variación en los predictores. Se resuelve en el diseño (§11).

**Opción B — Desigualdad ambiental y biodiversidad**
> ¿La desigualdad en cobertura arbórea entre barrios de Temuco se traduce en desigualdad en la biodiversidad urbana que sus habitantes pueden encontrar cerca de su casa?

- **Falsable:** sí, y con un resultado potencialmente incómodo (puede que no haya diferencia).
- **Fortaleza:** conecta con el índice de equidad que ya construimos y con justicia ambiental.
- **Debilidad:** el barrio como unidad reduce mucho el tamaño muestral. Con 4-6 barrios no hay poder estadístico para una comparación entre barrios como tal.

**Opción C — Irremplazabilidad del arbolado maduro**
> ¿Puede un árbol joven reemplazar ecológicamente a un árbol maduro talado, en términos de la biodiversidad que sostiene?

- **Falsable:** sí, y es la pregunta con mayor filo político en Temuco.
- **Debilidad:** es un caso particular de A (el efecto del DAP). Como pregunta única es demasiado estrecha para sostener un proyecto de 9 meses.

### Cuál es la más sólida

**La A**, por tres razones:

1. **Subsume a C** (el tamaño es uno de los atributos evaluados) y **habilita B** como análisis secundario sin costo adicional, porque la estratificación territorial (§11) ya reparte los árboles entre barrios contrastantes.
2. **La unidad de análisis es el árbol**, no el barrio: con 200-350 árboles hay poder estadístico real. Con 6 barrios, no.
3. **Ningún resultado la deja sin sentido.** Si el tamaño manda → argumento contra la tala de ejemplares maduros. Si el origen manda → argumento para plantar nativas. Si nada explica → hallazgo genuino sobre homogeneización de la biota urbana, publicable igual.

> **Pregunta central adoptada:**
> **¿Qué atributos del arbolado urbano de Temuco explican la biodiversidad que sostiene, y cómo se distribuye esa capacidad entre barrios con distinta cobertura arbórea?**

---

## 2. Hipótesis

**H1 — El tamaño pesa más que el origen.**
El diámetro del tronco (DAP) explica más variación en la riqueza de biodiversidad asociada que la condición de nativo o exótico del árbol.
→ *Predicción:* en un modelo con ambos predictores, el DAP tiene efecto significativo y mayor tamaño de efecto estandarizado que el origen.
→ *Refutación:* el origen resulta significativo y el DAP no, o el DAP no muestra relación.

**H2 — El contexto importa más allá del árbol.**
La riqueza asociada a un árbol aumenta con la cobertura arbórea en un radio de 100 m, **controlando por los atributos del propio árbol**.
→ *Predicción:* efecto positivo de la cobertura del entorno en un modelo mixto con la escuela como factor aleatorio.
→ *Refutación:* el efecto es nulo → los árboles funcionan como islas independientes, lo que cambiaría la estrategia (plantar donde sea vs. plantar conectando).

**H3 — Los líquenes registran el gradiente de contaminación.**
La riqueza y cobertura de líquenes en la corteza disminuye en los sectores con mayor exposición a humo de leña.
→ *Predicción:* gradiente detectable entre sectores.
→ *Refutación:* sin patrón espacial → o no hay gradiente, o el método no lo detecta (y eso también hay que reportarlo).

**H4 (opcional, exploratoria) — El árbol deteriorado no está vacío.**
Los árboles en mal estado sanitario no tienen menor riqueza total, sino **composición distinta** (más taxones asociados a madera muerta y corteza desprendida).
→ Se contrasta con diversidad beta, no con riqueza.
→ Es la hipótesis que más puede sorprender y la que mejor comunica que "sano" y "valioso" no son sinónimos.

**Recomendación:** comprometer **H1, H2 y H3** en la postulación. H4 como análisis exploratorio declarado como tal.

---

## 3. Variables

### 3.1 Independientes (predictoras)

| Variable | Tipo | Cómo se obtiene | Nivel |
|---|---|---|---|
| **DAP** (diámetro a 1,3 m) | continua | perímetro medido ÷ π | árbol |
| **Origen** (nativo / exótico) | binaria | de la especie identificada | árbol |
| **Especie** | categórica | identificación validada | árbol |
| **Altura total** | continua | estimada (vara o app) | árbol |
| **Área de copa** | continua | dos diámetros perpendicularmente → elipse | árbol |
| **Estado sanitario** | ordinal (3 clases) | protocolo visual | árbol |
| **Tipo de emplazamiento** | categórica | vereda / bandejón / plaza / patio escolar | árbol |
| **Cobertura arbórea 100 m** | continua | **de nuestra capa satelital existente** | entorno |
| **Temperatura de superficie** | continua | **de nuestra capa Landsat existente** | entorno |
| **Distancia a calzada con tráfico** | continua | medida o SIG | entorno |
| **Estrato de cobertura del barrio** | categórica | del índice de equidad propio | barrio |

Las tres variables de entorno **no las miden los estudiantes**: las aporta el Observatorio desde el análisis satelital ya operativo. Ese es el aporte diferencial de tener trayectoria previa.

### 3.2 Dependientes (respuesta)

| Variable | Definición operativa |
|---|---|
| **Riqueza de morfoespecies** | nº de tipos distintos registrados por árbol, con esfuerzo estandarizado |
| **Riqueza de líquenes** | nº de morfotipos en la grilla de corteza |
| **Cobertura de líquenes** | % de celdas ocupadas en la grilla |
| **Abundancia de aves** | nº de individuos por punto de conteo |
| **Riqueza de aves** | nº de especies por punto de conteo |
| **Composición** | matriz árbol × taxón, para análisis de diversidad beta |

### 3.3 De control (hay que registrarlas o los datos no valen)

| Variable | Por qué |
|---|---|
| **Esfuerzo de muestreo** (minutos por árbol) | Sin esfuerzo constante, "más riqueza" solo significa "más rato mirando". **Es la variable de control más importante de todo el diseño** |
| **Fecha y hora** | La detectabilidad de aves e insectos cambia con la hora y la estación |
| **Condición meteorológica** (3 clases) | Con lluvia o viento no se detectan insectos ni aves |
| **Observador / equipo** | Efecto observador: unos ven más que otros. Se modela como factor aleatorio |
| **Superficie de corteza evaluada** | La grilla estandariza esto para líquenes |
| **Altura de muestreo en el tronco** | Fija: grilla entre 1,0 y 1,5 m |
| **Escuela / sitio** | Factor aleatorio en los modelos mixtos (evita pseudorreplicación) |

---

## 4. Unidad de muestreo

**Decisión: diseño jerárquico con el árbol como unidad de muestreo y observación.**

```
Estrato de cobertura arbórea  (2 niveles: baja / alta — del índice de equidad)
   └── Escuela / sitio        (4-6, con buffer de 500 m)
          └── ÁRBOL           (40-60 por sitio)  ← unidad de muestreo
                 ├── grilla de corteza (líquenes)
                 ├── observación de artrópodos (esfuerzo fijo)
                 └── punto de conteo de aves (nivel sitio, no árbol)
```

**Justificación científica:**

1. **Las hipótesis son sobre atributos del árbol** (DAP, origen, estado). Si la unidad fuera la parcela o el barrio, esos atributos se promediarían y la pregunta se volvería incontestable. La unidad de muestreo debe estar al nivel donde varía el predictor.
2. **Poder estadístico.** 200-350 árboles permiten modelar; 4-6 barrios no. Con el barrio como unidad, n = 6.
3. **Pero los árboles del mismo sitio no son independientes** (comparten clima, manejo, entorno). Ignorarlo sería **pseudorreplicación**, el error clásico. Se resuelve con **modelos lineales generalizados mixtos (GLMM)** con la escuela como factor aleatorio. Esto hay que decirlo explícitamente en la postulación: es la señal más clara de que el diseño lo pensó alguien que sabe.
4. **Las aves son la excepción.** No se pueden asignar a un árbol individual: se mueven. Su unidad natural es el **punto de conteo** (radio fijo, tiempo fijo) a nivel de sitio. Por eso las aves responden a H2 (contexto) pero **no** a H1 (atributos del árbol individual). Conviene declararlo y no forzarlo.

---

## 5. Ficha de terreno

### 5.1 Datos imprescindibles

| Campo | Formato | Quién |
|---|---|---|
| **Código del árbol** | `ARB-TEM-0001` correlativo | estudiante |
| **Coordenadas GPS** | lat, lon (celular) | estudiante |
| **Foto del árbol completo** | 1 foto | estudiante |
| **Foto de la corteza** con referencia de escala | 1 foto | estudiante |
| **Foto de hoja / fruto / flor** (para identificar) | 1-2 fotos | estudiante |
| **Perímetro del tronco a 1,3 m** | cm, 1 decimal | estudiante |
| **Estado sanitario** | 3 clases: bueno / regular / malo | estudiante |
| **Tipo de emplazamiento** | vereda / bandejón / plaza / patio | estudiante |
| **Esfuerzo de observación** | minutos exactos | estudiante |
| **Fecha, hora, clima, equipo observador** | — | estudiante |
| **Especie** | nombre científico | **validada por especialista** |

### 5.2 Datos recomendables (mejoran mucho, cuestan poco)

| Campo | Por qué vale la pena |
|---|---|
| **Altura total estimada** | Entra en las ecuaciones de biomasa; la app de celular basta |
| **Diámetro de copa en dos ejes** (N-S, E-O) | Da área de copa y sombra proyectada por geometría simple |
| **Altura a la base de la copa** | Necesaria para área foliar en i-Tree |
| **Nº de fustes** | Un árbol multifuste rompe las ecuaciones alométricas si no se registra |
| **Distancia a la calzada** | Control de exposición a contaminación y sal |
| **Presencia de daño visible** (heridas, desmoche previo, cables) | Explica el estado sanitario y documenta la poda severa |

### 5.3 Datos que **NO** hay que levantar (y por qué)

| Campo | Motivo del descarte |
|---|---|
| **Edad del árbol** | No es medible sin barrenar. Estimarla por diámetro es circular: ya tenemos el diámetro |
| **% de copa faltante** | Requiere criterio entrenado; entre estudiantes la variabilidad entre observadores supera la señal |
| **Exposición a la luz (CLE)** | Concepto de i-Tree difícil de aplicar sin entrenamiento; aporta poco en calle abierta |
| **Identificación de insectos a nivel de especie en terreno** | Imposible sin lupa binocular y clave. **Se fotografía, no se determina** |
| **Temperatura con termómetro de mano** | Ruido puro: varía con sol, hora, viento. La LST satelital es más comparable |
| **Volumen de madera / biomasa calculada en terreno** | Es un cálculo posterior, no un dato de campo. Pedirlo induce a inventar |
| **Estado sanitario en 5 o más clases** | Más clases = menos concordancia entre observadores. Tres clases se pueden auditar |
| **Conteo total de individuos de artrópodos** | Inviable. Se registran **morfoespecies presentes**, no abundancias |

**Criterio general:** un dato entra a la ficha solo si (a) responde una hipótesis, (b) un estudiante de 12-16 años puede levantarlo de forma repetible, y (c) podemos auditarlo después. Si falla alguna, fuera.

---

## 6. Biodiversidad: qué es realista estudiar

| Grupo | Viabilidad | Protocolo | Veredicto |
|---|---|---|---|
| **Líquenes** | ✅ **Alta** | Grilla estandarizada sobre el tronco (1,0–1,5 m), conteo de morfotipos y frecuencia por celda | **Grupo núcleo.** Sésiles (no se arrancan ni escapan), presentes todo el año, fotografiables, y con método consolidado internacionalmente y usado en escuelas |
| **Aves** | ✅ **Alta con protocolo** | Punto de conteo de 10 min, radio 25 m, primeras horas de la mañana | **Grupo secundario.** Carismático y motivador; exige entrenamiento auditivo y tiene sesgo de detectabilidad |
| **Artrópodos** | 🟡 **Media** | Observación visual de esfuerzo fijo (5 min) sobre tronco y follaje bajo + golpeteo sobre paño blanco | **Como morfoespecies fotografiadas**, nunca como determinación en terreno |
| **Plantas epífitas y trepadoras** | ✅ Alta | Presencia/ausencia (musgos, hiedra, enredaderas) | Complemento fácil, baja diversidad |
| **Hongos** | 🟡 Baja-media | Solo registro oportunista | **Estacional y efímero.** No comprometerlo como componente sistemático |
| **Mamíferos, reptiles, anfibios** | ❌ | — | Requieren esfuerzo y permisos desproporcionados |

**Decisión: líquenes (núcleo) + aves (secundario) + artrópodos como morfoespecies (terciario).** Hongos y epífitas, oportunistas.

> **Actualización del 12-08-2026 tras la Jornada de Orientación:**
> **(a) Las aves suben de prioridad.** La **Q32** valida explícitamente un proyecto de *conservación de
> aves urbanas* dentro de la temática 1. Dejan de ser un componente prescindible y pasan a ser un
> anclaje temático útil — siempre que haya quién las identifique de oído.
> **(b) Restricción estacional que hay que respetar.** La ventana de ejecución es dic-2026 a ago-2027
> (**Q11/Q12**), y al cruzarla con el calendario escolar chileno la única franja con **clases y clima
> favorable** es **marzo-abril de 2027**: unas seis semanas para todo el terreno de artrópodos y aves.
> **Los líquenes son el único grupo observable todo el año**, lo que confirma su rol de núcleo.
> Detalle en [`FMA_2026_REVISION_TRAS_JORNADA.md`](FMA_2026_REVISION_TRAS_JORNADA.md) §13.

**El concepto clave que hay que instalar: morfoespecie.** Los estudiantes **no necesitan saber el nombre**. Registran "tipo A: liquen gris en costra", lo fotografían, y la identificación la resuelve después la comunidad de iNaturalist y el especialista del equipo. Esto convierte una limitación en método válido: la riqueza de morfoespecies es una métrica aceptada cuando la determinación taxonómica no es viable — **siempre que se declare como tal**.

**Por qué los líquenes son la mejor apuesta:** conectan biodiversidad con calidad del aire —el problema ambiental número uno de Temuco en invierno— **sin caer en la afirmación falsa de que los árboles limpian el aire**. El liquen no limpia: *registra*. Es un bioindicador, y esa distinción es exactamente el tipo de precisión que buscamos.

---

## 7. iNaturalist: mecanismo verificado y sus límites

### 7.1 Lo que verifiqué

- **Cualquier usuario puede crear un campo de observación** (*observation field*), con tipos de dato texto (incluido texto con valores predefinidos separados por `|`), número, fecha y taxón.
- **Los campos de observación solo funcionan con Proyectos Tradicionales** (*Traditional Projects*), no con los de Colección.
- Un proyecto tradicional puede **marcar un campo como obligatorio**: la observación no entra al proyecto sin ese dato.
- ⚠️ La propia documentación advierte que los campos **"no están estrictamente regulados"**: hay campos redundantes y de uso muy específico.
- ⚠️ Han existido **fallas documentadas en la exportación** de campos de observación (reportadas y corregidas en 2021, con quejas recurrentes posteriores).

### 7.2 Mecanismo propuesto

1. Crear el **Proyecto Tradicional** "Arbolado Urbano de Temuco".
2. Crear el campo de observación **`Arbol_OCAU`** (texto), obligatorio en el proyecto.
3. Cada observación de un organismo lleva el **código del árbol**: `ARB-TEM-0042`.
4. **Redundancia obligatoria:** además, escribir el mismo código en la **descripción/notas** de la observación. Las notas se exportan siempre; los campos de observación han fallado. Con el código en dos lugares, un `grep` recupera el vínculo aunque el campo falle.
5. El Observatorio cruza por código: `observación de biodiversidad ↔ árbol medido`.

### 7.3 Limitaciones que hay que declarar

| Limitación | Impacto | Mitigación |
|---|---|---|
| Campos solo en proyectos tradicionales | Los tradicionales son una funcionalidad heredada, menos priorizada por iNaturalist | El código en notas nos independiza de la plataforma |
| Exportación de campos históricamente inestable | Podríamos perder el vínculo | Redundancia en notas |
| El estudiante puede olvidar el código | Observación huérfana | Validación semanal; el código se anota primero en la ficha de papel |
| iNaturalist **oscurece las coordenadas de especies amenazadas** | Si aparece un taxón sensible, su ubicación se difumina | Nuestro vínculo es por código, no por coordenadas → **no nos afecta**. Ventaja del diseño |
| Sesgo de muestreo de ciencia ciudadana | Se observa donde hay gente y cuando hace buen tiempo | Esfuerzo estandarizado + selección sistemática de árboles (§11) |
| Dependencia de una plataforma externa | Si iNaturalist cambia sus reglas | Los datos del árbol son nuestros; solo la identificación depende de ellos |

⚠️ **Verificación pendiente obligatoria:** probar todo el circuito con **10 observaciones reales** antes de comprometerlo en la postulación (es parte del piloto, §13).

### 7.4 Por qué no duplicamos iNaturalist

iNaturalist registra *"un liquen, en este punto GPS"*. Nosotros registramos *"este liquen, sobre **este** árbol de 45 cm de DAP, en estado regular, en un barrio con 3% de cobertura"*.

**Ese vínculo individuo-a-individuo no existe en iNaturalist** y es precisamente lo que permite contrastar H1, H2 y H4. Además, todas las observaciones validadas fluyen a **GBIF**: el proyecto aporta datos primarios de biodiversidad a la infraestructura global, sin construir una plataforma que compita.

---

## 8. Protocolo de ciencia ciudadana

### 8.1 Las siete etapas y quién hace qué

| Etapa | Estudiantes | Especialistas |
|---|---|---|
| **Aprender** | Taller: qué es un árbol como hábitat, cómo se mide, qué es una morfoespecie | Diseñan y dictan |
| **Observar** | Recorrido, detección, fotografía con esfuerzo estandarizado | Acompañan la primera salida |
| **Medir** | Perímetro, altura, copa, estado sanitario en 3 clases | Capacitan y auditan submuestra |
| **Registrar** | Ficha en papel + iNaturalist + código del árbol | Revisan consistencia |
| **Validar** | Proponen identificación | ⚠️ **Confirman la determinación taxonómica** (indelegable) |
| **Analizar** | Gráficos descriptivos, comparación entre sus propios sitios | ⚠️ **Modelos estadísticos (GLMM)** |
| **Comunicar** | Presentan a su comunidad escolar; deciden qué árbol proponer como patrimonial | Apoyan; preparan el expediente Art. 9 |

**Regla de honestidad:** la identificación taxonómica final y el análisis estadístico **no** los hacen los estudiantes. Decirlo así en la postulación **fortalece** la propuesta: muestra que sabemos dónde está el límite y que no estamos vendiendo participación decorativa.

### 8.2 Sistema de control de calidad

Tres capas, todas ejecutables:

**Capa 1 — Prevención.** Protocolo escrito de una página plastificada, ficha con campos cerrados, códigos preimpresos, capacitación con árboles de práctica en el patio antes de salir.

**Capa 2 — Submuestra de control (el corazón del sistema).**
Un técnico remide, **a ciegas**, el **15% de los árboles** (30-50 ejemplares repartidos entre todos los sitios y equipos). Con eso se calcula:

| Métrica | Qué mide | Umbral de aceptación propuesto |
|---|---|---|
| **RMSE del perímetro** | error de medición del DAP | < 5 cm |
| **Sesgo medio** | ¿los estudiantes sobre o subestiman sistemáticamente? | ⏐sesgo⏐ < 2 cm |
| **% de concordancia en especie** | identificación correcta a nivel de género | > 80% |
| **Kappa de Cohen en estado sanitario** | concordancia en variable ordinal, corregida por azar | κ > 0,6 |
| **Tasa de detección de líquenes** | ¿cuántos morfotipos se les pasan? | reportada, sin umbral previo |

**Este contraste es un resultado publicable por sí mismo.** "Cuánto se equivocan los datos ciudadanos y en qué dirección" es una pregunta metodológica abierta y con demanda real. Convierte la debilidad más obvia de la propuesta en un aporte.

**Capa 3 — Corrección.** Si aparece sesgo sistemático, se corrige el conjunto de datos con el factor estimado y se declara en los metadatos. Un dato con error conocido y corregido es utilizable; un dato con error desconocido, no.

---

## 9. Carbono y oxígeno: análisis crítico

Los tres por separado, con veredicto.

### 9.1 Carbono almacenado — 🟡 estimable, con incertidumbre grande

- **Datos necesarios:** especie, DAP, altura. Los tenemos con el protocolo N2.
- **Método:** ecuaciones alométricas → biomasa aérea → × (1 + 0,26 raíz/tallo) → × 0,47 (fracción de carbono IPCC) → × 3,67 si se expresa en CO₂.
- **Ecuaciones:** Dobbs, Hernández & Escobedo (2011) para las 8 especies exóticas coincidentes; genéricas con **factor de corrección urbano 0,8** para el resto.
- **Incertidumbre acumulada, honestamente:**

| Fuente de error | Magnitud |
|---|---|
| Medición del perímetro por estudiantes | ±3-5% |
| Ecuación fuera de su zona de calibración (Santiago → Temuco) | **el mayor de todos, no cuantificable con lo que tenemos** |
| R² modestos de las ecuaciones (0,40-0,60 en varias especies) | ±20-40% |
| Especies sin ecuación (nativas del sur) | genérica + 0,8, error desconocido |

→ **Veredicto:** se puede publicar **como rango con incertidumbre declarada** y a nivel agregado (total del conjunto muestreado), **nunca por árbol individual**. No puede ser un objetivo comprometido del proyecto: es un producto derivado.

### 9.2 CO₂ secuestrado anualmente — ❌ NO en este proyecto

El secuestro es un **flujo**: requiere medir crecimiento, o sea **dos mediciones separadas en el tiempo**. El proyecto dura 9 meses. El crecimiento diamétrico anual de un árbol urbano es del orden de milímetros a pocos centímetros — **por debajo del error de medición de nuestros propios estudiantes** (RMSE objetivo < 5 cm de perímetro ≈ 1,6 cm de diámetro).

Medir crecimiento en 9 meses con este instrumental es **físicamente imposible**. Comprometerlo sería una promesa incumplible y verificable por cualquier evaluador con formación forestal.

→ **Veredicto: excluir.** Lo que sí se puede comprometer, y es más valioso: **dejar instalada la línea base con árboles marcados y georreferenciados para remedición en 3-5 años.** Eso es exactamente el "potencial de impulsar acciones a largo plazo" que piden las bases.

### 9.3 Oxígeno liberado — ❌ excluir sin excepción

No es una medición independiente: es el secuestro de carbono × 2,67. Como el secuestro no se puede medir (§9.2), **el oxígeno tampoco**. Y aunque se pudiera, Nowak, Hoehn & Crane (2007) —los autores del método— lo declaran **"relativamente insignificante"** y de valor prácticamente nulo.

→ **Veredicto: fuera.** Y usarlo como contenido educativo: *"¿por qué esta cifra que suena tan bien no sirve para nada?"* es una excelente lección sobre pensamiento crítico y sobre cómo se construyen los argumentos ambientales.

### 9.4 Lo que sí podemos afirmar sobre servicios

| Servicio | Estado |
|---|---|
| **Sombra proyectada** | ✅ **Medible directamente.** Área de copa por geometría. Sin modelos, sin supuestos |
| **Regulación térmica** | ✅ **Ya medida por nosotros**, vía satélite: +1,4 °C donde se perdió el dosel |
| **Hábitat / soporte de biodiversidad** | ✅ **Medido en este proyecto.** Es el aporte central |
| Carbono almacenado | 🟡 Estimado, con rango |
| Secuestro, oxígeno, contaminantes, agua | ❌ Fuera |

**Los tres primeros son suficientes**, y tienen algo que el carbono no tiene: se miden, no se modelan.

---

## 10. Indicadores de biodiversidad

| Indicador | Cómo se calcula | Qué necesita | Escala |
|---|---|---|---|
| **Riqueza (S)** | nº de morfoespecies distintas | matriz árbol × taxón | árbol y sitio |
| **Abundancia** | nº de individuos (solo aves y líquenes por frecuencia en grilla) | conteos | punto / árbol |
| **Diversidad de Shannon (H′)** | H′ = −Σ pᵢ ln pᵢ | abundancias relativas | sitio |
| **Dominancia de Simpson (D)** | D = Σ pᵢ² | abundancias relativas | sitio |
| **Riqueza rarificada** | rarefacción por individuos o por cobertura | esfuerzo registrado | sitio |
| **Curvas de acumulación** | especies acumuladas vs. nº de árboles muestreados | orden de muestreo | sitio |
| **Diversidad beta** | disimilitud de Bray-Curtis o Jaccard entre sitios / clases de árbol | matriz de composición | entre sitios |
| **Relación atributo–riqueza** | **GLMM**: riqueza ~ DAP + origen + estado + cobertura100m + (1⏐escuela) | todo lo anterior | árbol |
| **Cobertura liquénica** | % de celdas de la grilla ocupadas | grilla | árbol |

**Dos advertencias técnicas que hay que incorporar al diseño, no al final:**

1. **La rarefacción no es opcional.** Si un equipo mira 30 árboles y otro 60, el segundo encontrará más especies aunque el sitio sea más pobre. Comparar riqueza cruda entre sitios con esfuerzo distinto es un error de principiante. **La rarefacción y el esfuerzo estandarizado son la defensa.**
2. **Los índices de diversidad clásicos (Shannon, Simpson) exigen abundancias**, y para artrópodos solo tendremos presencia/ausencia. Con presencia/ausencia se usa **riqueza y diversidad beta**, no Shannon. Aplicar Shannon a datos de presencia sería un error visible.

**El indicador estrella del proyecto es el GLMM**, porque es el único que responde directamente a H1 y H2. Todo lo demás es descriptivo.

---

## 11. Diseño territorial

### 11.1 Selección de escuelas: estratificada, no por conveniencia

El riesgo que planteas —elegir escuelas por facilidad de contacto— es real y arruinaría el diseño: si todas las escuelas quedan en barrios parecidos, no hay variación en el predictor principal de H2 y la hipótesis se vuelve incontestable.

**Procedimiento propuesto:**

1. **Estratificar las 36 unidades vecinales** con el índice de equidad que ya tenemos, en dos estratos: **cobertura arbórea baja** (prioridad alta: Estación, Alemania, Prieto Sur, Javiera Carrera Oriente, Tromen Mollulco) y **cobertura media-alta**.
2. **Listar todas las escuelas públicas** de cada estrato (dato público del MINEDUC).
3. **Sortear el orden de contacto** dentro de cada estrato, y contactar en ese orden hasta conseguir 2-3 por estrato.
4. **Documentar las que declinaron.** Un diseño que reporta su tasa de aceptación es transparente; uno que solo muestra a quienes aceptaron, no.

Esto es **muestreo estratificado con reemplazo por no respuesta**: no es aleatorización pura —la participación es voluntaria y eso no se puede evitar— pero es defendible y auditable. La diferencia con "elegí las que me contestaron" es enorme.

### 11.2 Selección de árboles dentro de cada sitio

**Aquí está el sesgo más peligroso de todos:** si los estudiantes eligen los árboles, van a elegir **los grandes, bonitos y sanos**. Eso destruye H1 y H4, que dependen justamente de tener árboles chicos, feos y enfermos en la muestra.

**Procedimiento:**
- Buffer de **500 m** alrededor de la escuela (el barrio caminable).
- **Transectos por eje de calle**, y dentro de cada transecto **selección sistemática**: se mide **cada n-ésimo árbol** (p. ej. cada tercero), sea cual sea su estado.
- **Regla explícita e innegociable: los árboles feos, chicos y enfermos entran igual.** Conviene enseñarla como parte del taller — es una lección de método que se entiende bien.
- Cuota mínima por clase diamétrica para asegurar rango en el predictor: al menos 25% de árboles con DAP < 15 cm.

### 11.3 Cobertura y esfuerzo

| Parámetro | Valor propuesto |
|---|---|
| Sitios (escuelas) | 4-6 |
| Estratos | 2 (baja / media-alta cobertura) |
| Árboles por sitio | 40-60 |
| **Total de árboles** | **200-350** |
| Submuestra de control | 15% (30-50 árboles) |
| Puntos de conteo de aves por sitio | 3-4, repetidos 2 veces |

---

## 12. Resultado científico esperado

**Lo que existiría al terminar y hoy no existe:**

1. **El primer conjunto de datos estructurado del arbolado urbano de Temuco** con atributos medidos (especie, DAP, altura, copa, estado) **y** biodiversidad asociada por individuo. No existe para Temuco, y hasta donde alcanza nuestra revisión, es poco frecuente para ciudades intermedias del sur de Chile.

2. **Una respuesta —confirmatoria o refutatoria— sobre qué atributos del arbolado sostienen biodiversidad.** Con consecuencia directa de política: si H1 se confirma, el criterio de protección deja de ser la especie y pasa a ser el **tamaño**, lo que contradice la práctica habitual de talar ejemplares maduros exóticos y "compensar" plantando nativas jóvenes.

3. **Una estimación empírica del error de los datos de ciencia ciudadana escolar** en medición dendrométrica e identificación — con valor metodológico transferible a otros observatorios.

4. **Datos primarios de biodiversidad urbana incorporados a GBIF** vía iNaturalist, desde una región y un tipo de ecosistema subrepresentados.

5. **Una línea base marcada y georreferenciada para remedición**, que convierte un proyecto de 9 meses en el punto cero de una serie de largo plazo.

6. **Expedientes de árboles patrimoniales (Art. 9 de la Ordenanza 004/2021)** elaborados por las comunidades escolares. Es el producto de **conservación efectiva**: no sensibilización, sino protección legal de ejemplares concretos.

**Aporte a la conservación, en una frase:** el proyecto produce el criterio ecológico —hoy inexistente— para decidir **qué árboles de Temuco no se pueden talar**, y deja instalada en escuelas la capacidad de generarlo y de accionar el mecanismo legal que lo protege.

---

## 13. Protocolo piloto (ejecutable antes de cerrar la propuesta)

**Objetivo:** detectar problemas metodológicos, no producir resultados.

| Parámetro | Valor |
|---|---|
| **Sitios** | 1 escuela (o 1 grupo de estudiantes disponible) |
| **Estudiantes** | 15-20, en equipos de 3-4 |
| **Árboles** | **20-25** |
| **Duración** | 1 sesión de aula (60 min) + 1 salida (2-3 h) + 1 sesión de cierre (45 min) |
| **Plazo** | 2 semanas |

**Variables a probar:** código de árbol, GPS, fotos (árbol, corteza, hoja), perímetro a 1,3 m, estado sanitario en 3 clases, emplazamiento, tiempo de observación, grilla de líquenes, 5 min de artrópodos, registro en iNaturalist con código.

**Materiales:** huinchas de costurera (1 por equipo, ~$1.500 c/u), grilla de acetato de 10×10 cm con cuadrícula, planillas impresas plastificadas, celulares de los propios estudiantes, tiza o marcadores para código temporal, un cuaderno de campo.
**Costo estimado: bajo, del orden de $30.000–50.000.**

**Qué debe producir el piloto — siete respuestas concretas:**

1. **¿Cuántos minutos toma un árbol completo?** De aquí sale toda la planificación. Si son 25 min, 50 árboles por sitio son inviables con un curso.
2. **¿Qué campos se llenan mal o quedan vacíos?** Los que fallen se simplifican o se eliminan.
3. **¿Cuál es el error de medición del perímetro?** Se remiden 5 árboles con un técnico → primera estimación de RMSE.
4. **¿Funciona el vínculo con iNaturalist?** Prueba con **10 observaciones reales**: crear proyecto y campo, cargar, exportar, verificar que el código sobrevive. **Este es el punto que hay que verificar sí o sí antes de comprometerlo por escrito.**
5. **¿Los estudiantes pueden distinguir morfotipos de líquenes?** Si no, la grilla se simplifica a cobertura total.
6. **¿La regla de "el árbol feo entra igual" se cumple?** Se compara la distribución de DAP muestreada con la real del tramo.
7. **¿Qué preguntan los estudiantes?** El taller definitivo se diseña con esas preguntas, no con las nuestras.

**Criterio de éxito del piloto:** no es "salió bien". Es **haber encontrado al menos tres problemas** y haberlos corregido en el protocolo. Un piloto sin problemas detectados es un piloto mal hecho o mal observado.

**Y un beneficio adicional, nada menor:** ejecutar este piloto antes del 24 de agosto convierte "trabajo previo con escuelas" de promesa en hecho documentado, con fotos y datos. Es la evidencia que hoy nos falta frente a las bases.

---

## 14. Lo que hay que decidir para avanzar

1. **¿Se incluyen las aves?** Suman mucho en motivación y en H2, pero exigen alguien con oído entrenado y salidas a primera hora. Si no hay quién, mejor comprometer solo líquenes y artrópodos y hacerlo bien.
2. **¿4 o 6 escuelas?** Con 6 el diseño es más robusto; con 4 el presupuesto respira. Mi recomendación: **4 escuelas, 60 árboles cada una**, mejor que 6 con 35.
3. **¿Quién valida taxonómicamente?** Es el rol indelegable. Sin esa persona comprometida, H1 y H3 no se sostienen.
4. **¿Se alcanza a hacer el piloto antes del 24 de agosto?** Si hay una sola escuela disponible, vale la pena aunque sea con 10 árboles.
