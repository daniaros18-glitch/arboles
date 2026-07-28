# Estado del proyecto — Observatorio del Arbolado Urbano de Temuco

**Última actualización:** 28 de julio de 2026 · Cierre de sesión de trabajo.
Este documento resume qué está funcionando, con qué credenciales, qué se aprendió y qué falta. Sirve para retomar el proyecto sin depender de la memoria de nadie.

---

## 1. Qué está funcionando hoy

🌐 **Sitio público:** https://daniaros18-glitch.github.io/arboles/
📝 **Formulario de denuncias:** https://daniaros18-glitch.github.io/arboles/denuncia.html

| Pieza | Estado |
|---|---|
| Sitio web (GitHub Pages desde `/docs`) | ✅ en línea |
| Serie satelital anual 2005–2024 con deslizador | ✅ |
| Mapa interactivo con capas (calles / satélite / satélite con nombres) | ✅ |
| Capa de calor (LST) y Dynamic World | ✅ |
| Cruce con loteos oficiales | ✅ |
| Índice de equidad de sombra por barrio | ✅ |
| Formulario de denuncias con mapa, GPS y buscador de direcciones | ✅ |
| Mapa público de denuncias con íconos por tipo y leyenda | ✅ |
| Sección de transparencia (huella hídrica de la IA) | ✅ |
| Marco legal (OCR de la Ordenanza 004/2021) | ✅ |

## 2. Cuentas y credenciales

- **GitHub:** `daniaros18-glitch/arboles` — Pages publica la carpeta `/docs`.
- **Google (daniaros18@gmail.com):** formulario, planilla de respuestas y publicación CSV.
- **Google Earth Engine:** proyecto `arbolado-urbano-502605` (Community, gratuito).

### Circuito de denuncias
```
Vecino → denuncia.html → Google Form → Planilla → (moderación) → Mapa público
```
- La planilla completa (con **Nombre** y **Contacto**) es **privada**.
- Solo se publica la hoja *Sheet1*, que mediante una fórmula `QUERY` **excluye esos dos campos**.
  ⚠️ **No borrar ni editar esa fórmula:** es lo que protege la privacidad de quien denuncia.
- La **foto** llega por correo (no se sube sola al mapa): si se quiere mostrar, hay que pegar su enlace en la columna *Foto*.

## 3. Modo de publicación: `manual` (moderado)

`docs/data/config.json` tiene `"modo_denuncias": "manual"`:
al mapa **solo llegan** las denuncias marcadas `VERIFICADA` en la columna **ESTADO** de la planilla.
La prueba con personas (27/07/2026) terminó y se cerró el modo `auto`.

- Para publicar una denuncia: escribir `VERIFICADA` en **ESTADO** → aparece en ~10 segundos.
- Escribir **`RECHAZADA`** la oculta, en cualquiera de los dos modos.
- Para volver a abrir una prueba en vivo: cambiar a `"auto"` y **acordarse de devolverlo a `"manual"` al terminar**.

⚠️ Queda pendiente **borrar de la planilla la fila de prueba** (fila 2: *León Gallo 98*, 27/07/2026 23:01). Con el modo `manual` ya no se ve en el mapa, pero sigue en la planilla.

## 4. Resultados científicos (y cómo deben citarse)

- **La cifra más fuerte:** dentro de los **344 loteos aprobados entre 2005 y 2024** se perdió **4,2 veces más verde** (44,9%) que en el resto de la ciudad (10,7%). Es evidencia directa de la relación entre expansión inmobiliaria y pérdida de arbolado.
- **Calor:** donde se perdió el dosel hay hoy **+1,4 °C** respecto de donde se mantuvo (30,8 vs 29,3 °C); 31,6 °C donde nunca hubo árboles.
- **Casco urbano:** el dosel baja de ≈252 a ≈233 ha (−8%) entre 2005 y 2025.
- ❗ **A escala de toda la comuna el balance neto no baja**, porque la periferia rural reverdece. **Nunca presentar un "% de pérdida neta comunal" como si fuera deforestación urbana.** El satélite localiza y explica el problema; no cuenta árboles individuales a 30 m de resolución.
- **Equidad:** índice por Unidad Vecinal (Censo 2024). Mayor prioridad de plantación: Estación, Alemania, Prieto Sur, Javiera Carrera Oriente, Tromen Mollulco.

## 5. Marco legal clave

**Ordenanza Municipal N°004/2021** (transcrita en `investigacion/regulacion/Ordenanza_004_2021_OCR_articulado.md`):
- **Art. 28°** — el municipio **debe** mantener un catastro forestal y una **plataforma pública que reciba aportes de los vecinos**. Esa plataforma **no existe**: este Observatorio la materializa. Es el argumento más fuerte ante el municipio y ante los fondos.
- Art. 9° (registro patrimonial por solicitud vecinal) · Art. 19° (monitoreo periódico) · Art. 25/31 (deber de denuncia; multa 1–5 UTM) · Art. 32° (valoración económica del árbol).
- A nivel nacional, el proyecto de ley de Arbolado Urbano (**Boletín 14.213-12**) **aún no es ley**.

## 6. Pendientes

1. **Borrar la fila de prueba de la planilla** (el modo ya volvió a `"manual"`).
2. Generar un **código QR** del formulario para difusión en terreno.
3. Agregar estimación de **energía y CO₂** a la sección de transparencia.
4. **Capa 2:** conteo manual de copas en un corredor piloto (guía en `docs/recursos/GUIA_CAPA2_CONTEO_MANUAL.md`). Da la cifra "había N árboles, quedan M".
5. **Postular a fondos**: FPA del Ministerio del Medio Ambiente (~$6M, convocatoria ~agosto), FNDR 8% del GORE Araucanía, ANID Ciencia Pública, fondos municipales.
   ⚠️ Casi todos exigen **personalidad jurídica sin fines de lucro con 2 años de antigüedad** → postular a través de una junta de vecinos, la ONG Verde Urbano o la UFRO.
6. **Pedir el catastro de árboles patrimoniales** por Ley de Transparencia (portaltransparencia.cl) o a la DMAO (aseo@temuco.cl). Existe un estudio del Dr. Rodrigo Vargas (UFRO) con 98 ejemplares caracterizados.
7. **Contactar el proyecto hermano**: github.com/MendozaVolcanic/observatorio-arbolado-temuco — misma iniciativa, más madura técnicamente. Fusionar esfuerzos sería lo más inteligente.
8. **Verificar** la cita "Smith & Romero 2022" (no se localizó) y la cifra de m²/hab de Temuco contra el catastro oficial del INE.
9. Aportar datos al **PLADECO 2027-2032** y a la modificación del PRC (ambos procesos abiertos).

## 7. Criterio editorial (mantener)

Honestidad radical: **rangos en vez de cifras falsas**, limitaciones siempre explícitas, cero greenwashing —incluido el impacto ambiental del propio sitio, declarado en la sección *Transparencia*.

---

## Estructura del repositorio

| Ruta | Contenido |
|---|---|
| `docs/` | Sitio web publicado (Pages) |
| `docs/denuncia.html` | Formulario de denuncias |
| `docs/data/config.json` | **Modo de publicación** (auto / manual) |
| `docs/mapas/` | Mapas generados con Earth Engine |
| `docs/recursos/` | Guías y documentos descargables |
| `scripts/sync_denuncias.py` | Robot planilla → mapa |
| `.github/workflows/` | Automatización (cada 3 h) |
| `investigacion/` | Regulación, papers, geodatos oficiales |
| `PLAN_TECNICO_SATELITAL.md` | Metodología de teledetección |
| `Observatorio_Arbolado_Temuco_GEE.ipynb` | Notebook reproducible |
