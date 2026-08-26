# Paso 5 — Plan de actividades

**Proyecto:** Observatorio Ciudadano del Arbolado Urbano de Temuco · Fondo FMA 2026-2027
**Postulante:** Acción Ecologista Ekuwün — ⬜ datos institucionales pendientes
**Ventana de ejecución:** diciembre 2026 – agosto 2027 · **9 meses · 36 semanas**
**Fecha:** 13 de agosto de 2026

**Base:** [`FMA_2026_DISENO_CIENTIFICO.md`](FMA_2026_DISENO_CIENTIFICO.md) · [`FMA_2026_DECISION_SITIOS.md`](FMA_2026_DECISION_SITIOS.md) · [`FMA_2026_SERVICIOS_LINEA_BASE_Y_MONITOREO.md`](FMA_2026_SERVICIOS_LINEA_BASE_Y_MONITOREO.md) · [`FMA_2026_ESCUELAS_E_INCLUSION.md`](FMA_2026_ESCUELAS_E_INCLUSION.md) · [`FMA_2026_EQUIPO.md`](FMA_2026_EQUIPO.md)

> **Para qué sirve este documento.** Es la fuente única de la que salen las tres cosas que faltan:
> las **partidas del presupuesto** (paso 7), las **barras de la carta Gantt** (paso 8) y las
> **metas verificables** de las 500 palabras del formulario. Cada actividad declara qué produce,
> quién la hace, en qué semanas y qué gasto genera.

---

## 0. Las cuatro reglas que ordenan el plan

1. **El terreno con estudiantes cabe en marzo-abril.** Es la única franja con clases y clima. Todo lo que no sea terreno se acomoda alrededor de esa restricción, no al revés.
2. **Nada se promete sin responsable.** Donde el rol está vacante, la actividad va marcada ⬜ y con su plan B escrito.
3. **Cada actividad produce algo verificable.** Si no deja un archivo, un documento o un dato, no es una actividad: es una intención.
4. **La mitad del plan construye la línea base; la otra mitad instala el sistema de monitoreo.** El segundo producto no es el epílogo del primero: tiene actividades propias, con costo propio.

---

## 1. Corrección de escala respecto del diseño científico

El diseño escribió 4-6 sitios y 200-350 árboles cuando aún se contemplaba un sitio de referencia externo. Con **tres escuelas** el número real es otro y conviene declararlo así, no heredar un rango que ya no corresponde:

| Parámetro | Diseño original | **Este plan** |
|---|---|---|
| Sitios | 4-6 | **3** (una por escuela, radio 500 m) |
| Árboles por sitio | 40-60 | **70** |
| **Total de árboles** | 200-350 | **210** (meta), **180 mínimo comprometido** |
| Submuestra de control | 15% | **15% → 32 árboles** |
| Puntos de conteo de aves | 3-4 por sitio, 2 repeticiones | **3 por sitio × 2 = 18 conteos** |

**Por qué 210 y no más:** el piloto dirá cuántos minutos toma un árbol completo. Hasta saberlo, comprometer 350 con tres cursos es apostar. **Se compromete 180 y se declara 210 como meta**; si el piloto muestra que rinde más, se sube. Un proyecto que entrega por encima de lo comprometido se lee bien; al revés, no.

### 1.1 Recorte de alcance (13-08-2026, tras la revisión de Nicolás Mendoza)

Su objeción —*"parece harta carga, y requiere varias personas comprometidas"*— es correcta, y se refuerza con un hallazgo de las bases: **no existe planilla de evaluación**. La respuesta 33 de la jornada oficial confirma que el comité evalúa *cumplimiento de requisitos y coherencia*. **Abarcar más no suma puntaje, porque no hay puntaje.** Un proyecto sobrecargado es menos coherente, no mejor evaluado.

| Componente | Antes | **Ahora** |
|---|---|---|
| Árboles | 210 | **180 comprometidos · 210 como meta** |
| Grupos de organismos | 5 comprometidos | **Líquenes y hongos comprometidos** (co-núcleo, con especialista). **Aves y artrópodos: componentes complementarios**, se ejecutan y se reportan, pero no se comprometen como resultado |
| Expedientes Art. 9 | 3 | **1 comprometido · 3 como meta** (uno por escuela) |
| Herbario ilustrado | — | **Se mantiene**: es campo obligatorio del formulario, no es opcional |
| Tres escuelas | — | **Se mantienen**: son la identidad del proyecto y el argumento de replicabilidad |

💡 **Y la mejor idea que salió de esa revisión, que no es un recorte sino un cambio de encuadre:** el protocolo debe integrarse **dentro de asignaturas**, no ejecutarse además de ellas. Los objetivos de aprendizaje de indagación científica de Ciencias Naturales de 7° y 8° son literalmente el protocolo; el mapuzugun de Los Trigales cubre los nombres; y el perímetro a diámetro y el área de copa son geometría de Matemática. ⬜ **Hay que preguntarles a los docentes en qué asignatura y unidad lo meterían**, y escribirlo así en el formulario: es la diferencia entre "haremos talleres" y "esto se ejecuta dentro de la asignatura X", y es lo que responde de verdad el campo de proyección a largo plazo.

### 1.2 Qué va dentro del currículum y qué va fuera (23-08-2026)

La distinción es deliberada y conviene que quede escrita, porque las dos mitades sostienen argumentos distintos.

| Componente | Dónde va | Por qué |
|---|---|---|
| **Protocolo de medición y registro** | 🔑 **Dentro de asignaturas**: Ciencias Naturales y Matemática | Ahí vive el argumento de continuidad, porque se repite sin financiamiento nuevo. Y no puede haber autoselección: si solo miden los interesados, la muestra se rompe |
| **Herbario ilustrado** | **Taller de educación ambiental de Ekuwün**, en horario protegido | Es lo que la organización sabe hacer y puede acreditar. **Y no alimenta la base de datos**, así que la participación voluntaria no sesga nada |

⚠️ **El riesgo que esto evita.** El fondo advirtió que los talleres escolares que solo se repiten cada año con financiamiento nuevo se leen como poca proyección a largo plazo. Si todo el proyecto fuera taller extraprogramático, caeríamos justo ahí. Al revés, si todo fuera currículum, Ekuwün quedaría como quien facilita el programa de otro. **Separados, cada mitad hace lo que sabe hacer.**

---

⚠️ **Consecuencia estadística, dicha derecho:** con n = 180-210 árboles y la escuela como factor aleatorio de **solo tres niveles**, el GLMM se estima con un factor aleatorio pobremente poblado. Es aceptable —el interés está en los efectos fijos, y el gradiente se busca dentro de cada sitio— pero hay que decirlo y no fingir un diseño más robusto del que hay. La alternativa, si el modelo no converge, es tratar la escuela como **efecto fijo de tres niveles**, que con tres sitios es lo técnicamente correcto.

---

## 2. Etapa 1 — Preparación y formación

**Diciembre 2026 – febrero 2027 · semanas 1-12**

⚠️ **Restricción de calendario que manda en toda la etapa:** el año escolar 2026 termina a mediados de diciembre y el 2027 empieza el 1 de marzo. **Enero y febrero no hay estudiantes ni docentes.** Por eso la etapa se parte en dos: lo que necesita escuela ocurre en **diciembre**, y enero-febrero es trabajo interno de gabinete. La formación docente se agenda en la **última semana de febrero**, cuando los equipos vuelven a planificar.

| # | Actividad | Semanas | Quién | Producto verificable | Ítem presupuestario |
|---|---|---|---|---|---|
| **1.1** | **Instalación del proyecto y acuerdos operativos con las tres escuelas.** Reunión con cada dirección y equipo docente: cursos participantes, horarios, autorizaciones de salida, permisos de imagen. | 1-3 | Coordinación | Acta de acuerdo por escuela, con cursos y docentes nombrados | 2 · traslados |
| **1.2** | **Piloto metodológico con un curso.** 20-25 árboles, las siete preguntas del §13 del diseño. Incluye la prueba de las 10 observaciones reales en iNaturalist. | 2-4 | Terreno + coordinación pedagógica ⬜ | Informe de piloto con **al menos tres problemas detectados y corregidos** | 2 · materiales, traslados |
| **1.3** | **Sistema de fichas de ciencia ciudadana.** No es una ficha: son **F1 (ficha del árbol) en tres formatos** (pictográfica, estándar y técnica), **F2 (ficha del tramo)** y **F3 (ficha de revisita)**, más el protocolo de una plana. Incorpora el estado sanitario anidado en 3 y 5 clases y el emplazamiento alineado al factor `fu`. Diseño detallado en [`FMA_2026_SISTEMA_DE_FICHAS.md`](FMA_2026_SISTEMA_DE_FICHAS.md). 🔑 **La versión pictográfica no se diseña: se co-diseña, se pilotea y se ajusta** con las fonoaudiólogas, educadoras y equipo de apoyo de Hablaarte, en tres pasos verificables. No comprometemos un método validado, porque para esta población no existe; comprometemos el proceso. **Las variables y el objetivo científico no se ajustan: lo que se adapta es la vía de acceso y de registro.** | 5-8 | Especialista + pedagógica ⬜ + **diseño gráfico** + **equipo de Hablaarte** | F1 en 3 formatos, F2, F3 y protocolo · **acta de la sesión de co-diseño** · **informe del pilotaje con los ajustes aplicados** | 3 · **diseño gráfico** e impresión |
| **1.4** | **Circuito de datos.** Proyecto tradicional en iNaturalist, campo `Arbol_OCAU`, redundancia del código en notas, planilla maestra y validador de exportación. | 5-6 | Análisis y datos | Proyecto en línea + prueba de exportación documentada | — |
| **1.5** | **Fabricación y montaje de los kits de ciencia ciudadana.** No es solo comprar: se **fabrican** las varas de 1,30 m, los clinómetros caseros y las grillas con marco y relieve, y se montan **3 kits escolares y 1 técnico**, cada uno en su caja rotulada. Incluye compra de huinchas, clips macro, cronómetros, lupas, monoculares, chalecos y botiquines, y la preparación de los códigos correlativos. Composición y criterios en [`FMA_2026_EQUIPAMIENTO_INCLUSIVO.md`](FMA_2026_EQUIPAMIENTO_INCLUSIVO.md) §4. | 7-10 | Coordinación | 4 kits montados e inventariados · códigos preparados | **2 · el grueso de producción** |
| **1.6** | **Secuencia didáctica y cuadernillo docente v1.** Cuatro sesiones de aula por escuela, adaptadas a nivel y a las tres realidades. Co-diseño con las fonoaudiólogas de Hablaarte y con el equipo de mapuzugun de Los Trigales. | 5-11 | **Coordinación pedagógica ⬜** | Secuencia escrita + cuadernillo v1 en PDF | 1 · honorarios por producto |
| **1.7** | **Jornada de formación docente.** Una jornada presencial de 6 h con los docentes de las tres escuelas: protocolo, medición práctica, iNaturalist, criterios de calidad. | 11-12 | Pedagógica ⬜ + especialista | Lista de asistencia · docentes con cuenta iNaturalist activa | 1 · honorarios · 2 · alimentación |

**⬜ Riesgo declarado:** 1.2, 1.3, 1.6 y 1.7 dependen de la **coordinación pedagógica**, que hoy no tiene persona. Plan B si no aparece: el diseño de la secuencia lo asume la especialista en ciencias naturales junto a los docentes de las tres escuelas, y el cuadernillo se produce en la etapa 4 con lo aprendido en terreno en vez de anticiparse. Se pierde calidad didáctica; no se cae ninguna actividad.

---

## 3. Etapa 2 — Terreno con las comunidades escolares

**Marzo – abril 2027 · semanas 13-20**

Es la etapa crítica: ocho semanas, tres escuelas, 210 árboles. Todo lo demás existe para que esto salga bien.

| # | Actividad | Semanas | Quién | Producto verificable | Ítem |
|---|---|---|---|---|---|
| **2.1** | **Trazado de transectos y selección sistemática de árboles.** El equipo técnico define, antes de que salgan los estudiantes, los ejes de calle dentro del radio de 500 m y la regla del *n*-ésimo árbol. En Hablaarte incluye el corredor ribereño del Cautín (451 m); en Los Trigales y Campos Deportivos, deliberadamente los puntos más arbolados del sector —plaza, bandejón, patio— para estirar el rango de cobertura. | 13-15 | Análisis y datos + terreno | Mapa de transectos por escuela con puntos preasignados | 2 · traslados |
| **2.2** | **Talleres de aula y práctica en el patio.** Sesiones 1 y 2 de la secuencia: el árbol como hábitat, qué es una morfoespecie, y medición de práctica en árboles del propio patio antes de salir a la calle. Incluye la regla innegociable: **el árbol feo, chico y enfermo entra igual**, y la **calibración del paso de cada estudiante**, que mide cuánto mide su propio paso y lo usa todo el proyecto para estimar copa y distancias. | 13-14 | Pedagógica ⬜ + docentes | Registro por curso · práctica con 3 árboles del patio · **tabla de calibración de pasos por estudiante** | 1 · honorarios |
| **2.3** | **Salidas de medición dendrométrica y codificación.** Perímetro a 1,30 m, nº de fustes, altura, copa en dos ejes, estado sanitario en 5 clases, emplazamiento, daños, GPS, tres fotos, placa con código. Equipos de cuatro con roles rotativos (medir / registrar / fotografiar / cronometrar). | 14-19 | Estudiantes + docentes + terreno | **Fichas de 210 árboles** codificados y georreferenciados | 2 · traslados, materiales |
| **2.4** | **Registro de biodiversidad asociada.** Grilla de líquenes de 10×10 cm entre 1,0 y 1,5 m; hongos sobre el individuo; 5 min de artrópodos con esfuerzo fijo; epífitas por presencia. Todo fotografiado y subido a iNaturalist con el código del árbol en el campo y en las notas. | 14-19 | Estudiantes + especialista | Observaciones en el proyecto de iNaturalist, vinculadas por código | 2 · materiales |
| **2.5** | **Puntos de conteo de aves** *(componente complementario, no comprometido — ver §1.1)*. 10 min, radio 25 m, primeras horas de la mañana, 3 puntos por sitio repetidos 2 veces. En Hablaarte, un punto en el corredor ribereño. Requiere identificación auditiva. | 15-19 | **Especialista** + estudiantes | 18 planillas de conteo con hora, clima y observador | 2 · traslados |
| **2.6** | **Submuestra de control a ciegas.** Un técnico remide el 15% (32 árboles) sin ver los datos de los estudiantes, repartidos entre las tres escuelas y todos los equipos. | 16-20 | **Terreno y control de calidad** | Planilla de remedición pareada por código | 1 · honorarios por jornada |
| **2.7** | **Salida al corredor ribereño y al Humedal Urbano Antumalén** con la comunidad de Hablaarte. Coordinada con la mesa municipal de fiscalización de humedales. | 17-18 | Coordinación + especialista | Registro de la salida · observaciones de biodiversidad ribereña | 2 · transporte escolar |
| **2.8** | 🔑 **Digitación en aula, en la sesión siguiente a cada salida.** Los propios estudiantes ingresan sus fichas de papel a un formulario en línea, con un adulto acompañando. **No es trabajo administrativo posterior: es parte del taller.** Los datos entran frescos, ingresar datos es contenido curricular de registro y organización de información, y el error se detecta cuando todavía se puede volver al árbol. Sin esta actividad, 180 fichas de papel se acumulan para el final y se digitan mal y tarde. | 15-20 | Docentes + estudiantes + pedagógica ⬜ | **180 fichas digitadas** con menos de una semana de rezago | 1 · horas de acompañamiento |
| **2.9** | **Registro audiovisual del proceso.** Transversal a las salidas: fotografía y video breve para el material educativo y el compromiso de difusión con FMA. | 13-20 | Dentro del equipo | Banco de imágenes con autorizaciones firmadas | — |

⚠️ **Dos riesgos de esta etapa y sus mitigaciones:**
- **Lluvia.** En marzo-abril en Temuco llueve. Cada salida tiene fecha alternativa dentro de la misma semana, y el clima se registra como variable de control porque afecta la detectabilidad.
- **Rendimiento por árbol.** Si el piloto muestra que un árbol completo toma más de 20 minutos, se reduce la meta a 180 y se declara en el informe. **La meta se ajusta; el protocolo no se recorta.**

---

## 4. Etapa 3 — Validación, análisis y componente artístico

**Mayo – julio 2027 · semanas 21-32**

| # | Actividad | Semanas | Quién | Producto verificable | Ítem |
|---|---|---|---|---|---|
| **3.1** | **Validación taxonómica.** Confirmación de especies arbóreas desde fotos, curación de las identificaciones de iNaturalist, determinación de hongos, revisión de morfotipos de líquenes. | 19-24 | **Especialista** (indelegable) | % de árboles con especie confirmada · registro de identificaciones | 1 · honorarios por producto |
| **3.2** | **Control de calidad de los datos ciudadanos.** RMSE del perímetro, sesgo medio, concordancia en especie a nivel de género, kappa de Cohen en estado sanitario, tasa de detección de líquenes. Comparación **entre las tres escuelas**. | 21-23 | Análisis y datos | Informe de calidad con las cinco métricas y su comparación por sitio | — |
| **3.3** | **Base de datos y cruce territorial.** Depuración, corrección de sesgo si aparece, y cruce de cada árbol con las capas propias del observatorio: cobertura vegetal a 100 m, temperatura de superficie, unidad vecinal, distancia a calzada. **Incluye la validación en tierra de la capa satelital**: qué fracción de la "cobertura vegetal" que ve el satélite es realmente arbórea, contrastada con los árboles medidos dentro de esos mismos radios. | 21-25 | Análisis y datos | Base de datos abierta, documentada, con metadatos y errores declarados · **nota de validación de la capa satelital** | — |
| **3.4** | **Estimación de servicios ecosistémicos.** Área basal, área de copa y sombra, biomasa, carbono almacenado, CO₂ equivalente, secuestro anual por i-Tree, y **valor económico según Vt = Vb·fd·fu·fs del Art. 32**. Todo con supuestos y rango de incertidumbre declarados. Incluye consulta a la DMAO sobre su criterio DAP→edad. | 24-28 | Análisis y datos | Planilla de estimaciones + nota metodológica con incertidumbres | — |
| **3.5** | **Análisis estadístico.** GLMM para H1 y H2, riqueza rarificada, curvas de acumulación, diversidad beta para H4, contraste de líquenes entre sectores para H3 en versión morfotipo. | 25-30 | Análisis y datos | Script reproducible + resultados por hipótesis, incluidas las refutadas | — |
| **3.6** | **Herbario ilustrado, como taller de educación ambiental de Ekuwün.** Los estudiantes producen láminas de observación de sus propios árboles y de los organismos que sostienen: dibujo de campo, corteza, hoja, liquen. Una colección física por escuela y una digital en el observatorio. 🔑 **Es el único componente que va fuera de asignatura**, y funciona ahí porque **no alimenta la base de datos**: al no producir dato, la participación voluntaria no sesga ningún resultado. ⚠️ **Se ejecuta en horario protegido**, en el último bloque del día o en una hora libre, nunca después de clases: en un establecimiento con IVE de 90% quedarse más tarde excluye a quien cuida hermanos o depende del furgón. | 21-30 | **Ekuwün** + docentes de arte | **Tres colecciones físicas** + galería digital publicada | 3 · materiales de arte, impresión |
| **3.7** | **Informe científico de línea base.** Resultado por hipótesis, servicios estimados, error de los datos ciudadanos, y limitaciones. | 29-32 | Análisis + especialista | Informe de línea base en PDF, publicado | — |

💡 **Sobre 3.6:** el herbario ilustrado es el campo obligatorio de prácticas artísticas del formulario, y no es un adorno: **el dibujo de observación obliga a mirar detenido**, que es exactamente la destreza que el protocolo necesita. En Hablaarte, además, es una vía de registro que no depende de la palabra escrita.

⚠️ **Vacaciones de invierno** (≈ dos semanas de julio): 3.6 y todo lo que requiera estudiantes debe cerrar antes. Lo de julio en adelante es trabajo de gabinete.

---

## 5. Etapa 4 — Devolución, sistema de monitoreo e incidencia

**Julio – agosto 2027 · semanas 29-36**

Esta etapa **es el segundo producto**. No es la difusión del primero.

| # | Actividad | Semanas | Quién | Producto verificable | Ítem |
|---|---|---|---|---|---|
| **4.1** | **Cuadernillo docente, ficha de revisita y kit de ciencia ciudadana.** Versión final del cuadernillo con lo aprendido; la **ficha F3 de revisita**, que registra cambios y trae impresa la medición y la foto anteriores para repetir el encuadre; y el **kit** que reúne todo lo producido bajo licencia abierta, incluida la **guía de errores frecuentes con el margen de error real medido** en este proyecto. El kit es la forma tangible del segundo producto, no un producto aparte. | 29-33 | Pedagógica ⬜ + especialista | Cuadernillo y F3 impresos y en PDF, entregados a las tres escuelas · kit publicado | 1 · honorarios · 3 · impresión |
| **4.2** | **Prueba de relocalización a ciegas.** 🔑 Una persona que no participó del terreno intenta reencontrar 20 árboles solo con el código y las coordenadas. **Es la verificación de que el sistema de monitoreo existe de verdad**, no solo en el papel. | 33-34 | Terreno | % de árboles relocalizados · informe de fallas del sistema de códigos | 1 · por jornada |
| **4.3** | **Publicación de datos abiertos en el observatorio.** Los árboles con su ficha, sus estimaciones y su biodiversidad asociada, en el sitio que ya existe y no cuesta operar. Observaciones fluyendo a GBIF vía iNaturalist. Incluye la **página de cada árbol**, generada desde la base y no escrita a mano. | 31-34 | Análisis y datos | Capa pública en línea · registros visibles en GBIF | — |
| **4.3.bis** | **Preparación de la devolución y convocatoria barrial.** Los estudiantes preparan cómo van a contar lo que encontraron, y se convoca a las juntas de vecinos, organizaciones comunitarias, personas mayores y vecinos de cada sector. | 31-33 | Pedagógica ⬜ + coordinación | Convocatoria enviada en los tres sectores · material de presentación preparado | 2 · convocatoria |
| **4.4** | 🔑 **Devoluciones barriales, una en cada sector.** No es publicar en la web: los estudiantes presentan los resultados de su propio barrio a la gente de su propio barrio. Se muestran las fichas de los árboles más relevantes del sector y se conversa con quienes viven ahí sobre qué significan esos árboles y cómo cuidarlos. **Es además la instancia donde los expedientes del Art. 9 consiguen respaldo vecinal**, porque la ordenanza exige que sean los vecinos quienes propongan. Cada devolución deja un panel de datos del sector, que queda en la escuela, y una copia en la junta de vecinos. | 33-35 | Todo el equipo + docentes | **3 devoluciones barriales** · 3 paneles de datos entregados · respaldos vecinales recogidos | 2 · colación, amplificación · 3 · impresión |
| **4.5** | **Expedientes de árboles patrimoniales (Art. 9).** Cada comunidad escolar elige y documenta al menos un ejemplar candidato y presenta el expediente al municipio. Es el producto de conservación efectiva del proyecto. | 31-35 | Coordinación + escuelas | **Al menos 3 expedientes ingresados**, con número de recepción | 3 · impresión |
| **4.6** | **Encuentro de cierre y entrega institucional.** Un encuentro con delegaciones de las tres escuelas y las contrapartes institucionales. No es un evento aparte: es la forma pública de la entrega al municipio. 🔑 **Entrega formal del kit a cada escuela con acta**: el equipamiento no vuelve a Ekuwün, se queda donde se usó. Presentación de resultados a la DMAO, a la mesa municipal de humedales y, si los plazos calzan, como insumo al PLADECO. Informe final y rendición a FMA. | 35-36 | Coordinación | **3 actas de entrega de kit** · actas de entrega institucional · informe final y rendición aprobados | — |

---

## 6. Indicadores de proceso (lo que faltaba del paso 6)

Los indicadores científicos ya estaban en el diseño. Estos son los de ejecución, que son los que el formulario pide como "metas y cómo se verifican".

| Indicador | Meta | Cómo se verifica | Cuándo |
|---|---|---|---|
| Escuelas con acuerdo formal | 3 de 3 | Actas firmadas | S3 |
| Problemas detectados y corregidos en el piloto | ≥ 3 | Informe de piloto | S4 |
| Sistema de fichas producido | F1 en 3 formatos + F2 + F3 + protocolo | Archivos e impresiones | S8 |
| **Co-diseño de la ficha pictográfica con el equipo de Hablaarte** | Sesión realizada | Acta firmada | S6 |
| **Pilotaje de la ficha co-diseñada y ajustes aplicados** | Al menos un ajuste documentado | Informe de pilotaje | S8 |
| **Rezago de digitación** | < 1 semana entre salida y datos ingresados | Fecha de salida vs. fecha de ingreso | S20 |
| Docentes formados | ≥ 6 (2 por escuela) | Lista de asistencia + cuenta iNaturalist activa | S12 |
| **Árboles caracterizados** | **180 comprometidos · 210 meta** | Base de datos con código y coordenadas | S19 |
| Árboles con especie confirmada | ≥ 90% | Registro de validación | S24 |
| Observaciones de biodiversidad vinculadas por código | ≥ 600 | Exportación del proyecto iNaturalist | S19 |
| Submuestra de control ejecutada | 15% (32 árboles) | Planilla pareada | S20 |
| **RMSE del perímetro** | < 5 cm | Informe de calidad | S23 |
| **Kappa en estado sanitario** | κ > 0,6 (agrupado en 3 clases) | Informe de calidad | S23 |
| **Calidad equivalente entre escuelas** | Sin diferencia significativa en RMSE y κ entre los tres establecimientos | Informe de calidad | S23 |
| Estudiantes con al menos un registro atribuible | ≥ 80% de los participantes | Base de datos por observador | S19 |
| Láminas del herbario ilustrado | **≥ 45 (15 por escuela)** | Tres colecciones físicas | S30 |
| Validación en tierra de la capa satelital | Fracción arbórea de la cobertura vegetal, estimada en los 3 sectores | Nota metodológica en la base de datos | S25 |
| **Árboles relocalizados a ciegas** | **≥ 85% de 20** | Informe de relocalización | S34 |
| **Devoluciones barriales realizadas** | **3 de 3**, con asistencia de organizaciones del sector | Registro de cada instancia | S35 |
| Paneles de datos entregados a escuela y junta de vecinos | 3 y 3 | Actas de entrega | S35 |
| **Kits entregados a las escuelas, con acta** | **3 de 3** | Actas de entrega firmadas | S36 |
| Expedientes Art. 9 ingresados | **≥ 1 comprometido · 3 meta** | Número de recepción municipal | S35 |
| **Docentes que ejecutan una salida sin acompañamiento externo** | ≥ 1 por escuela | Registro de la salida | S35 |

🔑 Los tres en negrita del final —relocalización, expedientes y salida autónoma docente— **son los indicadores del segundo producto**. Son los que responden la pregunta del campo decisivo del formulario: *¿qué queda funcionando cuando el proyecto termina?*

---

## 7. Resumen para la carta Gantt

Las cuatro etapas, en las 36 semanas reetiquetadas de diciembre 2026 a agosto 2027:

```
                    DIC   ENE   FEB   MAR   ABR   MAY   JUN   JUL   AGO
Semanas             1-4   5-8   9-12 13-16 17-20 21-24 25-28 29-32 33-36
E1 Preparación      ████  ████  ████
E2 Terreno                            ████  ████
E3 Validación                                ██  ████  ████  ████
E4 Devolución                                            ██  ████  ████
```

**Cinco solapamientos deliberados**, no errores de planificación:
1. **1.2 piloto (S2-4) con 1.1 acuerdos (S1-3)** — el piloto se hace con la primera escuela que confirme.
2. **3.1 validación (S19) empieza dentro de la etapa 2** — identificar tras cada salida, no al final; si se acumula, no se termina.
3. **3.6 herbario (S21-30) atraviesa mayo-junio** — es la única forma de tener a los estudiantes trabajando después del terreno y antes de las vacaciones de invierno.
4. **4.1 cuadernillo (S29) empieza dentro de la etapa 3** — se escribe con los resultados en la mano.
5. **4.5 expedientes (S31-35) se solapa con la devolución** — el expediente se arma con lo que los estudiantes presentan.

---

## 8. De aquí sale el presupuesto (paso 7)

Las partidas que este plan genera, sin cifras todavía:

**Ítem 1 · Honorarios** — coordinación general (transversal, 9 meses) · análisis territorial y datos (dic-ene y may-ago) · especialista en ciencias naturales (por producto, concentrada mar-may) · **coordinación pedagógica ⬜** (dic-feb y mar-abr) · terreno y control de calidad (por jornada, mar-abr y ago) · horas de acompañamiento a la digitación en aula.

**Ítem 2 · Producción** — **los 4 kits de ciencia ciudadana**, evaluados uno a uno con los criterios de valor científico, valor educativo, inclusión y continuidad en [`FMA_2026_EQUIPAMIENTO_INCLUSIVO.md`](FMA_2026_EQUIPAMIENTO_INCLUSIVO.md) §4.3, con un orden de magnitud de **$1.267.000 pendiente de cotización** · traslados del equipo a las tres escuelas · transporte escolar para la salida al humedal · alimentación de la jornada de formación docente.

🔑 **Criterio de compra que ordena todo el ítem: el equipamiento se compra para las escuelas y se queda en las escuelas**, con acta de entrega en la actividad 4.6. Eso convierte una partida de producción en el soporte material del segundo producto.
❌ **No se compra dron.** Las razones, legales, presupuestarias y de participación, están en §5 de ese mismo documento.

**Ítem 3 · Otros** — **diseño gráfico** del sistema de fichas (F1 en tres formatos, F2 y F3) e impresión plastificada · materiales del herbario ilustrado · impresión del cuadernillo docente y del kit · impresión de expedientes Art. 9.

⚠️ **El diseño gráfico de la ficha pictográfica es una partida real y no la puede hacer cualquiera.** Es lo que hace materialmente posible la participación de Hablaarte y de los cursos pequeños, así que no es un gasto de presentación: es la condición del componente inclusivo que el formulario pregunta como campo obligatorio.

⚠️ **Lo que sigue bloqueando el presupuesto son dos números, no una decisión de diseño:** los **meses de dedicación de cada rol** y la **tasa de retención (14,5% o 10,75%)**. Con eso, el paso 7 se cierra en una sesión.

---

## 9. Lo que este plan asume y hay que confirmar

| # | Supuesto | Si resulta falso |
|---|---|---|
| 1 | Hay coordinación pedagógica | Plan B del §2: la especialista y los docentes asumen el diseño didáctico |
| 2 | La especialista está disponible dic-ago y puede identificar aves de oído en terreno | Los conteos de aves salen del plan y H2 se responde solo con líquenes, hongos y artrópodos |
| 3 | El corredor ribereño de Hablaarte tiene arbolado medible | El gradiente de Hablaarte se apoya en sus calles arboladas; el humedal queda como sitio de biodiversidad, no de dendrometría |
| 4 | Marzo-abril coincide con fructificación de macrohongos en Temuco | Los hongos vuelven a registro oportunista y H4 se declara exploratoria |
| 5 | Las tres escuelas autorizan salidas fuera del establecimiento | El muestreo se concentra en patio y entorno inmediato; baja el n y hay que declararlo |
| 5.bis | 🔴 **Hablaarte atiende también educación básica** | Si es solo parvularia (3 a 6 años), **ningún estudiante puede producir medidas numéricas**: trabajan íntegramente en nivel Explorador (fotografía, cronómetro, conteo de morfotipos, dibujo y nombrar), y el bloque de medición lo levantan docentes y equipo con los niños presentes. Hablaarte aportaría menos árboles al inventario dendrométrico y más al registro de biodiversidad. **Es honesto y replicable si se declara**; lo insostenible sería fingir dendrometría de niños de cinco años |
| 5.ter | Un árbol completo toma alrededor de 20 minutos | El orden de recorte está decidido de antemano en [`FMA_2026_SISTEMA_DE_FICHAS.md`](FMA_2026_SISTEMA_DE_FICHAS.md) §8, para no improvisar en terreno |
| 6 | El calendario escolar 2027 empieza el 1 de marzo | Se corren las semanas 13-20 en bloque, sin cambiar la estructura |

---

## 10. Estado tras este paso

| Paso | Estado |
|---|---|
| 1. Diseño científico | ✅ |
| 2. Piloto | ✅ |
| 3. Equipo | 🟡 falta coordinación pedagógica y dedicaciones |
| 4. Escuelas y alianzas | ✅ · ⬜ cartas de apoyo |
| **5. Actividades** | ✅ **este documento** |
| 6. Indicadores | ✅ científicos (diseño) + de proceso (§6 de aquí) |
| 7. Presupuesto | ⏭️ **siguiente** — solo faltan dedicaciones y retención |
| 8. Carta Gantt | ⏭️ desbloqueado — §7 de aquí es su contenido |
| 9. Textos del formulario | ⬜ 4.900 palabras |
| 10. PDF de presentación | ⬜ 7 planas |
