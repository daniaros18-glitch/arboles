# 🌳 Observatorio Satelital y Ciudadano del Arbolado Urbano de Temuco

Proyecto de investigación y ciencia ciudadana para **documentar, cuantificar y visibilizar la pérdida de arbolado urbano en Temuco**, cruzando teledetección histórica (2005–2025, Landsat/Sentinel-2) con la participación vecinal.

## Contenido del repositorio

| Archivo / carpeta | Qué es |
|---|---|
| `docs/` | **Sitio web** (GitHub Pages). `docs/index.html` es la página. |
| `docs/recursos/` | Copias descargables de los documentos y el notebook (servidas por el sitio). |
| `PLAN_TECNICO_SATELITAL.md` | Metodología de teledetección completa. |
| `Observatorio_Arbolado_Temuco_GEE.ipynb` | Notebook de Google Earth Engine (análisis reproducible). |
| `observatorio_arbolado_temuco.html` | Versión "artifact" de la página (para vista rápida). |
| `investigacion/` | Investigación: síntesis, papers, regulación (con OCR de la Ordenanza 004) y geodatos oficiales. |
| `investigacion/geodata/` | Límite urbano, áreas verdes (1.150), zonificación PRC y planos PRC01–03 (IDE Municipal de Temuco). |

## 🚀 Cómo publicar el sitio en GitHub Pages (paso a paso)

1. Crea una cuenta en [github.com](https://github.com) (si no tienes).
2. Crea un repositorio nuevo, por ejemplo `observatorio-arbolado-temuco`.
3. Sube esta carpeta al repositorio. Si usas la web de GitHub: botón **"Add file" → "Upload files"**, arrastra todo y confirma (*Commit*). Si usas la terminal:
   ```bash
   git init
   git add .
   git commit -m "Observatorio del Arbolado de Temuco"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/observatorio-arbolado-temuco.git
   git push -u origin main
   ```
4. En el repositorio: **Settings → Pages**.
5. En **"Build and deployment" → Source**, elige **"Deploy from a branch"**.
6. En **Branch**, elige `main` y la carpeta **`/docs`**. Guarda (*Save*).
7. Espera ~1 minuto. GitHub te dará la dirección pública, del tipo:
   `https://TU_USUARIO.github.io/observatorio-arbolado-temuco/`

¡Listo! Cualquiera puede visitar y usar el sitio. Cada vez que subas cambios a `docs/`, la web se actualiza sola.

> **Nota:** los planos PRC (PDF de 19–44 MB) y algunos geodatos son pesados. Si el repositorio queda muy grande, puedes dejarlos fuera de GitHub y enlazarlos desde el sitio de la Municipalidad.

## 🛰️ Cómo generar los mapas satelitales

1. Regístrate (gratis, uso de investigación) en [Google Earth Engine](https://earthengine.google.com).
2. Abre `Observatorio_Arbolado_Temuco_GEE.ipynb` en [Google Colab](https://colab.research.google.com) o en Jupyter.
3. En la celda 1, pon el ID de tu proyecto de Earth Engine.
4. Ejecuta las celdas de arriba hacia abajo. Con `TEST_MODE = True` corre una prueba rápida (2005 vs 2025 en un sector); ponlo en `False` (y `USE_OFFICIAL_BOUNDARY = True`) para el análisis completo de la ciudad.
5. Exporta los mapas (celda 11) y reemplaza los marcadores de posición de la sección **Mapas** del sitio.

## Estado

- ✅ Sitio web, plan técnico, notebook, investigación (regulación + papers), geodatos oficiales.
- ⏳ Pendiente: correr el notebook bajo una cuenta GEE para generar los mapas; conectar un formulario de denuncias ciudadanas (KoboToolbox/Google Forms).

---

*Datos oficiales: IDE Municipal de Temuco · INE · MINVU. Marco legal: Ordenanza Municipal N°004/2021.*
