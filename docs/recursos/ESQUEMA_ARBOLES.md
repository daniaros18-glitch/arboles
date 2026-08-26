# Esquema de la capa de árboles del Observatorio

**Archivo que produce:** `docs/data/arboles.geojson`
**Fecha:** 25 de agosto de 2026

> **Qué resuelve este esquema.** Hoy el Observatorio solo tiene datos de satélite, que miden
> **cobertura vegetal** y no árboles. Esta capa es la primera que registra **árboles individuales**.
> Está diseñada para recibir datos de orígenes muy distintos sin mezclarlos, y para que lo que se
> levante ahora siga sirviendo si el proyecto FMA se adjudica.

---

## 1. La regla que ordena todo: cada árbol declara de dónde viene

Los datos van a llegar de al menos cuatro fuentes distintas, con calidades distintas y con derechos
distintos sobre ellas. **Mezclarlas sin etiquetar sería el mismo error que el proyecto se ha cuidado
de no cometer en los textos.**

| `fuente` | Quién lo levantó | Qué puede afirmar | Permiso para publicar |
|---|---|---|---|
| `serviu` | SERVIU Araucanía, catastro oficial del proyecto Av. Caupolicán | Especie, estado, recomendación de extracción | ✅ Documento público, vía Ley 20.285 |
| `catastro_ciudadano` | Red de organizaciones socioambientales, febrero 2026 | Especie, ubicación, perímetro, altura | 🔴 **Requiere acuerdo con la red. No es de Ekuwün** |
| `ocau` | Observatorio, terreno propio | Ficha F1 completa | ✅ Propio |
| `escuela` | Comunidades escolares, proyecto FMA | Ficha F1 completa, con control de calidad | ✅ Si se adjudica, con autorizaciones |

⚠️ **`catastro_ciudadano` no se publica hasta que la red lo autorice.** El campo existe para que el
dato pueda cargarse y trabajarse internamente, pero la capa pública filtra por `publicable`.

---

## 2. Campos

### 2.1 Identidad y procedencia

| Campo | Tipo | Obligatorio | Notas |
|---|---|---|---|
| `codigo` | texto | ✅ | `PREFIJO-NNN`, p. ej. `CAU-014`. Prefijo de 3 letras por sector. **Clave primaria** |
| `fuente` | enum | ✅ | `serviu` · `catastro_ciudadano` · `ocau` · `escuela` |
| `fuente_detalle` | texto | ✅ | Cita completa del origen, para que sea rastreable |
| `publicable` | booleano | ✅ | Si es `false`, no entra al mapa público |
| `fecha` | fecha | ✅ | `YYYY-MM-DD` del levantamiento |
| `sector` | texto | ✅ | `Av. Caupolicán` · `Los Trigales` · `Campos Deportivos` · `Hablaarte` |

### 2.2 Ubicación

| Campo | Tipo | Notas |
|---|---|---|
| *geometry* | Point | `[lon, lat]`, 6 decimales |
| `precision_gps_m` | número | Si no se conoce, `null`. **No inventar precisión** |
| `direccion` | texto | Calle y referencia, para relocalizar |

### 2.3 Identificación

| Campo | Tipo | Notas |
|---|---|---|
| `especie` | texto | Nombre científico si lo hay |
| `especie_validada_por` | texto | Vacío mientras nadie la confirme. 🔑 **Distingue lo identificado de lo validado** |
| `nombre_local` | texto | "Cómo lo llamamos". Etnobotánica |
| `nombre_mapuzugun` | texto | Campo del proyecto, obligatorio en el formulario FMA |
| `origen` | enum | `nativa` · `exotica` · `desconocido`. **Por defecto `desconocido`** |

### 2.4 Medición

| Campo | Tipo | Notas |
|---|---|---|
| `perimetro_cm` | número | Medido a 1,30 m |
| `altura_medicion_cm` | número | Normalmente 130. 🔑 **Metadato para la revisita** |
| `dap_cm` | número | **Derivado**: `perimetro_cm / π`. No se pide en terreno |
| `n_fustes` | entero | Alometría |
| `altura_m` | número | Estimada |
| `copa_ns_m`, `copa_eo_m` | número | Sombra y área foliar. Nivel técnico |
| `estado_3` | enum | `bueno` · `regular` · `malo` |
| `estado_5` | entero | 1 a 5. Nivel técnico, para el Art. 32 |
| `danos` | lista | `desmoche` · `heridas` · `pudricion` · `anillado` · `otro` |

### 2.5 Entorno

| Campo | Tipo | Notas |
|---|---|---|
| `superficie_pie` | enum | `tierra` · `pasto` · `cemento` · `adoquin` · `mixto`. Lo que el satélite no ve |
| `distancia_calzada_m` | número | Exposición |
| `cables_sobre` | booleano | Explica el desmoche |
| `arboles_cerca_10pasos` | entero | H2 a escala fina |
| `amenazas` | lista | `obra_cercana` · `tocon_vecino` · `poda_severa` · `vehiculos` · `basura` |

🔑 `tocon_vecino` es la señal de tala reciente. Vale por sí sola.

### 2.6 Biodiversidad asociada

| Campo | Tipo | Notas |
|---|---|---|
| `grupos_observados` | lista | `liquenes` · `hongos` · `musgos` · `epifitas` · `artropodos` · `aves` |
| `sin_observaciones` | booleano | 🔑 **"No vimos nada" es un dato real, no un campo vacío** |
| `liquen_celdas` | entero | De 100. Cobertura |
| `liquen_morfotipos` | entero | Riqueza |
| `cavidad_visible` | booleano | 🆕 **Estructura de hábitat, no daño.** Solo si la cavidad se ve; **nunca si está ocupada** |
| `cara_tronco_grilla` | enum | `N` · `S` · `E` · `O`. Metadato de revisita |
| `inaturalist_url` | texto | Vínculo a las observaciones con este código |

### 2.7 Registro

| Campo | Tipo | Notas |
|---|---|---|
| `fotos` | lista | URLs. Mínimo 3: completo, tronco, hoja |
| `observador` | texto | 🔴 **Nunca nombre personal.** Solo `equipo 3` o el nombre de la organización |
| `notas` | texto | Campo libre |

---

## 3. Privacidad

🔴 **Nunca entran a la capa pública:** nombres de personas, correos, teléfonos ni RUT. El script de
sincronización descarta cualquier columna que contenga esas palabras, igual que hace el de denuncias.

---

## 4. Un árbol de ejemplo

```json
{
  "type": "Feature",
  "geometry": { "type": "Point", "coordinates": [-72.598431, -38.739218] },
  "properties": {
    "codigo": "CAU-014",
    "fuente": "ocau",
    "fuente_detalle": "Observatorio Ciudadano del Arbolado Urbano de Temuco, salida de terreno",
    "publicable": true,
    "fecha": "2026-09-07",
    "sector": "Av. Caupolicán",
    "precision_gps_m": 5,
    "direccion": "Bandejón central, altura 1200",
    "especie": "Platanus x acerifolia",
    "especie_validada_por": "",
    "nombre_local": "plátano oriental",
    "nombre_mapuzugun": "",
    "origen": "exotica",
    "perimetro_cm": 108.0,
    "altura_medicion_cm": 130,
    "dap_cm": 34.4,
    "n_fustes": 1,
    "altura_m": 9,
    "estado_3": "regular",
    "danos": ["desmoche"],
    "superficie_pie": "tierra",
    "cables_sobre": true,
    "amenazas": ["obra_cercana"],
    "grupos_observados": ["liquenes", "artropodos"],
    "sin_observaciones": false,
    "fotos": [],
    "observador": "Acción Ecologista Ekuwün",
    "notas": ""
  }
}
```

---

## 5. Cómo entran los datos

Hay **dos caminos**, porque las fuentes son de naturaleza distinta.

### 5.1 Formulario, para el levantamiento propio y escolar

Mismo patrón que las denuncias, ya probado:

```
Formulario Google → Planilla → GitHub Action (cada 3 h) → sync_arboles.py → arboles.geojson → mapa
```

```bash
python scripts/sync_arboles.py --sheet "<url_csv_publicada>"
```

### 5.2 Importación puntual, para datos de terceros

El catastro del SERVIU y el de la red no vienen de un formulario: llegan como tabla o PDF. Se
convierten a CSV y se importan declarando su origen:

```bash
python scripts/sync_arboles.py --csv serviu_caupolican.csv --fuente serviu --sector "Av. Caupolicán" --fuente-detalle "SERVIU Araucanía, catastro del proyecto Mejoramiento Av. Caupolicán, obtenido por Ley 20.285 el [fecha]"
```

Las importaciones se **acumulan**: cada fuente conserva sus árboles y el script fusiona por `codigo`.

---

## 6. Lo que este esquema deliberadamente no hace

- **No estima carbono, sombra ni valor del Art. 32.** Esas son salidas calculadas, no campos de
  entrada. Se derivan después, con sus supuestos y rangos declarados.
- **No fuerza a completar todo.** Un árbol del SERVIU va a traer especie y estado y nada más. Está
  bien: el campo `fuente` dice qué se le puede pedir a cada registro.
- **No asume que el dato es válido.** `especie_validada_por` vacío significa que nadie la confirmó,
  y así debe mostrarse en la página del árbol.
