# Observatorio del Arbolado — en preparación (no publicado)

Esta carpeta guarda el sitio completo del **Observatorio Satelital y Ciudadano del Arbolado Urbano de Temuco**, que **todavía no se lanza**.

Está deliberadamente **fuera de `docs/`**, que es la única carpeta que GitHub Pages publica como sitio web. Por lo tanto, hoy **no existe ninguna dirección web que muestre el Observatorio**.

## Por qué

La primera etapa pública se acotó a la **plataforma de denuncias por tala y poda**, presentada como una iniciativa de las organizaciones socioambientales de Temuco. El Observatorio se lanzará más adelante, alimentado por los datos que esta etapa vaya reuniendo.

## Qué contiene

| Archivo | Qué es |
|---|---|
| `index.html` | El sitio completo del Observatorio: portada, análisis satelital 2005–2025, calor urbano, loteos, equidad, marco legal y transparencia |
| `mapas/` | 46 imágenes generadas con Google Earth Engine (serie anual, NDVI, LST) |
| `fuentes/` | Página de fuentes y referencias |
| `ver.html` | Visor de los documentos de `docs/recursos/` |

## Lo que NO se detuvo

El circuito de denuncias sigue funcionando y **acumulando información para el futuro Observatorio**:

- `docs/index.html` — la plataforma de denuncias (hoy es la portada del sitio)
- `docs/denuncia.html` — el formulario
- `docs/data/` — configuración, denuncias publicadas y casos documentados por el equipo
- `scripts/sync_denuncias.py` + `.github/workflows/sync-denuncias.yml` — el robot que sincroniza la planilla cada 3 horas

## Cómo reponerlo cuando llegue el lanzamiento

1. Devolver los archivos a `docs/`:
   ```
   git mv observatorio_en_preparacion/mapas    docs/mapas
   git mv observatorio_en_preparacion/fuentes  docs/fuentes
   git mv observatorio_en_preparacion/ver.html docs/recursos/ver.html
   ```
2. Decidir qué queda en la portada. Hoy `docs/index.html` es la plataforma de denuncias y `docs/mapa.html` redirige hacia ella. Si el Observatorio vuelve a ser la portada, hay que:
   - renombrar la plataforma de denuncias a `docs/mapa.html` (reemplazando la redirección),
   - poner el Observatorio como `docs/index.html`,
   - y revisar los enlaces de `docs/denuncia.html`, que hoy apuntan a `index.html`.
3. Revisar las rutas internas de `index.html`: usa `data/`, `mapas/`, `recursos/` de forma relativa, así que funcionan apenas vuelve a `docs/`.
4. Reponer en el sitio las referencias al Observatorio que se retiraron en esta etapa (hoy la plataforma se presenta solo como iniciativa de las organizaciones socioambientales).
