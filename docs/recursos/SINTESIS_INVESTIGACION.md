# Síntesis de Investigación

## Observatorio Satelital y Ciudadano del Arbolado Urbano de Temuco

**Fecha:** 2026-07-15 · **Método:** skill `investigacion` (guía maestra) + búsqueda propia + 3 subagentes con fronteras disjuntas.
**Verificación:** DOIs comprobados en Crossref por el agente técnico; PDFs regulatorios descargados y validados por *magic bytes* (`%PDF`).

Esta síntesis tiene tres partes: **(A) marco regulatorio** que da base legal al proyecto, **(B) literatura técnica** para mejorar la metodología, y **(C) contexto científico local** de Temuco. Cierra con un bloque de **mejoras concretas** al proyecto.

---

## A. Marco regulatorio y de planificación (Temuco / Chile)

> PDFs descargados en `investigacion/regulacion/`.

### A.1 — Ordenanza N°004/2021: la base legal directa ⭐ (OCR completado)
**"Marco Regulatorio de árboles urbanos y áreas verdes en bien nacional de uso público"**, decretada el **16/11/2021** (acuerdo Concejo 02/11/2021; firma Alcalde Roberto Neira Aburto). Deroga la Ordenanza de Ornato N°002/1991.
- Archivo: `Ordenanza_004_2021_Arbolado_Urbano_AreasVerdes_Temuco.pdf` (PDF escaneado) → **transcripción completa en `regulacion/Ordenanza_004_2021_OCR_articulado.md`** (OCR por visión, 11 pp.).
- Índice oficial: https://transparencia.temuco.cl/g_resoluciones/ordenanzas/2021/index.htm
- **Artículos clave para el proyecto:**
  - **Art. 28° — Catastro Forestal + plataforma pública** que cuantifique especies digitalmente y **reciba aportes de vecinos** → mandato legal exacto del Observatorio. ⭐
  - **Art. 9° — Registro de árboles patrimoniales** por solicitud de un grupo de vecinos (informe con especie, ubicación, criterio, firmas).
  - **Art. 18° — Censo Comunal de Arbolado Urbano** (interoperar).
  - **Art. 19° — monitoreo periódico municipal** del estado del arbolado (el pipeline satelital lo cumple).
  - **Art. 25° + 31° — deber de denuncia** (a DMAO/Carabineros/JPL) con medios probatorios; multa **1 a 5 UTM por evento**.
  - **Art. 11° — obras públicas deben reparar/reconstruir** áreas verdes destruidas (aplica a aperturas viales).
  - **Art. 32° — fórmula de valoración económica del árbol:** `Vt = Vb·fd·fu·fs` (Vb en UTM por grupo/edad; fu ubicación 50–200%; fs singularidad 400–700%). Permite **traducir la pérdida de dosel a pesos**.
- ⚠️ **Corrección de dato:** la cifra "multas hasta ~$20 millones" (prensa) es incorrecta como *multa*: el tope de infracción es **5 UTM/evento** (Art. 31). Los montos altos provienen del **cobro de derechos por daño** (Art. 32), que para un patrimonial sí puede ser elevado.

### A.2 — Plan Regulador Comunal (PRC)
Vigente desde **2010** (D.O. 02-02-2010), ordenanza actualizada a **noviembre 2015**. Define el uso de suelo "Área Verde", zonas de protección y humedales urbanos.
- Ordenanza vigente: `PRC_Temuco_Ordenanza_2015.pdf` — https://www.temuco.cl/wp-content/uploads/2022/04/MPRO-2.-Ordenanza-Actualizada-Noviembre-2015.pdf
- Diagnóstico ambiental: `PRC_Diagnostico_Cap7_Ambiental.pdf`
- Landing con planos/estudios: https://www.temuco.cl/municipio/informacion-de-interes/plan-regulador/
- **Proceso de modificación en curso** (EMPR, con Evaluación Ambiental Estratégica): descargables ZIP en la landing + sitio vivo https://prctemuco.territorio.cl/
- **Aporte:** el PRC define *dónde* debe haber área verde. Cruzar la pérdida de dosel medida por satélite contra la zonificación "Área Verde" del PRC evidencia incumplimientos y da argumento para la modificación en curso.

### A.3 — PLADECO 2020-2024
Elaborado con la **Universidad de La Frontera (UFRO)**. Eje ambiental "ciudad limpia y amigable con el medio ambiente".
- `PLADECO_Temuco_2020-2024_ResumenEjecutivo.pdf` — https://www.temuco.cl/wp-content/uploads/2022/04/RESUMEN-EJECUTIVO-PLADECO-TEMUCO-2020-2024-.pdf
- **En actualización:** PLADECO **2027-2032** ("Yo tengo un Plan para Temuco") lanzado 2025, con talleres temáticos de medio ambiente → **ventana de incidencia**: el Observatorio puede aportar datos al diagnóstico participativo.

### A.4 — SECAP Temuco 2020 (Plan de Acción para el Clima y la Energía Sostenible) ⭐
Bajo el Pacto de Alcaldes. Estrategias de mitigación y adaptación 2020-2030.
- `SECAP_Temuco_2020.pdf` — https://pactodealcaldes-la.org/wp-content/uploads/2017/10/SECAP-TEMUCO-2020.pdf
- **Aporte:** conecta directamente el arbolado con adaptación climática (isla de calor, sumideros de carbono); marco de política donde el proyecto encaja perfecto.

### A.5 — Normativa nacional aplicable
| Norma | Qué aporta | Fuente |
|---|---|---|
| **Ley 18.695 LOC Municipalidades** | Áreas verdes y ornato = función **privativa** municipal → base para exigir su mantención | bcn.cl/leychile idNorma=30077 |
| **OGUC** (art. 2.1.31) + estándar **SIEDU 10 m²/hab** (OMS 9) | Vara oficial para medir déficit por sector | minvu.gob.cl |
| **Ley 20.283 Bosque Nativo** | Protege bosque nativo en áreas verdes cedidas en urbanización | bcn.cl idNorma=274894 |
| **"Ley de Arbolado Urbano" (proyecto Senado, 2021)** | Si avanza, exigiría catastro municipal del arbolado → el Observatorio ya lo construiría | senado.cl |

### A.6 — Datos oficiales para interoperar
- **IDE Municipal de Temuco (ArcGIS Hub):** https://ide-munitemuco.hub.arcgis.com/ ⭐ — capa oficial georreferenciada con la que el proyecto **debe interoperar** (áreas verdes, límite urbano).
- **INE — Catastro de Áreas Verdes 2024:** `INE_Catastro_AreasVerdes_2024.pdf` — línea base oficial de superficie verde por comuna.
- **SIEDU / Portal de mapas INE-MINVU:** indicador m²/hab y distancia a áreas verdes.
- **IDE MINVU — geodato PRC Temuco / límite urbano:** https://ide.minvu.cl

### A.7 — Geodatos oficiales descargados (`investigacion/geodata/`)
Del IDE Municipal de Temuco (ArcGIS: `services5.arcgis.com/eRZzgPfrzSdIBqJq`), en GeoJSON EPSG:4326:
- `limite_urbano_temuco.geojson` (límite urbano oficial — **AOI del notebook**).
- `areas_verdes_temuco.geojson` (**1.150** áreas verdes del PRC — validación y m²/hab).
- `zonificacion_zonas_temuco.geojson` (608 zonas del PRC).
- `limite_comunal_temuco.geojson`; planos `PRC01–03.pdf`.
> El notebook GEE ya puede usar el límite urbano oficial (`USE_OFFICIAL_BOUNDARY = True`).

> ⚠️ **A verificar:** la cifra "~19 m²/hab" de Temuco circula en prensa (dato INE) pero depende de una definición amplia de "área verde"; confirmar contra el catastro oficial antes de citarla.

---

## B. Literatura técnica — teledetección de dosel urbano

> 15 referencias con DOI verificado en Crossref. OA = acceso abierto confirmado.

### B.1 Métodos de mapeo (índices, Random Forest, fusión L8+S2)
- **Belgiu & Drăguț (2016)** — *Random forest in remote sensing: a review.* ISPRS J. Photogramm. RS. `10.1016/j.isprsjprs.2016.01.011` — referencia canónica de RF.
- **Claverie et al. (2018)** — *The Harmonized Landsat and Sentinel-2 (HLS) surface reflectance data set.* RSE. `10.1016/j.rse.2018.09.002` — base para fusionar 30 m y 10 m coherentemente.
- **Bonney et al. (2024)** — *Mapping canopy cover for municipal forestry monitoring: free Landsat + ML.* Urban For. Urban Green. `10.1016/j.ufug.2024.128490` — **caso casi idéntico al proyecto.**

### B.2 Altura de dosel / separar árbol de pasto
- **Lang et al. (2023)** — *A high-resolution canopy height model of the Earth.* Nature Ecol. Evol. `10.1038/s41559-023-02206-6` — **OA.** ETH Global Canopy Height **10 m**.
- **Tolan et al. (2024)** — *Very high resolution canopy height maps from RGB (Meta/WRI 1 m).* RSE. `10.1016/j.rse.2023.113888` — detalle de árboles individuales.
- **Potapov et al. (2021)** — *Mapping global forest canopy height (GEDI+Landsat).* RSE. `10.1016/j.rse.2020.112165`.
- **Dubayah et al. (2020)** — *GEDI.* Sci. Remote Sens. `10.1016/j.srs.2020.100002` — **OA.**

### B.3 Detección de cambio multitemporal
- **Kennedy et al. (2010)** — *LandTrendr.* RSE. `10.1016/j.rse.2010.07.008`.
- **Zhu & Woodcock (2014)** — *CCDC — Continuous Change Detection and Classification.* RSE. `10.1016/j.rse.2014.01.011`.
- **Mugiraneza et al. (2020)** — *Urban land cover change trajectories with LandTrendr–GEE.* Remote Sensing. `10.3390/rs12182883` — **OA, aplicación urbana directa.**

### B.4 Expansión urbana, LST/isla de calor, servicios ecosistémicos
- **Weng (2009)** — *Thermal infrared RS for urban climate.* ISPRS J. `10.1016/j.isprsjprs.2009.03.007` — guía LST Landsat.
- **He et al. (2024)** — *Quantifying the impact of urban trees on land surface temperature in global cities.* ISPRS J. `10.1016/j.isprsjprs.2024.03.007` — enfriamiento del dosel vía LST.
- **Nowak et al. (2013)** — *Urban forest structure, ecosystem services (Syracuse).* Urban Ecosystems. `10.1007/s11252-013-0326-z` — protocolo tipo **i-Tree Eco**.

### B.5 Nubosidad y compuestos en GEE
- **Gorelick et al. (2017)** — *Google Earth Engine.* RSE. `10.1016/j.rse.2017.06.031` — **OA.**
- **Zhu et al. (2015)** — *Fmask (nubes/sombra) para Landsat 4-8 y Sentinel-2.* RSE. `10.1016/j.rse.2014.12.014`.

### B.6 — Papers descargados y analizados (texto completo) ✅
> PDFs en `investigacion/papers/` · fichas con parámetros en `investigacion/papers/FICHAS.md`.

| Estado | Archivo | Fuente |
|---|---|---|
| ✅ | `Lang_2022_CanopyHeightModel.pdf` | arXiv 2204.08322 (ETH Canopy Height) |
| ✅ | `Tolan_2023_VeryHighResCanopyHeight.pdf` | arXiv 2304.07213 (Meta/WRI 1 m) |
| ✅ | `Gorelick_2017_GoogleEarthEngine.pdf` | copia OA |
| ✅ | `Moreno_2024_CorredoresVerdesTemuco.pdf` | RevArq Bogotá (OA) |
| ✅ | `Sarricolea_2014_IslaCalorSantiago.pdf` | SciELO Chile |
| ✅ | `Alvarez_2018_ContaminacionAmbiental.pdf` | RICA UNAM (OA) |
| ❌ manual | Mugiraneza 2020 (MDPI) | `https://www.mdpi.com/2072-4292/12/18/2883/pdf` (MDPI bloquea curl) |
| ❌ manual | Dubayah 2020 GEDI (Elsevier gold OA) | `https://www.sciencedirect.com/science/article/pii/S2666017220300018` |
| ❌ paywall | Kennedy, Zhu&Woodcock, Belgiu, Claverie, Weng, He, Potapov, Nowak | Elsevier/Springer sin preprint OA — requieren VPN institucional |

**Mejoras extraídas del TEXTO REAL de los PDF (no del abstract):**
1. **Ponderar por bin de altura de 1 m (Lang 2022):** los productos globales saturan en 25–30 m; ponderar inverso a la frecuencia por intervalo evita subestimar copas altas al restar años.
2. **Filtrar el ~20% de píxeles más inciertos antes de detectar cambio (Lang 2022)** y usar ~10 fechas Sentinel-2/año por celda → menos falsos positivos de "pérdida" por ruido/nubes.
3. **Corregir sesgo local con GEDI/LiDAR (Tolan 2023):** ruta para desagregar el producto S2 de 10 m a árbol individual (MAE ~2.8 m con imágenes submétricas).
4. **Homogeneidad estricta por banda al fusionar Landsat+S2 en GEE (Gorelick 2017):** igual tipo de dato/resolución/proyección y composites server-side sobre tiles.
5. **Máscara topográfica + LST como variable de impacto (Sarricolea 2014):** acotar el área urbana por altitud/pendiente y traducir la pérdida de dosel a intensidad de isla de calor, cruzándola con los buffers de accesibilidad (300 m / 2 km) de Moreno 2024 para priorizar restauración.

---

## C. Contexto científico local (Temuco / Chile)

- **Fonseca Luengo, Soto Moya & Aguayo (2023)** — *Análisis espacio-temporal de las áreas verdes urbanas, temperaturas y habitantes — caso Temuco* (cap. de libro, ISBN 978-84-124962-9-1) — **vincula verde, calor e inequidad social en Temuco.**
- **Moreno, Lora-González, Galán & Zamora-Díaz (2024)** — *Corredores verdes urbanos potenciales en Temuco.* Rev. de Arquitectura (Bogotá) 26(2). DOI `10.14718/RevArq.2024.26.5503` — **OA. Metodología NDVI+conectividad replicable; barrios antiguos = mayores copas.**
- **Capelli de Steffens et al. (2001)** — *La isla de calor estival en Temuco.* Papeles de Geografía 33 — evidencia histórica de ICU.
- **Frick Raggi & Napadensky Pastene (2013)** — *Temperaturas superficiales y tejidos urbanos, Temuco–Padre Las Casas.* U. del Bío-Bío.
- **Sarricolea & Martín-Vide (2014)** — *ICU superficial con MODIS.* Rev. Geografía Norte Grande (SciELO) — referente metodológico térmico chileno.
- **Smith & Romero (2022)** — *Injusta distribución de la vegetación en Santiago.* Rev. Geografía Norte Grande (SciELO) — marco de **justicia ambiental verde**. ⚠️ **Cita NO verificada:** al intentar descargarla no se encontró el artículo con esos datos exactos; tratar como referencia tentativa hasta confirmar autor/año/revista (posible imprecisión de la búsqueda inicial). El marco de justicia ambiental verde sí está respaldado por Fonseca 2023 (Temuco) y la línea de trabajo de Romero/Smith.
- **Álvarez & Boso (2018, UFRO)** — *Contaminación del aire y estufas de leña en Temuco.* Rev. Int. Contaminación Ambiental 34(3). DOI `10.20937/rica.2018.34.03.14` — dimensión de **zona saturada MP2.5**.
- **Plan de Descontaminación Atmosférica Temuco-PLC (DS N°8, MMA)** — sustenta el arbolado como mitigación de particulado.

### Ciencia ciudadana (antecedentes replicables)
- **Red Árbol Urbano — Fundación Ciencia Ciudadana** (cienciaciudadana.cl) — antecedente nacional que impulsa la Ley de Arbolado Urbano.
- **Arbocensus (U. de los Andes, 2024)** — app con IA para censo de árboles.
- **KoboToolbox / ODK + iNaturalist** — instrumentos de captura en terreno (offline) ya usados por IDE Chile → elección instrumental justificada para el Observatorio.

**Triple presión documentada en Temuco:** isla de calor confirmada + zona saturada por leña + distribución inequitativa del verde. El arbolado es el servicio ecosistémico que mitiga las tres, pero los datos existentes son municipales, estáticos y de definición discutible → **el Observatorio llena el vacío de datos actualizados, granulares y participativos.**

---

## D. Mejoras concretas al proyecto (accionables)

**Metodología satelital**
1. **Anclar la definición de "árbol" con altura, no solo NDVI:** usar **ETH Global Canopy Height 10 m (Lang 2023)** para el corte ~2020 y Meta/WRI 1 m como validación; umbral de altura >2–3 m para excluir césped. → Resuelve el problema árbol-vs-pasto identificado en el plan técnico.
2. **Homogeneizar sensores antes de comparar:** trabajar sobre **HLS (Claverie 2018)** o remuestrear Sentinel-2 a 30 m para 2005–2025, evitando que el cambio de resolución se confunda con pérdida real.
3. **Adoptar CCDC o LandTrendr en GEE** (Zhu & Woodcock 2014; Mugiraneza 2020) en vez de solo ΔNDVI entre dos fechas → matrices de transición árbol→impermeable con mayor robustez.
4. **Estandarizar compuestos estacionales** con **Fmask (Zhu 2015)** sobre GEE (Gorelick 2017), ventana fenológica fija cada año.
5. **Cerrar con servicios ecosistémicos:** LST térmica Landsat (Weng 2009; He 2024) + **i-Tree Eco (Nowak 2013)** para cuantificar enfriamiento y captura.

**Integración normativa e institucional**
6. **Interoperar con el IDE Municipal de Temuco (ArcGIS Hub)** y el catastro INE 2024 como líneas base oficiales; reportar déficit por sector contra el estándar **SIEDU 10 m²/hab**.
7. **Anclar legalmente el Observatorio en la Ordenanza N°004/2021** (registro patrimonial + denuncias) y en la función privativa municipal (Ley 18.695).
8. **Incidir en la modificación del PRC en curso y en el PLADECO 2027-2032** aportando la evidencia del monitoreo a sus procesos participativos abiertos.

**Instrumento ciudadano**
9. **Usar KoboToolbox/ODK** para la captura en terreno (georreferenciada, offline) e **iNaturalist** para identificación de especies, siguiendo el modelo de Red Árbol Urbano / Arbocensus.

---

## Pendientes / a verificar
- [x] **OCR de la Ordenanza N°004/2021** — hecho (ver `regulacion/Ordenanza_004_2021_OCR_articulado.md`).
- [ ] Confirmar cifra oficial de m²/hab de Temuco contra el catastro INE (no citar el "~19" de prensa sin verificar).
- [ ] Descargar el estudio EMPR (ZIP) de la modificación del PRC si se requiere el diagnóstico territorial completo.
- [ ] Buscar PLADECO 2027-2032 cuando se publique el documento final.
