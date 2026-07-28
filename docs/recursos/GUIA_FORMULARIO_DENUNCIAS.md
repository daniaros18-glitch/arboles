# Guía — Conectar el formulario de denuncias con la base de datos en GitHub

Así funciona el circuito completo del registro ciudadano:

```
Vecino/a          →  Planilla Google        →  Tú revisas          →  Robot GitHub   →  Mapa público
(denuncia.html)      (respuestas)              (ESTADO=VERIFICADA)    (cada 3 horas)    (index.html#registro)
```

**Nada se publica sin tu aprobación.** El robot solo copia las filas marcadas `VERIFICADA`.

---

## Paso 1 — Crear el formulario en Google (10 minutos)

1. Entra a [forms.google.com](https://forms.google.com) y crea un **formulario en blanco**.
2. Título: `Denuncias — Observatorio del Arbolado de Temuco`.
3. Agrega **exactamente estas preguntas, en este orden** (los nombres importan: el robot los busca por su texto):

| # | Pregunta | Tipo |
|---|---|---|
| 1 | `Tipo` | Selección múltiple: Tala · Poda severa / mala poda · Árbol dañado · Propuesta de árbol patrimonial · Área verde eliminada por obra · Otro |
| 2 | `Especie` | Respuesta corta |
| 3 | `Fecha del hecho` | Fecha |
| 4 | `Direccion` | Respuesta corta |
| 5 | `Coordenadas` | Respuesta corta |
| 6 | `Descripcion` | Párrafo |
| 7 | `Foto` | Subir archivo *(opcional; requiere que el vecino tenga sesión Google)* |
| 8 | `Nombre` | Respuesta corta |
| 9 | `Contacto` | Respuesta corta |

> Las preguntas 1, 5 y 6 conviene marcarlas **obligatorias**.

4. En **Respuestas** → botón verde de **Hoja de cálculo** → crea la planilla vinculada.

## Paso 2 — Agregar la columna de moderación

En la planilla de respuestas:
1. En la **primera columna vacía a la derecha**, escribe el encabezado **`ESTADO`**.
2. Cada denuncia nueva llega con esa celda **vacía** (= no se publica).
3. Tu trabajo de revisión: escribir en esa celda
   - **`VERIFICADA`** → se publica en el mapa,
   - **`RECHAZADA`** (o dejarla vacía) → nunca se publica.
4. Si borras el `VERIFICADA`, la denuncia **desaparece** del mapa en la siguiente sincronización.

> Consejo: usa *Datos → Validación de datos* con la lista `VERIFICADA, RECHAZADA, PENDIENTE` para elegirlo con un clic.

### Qué revisar antes de marcar VERIFICADA
- ¿La ubicación es coherente con la dirección descrita?
- ¿La foto (si hay) corresponde a lo denunciado?
- ¿La descripción evita acusar a personas por su nombre? (mejor "una empresa contratista" que un nombre propio)
- ¿No hay datos personales de terceros ni patentes visibles en la foto?

## Paso 3 — Publicar la planilla como CSV

1. En la planilla: **Archivo → Compartir → Publicar en la Web**.
2. Pestaña **Enlace** → elige la hoja de **Respuestas de formulario 1** → formato **Valores separados por comas (.csv)**.
3. Clic en **Publicar** y **copia la URL** (termina en `output=csv`).

> Publica solo esa hoja. Recuerda que quedará accesible para quien tenga el enlace: por eso el robot **descarta el nombre y el contacto** y nunca los sube al mapa.

## Paso 4 — Darle la URL al robot

1. Ve a tu repositorio → **Settings** → **Secrets and variables** → **Actions** → pestaña **Variables**.
2. **New repository variable**:
   - **Name:** `SHEET_CSV_URL`
   - **Value:** la URL del paso 3.
3. Guarda.

Listo: cada 3 horas el robot revisa la planilla y publica las verificadas. También puedes ejecutarlo al instante desde la pestaña **Actions → Sincronizar denuncias verificadas → Run workflow**.

## Paso 5 — Conectar la página de denuncia con el formulario

Para que `denuncia.html` (con su mapa y GPS) guarde directo en la planilla:

1. Abre el formulario de Google, clic derecho → **Ver código fuente de la página** (o usa la vista previa).
2. Busca la dirección de envío (`.../formResponse`) y los identificadores de cada pregunta (`entry.123456789`).
3. Pégalos en el bloque **`GFORM`** al inicio del `<script>` de `docs/denuncia.html`:

```js
const GFORM = {
  action: 'https://docs.google.com/forms/d/e/TU-ID/formResponse',
  campos: {
    tipo:'entry.111', especie:'entry.222', fecha:'entry.333', direccion:'entry.444',
    coords:'entry.555', descripcion:'entry.666', nombre:'entry.777', contacto:'entry.888'
  }
};
```

> **Mientras ese bloque esté vacío, la página sigue funcionando**: envía la denuncia por correo a daniaros18@gmail.com. No se rompe nada; solo que esas denuncias hay que pasarlas a la planilla a mano.

---

## Preguntas frecuentes

**¿Puedo revisar desde el celular?** Sí: la app de Google Sheets permite escribir `VERIFICADA` en la columna ESTADO.

**¿Y si me equivoco y publico algo incorrecto?** Borra o cambia el `VERIFICADA` en la planilla: en la siguiente sincronización desaparece del mapa.

**¿Dónde queda la base de datos?** En el propio repositorio, en `docs/data/denuncias.geojson`, con historial completo de cambios en GitHub.

**¿Se publica el nombre de quien denuncia?** No. El robot está programado para descartar nombre y contacto; solo publica tipo, fecha, dirección, descripción, foto y ubicación.

---

*Observatorio Satelital y Ciudadano del Arbolado Urbano de Temuco.*
