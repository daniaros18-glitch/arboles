# Guía — Capa 2: Conteo manual de copas (la cifra "árbol por árbol")

## Por qué esta capa
El satélite (Capa 1) mide **tendencia** de dosel a 30 m: dice *dónde y cuándo* cambió el verde, pero **no cuenta el árbol de calle individual** (a esa resolución un árbol es más chico que un píxel). La cifra irrebatible —"en esta cuadra había **N** árboles y hoy quedan **M**"— se obtiene mirando **imagen de muy alta resolución histórica** y contando copas a mano. Eso es la Capa 2.

Se hace en **corredores piloto** (no toda la ciudad): tramos emblemáticos donde la comunidad ya denunció talas. Recomendados:
- **Av. Caupolicán** (bandejón central) — el caso testigo del proyecto.
- **Eje Av. Imperial hacia Pablo Neruda** — aperturas viales.
- **Av. Olimpia u otro tramo con conteo previo de la ONG** — sirve de validación.

---

## Herramienta: Google Earth Pro (gratis)
Descarga: https://www.google.com/earth/versions/ (versión **Pro para escritorio**). Permite ver **imágenes históricas** (botón del reloj 🕐) desde ~2003 y **medir/dibujar**.

> Nota de licencia: Google Earth Pro permite **conteo/medición manual** para uso propio. **No** se puede usar su imagen para entrenar una IA ni redistribuir capturas masivamente. Para este conteo manual está bien.

---

## Paso a paso

### 1. Preparar el corredor
1. Abre Google Earth Pro y busca el tramo (ej. *"Avenida Caupolicán, Temuco"*).
2. Acércate hasta ver las copas individuales (los árboles se ven como manchas verdes redondeadas).
3. Menú **Ver → Barra lateral** para tener el panel de "Lugares".

### 2. Fijar dos fechas (antes / después)
1. Clic en el botón de **imágenes históricas** (🕐 reloj, arriba).
2. Mueve la línea de tiempo a una fecha **temprana** (ej. 2005–2008, en verano si se puede: más follaje).
3. Elige una segunda fecha **reciente** (ej. 2023–2025).
4. Anota ambas fechas exactas (aparecen abajo a la izquierda).

### 3. Contar las copas (crear un punto por árbol)
Para **cada fecha** por separado:
1. Crea una carpeta: clic derecho en "Mis lugares" → **Agregar → Carpeta**. Nómbrala p.ej. `Caupolican_2006`.
2. Con la carpeta seleccionada, usa la herramienta **Agregar marca de posición** (chincheta amarilla 📍) y pon **un punto en el centro de cada copa** del tramo. Numéralas o déjalas con el nombre por defecto.
3. Repite en la otra fecha en una carpeta `Caupolican_2024`.

> Truco: cuenta siempre en el **mismo tramo delimitado** (por ejemplo entre dos calles transversales) para que "antes" y "después" sean comparables. Mide el largo del tramo con la **regla** (Herramientas → Regla) y anótalo.

### 4. (Opcional) Medir el área de sombra perdida
Para los árboles que desaparecieron, con la herramienta **Polígono** dibuja la copa (su sombra aproximada) y Google Earth te da el **área en m²**. Suma las copas perdidas → **m² de sombra perdida** en el tramo. Es la cifra más potente para la comunidad.

### 5. Exportar a archivo (para el mapa del Observatorio)
1. Clic derecho en la carpeta → **Guardar lugar como…** → formato **KML** o **KMZ**.
2. Guarda `Caupolican_2006.kml` y `Caupolican_2024.kml`.
3. Convertir KML → GeoJSON (para el sitio web) en https://mapshaper.org (arrastra el KML → *Export → GeoJSON*), o con Python:
   ```python
   import geopandas as gpd
   gpd.read_file("Caupolican_2006.kml").to_file("caupolican_2006.geojson", driver="GeoJSON")
   ```
4. Deja los `.geojson` en `docs/data/` para sumarlos como capa de puntos al mapa interactivo.

### 6. Registrar el resultado
Anota en una tabla (una fila por corredor):

| Corredor | Tramo | Fecha antes | N° árboles antes | Fecha después | N° árboles después | Perdidos | Sombra perdida (m²) | Obra asociada |
|---|---|---|---|---|---|---|---|---|
| Caupolicán | (entre calle X e Y) | 2006 | | 2024 | | | | apertura Pablo Neruda |

### 7. Validar y cruzar
- **Validar** contra cualquier conteo de terreno existente (ej. los árboles ya documentados por la ONG). Si tu conteo en Earth Pro se acerca al de terreno, tu método es confiable.
- **Cruzar** con el **permiso de obra / loteo** responsable (ver capa de loteos del mapa, o pedir el permiso por Transparencia) para atribuir la pérdida a la obra concreta.

---

## Qué entregar al Observatorio
1. Los `.geojson` de puntos (antes/después) por corredor.
2. La tabla de la sección 6.
3. Las fechas exactas de las imágenes usadas.
4. (Si se hizo) el m² de sombra perdida.

Con eso, el equipo técnico integra la cifra "árbol por árbol" al sitio y la conecta con el mapa satelital y, vía **Art. 32 de la Ordenanza 004/2021**, con la **valoración económica** de los ejemplares perdidos.

---

*Capa 2 del Observatorio Satelital y Ciudadano del Arbolado Urbano de Temuco.*
