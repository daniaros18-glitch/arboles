# Plan Técnico Satelital

## Observatorio Satelital y Ciudadano del Arbolado Urbano de Temuco

Cuantificación automatizada de la pérdida de cobertura arbórea urbana mediante teledetección, con cortes temporales en **2005, 2010, 2015, 2020 y 2025**.

---

## 1. Marco y zona de estudio

- **Comuna:** Temuco, Región de La Araucanía, Chile.
- **Coordenadas aproximadas:** 38.74° S, 72.60° O.
- **Área de interés (AOI):** definir un polígono del límite urbano consolidado de Temuco (radio urbano). Se recomienda usar el límite urbano del Plan Regulador Comunal o el polígono de zona urbana del INE. Guardar como `aoi_temuco.geojson`.
- **Sectores prioritarios** (validación cruzada con denuncias ciudadanas): ejes viales de **Avenida Pablo Neruda, Avenida Costanera/Imperial y Caupolicán**, bandejones centrales y áreas de expansión inmobiliaria del sector poniente y Labranza.

### Consideración climática crítica

Temuco tiene clima templado lluvioso con fuerte nubosidad gran parte del año. Esto obliga a:
1. Trabajar con **compuestos temporales** (median composites) sobre una ventana estacional, no imágenes individuales.
2. Restringir el análisis al **verano austral (diciembre–febrero / marzo)**, cuando (a) hay menos nubes y (b) las especies caducas (muy comunes en el arbolado urbano de Temuco: plátanos orientales, liquidámbar, robles) están con dosel pleno. Comparar siempre la misma ventana fenológica entre años evita confundir estacionalidad con tala real.

---

## 2. Plataforma y datos

### Plataforma recomendada: Google Earth Engine (GEE)

Acceso gratuito con fines de investigación al archivo histórico completo de Landsat y Sentinel-2, procesamiento en la nube (no requiere descargar terabytes), y API en Python (`geemap` + `earthengine-api`) o JavaScript. Alternativa 100% local: descarga desde USGS EarthExplorer / Copernicus Data Space + procesamiento con `rasterio`, `xarray`/`rioxarray` y `geopandas`.

### Sensores por corte temporal

| Año  | Sensor primario            | Resolución | Notas |
|------|----------------------------|-----------|-------|
| 2005 | Landsat 5 TM               | 30 m      | Único archivo óptico consistente disponible. |
| 2010 | Landsat 5 TM               | 30 m      | L5 operó hasta 2011/2013. |
| 2015 | Landsat 8 OLI **+ Sentinel-2** | 30 m / 10 m | S2 disponible desde jun-2015. |
| 2020 | Sentinel-2 (L2A)           | 10 m      | Mejor resolución para dosel urbano. |
| 2025 | Sentinel-2 (L2A) / Landsat 9 | 10 m / 30 m | Corte más reciente. |

> **Evitar Landsat 7 ETM+** para compuestos por el defecto SLC-off (bandas de datos faltantes desde 2003).

### La decisión metodológica clave: consistencia vs. resolución

Existe un dilema entre comparar peras con peras (misma resolución) y usar el mejor dato disponible:

- **Serie A — "consistencia" (recomendada para la métrica oficial de pérdida):** usar **Landsat a 30 m en TODOS los cortes (2005→2025)**. Landsat 5/8/9 cubre toda la serie. Garantiza que las diferencias de NDVI reflejen cambio real y no cambio de sensor/resolución. Limitación: 30 m es grueso para árboles de calle individuales; mide masas de dosel, no ejemplares.
- **Serie B — "detalle" (para 2015→2025):** usar **Sentinel-2 a 10 m** para mapas finos de los últimos 10 años, donde se aprecian árboles de bandejón y patios.

Reportar ambas y ser explícito sobre la limitación de cada una. La comparación 2005–2025 se ancla en la Serie A; los mapas "antes/después" de alta resolución de sectores puntuales usan la Serie B.

---

## 3. Flujo de procesamiento (pipeline)

Para cada uno de los 5 años:

1. **Filtrar colección** por AOI, rango de fechas (ventana verano austral, p. ej. `2005-12-01` a `2006-03-15`) y `CLOUD_COVER < 60%`.
2. **Corrección / nivel de producto:** usar reflectancia superficial (Surface Reflectance): Landsat Collection 2 L2, Sentinel-2 L2A. Aplicar factores de escala.
3. **Enmascarar nubes y sombras:** banda QA_PIXEL (Landsat) o SCL / banda de probabilidad de nube `s2cloudless` (Sentinel-2).
4. **Compuesto mediana** de todas las escenas válidas de la ventana → una imagen limpia y sin nubes por año.
5. **Calcular índices de vegetación** (sección 4).
6. **Recortar** al AOI y exportar como GeoTIFF (`ndvi_2005.tif`, …) más un mapa RGB de referencia.

Pseudocódigo GEE (Python):

```python
import ee, geemap
ee.Initialize()

aoi = ee.FeatureCollection('users/tu_usuario/aoi_temuco').geometry()

def mask_l8_sr(img):
    qa = img.select('QA_PIXEL')
    cloud = qa.bitwiseAnd(1 << 3).eq(0).And(qa.bitwiseAnd(1 << 4).eq(0))
    optical = img.select('SR_B.').multiply(2.75e-05).add(-0.2)
    return img.addBands(optical, None, True).updateMask(cloud)

def ndvi_l8(img):
    return img.normalizedDifference(['SR_B5', 'SR_B4']).rename('NDVI')

col = (ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
       .filterBounds(aoi)
       .filterDate('2020-12-01', '2021-03-15')
       .filter(ee.Filter.lt('CLOUD_COVER', 60))
       .map(mask_l8_sr))

ndvi_2020 = col.map(ndvi_l8).median().select('NDVI').clip(aoi)
```

---

## 4. Índices y detección de vegetación arbórea

### NDVI (índice base)

`NDVI = (NIR − Rojo) / (NIR + Rojo)` — Landsat 8/9: `(B5−B4)/(B5+B4)`; Sentinel-2: `(B8−B4)/(B8+B4)`.

Rangos orientativos: agua/cemento < 0.1; suelo desnudo/pavimento 0.1–0.2; pasto/vegetación rala 0.2–0.5; dosel arbóreo denso y sano 0.5–0.9.

### El problema de separar ÁRBOLES de PASTO/césped

NDVI por sí solo **no distingue un árbol de un césped o una cancha**: ambos son "verde". Estrategias, en orden de robustez:

1. **Umbral de NDVI alto + persistencia:** clasificar como dosel candidato solo píxeles con NDVI > ~0.6 que además se mantienen verdes en el compuesto de fin de verano (el pasto de secano en Temuco se agosta/seca; el árbol no). Diferenciar por comportamiento fenológico.
2. **Textura / estructura:** el dosel arbóreo tiene mayor varianza espacial local que un césped homogéneo (usar GLCM sobre NIR).
3. **Altura (la mejor señal, si hay dato):** si existe **LiDAR** de Temuco (algunos vuelos del MOP / SAF / municipio) o modelos globales de altura de dosel (p. ej. datos derivados de GEDI / ETH Global Canopy Height 10 m, 2020), cruzar NDVI alto **con altura > 2–3 m** = árbol. Esta es la vía preferente para 2020/2025.
4. **Clasificación supervisada:** entrenar un Random Forest (bandas espectrales + índices + textura) con puntos etiquetados por fotointerpretación (árbol / pasto / techo / pavimento / agua). Aquí es donde la **ciencia ciudadana valida el satélite**: las mediciones de terreno de vecinos (copa, ubicación GPS de árboles en Caupolicán, etc.) sirven como puntos de entrenamiento y validación reales.

Recomendación: para la métrica principal, **Enfoque 1 (umbral + persistencia) reforzado con altura de dosel (Enfoque 3) donde el dato exista**, y reservar la clasificación supervisada (Enfoque 4) para los sectores prioritarios de mayor detalle.

---

## 5. Detección de cambio (deforestación urbana)

Dos productos complementarios:

1. **ΔNDVI (mapa de calor de pérdida):** restar rásteres, p. ej. `ΔNDVI = NDVI_2025 − NDVI_2005`. Valores muy negativos = pérdida de verde. Se visualiza como el "mapa de calor" (rojo = pérdida, verde = ganancia/estable). Genera las comparativas "antes y después" que son la evidencia visual central del proyecto.
2. **Cambio de clase de cobertura:** clasificar cada año a máscara binaria dosel/no-dosel y cruzar clases entre años → matriz de transición (dosel→cemento, dosel→pasto, etc.). Permite **cuantificar en hectáreas y m²** cuánto dosel pasó a superficie impermeable.

**Métricas a reportar por corte y por sector:**
- Superficie de dosel (ha) y % de cobertura arbórea urbana.
- Pérdida neta y bruta de dosel entre cortes (ha y %).
- Tasa anual de pérdida.
- Mapa de puntos calientes de deforestación (hotspots) por barrio/unidad vecinal.

---

## 6. Correlación urbanización ↔ deforestación

Cruzar la capa de pérdida de dosel con capas de causa para demostrar la relación:
- **Expansión de suelo impermeable:** incremento de superficie construida (se puede derivar del mismo satélite: caída de NDVI + alza de índices de construido como NDBI, o datos de Global Human Settlement Layer / World Settlement Footprint).
- **Obras viales:** superponer trazados y fechas de aperturas (Pablo Neruda, ejes Imperial y Caupolicán) sobre los hotspots de pérdida y medir la pérdida atribuible a cada obra (buffer alrededor del eje vial).
- **Permisos de edificación / loteos:** si hay datos municipales, correlacionar temporal y espacialmente.

Producto: para cada caso documentado (p. ej. "árboles eliminados por la carretera en Av. Imperial"), extraer del ráster la **superficie exacta de dosel perdida en ese polígono**, convirtiendo la denuncia vecinal en una cifra técnica.

---

## 7. Pérdida de servicios ecosistémicos

Traducir píxeles a impacto cotidiano:

- **Sombra perdida:** el área de dosel perdida (m²) es una primera aproximación directa a la sombra perdida al mediodía.
- **Efecto en temperatura (isla de calor urbana):** usar la **banda térmica** de Landsat (Land Surface Temperature, LST) — bandas TIRS de Landsat 8/9, o ST de Collection 2 L2 — y comparar la temperatura superficial de zonas que perdieron dosel vs. zonas que lo conservan, en los mismos días de verano. Esto evidencia cuánto suben los grados en barrios que perdieron árboles.
- **Otros (estimables por área de dosel):** captura de CO₂, retención de aguas lluvia, hábitat. Usar factores estándar por m² de dosel (p. ej. i-Tree) como estimación divulgativa.

---

## 8. Integración con el Observatorio Ciudadano

El satélite y la comunidad se retroalimentan:
- Las **denuncias georreferenciadas** (foto + GPS + fecha) entran como puntos que se cruzan con el ráster de ΔNDVI para confirmar y medir el evento.
- Las **mediciones de terreno** (diámetro de tronco, diámetro de copa en Caupolicán) alimentan el entrenamiento/validación de la clasificación y calibran la relación píxel→copa real.
- El **catálogo de arbolado patrimonial** se mapea como capa de puntos a proteger, y se monitorea su entorno inmediato con las imágenes más recientes para alertar cambios.

Formato de datos ciudadanos sugerido: tabla/GeoJSON con `id, lat, lon, fecha, tipo_evento (tala/poda_severa/patrimonial), foto_url, medicion_copa_m, autor`.

---

## 9. Entregables técnicos

1. **Rásteres NDVI** por año (`ndvi_2005…2025.tif`) y mapas RGB de referencia.
2. **Máscaras de dosel** binarias por año.
3. **Mapa de calor ΔNDVI** 2005–2025 (y por quinquenios) — el producto visual estrella.
4. **Matriz de transición** y **tabla de métricas** (ha y % de dosel por año y por sector) en CSV/XLSX.
5. **Mapas "antes/después"** de sectores prioritarios (Pablo Neruda, Imperial, Caupolicán).
6. **Capa de temperatura (LST)** y análisis de correlación dosel–temperatura.
7. **Cuaderno reproducible** (`notebook.ipynb`) con todo el pipeline GEE/Python.
8. **Visor web** con las capas (opcional): `geemap`/`leafmap` o un GIS ligero para el Observatorio.

---

## 10. Stack tecnológico

| Función | Herramienta |
|---|---|
| Acceso y procesamiento satelital | Google Earth Engine (`earthengine-api`, `geemap`) |
| Análisis ráster local | `rasterio`, `rioxarray`, `xarray`, `numpy` |
| Análisis vectorial / cruces | `geopandas`, `shapely` |
| Clasificación | `scikit-learn` (Random Forest) o clasificadores nativos de GEE |
| Visualización | `matplotlib`, `leafmap`/`folium`, QGIS |
| Datos ciudadanos | GeoJSON + formulario (Kobo/ODK/Google Forms georreferenciado) |

---

## 11. Limitaciones y honestidad metodológica

- A 30 m, Landsat mide **masas de dosel, no árboles individuales**; ejemplares de calle aislados pueden quedar por debajo del píxel. Por eso la escala satelital cuantifica tendencia territorial y la escala ciudadana aporta el conteo fino.
- Diferencias de sensor y de resolución entre cortes introducen incertidumbre: se mitiga con la Serie A (Landsat homogéneo) para la comparación oficial.
- La nubosidad de Temuco limita la cantidad de escenas: los compuestos mediana la reducen pero conviene ampliar la ventana estacional si un año tiene pocas escenas válidas.
- NDVI no separa perfectamente árbol de pasto: la altura de dosel y la validación ciudadana son las salvaguardas.

---

## 12. Mejoras metodológicas incorporadas (revisión de literatura, jul-2026)

Derivadas de la revisión bibliográfica (ver `investigacion/SINTESIS_INVESTIGACION.md`; DOIs verificados en Crossref). Refinan y, en algunos puntos, reemplazan lo planteado arriba.

1. **Anclar la definición de "árbol" con ALTURA, no solo NDVI.** El problema árbol-vs-pasto (§4) se resuelve mejor cruzando NDVI alto con un modelo de altura de dosel:
   - **ETH Global Canopy Height 10 m** (Lang et al. 2023, `10.1038/s41559-023-02206-6`, OA) para el corte ~2020 → umbral de altura **>2–3 m** = árbol.
   - **Meta/WRI Canopy Height 1 m** (Tolan et al. 2024, `10.1016/j.rse.2023.113888`) como validación de detalle intraurbano.
   - **GEDI + Landsat** (Potapov et al. 2021, `10.1016/j.rse.2020.112165`) para extrapolar altura a la grilla Landsat en años sin producto directo.
2. **Homogeneizar sensores antes de comparar (30 m ↔ 10 m).** Usar el producto **HLS – Harmonized Landsat–Sentinel-2** (Claverie et al. 2018, `10.1016/j.rse.2018.09.002`) o remuestrear Sentinel-2 a 30 m para toda la Serie A. Evita que el cambio de resolución se confunda con pérdida real de dosel.
3. **Detección de cambio robusta en vez de solo ΔNDVI de 2 fechas.** Adoptar **CCDC** (Zhu & Woodcock 2014, `10.1016/j.rse.2014.01.011`) y/o **LandTrendr** (Kennedy et al. 2010, `10.1016/j.rse.2010.07.008`), ambos disponibles en GEE. Aplicación urbana directa: **Mugiraneza et al. 2020** (`10.3390/rs12182883`, OA) con matrices de trayectoria. Mantener ΔNDVI solo como capa comunicacional ("mapa de calor").
4. **Enmascarado y compuestos estándar.** **Fmask** (Zhu et al. 2015, `10.1016/j.rse.2014.12.014`) para nubes/sombra sobre Landsat y Sentinel-2, con compuestos mediana de ventana fenológica fija en **GEE** (Gorelick et al. 2017, `10.1016/j.rse.2017.06.031`, OA).
5. **Servicios ecosistémicos cuantificados.** Vincular pérdida de dosel a **LST térmica Landsat** (Weng 2009, `10.1016/j.isprsjprs.2009.03.007`; He et al. 2024, `10.1016/j.isprsjprs.2024.03.007`) y a **i-Tree Eco** (Nowak et al. 2013, `10.1007/s11252-013-0326-z`) para traducir m² de dosel a enfriamiento y captura.
6. **Referencia de método urbano casi idéntico:** Bonney et al. 2024 (`10.1016/j.ufug.2024.128490`) — dosel urbano municipal con Landsat gratuito + Random Forest.
7. **Clasificador:** Random Forest como base (Belgiu & Drăguț 2016, `10.1016/j.isprsjprs.2016.01.011`), con puntos de entrenamiento de la validación ciudadana.

## 13. Anclaje normativo y valoración económica del dosel

El proyecto no es solo técnico: se ancla en la **Ordenanza Municipal N°004/2021 de Temuco** (ver `investigacion/regulacion/Ordenanza_004_2021_OCR_articulado.md`).

- **Art. 28° — Catastro Forestal:** obliga al municipio a mantener una **plataforma pública** que cuantifique especies digitalmente y reciba aportes ciudadanos → el Observatorio interopera con (o materializa) ese mandato. Interoperar con el **IDE Municipal de Temuco** (ide-munitemuco.hub.arcgis.com) y el **Censo Comunal de Arbolado** (Art. 18°).
- **Art. 9° — Registro patrimonial por solicitud vecinal:** funcionalidad directa del Observatorio (informe con especie, ubicación, criterio y firmas).
- **Art. 19° — monitoreo periódico municipal:** el pipeline satelital + terreno es ese instrumento.
- **Art. 32° — Valoración económica de cada árbol** (útil para traducir la pérdida de dosel a dinero):

  **Vt = Vb · fd · fu · fs**, con Vb en UTM por grupo de especie y edad; **fd** (sanidad 0–100%), **fu** (ubicación: plazas 200% / calle alta visibilidad 150% / media 80% / baja 50%), **fs** (singularidad: patrimonial 500% / alto valor conservación 400% / monumento natural 700%). Grupos de especie: 1 = exóticas comunes, 2 = ornamentales/coníferas, 3 = **nativas de alto valor** (Araucaria, Nothofagus, Fitzroya, etc.).

  → **Idea de producto:** cruzar los polígonos de pérdida de dosel (ΔNDVI/CCDC) con la clasificación de especie/ubicación y aplicar Art. 32° para estimar el **costo económico de la deforestación urbana por sector u obra**, expresado en UTM/pesos. Convierte "se perdieron N m² de sombra" en "se destruyó patrimonio arbóreo valorado en X UTM".
- **Estándar de referencia:** SIEDU **10 m²/hab** (OMS 9) para reportar déficit por sector; línea base oficial = **Catastro INE de Áreas Verdes 2024**.

---

*Documento técnico del Observatorio Satelital y Ciudadano del Arbolado Urbano de Temuco. Actualizado jul-2026 con revisión bibliográfica y anclaje normativo (Ordenanza 004/2021).*
