# Cierre de sesión · 17 de septiembre de 2026

**Observatorio Ciudadano del Arbolado Urbano de Temuco**
Sitio: https://daniaros18-glitch.github.io/arboles/ · Repositorio: `daniaros18-glitch/arboles`

> **Este es el documento para retomar.** Resume lo trabajado entre el 24 de agosto y el 17 de
> septiembre de 2026, cómo funciona hoy el sitio, qué quedó pendiente y qué se aprendió.
> Todo lo que se menciona está publicado: al cierre no quedó nada sin commitear.
>
> 🔴 **Este repositorio es público.** No escribir aquí RUT, teléfonos, direcciones ni nombres de
> representantes, ni el nombre de locales comerciales vinculados a una denuncia.

---

## 0. Fechas que vencen

| Fecha | Qué | Acción |
|---|---|---|
| 🔴 **21 sep al 2 oct 2026** | Entrevistas de preselección del Fondo FMA | Revisar el correo: no sabemos si hubo preselección. Si la hay, **máximo 10 diapositivas y 10 minutos** |
| **5 oct 2026** | Resultado del Fondo FMA | |
| **Octubre 2026** | La DMAO lleva al Concejo el listado anual de árboles patrimoniales (Art. 9) | Preguntar a la DMAO **hasta cuándo reciben propuestas vecinales** |
| **12 oct al 30 nov 2026** | Firma de convenio FMA, si se adjudica | Pedir el **segundo tramo al cierre de la Etapa 1, fines de febrero 2027**. Ver `postulaciones/FMA_2026_FLUJO_DE_CAJA.md` |

---

## 1. Qué se hizo

### 1.1 Postulación al Fondo FMA (enviada el 24-08-2026)

- Los **15 textos enviados** (no 14) están transcritos literalmente en
  `postulaciones/FMA_2026_TEXTOS_ENVIADOS.md`, con un anexo de erratas.
- 🔴 **Errata de fondo:** el título enviado quedó como *"Construcción del Observatorio Ciudadano…"* y
  dice "monitorio" por monitoreo. Contradice el criterio de no presentar el observatorio como el
  producto. Si hay entrevista, el producto es **la línea base y el sistema de monitoreo**, no el sitio.
- **Flujo de caja:** el primer tramo (50%) se agota en marzo de 2027, justo al empezar el terreno.
  Febrero concentra $1.734.130 en compras de equipamiento. La carta Gantt enviada ya marca el
  segundo tramo en la semana 12.
- **Honorarios:** las bases no ponen tope; las preguntas frecuentes solo recomiendan no destinar la
  totalidad. El presupuesto enviado es 60,2% honorarios.
- `postulaciones/entrega/` **está fuera del repositorio** (`.gitignore`): contiene el presupuesto con
  datos administrativos de la organización.

### 1.2 Sitio: el árbol como hábitat

- **Sección nueva "Un árbol nunca está solo"** (`#habitat`), en tres movimientos: lo que un árbol
  puede sostener (con dibujo por estratos), lo que sabemos y no sabemos de Temuco, y lo que vamos a
  medir con sus límites. **Contador de vida asociada en 0.**
- Intervenciones en otras secciones para que la idea atraviese el relato: pérdida, calor,
  patrimoniales, educación, justicia ambiental, metodología, objetivos (ESP·05) y marco legal.
- **Objetivo general ampliado:** incluye "la vida que ese arbolado sostiene".
- **Correcciones de honestidad:** atribución del catastro de Av. Caupolicán (Ekuwün *participó*),
  registro ciudadano de árboles pasa a *en preparación*, mediciones que no existen escritas en
  futuro, y se quitaron las menciones a denuncias "verificadas" mientras el modo es automático.

### 1.3 Sitio: limpieza y portada

- **De 20 a 15 secciones.** Se eliminó el generador de contenido para redes y la línea de tiempo de
  sensores. Se fusionaron las tres secciones de participación y las dos de metodología.
- **Transparencia** quedó solo con la huella de agua: se quitó el bloque de energía y CO₂.
- **Portada nueva: "¿Qué pasó en tu cuadra?"**. Buscas tu calle o compartes tu ubicación, el mapa
  te lleva ahí y muestra los datos de tu unidad vecinal (dosel, temperatura, área verde por
  habitante y puesto entre 36 en prioridad de plantación). Encima hay una **cortina que se arrastra**
  para comparar 2005 con 2025.
- **Peso de la portada: de 2.015 KB a 286 KB.**
- La **serie año por año** quedó **solo en el mapa interactivo** (antes estaba duplicada).

### 1.4 Datos y herramientas

- **Capa de árboles individuales:** `docs/data/arboles.geojson` (vacía), su esquema en
  `docs/recursos/ESQUEMA_ARBOLES.md` y el script `scripts/sync_arboles.py`, que acepta formulario o
  importación de terceros. Cada árbol declara su `fuente` y si es `publicable`.
- **Campo "cavidad visible"** en la ficha F1, separado del daño sanitario. Solo registra que la
  cavidad se ve, **nunca si está ocupada**.
- **Visor de documentos:** `docs/recursos/ver.html?doc=NOMBRE.md` muestra cualquier `.md` de esa
  carpeta con el diseño del sitio. El documento de fuentes tiene dirección corta: `/arboles/fuentes/`.

### 1.5 Investigación

- **Revisión de literatura** sobre el árbol urbano como hábitat: 21 referencias con DOI verificado
  contra OpenAlex. Versión de trabajo en `investigacion/`, versión pública en `docs/recursos/`.
- **Hallazgo local clave:** Muñoz-Pedreros et al. 2018 (UC Temuco) estudió aves en áreas verdes de
  Temuco, incluidos bandejones. Acceso libre.
- **Sí existe literatura chilena** sobre epífitas en árboles, pero en bosque nativo (Díaz & Sieving
  2010; Muñoz & Chacón 2003). Lo que **no encontramos** es un registro urbano árbol por árbol. La
  estrategia de búsqueda está documentada para poder sostener "no encontramos" y no "no existe".

### 1.6 Primera denuncia real en el mapa

- **Roble desmochado en la vereda frente a Hochstetter 821**, septiembre 2026 (aprox.). Con foto.
- La foto está **recortada** (sin letrero del local, número de casa ni avisos) y **sin metadatos**.
- La ficha dice que **no se sabe quién hizo la intervención**. Especie sin confirmar si nativa o
  europea; la edad de unos 200 años va como dato recibido sin verificar.

---

## 2. Cómo funciona hoy el sitio (lo que no es obvio)

### Denuncias

```
denuncia.html → Google Form → Planilla → mapa (lee la planilla EN VIVO cada 10 s)
                                       ↘ robot cada 3 h → denuncias.geojson (solo respaldo)
```

- ⚠️ **Editar `denuncias.geojson` a mano no sirve:** el mapa lee la planilla en vivo y el robot
  reescribe ese archivo desde la planilla.
- **Casos que documenta el equipo:** van en `docs/data/denuncias_equipo.geojson`, con su foto en
  `docs/data/fotos/`. El robot no toca ese archivo y el mapa lo suma siempre.
- **Fotos del formulario:** llegan por correo, no al mapa. Un formulario de Google no recibe
  archivos. Para mostrar una, hay que alojarla y poner la dirección en la columna *Foto*.
- `docs/data/config.json` está en **modo `auto`**: todo lo que llega se publica sin revisión.
- ⚠️ **Siguen visibles 5 denuncias de prueba**, entre ellas "Puducita" y "Puducita v2", al lado del
  caso real. Se ocultan escribiendo **RECHAZADA** en la columna ESTADO de la planilla.
- El **formulario de denuncias no está lanzado**: no enviar público a él desde redes todavía.

### Portada

- Buscador de direcciones: **Nominatim** (OpenStreetMap), limitado a Temuco. Lo que se escribe se
  envía a ese servicio, y el sitio lo dice.
- Ubicación: **no sale del navegador.** Se usa para saber en qué unidad vecinal está la persona.
- Unidad vecinal: punto en polígono sobre `docs/data/prioridad_uv.geojson`.
- Cortina: `mapas/urbano_ndvi_2005.png` y `urbano_ndvi_2025.png`.

### Las 15 secciones

problema · pérdida · calor · causas · explora (mapa interactivo) · patrimoniales · educación ·
justicia · **hábitat** · huella · participa (incluye el mapa de denuncias `#registro`) · metodología
(incluye `#tecnica`) · objetivos · marco legal · descargas.

---

## 3. Pendientes

### Dependen de otras personas

1. ⬜ **Enviar la solicitud por Ley de Transparencia al SERVIU** (redactada en
   `postulaciones/SOLICITUD_TRANSPARENCIA_SERVIU.md`). Confirmar antes si el proyecto de Av.
   Caupolicán es del SERVIU o de Vialidad MOP; si hay duda, enviarla a ambos. **La cifra de 146
   árboles y 88 a extraer que usa la presentación FMA no tiene documento fuente archivado.**
2. ⬜ **Pedir a la red los datos del catastro de febrero** y el permiso para publicarlos. Hasta tener
   ese permiso, entran con `publicable: false`.
3. ⬜ **Marcar RECHAZADA las 5 denuncias de prueba** en la planilla.
4. ⬜ **Estudio del Dr. Rodrigo Vargas (UFRO), 98 árboles patrimoniales:** no está publicado como
   catastro. Conseguirlo con su permiso o por transparencia.
5. ⬜ **Escribir a la UC Temuco** (equipo de Muñoz-Pedreros): puede saber si hay trabajo local no
   indexado sobre vida asociada al arbolado.
6. ⬜ **Postulación FMA:** quién asume la coordinación pedagógica, confirmación de Paula, y si
   Hablaarte atiende básica o solo parvularia.
7. ⬜ **Proyecto hermano** `github.com/MendozaVolcanic/observatorio-arbolado-temuco`: evaluar unir
   esfuerzos.

### Roble de Hochstetter 821

8. ⬜ **Confirmar la especie.** Si tiene unos 200 años es anterior a la fundación de Temuco (1881),
   y muy probablemente es un **roble nativo**. Eso lo haría candidato claro a árbol patrimonial y
   cambia el cálculo del daño en el Art. 32.
9. ⬜ **Evaluar una propuesta Art. 9** para declararlo patrimonial, antes del listado de octubre.
10. ⬜ **Correo a la DMAO** preguntando hasta cuándo reciben propuestas para ese listado.

### Técnicos, en nuestras manos

11. ⬜ **Formulario de registro de árboles.** Es lo que haría que los contadores dejen de estar en
    cero. El circuito ya está armado; falta crear el formulario de Google y conectarlo.
12. ⬜ **Capa de árboles en el mapa interactivo**, lista para cuando haya datos.
13. ⬜ **Ficha pública de cada árbol** (diseñada en `postulaciones/FMA_2026_SISTEMA_DE_FICHAS.md` §5, no
    construida).
14. ⬜ **Imagen para compartir** (`og:image`): hoy el enlace del sitio no muestra miniatura en
    WhatsApp ni en redes.
15. ⬜ Opcional: quitar a la portada el selector Calles / Satélite, lo último que comparte
    visualmente con el mapa interactivo.
16. ⬜ **Resolver las fotos del formulario** antes de lanzar las denuncias: hoy llegan por correo y
    no al mapa.
17. ⬜ **Paso a producción de las denuncias:** modo `manual` y plazo de moderación declarado.
18. ⬜ **Correo personal público:** `daniaros18@gmail.com` aparece en cuatro archivos publicados.
    Borrarlo no lo saca del historial de Git; la salida es un correo del Observatorio hacia adelante.

### Ideas que surgieron y no se implementaron

- **Carteles explicativos en árboles patrimoniales** (propuesto en redes). Tres cuidados: el Art. 6
  prohíbe clavar o amarrar cosas al árbol; "patrimonial" es una categoría legal y solo aplica a
  árboles del registro municipal; la multa de 1 a 5 UTM aplica a intervenciones no autorizadas.
  Alternativa: primero en el mapa de patrimoniales del sitio, y un cartel físico con código QR a la
  ficha del árbol más adelante.

---

## 4. Aprendizajes técnicos (para no repetir errores)

| Trampa | Cómo evitarla |
|---|---|
| `scripts/md_a_word.py` recibe `(entrada, salida)` | Convertir **de a un archivo**: con dos `.md` sobrescribe el segundo |
| La consola de Windows no imprime acentos desde Python | Usar `PYTHONIOENCODING=utf-8` o escribir a archivo |
| Leaflet usa `<section>` en su control de capas | Al contar secciones, excluir las que están dentro de `.leaflet-container` |
| `fitBounds` redondea el zoom y deja márgenes | `zoomSnap: 0` para un ajuste exacto |
| Elementos absolutos se posicionan respecto al contenedor equivocado | Envolver el mapa en su propio contenedor relativo |
| Borrar bloques de JavaScript por líneas | Verificar que cada `<script>` compile: una vez quedó un `/*` sin cerrar que desactivó 142 líneas |
| GitHub Pages sirve los `.md` como texto plano | Enlazarlos por el visor `recursos/ver.html?doc=` |
| Todo lo que está en `docs/` es público | **No enlazar documentos de trabajo**: escribir una versión pública aparte |
| El panel del navegador a veces no captura imágenes | Verificar por JavaScript (estilos computados y geometría) |
| Fotos que llegan por WhatsApp | No traen GPS: ubicar por dirección y declarar la precisión |
| Punto de dirección de OpenStreetMap | Marca el terreno, no la vereda: proyectarlo sobre la calle para ubicar un árbol |

---

## 5. Criterios editoriales que se sumaron

- **"No encontramos" no es "no existe".** Toda afirmación de ausencia lleva su estrategia de búsqueda.
- Hablar de **indicadores observables de vida asociada**, nunca de "la biodiversidad del árbol".
- **Cavidad visible no es cavidad ocupada.**
- **El protocolo no es definitivo hasta el piloto:** no publicar como método cerrado la grilla de 100
  celdas ni los 5 minutos.
- Distinguir siempre **lo que ya existe, lo que estamos preparando y lo que queremos investigar**.
- **Fotos de denuncias:** recortar letreros, números de casa, personas y patentes; publicar sin
  metadatos; nunca sugerir quién fue responsable.
- **Publicaciones en redes:** no decir "ilegal" si no se sabe quién intervino; datos recibidos (como
  la edad de un árbol) siempre en condicional.
- **Pregunta del Observatorio sobre biodiversidad:** *¿Qué características de los árboles urbanos y
  de su entorno se relacionan con la vida que pueden sostener?* La especie u origen es una
  característica candidata entre varias, no la pregunta central.

---

## 6. Dónde está cada cosa

| Documento | Para qué |
|---|---|
| **`CIERRE_SESION_2026-09-17.md`** | **Este documento. Empezar aquí** |
| `ESTADO_DEL_PROYECTO.md` | Circuito de denuncias, credenciales, resultados científicos y marco legal |
| `postulaciones/ESTADO_FMA_CIERRE_SESION.md` | Estado de la postulación FMA |
| `postulaciones/FMA_2026_TEXTOS_ENVIADOS.md` | Los 15 textos tal como se enviaron, y sus erratas |
| `postulaciones/FMA_2026_FLUJO_DE_CAJA.md` | Qué pedir en la firma del convenio |
| `postulaciones/SOLICITUD_TRANSPARENCIA_SERVIU.md` | Solicitud lista para enviar |
| `postulaciones/FMA_2026_SISTEMA_DE_FICHAS.md` | Ficha F1, incluido el campo de cavidad visible |
| `investigacion/BIODIVERSIDAD_ARBOLADO_URBANO.md` | Revisión de literatura, versión de trabajo |
| `docs/recursos/BIODIVERSIDAD_ARBOLADO_URBANO.md` | Versión pública (se lee en `/arboles/fuentes/`) |
| `docs/recursos/ESQUEMA_ARBOLES.md` | Campos de la capa de árboles |
| `docs/data/denuncias_equipo.geojson` | Casos documentados por el equipo |
| `docs/data/fotos/` | Fotos de esos casos |
