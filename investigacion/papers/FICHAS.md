# Fichas bibliográficas — Papers descargados (acceso abierto)

Proyecto: Observatorio de arbolado / pérdida de dosel urbano en Temuco con Landsat / Sentinel-2.
Solo se fichan PDFs efectivamente descargados y verificados (`%PDF`, >100 KB). Extractos tomados del texto real de los PDF (pdftotext -layout), no de los abstracts.

---

## 1. Lang et al. 2023 — "A high-resolution canopy height model of the Earth"
Archivo: `Lang_2022_CanopyHeightModel.pdf` (18.8 MB) · arXiv:2204.08322 (versión revista ISPRS/RSE)

**Método.** Fusión GEDI (LiDAR full-waveform, referencia dispersa) + imágenes ópticas Sentinel-2. Ensemble de 5 CNN convolucionales que producen mapa denso de altura de dosel a 10 m de GSD, con cuantificación probabilística de incertidumbre (varianza aleatórica + epistémica). Entrenamiento con supervisión dispersa: la huella GEDI se rasteriza a la grilla S2 de 10 m; la pérdida se optimiza solo en píxeles de referencia válidos.

**Parámetros / umbrales concretos.**
- Muestras de entrenamiento: parches Sentinel-2 de **15×15 píxeles** centrados en cada huella GEDI; **~600 millones** de muestras; huellas GEDI adquiridas **abril–agosto** de 2019/2020 (ventana de plena foliación).
- Reweighting de la pérdida **inversamente proporcional a la frecuencia por intervalo de altura de 1 m** para corregir el sesgo hacia dosel bajo (distribución de cola larga). Reduce la saturación de doseles altos (los productos previos saturan en **25–30 m**).
- Errores: aRMSE **7.3 m** (balanceado por intervalos de 5 m), RMSE global **6.0 m**, sesgo **+1.3 m**; contra LiDAR aéreo LVIS RMSE 7.8 m.
- Filtrado de incertidumbre: descartar el **20 % de estimaciones más inciertas** reduce el error global; recalibrar la incertidumbre **por bioma**. Inferencia con **10 fechas/año** por ubicación (redundancia inversa-varianza).

**Aplicabilidad.** Directamente reutilizable: la altura de dosel a 10 m derivada de S2 es una línea base para detectar **pérdida** de dosel comparando dos años. Copiar (a) el reweighting por intervalo de altura para no subestimar árboles altos urbanos, (b) el uso de múltiples fechas por año para tapar nubes, y (c) el filtro por incertidumbre antes de calcular diferencias interanuales, evitando falsos positivos de "pérdida".

---

## 2. Tolan et al. 2024 — "Very high resolution canopy height maps from RGB imagery..."
Archivo: `Tolan_2023_VeryHighResCanopyHeight.pdf` (21.9 MB) · arXiv:2304.07213 (aceptado en Remote Sensing of Environment) · Meta/FAIR + WRI

**Método.** Imágenes RGB de muy alta resolución (Maxar Vivid2, **~0.59 m GSD**, 2018–2020). Encoder auto-supervisado **DINOv2** (vision transformer) + decodificador denso DPT entrenado contra **LiDAR aéreo de 1 m**. Paso de post-procesamiento: red convolucional entrenada con GEDI para corregir el sesgo geográfico del LiDAR local. Mapas a resolución sub-métrica para California y São Paulo.

**Parámetros / umbrales concretos.**
- MAE **2.8 m**, ME **0.6 m** a nivel de píxel sub-métrico (mejor que los 10 m de Lang/S2).
- Los transformers modelan dependencias espaciales globales (mejor en dosel cerrado) frente al campo receptivo local/gaussiano de las CNN.
- Referencia de escala fina: en agroforestería el **70 % de árboles de sombra <3 m** y **3 % >12 m** — la resolución fija qué estrato se captura.

**Aplicabilidad.** Marco para un producto de árbol individual en Temuco si se consigue imagery submétrica (Maxar/aérea) + un vuelo LiDAR local. La estrategia clave transferible: **entrenar el decodificador con LiDAR local y refinar el sesgo con GEDI**. Útil para validar/desagregar el producto a 10 m cuando se quiere atribuir la pérdida a árboles concretos, no a píxeles.

---

## 3. Gorelick et al. 2017 — "Google Earth Engine: Planetary-scale geospatial analysis for everyone"
Archivo: `Gorelick_2017_GoogleEarthEngine.pdf` (1.2 MB) · Remote Sensing of Environment 202:18-27 (copia OA repositorio eMapR/LT-GEE)

**Método.** Descripción de la plataforma GEE: catálogo multi-petabyte "analysis-ready", co-localizado con cómputo paralelo intrínseco, API cliente + IDE web. Operadores server-side que subdividen y distribuyen el cómputo automáticamente.

**Parámetros / umbrales concretos.**
- Catálogo: archivo **Landsat completo** + archivos completos **Sentinel-1 y Sentinel-2**; se actualiza a **~6000 escenas/día**, latencia típica **~24 h**.
- Ingesta: imágenes cortadas en **tiles de 256×256** en su proyección/resolución original + pirámides de resolución reducida para acceso rápido.
- Requisito de banda: cada banda debe ser homogénea en tipo de dato, resolución y proyección. Ejemplo de filtro típico de la API: seleccionar escenas con **<70 % de cobertura de nubes**.

**Aplicabilidad.** Es la plataforma base del observatorio (el notebook del proyecto ya usa GEE). De aquí salen buenas prácticas: filtrar la colección S2/Landsat por `<70 % nubes`, trabajar con composites server-side y respetar la homogeneidad de bandas/proyección al mezclar Landsat + Sentinel-2 para series de dosel.

---

## 4. Sarricolea & Martín-Vide 2014 — "Isla de Calor Urbana de Superficie del AMS con Terra-MODIS y ACP"
Archivo: `Sarricolea_2014_IslaCalorSantiago.pdf` (3.2 MB) · Rev. Geografía Norte Grande 57:123-141 (SciELO Chile)

**Método.** **53 imágenes Terra-MODIS LST** (temperatura de superficie) para Santiago; cálculo de temperaturas de emisión, mapas de intensidad de ICUs y **Análisis de Componentes Principales (ACP)** para sintetizar patrones espaciales típicos.

**Parámetros / umbrales concretos.**
- Cuatro patrones de ACP explican el **90.6 %** de las situaciones; intensidad máxima de ICUs **>5 °C** en comunas centrales + Huechuraba/Quilicura.
- Criterios de delimitación del área de influencia climática: altitud **400–1150 m s.n.m.** y pendientes **<16.7° (30 %)** para excluir zonas no urbanizadas con insolación distinta.
- Uso de MODIS LST diario y gratuito; se asume relación estrecha ICU-aire/ICUs en horario **nocturno** (hipótesis EPA).

**Aplicabilidad.** Vincula pérdida de dosel con servicio de regulación térmica: la ICUs es la variable a la que se traduce la pérdida de arbolado. Reutilizar (a) la máscara topográfica (400–1150 m, <30 % pendiente) adaptada a Temuco para acotar el análisis urbano, y (b) el uso de LST (MODIS o el térmico de Landsat) como covariable/impacto al mapear pérdida de dosel.

---

## 5. Moreno et al. 2024 — "Corredores verdes urbanos, caso Temuco"
Archivo: `Moreno_2024_CorredoresVerdesTemuco.pdf` (2.2 MB) · Revista de Arquitectura (Bogotá) 26(2):189-204 · DOI 10.14718/RevArq.2024.26.5503

**Método.** Propuesta metodológica para identificar corredores verdes urbanos en Temuco (superficie urbana **464 km²**), conectando áreas verdes núcleo (alta densidad/diversidad vegetacional) mediante áreas verdes pequeño-medianas + ciclovías + calles peatonales.

**Parámetros / umbrales concretos.**
- Umbral de accesibilidad: la población no debería vivir a **>300 m** de un área verde; distancia de conexión entre núcleos **300 m**; distancia máxima entre áreas verdes mayores **2 km** (Rueda 2011).
- Segmentos de corredor: tramos de **100 m de longitud y 4 m de ancho**; clases de ancho de vía para scoring de seguridad: **>2.4 m / 2.0–2.4 m / <2.0 m**.

**Aplicabilidad.** Es el paper local más alineado (mismo Temuco, mismo objeto: arbolado urbano). Los umbrales de **300 m de accesibilidad** y **2 km entre núcleos** sirven para priorizar dónde la pérdida de dosel es más crítica socialmente. Cruzar el mapa de pérdida de dosel (Landsat/S2) con estos buffers para focalizar la restauración en corredores.

---

## 6. Álvarez & Boso 2018 — "Representaciones sociales de la contaminación del aire y las estufas de leña en Temuco"
Archivo: `Alvarez_2018_ContaminacionAmbiental.pdf` (0.27 MB) · Rev. Int. de Contaminación Ambiental · DOI 10.20937/rica.2018.34.03.14

**Método.** Estudio **cualitativo** (diseño descriptivo transeccional, representaciones sociales) mediante entrevistas a usuarios de estufas de leña en distintos niveles socioeconómicos de Temuco. No es teledetección.

**Parámetros / umbrales concretos.**
- Contexto cuantitativo citado: Temuco es la **3.ª ciudad más contaminada de Chile** y **2.ª en MP10**; la calefacción residencial a leña es la fuente principal de material particulado.

**Aplicabilidad.** No aporta método de detección de dosel, pero da el **marco de impacto humano**: la pérdida de dosel agrava la exposición a MP10 en una ciudad ya crítica por calefacción a leña. Útil para la sección de justificación/impacto del observatorio y para segmentar el análisis por nivel socioeconómico (equidad ambiental), no para el procesamiento satelital en sí.
