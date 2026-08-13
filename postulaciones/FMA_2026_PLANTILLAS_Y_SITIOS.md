# Plantillas oficiales y ubicación definitiva de los sitios

**Fecha:** 13 de agosto de 2026 · **Cierre de postulación:** 24/08/2026, 23:59 — **11 días**

---

## 1. 🔴 Problema de diseño: las tres escuelas están en el mismo estrato

Con las direcciones confirmadas, ubiqué las tres en nuestra capa de unidades vecinales. El geocodificador anterior fallaba porque la dirección de Campos Deportivos es **01055** (con cero inicial), no 1055.

| Escuela | Unidad vecinal | Dosel | LST | Prioridad |
|---|---|---|---|---|
| **Campos Deportivos** | JAVIERA CARRERA ORIENTE | **3,1%** | 31,1 °C | 80,0 |
| **Hablaarte** | VALPARAÍSO | **3,3%** | 30,4 °C | 77,5 |
| **Los Trigales** | LAS ENCINAS | **7,4%** | **33,0 °C** | 76,5 |

🟢 Las tres direcciones geocodifican dentro de Temuco urbano y **las tres coordenadas caen en unidades vecinales de alta prioridad de plantación**. Campos Deportivos aparece registrada en OpenStreetMap con su nombre completo —"Escuela Municipal Campos Deportivos, 01055, Avenida Gabriela Mistral"— así que la ubicación es firme.

### El problema

**Las tres están en el estrato de baja cobertura (3,1% – 7,4%).** No hay contraste. Y el diseño científico contemplaba dos estratos precisamente para poder contrastar.

**Qué se cae y qué se salva:**

- ✅ **H1 se salva completa** (tamaño vs. origen del árbol): se contrasta entre árboles, no entre barrios. Con 200-350 árboles hay poder de sobra.
- ✅ **H2 se salva**, porque la definí a escala de **100 m alrededor de cada árbol**, no a escala de barrio. Aun dentro de una unidad vecinal con 3% promedio hay manzanas con árboles y manzanas peladas: esa variación fina existe y es medible con nuestra capa satelital.
- ❌ **Se cae la comparación entre barrios contrastantes** — la pregunta secundaria de justicia ambiental (¿la desigualdad de dosel se traduce en desigualdad de biodiversidad?). Con las tres en el mismo estrato, no se puede responder.
- ⚠️ **Y se pierde el rango del predictor**: si todos los sitios tienen poca cobertura, no sabemos qué pasa donde sí la hay.

### La solución que propongo: un sitio de referencia, no una cuarta escuela

Mantener las tres escuelas —como pediste— y agregar **un sitio de referencia medido por el equipo técnico**, no por estudiantes. Cuesta una salida de terreno adicional y restituye el gradiente completo.

**Candidato: Cerro Ñielol.**

| Por qué | Detalle |
|---|---|
| **Es el contraste extremo** | Unidad vecinal ÑIELOL: **52,1% de dosel** y **24,4 °C** — frente a 3,1% y 31,1 °C de Javiera Carrera Oriente. **28 puntos de cobertura y casi 7 °C de diferencia dentro de la misma comuna** |
| **Es área protegida oficial** | 🟢 **Monumento Natural Cerro Ñielol**, 90 ha, fiscal, creado en 1939, Bosque Caducifolio del Llano — según el *Diagnóstico de Biodiversidad de La Araucanía* del MMA |
| **Activa una característica valorada** | Las bases valoran *"vincular el proyecto a áreas protegidas/espacios de cuidado"*. Hoy no cumplimos ese criterio; con esto sí |
| **Conecta con el instrumento regional** | El mismo diagnóstico identifica el **Sitio Prioritario Rukamanque**, colindante con Ñielol, amenazado por *"población urbana aledaña, construcción de viviendas"* |
| **Tiene sentido pedagógico** | Llevar a estudiantes de un barrio con 3% de dosel a un bosque nativo dentro de su propia ciudad es la lección del proyecto en una salida |

⚠️ **Verificar antes de comprometerlo:** Ñielol es administrado por CONAF y **hay que preguntar si se requiere autorización** para medir árboles y registrar biodiversidad dentro del Monumento Natural. Si el trámite no alcanza, el plan B es un sitio de referencia **no protegido** en una unidad vecinal de alta cobertura —COSTANERA (21,8%) o ACCESO NORTE (22,5%)—, que no requiere permiso porque es arbolado urbano común.

---

## 2. Plantilla de presupuesto (Anexo 4) — estructura exacta

**Encabezado:** nombre del proyecto · dirección · fecha de elaboración.

**Columnas:**

| ITEM | PARTIDA | UNIDAD | CANTIDAD | $ UNITARIO | SUBTOTAL | IVA 19% | RET 14,5% | TOTAL | Responsable de financiamiento |
|---|---|---|---|---|---|---|---|---|---|

La última columna distingue entre **Fondo FMA**, **terceros** y **financiamiento propio**.

**Solo hay tres ítems, y son cerrados:**

| ITEM | Qué incluye (textual de la planilla) |
|---|---|
| **1. Honorarios de equipo o asesorías** | Ejemplo dado: "Coordinador general" |
| **2. Producción** | *"Incluye traslados, montaje, arriendos y compras de equipos"* — ejemplo: pasaje de avión |
| **3. Otros** | *"Cualquier otro ítem que no pertenezca a ítems asociados a honorarios…"* |

**Cierre:** TOTAL DE PROYECTO · TOTAL A POSTULAR FONDO FMA · **firma del postulante**.

**Notas al pie de la planilla:**
1. En **pesos chilenos** y **firmado**.
2. **No es obligatorio** tener aportes propios o de terceros.
3. El formato **puede modificarse** para mayor claridad.
4. **El aporte FMA no puede superar los $6.000.000.**

### 2.1 Tres cosas que cambian el presupuesto y no habíamos considerado

**a) La retención sobre honorarios se suma al costo.** En la planilla, el TOTAL = SUBTOTAL + IVA + RETENCIÓN. O sea que pagar $1.800.000 líquidos en honorarios **cuesta más de $1.800.000** al proyecto.

⚠️ **Y hay una inconsistencia en la propia planilla:** el encabezado dice **14,5%** pero el ejemplo calcula **$193.500 sobre $1.800.000, que es 10,75%**. Son cifras distintas. Recomiendo **presupuestar con 14,5%** (lo que dice el encabezado, y el escenario más caro) y, si quieres certeza, preguntarlo por correo — aunque el período de consultas ya cerró, este es un detalle de formato, no de bases.

**b) El IVA 19% aplica a las compras.** Binoculares, lupas y huinchas entran con IVA. El precio de vitrina ya suele incluirlo, pero hay que declararlo en la columna.

**c) El ejemplo revela cómo esperan que se exprese el trabajo:** *unidad 1, cantidad 6, $300.000 unitario* = **seis meses de coordinación a $300.000 mensuales**. Es decir, honorarios expresados como **valor mensual × número de meses**, no como suma global. Conviene seguir esa forma.

---

## 3. Plantilla de carta Gantt — estructura exacta

- **Filas:** cuatro **Etapas**, cada una con actividades (Actividad 1, 2, …).
- **Columnas:** 13 meses × 4 semanas cada uno = resolución **semanal**.
- ⚠️ **Los meses de la plantilla van de JUNIO a JUNIO** — no corresponden a nuestra ventana. La planilla dice ser "referencial" y la nota 3 del presupuesto autoriza modificar el formato, así que **hay que reetiquetar los meses a diciembre 2026 – agosto 2027** (9 meses, 36 semanas).

**Las cuatro etapas calzan casi solas con lo que ya diseñamos:**

| Etapa | Meses | Qué contiene |
|---|---|---|
| **1. Preparación y formación** | dic 2026 – feb 2027 | Piloto metodológico, ficha v2, formación docente, compra de materiales, prueba de iNaturalist |
| **2. Terreno con comunidades escolares** | **mar – abr 2027** | Salidas, medición, registro de biodiversidad, submuestra de control, sitio de referencia |
| **3. Validación y análisis** | may – jul 2027 | Identificación taxonómica, control de calidad, GLMM, herbario |
| **4. Devolución e incidencia** | jul – ago 2027 | Cuadernillo docente, devolución en cada escuela, expedientes Art. 9, publicación en el observatorio |

🔑 La concentración del terreno en **marzo-abril** no es una preferencia: es la única franja con **clases y clima favorable** dentro de la ventana. Ya estaba identificado y ahora queda anclado en el Gantt.

---

## 4. Ekuwün — lo que puedo usar y lo que falta

🔵 **Lo que me diste** (tu descripción, para redactar):
> Organización socioambiental y comunitaria activa en Temuco, enfocada en **ecoeducación, vinculación con la comunidad, conservación de los ecosistemas locales y defensa del arbolado urbano**.

**Eso ya sirve para tres cosas del formulario**, y sirve bien: la defensa del arbolado urbano hace que este proyecto **no sea un desvío temático sino la continuación natural** de lo que la organización ya hace. Eso responde mejor que cualquier declaración al requisito de coherencia entre trayectoria y proyecto.

⬜ **Lo que sigue pendiente:**

| Dato | Para qué |
|---|---|
| **Nombre legal exacto** (¿"Acción Ecologista Ekuwün" es la razón social registrada?) | Encabezado de todos los documentos |
| Tipo de personalidad jurídica y año de constitución | Datos de organización |
| Representante legal | Responsable del proyecto y firma del presupuesto |
| **Dirección** de la organización | Encabezado de la planilla de presupuesto |
| **Proyectos anteriores**: nombre, año, territorio, comunidad, resultado | Experiencia previa — 350 palabras |
| Trabajo previo **con estas tres escuelas** | Experiencia con comunidades del territorio |
| ¿Ekuwün postulará otro proyecto a este fondo? | ⚠️ Solo se permite uno |

🔒 **Sobre el RUT.** Me lo diste y lo tengo para completar el formulario, pero **deliberadamente no lo escribí en este repositorio**, que es público (es el mismo que publica el sitio en GitHub Pages). Los RUT de organización no son secretos, pero no hay razón para dejarlos indexados. Lo mismo vale para teléfonos de contacto. Cuando llegue el momento de llenar el formulario lo uso desde nuestra conversación.

---

## 5. Estado y lo que sigue

| Paso | Estado |
|---|---|
| 1. Diseño científico | ✅ |
| 2. Piloto | ✅ |
| 3. Equipo | 🟡 roles definidos · ⬜ personas por confirmar |
| 4. Escuelas y alianzas | ✅ ubicadas y caracterizadas · ⬜ cartas de apoyo |
| 5. Actividades | ⏭️ **listo para hacerse** — la estructura de 4 etapas ya está |
| 6. Indicadores | 🟡 los científicos están; faltan los de proceso |
| 7. Presupuesto | ⏭️ **desbloqueado** — tengo la planilla |
| 8. Carta Gantt | ⏭️ **desbloqueado** — tengo la planilla |
| 9. Postulación | ⬜ |

**Mi propuesta de orden para los 11 días que quedan:** actividades (paso 5) y presupuesto (paso 7) juntos, porque las actividades definen las partidas; después el Gantt, que es la misma información en el tiempo; y al final los textos, que se escriben solos cuando lo anterior está decidido.

**Lo único que sigue bloqueando de verdad es el equipo**: sin saber quiénes son y cuántos meses de dedicación, el presupuesto no se puede cerrar. Todo lo demás puede avanzar en paralelo.

---

## 6. Dos decisiones que necesito de ti

1. **¿Incorporamos el sitio de referencia?** Sin él perdemos la comparación entre barrios contrastantes. Mi recomendación: sí, con Ñielol si CONAF lo permite, o un barrio de alta cobertura si no.
2. **¿Presupuestamos la retención al 14,5% o al 10,75%?** Recomiendo 14,5%: si sobra, se reasigna; si falta, hay que recortar actividades.
