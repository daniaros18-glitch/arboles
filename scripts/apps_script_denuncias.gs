/**
 * Observatorio Ciudadano del Arbolado Urbano de Temuco
 * Acuse de recibo con folio para las denuncias vecinales.
 *
 * Qué hace, cada vez que alguien envía el formulario:
 *   1. Asigna un FOLIO correlativo (TEM-2026-0001, TEM-2026-0002, …) y lo escribe en la planilla.
 *   2. Avisa por correo al equipo del Observatorio, con todos los datos (incluido el contacto).
 *   3. Si quien denunció dejó un correo válido, le manda un acuse de recibo con su folio.
 *
 * Instalación: ver docs/recursos/GUIA_CORREOS_Y_FOLIO.md
 *
 * Privacidad: este script corre dentro de la cuenta de Google del Observatorio y lee la
 * planilla privada. El nombre y el contacto SOLO viajan al correo del equipo; nunca se
 * escriben en la hoja publicada ni salen al mapa.
 */

// ── Configuración ────────────────────────────────────────────────────────────
var CORREO_EQUIPO = 'daniaros18@gmail.com';          // a quién le llegan las denuncias
var PREFIJO_FOLIO = 'TEM';                            // TEM-2026-0001
var NOMBRE_OBSERVATORIO = 'Observatorio Ciudadano del Arbolado Urbano de Temuco';
var URL_MAPA = 'https://daniaros18-glitch.github.io/arboles/index.html#registro';
// Plazo declarado de revisión. Cambiar aquí si se compromete otro.
var PLAZO_REVISION = '5 días hábiles';

// ── Utilidades ───────────────────────────────────────────────────────────────

/**
 * minusculas y sin tildes: para comparar encabezados sin sufrir con los acentos.
 * normalize('NFD') separa cada letra de su tilde, y el rango U+0300-U+036F
 * borra esas tildes sueltas. Sirve para que un encabezado escrito con acento
 * y otro sin acento se comparen igual.
 */
var SIN_TILDES = new RegExp('[\\u0300-\\u036f]', 'g');
function normalizar_(texto) {
  return String(texto || '').normalize('NFD').replace(SIN_TILDES, '').trim().toLowerCase();
}

/** Devuelve el índice (0-based) de la primera columna cuyo encabezado contenga alguna clave. */
function buscarColumna_(encabezados, claves) {
  for (var c = 0; c < claves.length; c++) {
    for (var i = 0; i < encabezados.length; i++) {
      if (normalizar_(encabezados[i]).indexOf(claves[c]) !== -1) return i;
    }
  }
  return -1;
}

/** ¿Es una dirección de correo con pinta de válida? (el campo Contacto acepta teléfono también) */
function esCorreo_(texto) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(String(texto || '').trim());
}

/**
 * Siguiente folio correlativo. Se calcula mirando el mayor folio ya escrito, no la
 * cantidad de filas: así no se repite aunque se borren filas de prueba.
 */
function siguienteFolio_(hoja, colFolio) {
  var anio = new Date().getFullYear();
  var ultimaFila = hoja.getLastRow();
  var mayor = 0;
  if (ultimaFila > 1) {
    var valores = hoja.getRange(2, colFolio + 1, ultimaFila - 1, 1).getValues();
    var patron = new RegExp('^' + PREFIJO_FOLIO + '-' + anio + '-(\\d+)$');
    for (var i = 0; i < valores.length; i++) {
      var m = patron.exec(String(valores[i][0] || '').trim());
      if (m && +m[1] > mayor) mayor = +m[1];
    }
  }
  var n = mayor + 1;
  return PREFIJO_FOLIO + '-' + anio + '-' + ('000' + n).slice(-4);
}

/** Asegura que exista la columna FOLIO (se agrega al final para no mover las que ya están). */
function asegurarColumnaFolio_(hoja) {
  var ancho = hoja.getLastColumn();
  var encabezados = hoja.getRange(1, 1, 1, ancho).getValues()[0];
  var i = buscarColumna_(encabezados, ['folio']);
  if (i !== -1) return i;
  hoja.getRange(1, ancho + 1).setValue('FOLIO');
  return ancho;   // 0-based del recién creado
}

// ── Disparador principal ─────────────────────────────────────────────────────

/**
 * Se ejecuta con cada respuesta del formulario.
 * Hay que instalarlo como activador "Al enviarse el formulario" (ver la guía).
 */
function alRecibirDenuncia(e) {
  var hoja = e && e.range ? e.range.getSheet()
                          : SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
  var fila = e && e.range ? e.range.getRow() : hoja.getLastRow();
  if (fila < 2) return;

  var colFolio = asegurarColumnaFolio_(hoja);
  var ancho = hoja.getLastColumn();
  var encabezados = hoja.getRange(1, 1, 1, ancho).getValues()[0];
  var valores = hoja.getRange(fila, 1, 1, ancho).getValues()[0];

  // Si ya tiene folio (reintento del activador), no se vuelve a asignar ni a avisar.
  if (String(valores[colFolio] || '').trim()) return;

  var folio = siguienteFolio_(hoja, colFolio);
  hoja.getRange(fila, colFolio + 1).setValue(folio);

  var dato = function (claves) {
    var i = buscarColumna_(encabezados, claves);
    return i === -1 ? '' : String(valores[i] || '').trim();
  };

  var d = {
    tipo:        dato(['tipo']) || 'Sin especificar',
    especie:     dato(['especie']),
    direccion:   dato(['direccion', 'referencia', 'calle']),
    coords:      dato(['coordenada', 'ubicacion', 'gps']),
    descripcion: dato(['que paso', 'descripcion', 'detalle']),
    fecha:       dato(['fecha del hecho', 'fecha']),
    nombre:      dato(['nombre']),
    contacto:    dato(['contacto', 'correo', 'email', 'telefono'])
  };

  avisarAlEquipo_(folio, d);
  if (esCorreo_(d.contacto)) acusarRecibo_(folio, d);
}

// ── Correos ──────────────────────────────────────────────────────────────────

/** Aviso interno: todo el detalle, incluido quién denunció. */
function avisarAlEquipo_(folio, d) {
  var lineas = [
    'Nueva denuncia registrada en el Observatorio.',
    '',
    'FOLIO: ' + folio,
    'Tipo: ' + d.tipo,
    'Especie: ' + (d.especie || '—'),
    'Dirección: ' + (d.direccion || '—'),
    'Coordenadas: ' + (d.coords || '—'),
    'Fecha del hecho: ' + (d.fecha || '—'),
    'Descripción: ' + (d.descripcion || '—'),
    '',
    '— Quien denuncia (NO se publica) —',
    'Nombre: ' + (d.nombre || '(no dejó nombre)'),
    'Contacto: ' + (d.contacto || '(no dejó contacto)'),
    '',
    d.coords ? 'Ver en el mapa: https://www.google.com/maps?q=' + encodeURIComponent(d.coords) : '',
    'Planilla: ' + SpreadsheetApp.getActiveSpreadsheet().getUrl(),
    '',
    'Para publicarla en el mapa: escribir VERIFICADA en la columna ESTADO.',
    'Para ocultarla: escribir RECHAZADA.'
  ];
  MailApp.sendEmail({
    to: CORREO_EQUIPO,
    subject: '[Denuncia ' + folio + '] ' + d.tipo + (d.direccion ? ' — ' + d.direccion : ''),
    body: lineas.filter(function (l) { return l !== ''; }).join('\n')
  });
}

/** Acuse de recibo a quien denunció. Sin promesas que no podamos cumplir. */
function acusarRecibo_(folio, d) {
  var cuerpo = [
    'Hola' + (d.nombre ? ' ' + d.nombre : '') + ',',
    '',
    'Recibimos tu denuncia en el ' + NOMBRE_OBSERVATORIO + '. Gracias por tomarte el tiempo:',
    'sin registros vecinales como el tuyo no hay forma de documentar lo que pasa con los árboles de la ciudad.',
    '',
    'Tu número de folio es: ' + folio,
    'Guárdalo. Si necesitas consultarnos por esta denuncia, menciónalo y podremos ubicarla.',
    '',
    '— Lo que registramos —',
    'Tipo: ' + d.tipo,
    (d.direccion ? 'Dirección: ' + d.direccion : ''),
    (d.fecha ? 'Fecha del hecho: ' + d.fecha : ''),
    (d.descripcion ? 'Descripción: ' + d.descripcion : ''),
    '',
    'Qué pasa ahora: el equipo revisa cada denuncia antes de publicarla en el mapa público,',
    'dentro de un plazo aproximado de ' + PLAZO_REVISION + '. Si se publica, la verás acá:',
    URL_MAPA,
    '',
    'Dos cosas importantes, para que no haya malentendidos:',
    '· Tu nombre y tu contacto NO se publican nunca. Solo los usamos si necesitamos preguntarte algo.',
    '· El Observatorio es una iniciativa ciudadana, no es la Municipalidad: registrar acá NO reemplaza',
    '  una denuncia formal. Si hay daño en curso, llama también a Carabineros o al Juzgado de Policía Local',
    '  (la Ordenanza Municipal 004/2021 de Temuco establece el deber de denunciar destrozos, Art. 25).',
    '',
    '— ' + NOMBRE_OBSERVATORIO,
    'Este es un correo automático; puedes responderlo si necesitas agregar algo.'
  ];
  MailApp.sendEmail({
    to: d.contacto,
    subject: 'Recibimos tu denuncia — folio ' + folio,
    body: cuerpo.filter(function (l) { return l !== ''; }).join('\n'),
    name: 'Observatorio del Arbolado de Temuco',
    replyTo: CORREO_EQUIPO
  });
}

// ── Prueba manual ────────────────────────────────────────────────────────────

/**
 * Ejecutar a mano desde el editor para comprobar que los correos salen,
 * usando la ÚLTIMA fila de la planilla. No escribe folio si ya lo tiene.
 */
function probarConLaUltimaFila() {
  var hoja = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
  alRecibirDenuncia({ range: hoja.getRange(hoja.getLastRow(), 1) });
}
