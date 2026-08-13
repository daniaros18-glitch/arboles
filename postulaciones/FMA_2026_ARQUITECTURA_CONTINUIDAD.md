# La arquitectura de continuidad del proyecto

**Corrección y precisión sobre §2 de** [`FMA_2026_JORNADA_VIDEO_HALLAZGOS.md`](FMA_2026_JORNADA_VIDEO_HALLAZGOS.md)
**Fecha:** 12 de agosto de 2026

---

## 1. Dónde me equivoqué

Apliqué mal la advertencia de la jornada. Lo que el coordinador describió como problema fue:

> *"…talleres que quieren crear en un colegio, pero que **no se evidencia que realmente quieren proyectarlo hacia un escalamiento**… y que solamente están pensando en generar ese taller y el próximo año ojalá ser el mismo taller si consiguen financiamiento, y así perpetuamente."*

Ese es un proyecto **cuyo único producto es el taller** y que necesita financiamiento nuevo cada año para repetirse. **No es este proyecto.**

Acá los talleres **no son el fin: son el instrumento de muestreo.** Se hacen porque la pregunta científica —qué atributos del arbolado explican la biodiversidad que sostiene— **solo se puede responder con una red de observadores distribuida en la ciudad**. Y lo que producen no se agota en la jornada: entra a una infraestructura que ya existe, que no cuesta operar y que sigue funcionando después.

La distinción es real y hay que escribirla explícitamente, porque **un evaluador que lea rápido puede clasificarnos en la categoría equivocada.**

---

## 2. La arquitectura correcta, en tres niveles

```
      ¿PARA QUÉ?     →   INCIDENCIA EN POLÍTICA PÚBLICA
                         PLADECO 2027-2032 · modificación del PRC ·
                         catastro del Art. 28 · expedientes del Art. 9 ·
                         Estrategia Regional de Biodiversidad
                                    ▲
                                    │  alimenta con evidencia
                                    │
      ¿DÓNDE VIVE?   →   EL OBSERVATORIO  (infraestructura permanente)
                         serie satelital · índice de equidad por barrio ·
                         catastro ciudadano · mapa público · datos abiertos
                                    ▲
                                    │  alimenta con datos primarios
                                    │
      ¿CÓMO SE HACE? →   TALLERES Y TERRENO CON ESCUELAS  (método)
                         medir árboles · registrar biodiversidad · iNaturalist
```

**Leído de abajo hacia arriba:** los talleres son **cómo** se obtienen los datos. El observatorio es **dónde** viven y se vuelven comparables. La incidencia es **para qué** existe todo.

**Leído de arriba hacia abajo se entiende la continuidad:** aunque el financiamiento termine en agosto de 2027, los tres niveles siguen en pie. El observatorio no se apaga —es un sitio estático, de costo cero—, los datos quedan abiertos, los docentes quedan formados y los procesos de política pública siguen su curso con la evidencia ya entregada.

---

## 3. Una advertencia sobre cómo lo dijiste (y cómo conviene decirlo)

Cuando lo planteaste, dijiste: *"para poder darle continuidad a esta página que yo creé"*.

**Esa frase, tal cual, es peligrosa en la postulación.** Se lee como "necesito fondos para sostener mi plataforma", que es justo la lectura "proyecto tecnológico" que veníamos evitando — y además el fondo no financia mantención de sitios web.

**La relación es exactamente la inversa, y así hay que escribirla:**

| ❌ Cómo suena mal | ✅ Cómo es en realidad |
|---|---|
| El proyecto le da continuidad al observatorio | **El observatorio le da continuidad al proyecto** |
| Hacemos talleres para alimentar la plataforma | **El observatorio garantiza que los datos de las escuelas no mueran cuando termine el financiamiento** |
| Se pide plata para sostener el sitio | El sitio **ya existe, ya funciona y cuesta cero** — no se pide un peso para él |

El observatorio no es lo que hay que sostener: **es lo que hace que lo demás se sostenga solo.** Sin él, los datos de 240 árboles quedarían en una planilla en el computador de alguien y en tres años nadie podría remedirlos. Con él, quedan georreferenciados, públicos y comparables, y la remedición es posible aunque la haga otra gente.

Ese es el argumento de escalamiento que la jornada pedía, y es más fuerte que el de los proyectos que solo prometen "seguiremos haciendo talleres".

---

## 4. La incidencia en política pública ahora tiene respaldo documental

Fui a verificar tu intuición sobre incidir a nivel regional. **Está mejor respaldada de lo que suponías.**

**Fuente:** *Diagnóstico Estado y Tendencias de la Biodiversidad: Región de La Araucanía* (82 págs.), publicado en el sitio de la Estrategia Nacional de Biodiversidad del Ministerio del Medio Ambiente — [biodiversidad.mma.gob.cl](https://biodiversidad.mma.gob.cl/wp-content/uploads/2025/01/Diagnostico-09-Araucania.pdf). El MMA además tiene publicado el [avance de actualización de la Estrategia Regional de Biodiversidad de La Araucanía](https://biodiversidad.mma.gob.cl/avance-actualizacion-erb-araucania/), o sea que **el instrumento está en proceso de actualización ahora mismo** — igual que el PLADECO y el PRC de Temuco.

Lo que el diagnóstico regional dice, textual, y que nuestro proyecto responde:

| Línea de acción del diagnóstico regional | Qué aporta nuestro proyecto |
|---|---|
| *"Restauración y recuperación de sitios de relevancia para la conservación: humedales…, hábitat de especies bioindicadoras, ecosistemas de araucarias, sitios de significación cultural, **ecosistemas urbanos de relevancia**"* | **El instrumento regional nombra explícitamente los ecosistemas urbanos.** Ya no hay que argumentar que lo urbano cabe: está escrito |
| *"**Generación de línea de base** y estado de conservación de flora y fauna regional"* | Es literalmente nuestro entregable central |
| *"Identificación y clasificación de hongos macroscópicos, **plantas no vasculares, invertebrados**, etc."* | Son **exactamente nuestros grupos**: líquenes, musgos y artrópodos — los que "pasan desapercibidos" |
| *"Realizar estudios de **nuevas especies bioindicadoras** presentes en la región"* | Es nuestra hipótesis H3 sobre líquenes como bioindicadores |
| *"Desarrollar un **plan regional de educación ambiental transversal para establecimientos educacionales** de la región"* · *"Potenciar en los planes y programas el desarrollo y gestión de contenidos asociados a la biodiversidad"* · *"Generar material didáctico"* | Es el componente escolar, incluido el cuadernillo docente |
| **Brecha declarada:** *"No se ha identificado una **sistematización de la información** existente (línea de base regional)"* y *"**No se ha identificado un sistema de información territorial regional de la biodiversidad**"* | 🔑 **Esto es el observatorio.** El propio diagnóstico regional declara que ese sistema no existe |

**El último punto es el más fuerte de todos**, y conviene ponerlo al centro de la postulación: el instrumento de política pública regional **reconoce por escrito que falta un sistema de información territorial de biodiversidad**. Nuestro observatorio es una instancia funcionando de eso —acotada a lo urbano y a una comuna, pero funcionando, pública y reproducible.

Es la diferencia entre decir *"queremos incidir en política pública"* (intención) y *"el diagnóstico regional declara una brecha que nosotros ya estamos llenando"* (hecho verificable).

**Un hallazgo territorial adicional:** el diagnóstico identifica el **Sitio Prioritario Rukamanque** (612 ha), colindante con el **Monumento Natural Cerro Ñielol**, en la comuna de Temuco, y entre sus amenazas enumera *"población urbana aledaña, construcción de viviendas y conjuntos habitacionales"* y *"fragmentación de hábitat"*. Eso conecta de forma directa con nuestro hallazgo satelital de **4,2× más pérdida de verde dentro de los loteos aprobados**: la amenaza que el instrumento regional describe cualitativamente, nosotros la tenemos **medida**.

Y en nuestros propios datos, Ñielol es la unidad vecinal con **52% de cobertura arbórea** frente a barrios con 3%. El gradiente entre el sitio prioritario y la ciudad construida **está dentro de la misma comuna** — y es exactamente el gradiente que el diseño de muestreo estratificado va a recorrer.

⚠️ **Antes de citar esto en la postulación:** el documento es un **diagnóstico** regional publicado por el MMA, no la estrategia aprobada. Hay que describirlo con esa precisión —"el diagnóstico regional de biodiversidad de La Araucanía señala…"— y no atribuirle carácter de instrumento vigente aprobado. Conviene además revisar el estado de la actualización de la ERB en el enlace del MMA antes de enviar.

---

## 5. Cómo queda el argumento de continuidad, en cuatro frases

Para usar tal cual en la postulación, ajustando la redacción:

1. **Los talleres no son el producto: son el método.** La pregunta científica solo puede responderse con observadores distribuidos en la ciudad, y las comunidades escolares son quienes pueden estar en esos puntos de forma sostenida.
2. **Lo que se produce no se agota en la jornada.** Cada árbol medido entra a una infraestructura pública que ya existe, opera a costo cero y seguirá en línea después del proyecto.
3. **Lo que queda instalado no requiere financiamiento nuevo:** un protocolo en manos de docentes formados, una línea base georreferenciada para remedir, expedientes del Art. 9 que protegen ejemplares de forma permanente, y una colección de referencia en cada escuela.
4. **La evidencia tiene destinatarios concretos y con plazos abiertos:** el PLADECO 2027-2032, la modificación del Plan Regulador, el catastro que exige el Art. 28 de la Ordenanza y la actualización de la Estrategia Regional de Biodiversidad, cuyo diagnóstico declara la ausencia de un sistema de información territorial de biodiversidad.

---

## 6. Qué cambia en los documentos anteriores

| Documento | Cambio |
|---|---|
| `FMA_2026_JORNADA_VIDEO_HALLAZGOS.md` §2 | Se matiza: la advertencia sobre talleres **no** describe este proyecto, pero sigue siendo el riesgo de **lectura rápida** contra el que hay que redactar |
| `FMA_2026_ESTRUCTURA_CONCEPTUAL.md` | El argumento de incidencia gana respaldo documental (§4 de este documento) |
| `FMA_2026_DISENO_CIENTIFICO.md` §12 | Se agrega la brecha declarada en el diagnóstico regional como destinatario del resultado |
