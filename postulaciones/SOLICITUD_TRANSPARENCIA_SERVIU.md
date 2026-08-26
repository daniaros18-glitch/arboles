# Solicitud por Ley de Transparencia: catastro de arbolado de Av. Caupolicán

**Fecha:** 25 de agosto de 2026
**Para qué:** conseguir el catastro oficial del arbolado del proyecto vial de Av. Caupolicán, que hoy
se cita en la presentación enviada a Fundación Mar Adentro **sin tener el documento fuente archivado**.

---

## 1. Por qué esta solicitud vale la pena

| Razón | Detalle |
|---|---|
| **Respalda una cifra que ya usamos** | La presentación afirma que el catastro del SERVIU registra 146 árboles y recomienda extraer 88, entre ellos 20 grandes y consolidados en muy buen estado. **Ese documento no está en el repositorio.** Si lo piden en la entrevista, hoy no se puede mostrar |
| **No depende de la voluntad de nadie** | A diferencia del catastro ciudadano, este es un documento público y el órgano está obligado a entregarlo |
| **Es la primera capa de árboles del Observatorio** | Árboles individuales con especie y estado, sobre el eje que ya es el caso testigo del proyecto |
| **Permite el contraste** | Cuando llegue el catastro ciudadano, se puede comparar qué vio la comunidad y qué vio el estudio oficial sobre los mismos árboles |

---

## 2. Datos del trámite

| | |
|---|---|
| **Órgano** | SERVIU Región de La Araucanía |
| **Vía** | Portal de Transparencia, [portaltransparencia.cl](https://www.portaltransparencia.cl) |
| **Norma** | Ley 20.285 sobre Acceso a la Información Pública |
| **Plazo legal de respuesta** | 20 días hábiles, prorrogables por 10 más |
| **Costo** | Gratuito, salvo costos de reproducción |
| **Si no responden o niegan** | Amparo ante el Consejo para la Transparencia, dentro de 15 días hábiles |

⬜ **Verificar antes de enviar:** si el proyecto lo ejecuta el SERVIU o la Dirección de Vialidad del
MOP. Si es Vialidad, la misma solicitud va dirigida al MOP Araucanía. En caso de duda, **enviarla a
ambos**: no cuesta nada y el que no la tenga la deriva.

---

## 3. Texto para pegar en el portal

> **Solicitud de acceso a información pública — Ley 20.285**
>
> Junto con saludar, y en el marco de la Ley 20.285 sobre Acceso a la Información Pública, vengo en
> solicitar la siguiente información referida al proyecto de mejoramiento de Avenida Caupolicán,
> comuna de Temuco, Región de La Araucanía:
>
> 1. **Catastro o inventario del arbolado urbano** existente en el área de influencia del proyecto,
>    incluyendo para cada ejemplar: número o código identificador, especie, ubicación (dirección,
>    coordenadas o referencia en plano), diámetro o perímetro de tronco, altura, estado sanitario o
>    fitosanitario, y la recomendación técnica asociada (conservación, trasplante o extracción).
>
> 2. **El informe o estudio técnico** que fundamenta dichas recomendaciones, incluyendo la
>    metodología de evaluación empleada y la identificación del profesional o empresa que lo elaboró.
>
> 3. **Las medidas de compensación, reposición o reforestación** comprometidas por el proyecto
>    respecto del arbolado que se intervenga, con su número de ejemplares, especies y ubicación.
>
> 4. **Las autorizaciones o pronunciamientos** de la Ilustre Municipalidad de Temuco respecto de la
>    intervención del arbolado, considerando lo dispuesto en la Ordenanza Municipal N° 004/2021
>    sobre Arbolado Urbano y Áreas Verdes.
>
> Solicito que la información sea entregada **en formato digital y, cuando exista, en formato
> procesable** (planilla de cálculo, CSV o shapefile), de conformidad con lo dispuesto en la Ley
> 20.285 respecto de la entrega en la forma y por el medio requeridos.
>
> Agradezco desde ya su disposición.

---

## 4. Qué hacer cuando llegue la respuesta

1. **Archivar el documento original** en `investigacion/regulacion/`, con su fecha de obtención y el
   número de solicitud. Sin eso, la cifra de 146 y 88 sigue sin respaldo.
2. **Convertir la tabla a CSV** con los encabezados que el script reconoce: `Codigo`, `Especie`,
   `Latitud`, `Longitud` o `Coordenadas`, `Direccion`, `Perimetro`, `Altura total`,
   `Estado sanitario`, `Danos`.
3. **Importarla a la capa de árboles:**

```bash
python scripts/sync_arboles.py --csv serviu_caupolican.csv --fuente serviu --sector "Av. Caupolicán" --prefijo CAU --fuente-detalle "SERVIU Araucanía, catastro del proyecto Mejoramiento Av. Caupolicán. Obtenido por Ley 20.285, solicitud N° [folio], [fecha]"
```

4. **Corregir la cifra si no coincide.** Si el documento dice algo distinto de 146 y 88, se corrige
   en la presentación y se declara. La cifra que vale es la del documento, no la que recordamos.

---

## 5. Advertencias

⚠️ **Puede que la respuesta no traiga coordenadas.** Muchos catastros viales georreferencian por
kilometraje o por plano, no por GPS. Si llega así, los árboles igual entran a la capa pero hay que
ubicarlos después, y eso se declara en `precision_gps_m`.

⚠️ **Puede que nieguen parte de la información** alegando que es un proyecto en ejecución. Si eso
pasa, el amparo ante el Consejo para la Transparencia es gratuito y se hace en línea.

⚠️ **El catastro del SERVIU no es el catastro municipal de árboles patrimoniales.** Son documentos
distintos y el segundo sigue pendiente, como ya dice el sitio.

---

## 6. Lo que esta solicitud deliberadamente no pide

No se pide información sobre personas, ni sobre el detalle contractual de la obra. La solicitud se
limita al arbolado y a su tratamiento, que es lo que le compete al Observatorio. Pedir de más
alarga el trámite y desdibuja el propósito.
