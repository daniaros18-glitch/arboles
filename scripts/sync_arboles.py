# -*- coding: utf-8 -*-
"""Construye la capa de arboles individuales del Observatorio -> docs/data/arboles.geojson

Dos caminos de entrada, porque las fuentes son de naturaleza distinta:

  1) Formulario propio o escolar (planilla Google publicada como CSV):
       python scripts/sync_arboles.py --sheet "<url_csv>"

  2) Importacion puntual de datos de terceros (SERVIU, catastro ciudadano):
       python scripts/sync_arboles.py --csv serviu.csv --fuente serviu \
           --sector "Av. Caupolican" --fuente-detalle "SERVIU Araucania, ..."

Las importaciones se ACUMULAN: cada corrida fusiona por codigo sobre lo ya publicado.
Usar --reemplazar para descartar lo anterior de esa misma fuente.

Reglas que el script hace cumplir (ver docs/recursos/ESQUEMA_ARBOLES.md):
  - Todo arbol declara su fuente. Sin fuente no entra.
  - Nunca se publican nombres de personas ni datos de contacto.
  - publicable=false no llega al mapa publico (p.ej. datos de la red sin autorizacion).
  - El DAP se deriva del perimetro; no se pide en terreno.
"""
import argparse, csv, io, json, math, os, re, sys, unicodedata
from datetime import datetime, timezone
from urllib.request import urlopen, Request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "docs", "data", "arboles.geojson")

FUENTES = ("serviu", "catastro_ciudadano", "ocau", "escuela")
PRIVADOS = ("nombre", "contacto", "correo", "email", "telefono", "rut", "cedula")

ESTADO_3 = {"bueno": "bueno", "buena": "bueno", "regular": "regular",
            "malo": "malo", "mala": "malo", "muerto": "malo"}
SUPERFICIES = ("tierra", "pasto", "cemento", "adoquin", "mixto")
GRUPOS = ("liquenes", "hongos", "musgos", "epifitas", "artropodos", "aves")
AMENAZAS = ("obra_cercana", "tocon_vecino", "poda_severa", "vehiculos", "basura")
DANOS = ("desmoche", "heridas", "pudricion", "anillado", "otro")


# ---------------------------------------------------------------- utilidades

def limpiar(texto):
    """minusculas, sin acentos, sin espacios extra - para comparar encabezados."""
    t = unicodedata.normalize("NFKD", str(texto or "")).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", t).strip().lower()


def buscar_columna(encabezados, *claves):
    for clave in claves:
        for h in encabezados:
            if clave in limpiar(h):
                return h
    return None


def a_numero(valor):
    """Devuelve float o None. Acepta coma decimal y unidades pegadas ('108,5 cm')."""
    m = re.search(r"-?\d+(?:[.,]\d+)?", str(valor or ""))
    if not m:
        return None
    try:
        return float(m.group(0).replace(",", "."))
    except ValueError:
        return None


def a_entero(valor):
    n = a_numero(valor)
    return int(round(n)) if n is not None else None


def a_booleano(valor):
    v = limpiar(valor)
    if v in ("si", "s", "true", "verdadero", "1", "x", "sí"):
        return True
    if v in ("no", "n", "false", "falso", "0", ""):
        return False
    return None


def parsear_coords(texto):
    """Acepta '-38.7359, -72.5904'. Devuelve (lat, lon) o None."""
    nums = re.findall(r"-?\d+[.,]\d+", str(texto or ""))
    if len(nums) < 2:
        return None
    try:
        lat = float(nums[0].replace(",", "."))
        lon = float(nums[1].replace(",", "."))
    except ValueError:
        return None
    if not (-56 < lat < -17 and -76 < lon < -66):   # Chile continental
        return None
    return lat, lon


def normalizar_fecha(valor):
    v = str(valor or "").strip()
    if not v:
        return ""
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y", "%m/%d/%Y",
                "%d-%m-%Y %H:%M:%S", "%d/%m/%Y %H:%M:%S", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(v, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return v


def lista_desde(valor, permitidos):
    """Convierte 'Desmoche, heridas' en ['desmoche','heridas'], solo valores del vocabulario."""
    if not valor:
        return []
    crudo = re.split(r"[;,/|]", str(valor))
    salida = []
    for parte in crudo:
        p = limpiar(parte).replace(" ", "_")
        for permitido in permitidos:
            if permitido in p or p in permitido:
                if permitido not in salida:
                    salida.append(permitido)
                break
    return salida


def descargar_csv(url):
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 (ObservatorioArbolado)"})
    with urlopen(req, timeout=90) as r:
        return r.read().decode("utf-8-sig", errors="replace")


# ------------------------------------------------------------------ parseo

def fila_a_arbol(fila, col, args, n):
    """Convierte una fila del CSV en un Feature. Devuelve None si no es utilizable."""
    def val(clave):
        c = col.get(clave)
        return (fila.get(c) or "").strip() if c else ""

    # --- coordenadas: sin ubicacion el arbol no sirve para un catastro ---
    coords = parsear_coords(val("coords"))
    if not coords:
        lat, lon = a_numero(val("lat")), a_numero(val("lon"))
        coords = (lat, lon) if (lat is not None and lon is not None) else None
    if not coords:
        return None, "sin coordenadas validas"
    lat, lon = coords

    # --- codigo: si la fuente no trae uno, se genera correlativo por sector ---
    prefijo = (args.prefijo or (args.sector or "ARB")[:3]).upper()
    prefijo = re.sub(r"[^A-Z]", "", unicodedata.normalize("NFKD", prefijo)
                     .encode("ascii", "ignore").decode()) or "ARB"
    codigo = val("codigo").upper().replace(" ", "")
    if not codigo:
        codigo = f"{prefijo}-{n:03d}"
    elif re.fullmatch(r"\d+", codigo):
        # la fuente numera 1, 2, 3... -> se le antepone el prefijo del sector
        codigo = f"{prefijo}-{int(codigo):03d}"

    perimetro = a_numero(val("perimetro"))
    dap = round(perimetro / math.pi, 1) if perimetro else None

    props = {
        "codigo": codigo,
        "fuente": args.fuente,
        "fuente_detalle": args.fuente_detalle,
        "publicable": not args.no_publicable,
        "fecha": normalizar_fecha(val("fecha")) or args.fecha or "",
        "sector": val("sector") or args.sector or "",

        "precision_gps_m": a_numero(val("precision")),
        "direccion": val("direccion"),

        "especie": val("especie"),
        "especie_validada_por": val("validada"),
        "nombre_local": val("nombre_local"),
        "nombre_mapuzugun": val("mapuzugun"),
        "origen": limpiar(val("origen")) if limpiar(val("origen")) in
                  ("nativa", "exotica", "desconocido") else "desconocido",

        "perimetro_cm": perimetro,
        "altura_medicion_cm": a_numero(val("altura_medicion")) or (130 if perimetro else None),
        "dap_cm": dap,
        "n_fustes": a_entero(val("fustes")),
        "altura_m": a_numero(val("altura")),
        "copa_ns_m": a_numero(val("copa_ns")),
        "copa_eo_m": a_numero(val("copa_eo")),
        "estado_3": ESTADO_3.get(limpiar(val("estado_3")), ""),
        "estado_5": a_entero(val("estado_5")),
        "danos": lista_desde(val("danos"), DANOS),

        "superficie_pie": next((s for s in SUPERFICIES if s in limpiar(val("superficie"))), ""),
        "distancia_calzada_m": a_numero(val("distancia_calzada")),
        "cables_sobre": a_booleano(val("cables")),
        "arboles_cerca_10pasos": a_entero(val("arboles_cerca")),
        "amenazas": lista_desde(val("amenazas"), AMENAZAS),

        "grupos_observados": lista_desde(val("grupos"), GRUPOS),
        "sin_observaciones": a_booleano(val("sin_observaciones")) or False,
        # estructura de habitat, distinta del dano sanitario del bloque B.
        # Solo registra que la cavidad se ve; NUNCA si esta ocupada.
        "cavidad_visible": a_booleano(val("cavidad")),
        "liquen_celdas": a_entero(val("liquen_celdas")),
        "liquen_morfotipos": a_entero(val("liquen_morfotipos")),
        "cara_tronco_grilla": (val("cara_tronco")[:1].upper()
                               if val("cara_tronco")[:1].upper() in "NSEO" else ""),
        "inaturalist_url": val("inaturalist"),

        "fotos": [u.strip() for u in re.split(r"[,\s]+", val("fotos")) if u.strip().startswith("http")],
        "observador": val("observador"),
        "notas": val("notas"),
    }

    # "no vimos nada" es un dato real: si no hay grupos y nadie lo marco, queda explicito
    if not props["grupos_observados"] and not props["sin_observaciones"]:
        props["sin_observaciones"] = None    # None = no se pregunto, distinto de False

    # Blindaje de privacidad. El esquema se arma campo por campo mas arriba, asi que aqui
    # solo hay que limpiar lo que puede traer datos personales escritos a mano.
    # OJO: no filtrar por la palabra "nombre". nombre_local y nombre_mapuzugun son
    # campos legitimos de etnobotania y el filtro anterior los estaba borrando.
    for campo in ("observador", "notas", "direccion"):
        v = props.get(campo) or ""
        v = re.sub(r"\b[\w.+-]+@[\w-]+\.[\w.]+\b", "", v)                  # correos
        v = re.sub(r"\b(?:\+?56)?\s?9[\s.-]?\d{4}[\s.-]?\d{4}\b", "", v)   # telefonos
        v = re.sub(r"\b\d{1,2}\.\d{3}\.\d{3}-[\dkK]\b", "", v)             # RUT
        props[campo] = re.sub(r"\s{2,}", " ", v).strip()

    return {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [round(lon, 6), round(lat, 6)]},
        "properties": props,
    }, None


def construir(texto_csv, args):
    filas = list(csv.DictReader(io.StringIO(texto_csv)))
    if not filas:
        return [], 0, []

    enc = list(filas[0].keys())
    col = {
        "codigo": buscar_columna(enc, "codigo", "id arbol", "n arbol"),
        "coords": buscar_columna(enc, "coordenada", "ubicacion", "gps"),
        "lat": buscar_columna(enc, "latitud", "lat"),
        "lon": buscar_columna(enc, "longitud", "lon"),
        "precision": buscar_columna(enc, "precision"),
        "direccion": buscar_columna(enc, "direccion", "calle", "referencia"),
        "sector": buscar_columna(enc, "sector", "barrio"),
        "fecha": buscar_columna(enc, "fecha"),
        "especie": buscar_columna(enc, "especie", "nombre cientifico"),
        "validada": buscar_columna(enc, "validada", "confirmada"),
        "nombre_local": buscar_columna(enc, "lo llamamos", "nombre local", "nombre comun"),
        "mapuzugun": buscar_columna(enc, "mapuzugun", "mapudungun"),
        "origen": buscar_columna(enc, "origen", "nativa"),
        "perimetro": buscar_columna(enc, "perimetro", "circunferencia"),
        "altura_medicion": buscar_columna(enc, "altura de medicion"),
        "fustes": buscar_columna(enc, "fuste"),
        "altura": buscar_columna(enc, "altura total", "altura"),
        "copa_ns": buscar_columna(enc, "copa n", "copa norte"),
        "copa_eo": buscar_columna(enc, "copa e", "copa este"),
        "estado_3": buscar_columna(enc, "estado sanitario", "estado"),
        "estado_5": buscar_columna(enc, "estado 5", "clase"),
        "danos": buscar_columna(enc, "dano", "daos"),
        "superficie": buscar_columna(enc, "superficie", "al pie", "suelo"),
        "distancia_calzada": buscar_columna(enc, "distancia a calzada", "calzada"),
        "cables": buscar_columna(enc, "cable"),
        "arboles_cerca": buscar_columna(enc, "arboles a menos", "arboles cerca"),
        "amenazas": buscar_columna(enc, "amenaza"),
        "grupos": buscar_columna(enc, "grupos", "biodiversidad", "organismos"),
        "sin_observaciones": buscar_columna(enc, "no vimos", "sin observaciones"),
        "cavidad": buscar_columna(enc, "cavidad", "hueco visible"),
        "liquen_celdas": buscar_columna(enc, "celdas"),
        "liquen_morfotipos": buscar_columna(enc, "morfotipo"),
        "cara_tronco": buscar_columna(enc, "cara del tronco", "cara"),
        "inaturalist": buscar_columna(enc, "inaturalist"),
        "fotos": buscar_columna(enc, "foto", "imagen"),
        "observador": buscar_columna(enc, "equipo", "observador", "organizacion"),
        "notas": buscar_columna(enc, "nota", "comentario", "campo libre"),
    }

    features, omitidas = [], []
    for i, fila in enumerate(filas, start=1):
        f, motivo = fila_a_arbol(fila, col, args, len(features) + 1)
        if f is None:
            omitidas.append(f"  fila {i + 1}: {motivo}")
        else:
            features.append(f)
    return features, len(filas), omitidas


# -------------------------------------------------------------------- salida

def cargar_existentes():
    if not os.path.exists(SALIDA):
        return []
    try:
        with open(SALIDA, encoding="utf-8") as f:
            return json.load(f).get("features", [])
    except Exception:
        return []


def fusionar(previos, nuevos, fuente, reemplazar):
    """Fusiona por codigo. Si --reemplazar, descarta lo anterior de esta misma fuente."""
    if reemplazar:
        previos = [f for f in previos if f["properties"].get("fuente") != fuente]
    indice = {(f["properties"].get("fuente"), f["properties"].get("codigo")): i
              for i, f in enumerate(previos)}
    salida = list(previos)
    agregados = actualizados = 0
    for f in nuevos:
        clave = (f["properties"].get("fuente"), f["properties"].get("codigo"))
        if clave in indice:
            salida[indice[clave]] = f
            actualizados += 1
        else:
            salida.append(f)
            agregados += 1
    return salida, agregados, actualizados


def main():
    ap = argparse.ArgumentParser(description="Capa de arboles individuales del Observatorio")
    origen = ap.add_mutually_exclusive_group(required=True)
    origen.add_argument("--sheet", help="URL del CSV publicado de la planilla Google")
    origen.add_argument("--csv", help="Ruta a un CSV local (importacion puntual)")
    ap.add_argument("--fuente", required=True, choices=FUENTES)
    ap.add_argument("--fuente-detalle", default="", help="Cita completa del origen, rastreable")
    ap.add_argument("--sector", default="", help="Sector, si el CSV no lo trae")
    ap.add_argument("--prefijo", default="", help="Prefijo de 3 letras para codigos generados")
    ap.add_argument("--fecha", default="", help="Fecha del levantamiento, si el CSV no la trae")
    ap.add_argument("--no-publicable", action="store_true",
                    help="Carga los datos pero NO los muestra en el mapa publico "
                         "(p.ej. datos de la red sin autorizacion todavia)")
    ap.add_argument("--reemplazar", action="store_true",
                    help="Descarta lo anterior de esta misma fuente en vez de fusionar")
    args = ap.parse_args()

    if not args.fuente_detalle:
        print("AVISO: --fuente-detalle vacio. El esquema pide que el origen sea rastreable.")

    try:
        texto = descargar_csv(args.sheet) if args.sheet else \
            open(args.csv, encoding="utf-8-sig", errors="replace").read()
    except Exception as e:
        print("ERROR al leer el origen:", e)
        return 1

    nuevos, total, omitidas = construir(texto, args)
    print(f"Filas leidas: {total} | arboles validos: {len(nuevos)} | omitidos: {len(omitidas)}")
    for o in omitidas[:10]:
        print(o)
    if len(omitidas) > 10:
        print(f"  ... y {len(omitidas) - 10} mas")
    if not nuevos:
        print("Nada que escribir.")
        return 0

    features, agregados, actualizados = fusionar(
        cargar_existentes(), nuevos, args.fuente, args.reemplazar)

    publicos = sum(1 for f in features if f["properties"].get("publicable"))
    gj = {
        "type": "FeatureCollection",
        "actualizado": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "esquema": "docs/recursos/ESQUEMA_ARBOLES.md",
        "features": features,
    }
    os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
    with open(SALIDA, "w", encoding="utf-8") as f:
        json.dump(gj, f, ensure_ascii=False, indent=1)

    print(f"Agregados: {agregados} | actualizados: {actualizados}")
    print(f"Total en la capa: {len(features)} | publicables: {publicos}")
    por_fuente = {}
    for f in features:
        por_fuente[f["properties"].get("fuente")] = por_fuente.get(f["properties"].get("fuente"), 0) + 1
    for k, v in sorted(por_fuente.items()):
        print(f"   {k}: {v}")
    print("Escrito:", SALIDA)
    return 0


if __name__ == "__main__":
    sys.exit(main())
