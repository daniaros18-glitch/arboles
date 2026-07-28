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

## 3. ⚠️ Modo de publicación: `auto` (sitio en construcción)

`docs/data/config.json` tiene `"modo_denuncias": "auto"`: las denuncias aparecen en el mapa
**sin aprobación previa**, ~10 segundos después de enviarse. Es lo que corresponde mientras el
sitio está en construcción y se necesita ver el circuito funcionando de punta a punta.

- Escribir **`RECHAZADA`** en la columna ESTADO oculta una denuncia en ~10 s. Es el único freno en este modo.
- Al abrir el sitio al público de verdad: cambiar a `"manual"` → solo se publica lo marcado `VERIFICADA`.
- El mapa muestra el aviso «🧪 Modo prueba» mientras esté en `auto`, para no engañar a nadie sobre qué está viendo.

⚠️ **En `auto` no hay filtro humano**: lo que alguien escriba en la descripción se publica tal cual
(incluidos datos personales de terceros, si los escribe). El nombre y contacto de quien denuncia
siguen protegidos siempre por la fórmula `QUERY` de Sheet1.

### ⚠️ Las opciones del formulario deben calzar EXACTAS con el Google Form

El `<select>` de *Tipo de situación* en `denuncia.html` envía su `value` al Google Form.
Google **rechaza** cualquier valor que no esté en su propia lista de opciones, y como el envío
va por `fetch` con `mode:'no-cors'`, **la página no se entera: la denuncia se pierde en silencio.**

Ocurrió con dos opciones (28/07/2026): el sitio mandaba «Árbol dañado (herido, quemado, con
publicidad)» y «Propuesta de árbol patrimonial (Art. 9)», y el Form solo acepta «Árbol dañado» y
«Propuesta de árbol patrimonial». Ya está corregido separando `value` (exacto) del texto visible
(explicativo). **Si se agrega o edita una opción, hay que hacerlo en los dos lados.**

Las opciones válidas hoy son: `Tala` · `Poda severa / mala poda` · `Árbol dañado` ·
`Propuesta de árbol patrimonial` · `Área verde eliminada por obra` · `Otro`.

**Confirmado en la práctica:** una denuncia enviada el 28/07/2026 con el valor viejo
(*Propuesta de árbol patrimonial (Art. 9)* — Pudú Helados, Av. Pablo Neruda 01725) **llegó por
correo pero nunca entró a la planilla**. El correo sale de `formsubmit.co`, que acepta cualquier
cosa; la planilla depende del Google Form, que valida. Por eso el aviso puede llegar y el registro
perderse igual: **el correo no es prueba de que la denuncia quedó guardada.**

Esa denuncia se recuperó a mano el 28/07/2026 y ya está en la planilla.

**Tres defensas, para que ninguna denuncia se pierda otra vez:**

1. `python scripts/verificar_opciones.py` compara las opciones del sitio con las del Google Form
   y falla si alguna no calza. Correrlo cada vez que se toque la lista, en cualquiera de los dos lados.
2. En `denuncia.html`, la constante `TIPOS_DEL_FORM` lista lo que el Form acepta. Si alguien
   selecciona algo fuera de esa lista, **se envía como `Otro` y el tipo real se guarda al principio
   de la descripción** entre corchetes. Se pierde precisión en la clasificación, nunca la denuncia.
3. Después de enviar, la página **relee la planilla publicada** hasta 60 s buscando las coordenadas
   recién enviadas. Si aparecen, confirma; si no, avisa honestamente que no pudo confirmarlo y deja
   el correo de contacto. Nadie se va con un «Gracias» falso.

### Folio y acuse de recibo (pendiente de instalar)

Escrito y probado, **falta que lo instales en la planilla** (5 minutos):
[`docs/recursos/GUIA_CORREOS_Y_FOLIO.md`](docs/recursos/GUIA_CORREOS_Y_FOLIO.md) · código en [`scripts/apps_script_denuncias.gs`](scripts/apps_script_denuncias.gs).

Un Apps Script en la planilla asigna a cada denuncia un **folio correlativo** (`TEM-2026-0001`),
te avisa por correo con todos los datos, y le manda un **acuse de recibo con el folio** a quien
denunció (si dejó correo). El sitio es estático y no puede hacer nada de esto: no tiene servidor
ni forma de saber cuál fue el último número. Por eso el folio se asigna en la planilla.

⬜ Instalar el script y su activador «Al enviarse el formulario».
⬜ Ajustar `PLAZO_REVISION` (hoy dice 5 días hábiles) al plazo que se pueda sostener de verdad.

### Aviso por correo de cada denuncia

`denuncia.html` manda cada denuncia por **dos vías**: los datos van a la planilla (Google Form) y una
copia por correo a daniaros18@gmail.com vía `formsubmit.co`. **Hasta el 28/07/2026 el correo solo se
enviaba si la persona adjuntaba foto** — por eso la denuncia del 27/07 no avisó a nadie. Ya está
corregido: el correo sale siempre, con o sin foto.

- ⬜ **Verificar que `formsubmit.co` esté activado.** La primera vez que se usa, envía un correo de
  confirmación con un enlace que hay que abrir una sola vez. Si nunca se hizo, no llegará nada.
- ⬜ **Respaldo recomendado:** activar además en el Google Form *Respuestas* → ⋮ →
  «Recibir notificaciones por correo de respuestas nuevas». No depende de terceros.

### Checklist para el paso a producción

1. ⬜ Volver a `"modo_denuncias": "manual"`.
2. ✅ Contador de pendientes en el mapa: muestra «N denuncias en revisión» (solo el número, ni ubicación ni detalle). Solo se ve en modo `manual`.
3. ⬜ **Compromiso de plazo de moderación**: definir cada cuánto se revisa la planilla (p. ej. 48 h hábiles) y decirlo en `denuncia.html`. Sin plazo declarado, «en revisión» puede durar para siempre.

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
