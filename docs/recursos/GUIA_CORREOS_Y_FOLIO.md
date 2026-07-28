# Acuse de recibo con folio — instalación

Esta guía activa tres cosas que hoy no existen:

1. Cada denuncia recibe un **folio correlativo** (`TEM-2026-0001`, `TEM-2026-0002`, …), escrito en la planilla.
2. **A ti** te llega un correo con todos los datos de cada denuncia, incluido el contacto de quien la hizo.
3. **A quien denunció** le llega un acuse de recibo con su folio — siempre que haya dejado un correo electrónico.

Todo corre dentro de tu cuenta de Google. No hay servidores de terceros ni costo: es la misma cuenta que ya tiene la planilla.

---

## Por qué hace falta un script

El sitio es estático (GitHub Pages): no tiene servidor propio, así que **no puede mandar correos ni llevar la cuenta de un correlativo**. La página del formulario no sabe cuántas denuncias hubo antes, y si dos personas envían a la vez, dos números generados en el navegador podrían chocar.

La planilla sí puede: Google Apps Script se ejecuta del lado de Google, ve todas las filas y manda correos con tu propia cuenta. Por eso el folio se asigna **allá** y no en el navegador.

## Instalación (una sola vez, ~5 minutos)

**1. Abre el editor de scripts**
En la planilla de respuestas: menú **Extensiones → Apps Script**.

**2. Pega el código**
Borra lo que venga por defecto (`function myFunction() {}`) y pega **todo** el contenido de
[`scripts/apps_script_denuncias.gs`](../../scripts/apps_script_denuncias.gs).
Guarda con el ícono del disquete (o Ctrl+S).

Si alguna vez cambias de correo, edita arriba del archivo la línea `var CORREO_EQUIPO = ...`.

**3. Autoriza el script**
Arriba, elige la función **`probarConLaUltimaFila`** y pulsa **Ejecutar**.

Google te va a pedir permisos y va a mostrar una advertencia de *"Google no ha verificado esta aplicación"*. Es lo esperable: la aplicación eres tú misma, recién escrita, y nadie de Google la ha revisado. Para continuar: **Configuración avanzada → Ir a (nombre del proyecto)** → **Permitir**.

Los permisos que pide son ver la planilla y enviar correo como tú. Nada más.

Al terminar, revisa tu bandeja: debería haber llegado el correo de la última denuncia de la planilla, y en la hoja debería aparecer una columna **FOLIO** al final con `TEM-2026-0001`.

**4. Deja el activador andando**
En el menú lateral, ícono del **reloj** (*Activadores*) → **Añadir activador**:

| Campo | Valor |
|---|---|
| Función | `alRecibirDenuncia` |
| Origen del evento | Desde la hoja de cálculo |
| Tipo de evento | **Al enviarse el formulario** |

Guarda. Desde ese momento, cada denuncia nueva se procesa sola.

**5. Pruébalo de verdad**
Envía una denuncia desde el sitio poniendo **tu propio correo** en el campo de contacto. Deberían llegarte **dos** correos: el aviso interno y el acuse de recibo con folio. Revisa también spam la primera vez.

---

## Cosas que conviene saber

- **El acuse solo sale si hay correo.** El campo de contacto acepta teléfono; si la persona dejó un número, se registra igual pero no hay a dónde escribirle. El formulario ahora pide el correo de forma explícita y explica para qué sirve.
- **La columna FOLIO se agrega al final** de la hoja de respuestas, para no mover las columnas existentes. Aun así, **revisa que la fórmula `QUERY` de Sheet1 siga funcionando** después de instalarlo: es la que protege la privacidad y no debe tocarse.
- **El folio no se publica** en el mapa. Si más adelante quieres que la gente pueda buscar su denuncia por folio en el sitio, hay que incluir esa columna en el `QUERY` — decisión aparte, porque cambia lo que es público.
- **Límite de Gmail: 100 correos por día** en cuentas gratuitas. Como cada denuncia manda hasta 2, el techo real son ~50 denuncias diarias. Muy por encima de lo esperable, pero conviene saberlo si alguna vez el formulario se viraliza.
- **Si borras filas de prueba, los folios no se reciclan**: el script mira el número más alto ya usado, no la cantidad de filas. Es a propósito — un folio entregado a un vecino nunca debe apuntar a otra denuncia.
- **El correo con la foto sigue llegando aparte**, por `formsubmit.co`, porque la imagen no queda en la planilla. Son dos avisos complementarios: uno trae la foto, el otro trae el folio.

## Qué dice el correo que recibe el vecino

Está escrito para no prometer lo que el Observatorio no puede cumplir. Dice explícitamente que **esto no reemplaza una denuncia formal** ante Carabineros o el Juzgado de Policía Local, y que el nombre y el contacto no se publican nunca.

Menciona un plazo de revisión (`var PLAZO_REVISION`, hoy **5 días hábiles**). Cámbialo por el plazo que de verdad puedas sostener: un plazo declarado y no cumplido daña más la confianza que no declarar ninguno.
