# -*- coding: utf-8 -*-
"""Sincroniza las denuncias VERIFICADAS de la planilla Google -> docs/data/denuncias.geojson

Solo publica las filas cuya columna ESTADO diga VERIFICADA (moderacion previa).
NUNCA publica el nombre ni el contacto del denunciante (privacidad).

Uso:
    python scripts/sync_denuncias.py                 # usa la variable de entorno SHEET_CSV_URL
    python scripts/sync_denuncias.py <url_csv>       # o la URL como argumento
"""
import csv, io, json, os, re, sys, unicodedata
from datetime import datetime, timezone
from urllib.request import urlopen, Request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "docs", "data", "denuncias.geojson")

# Solo estos estados se publican (moderacion)
ESTADOS_PUBLICABLES = {"VERIFICADA", "VERIFICADO", "APROBADA", "APROBADO", "SI", "PUBLICAR"}
# Campos que NUNCA se publican
PRIVADOS = ("nombre", "contacto", "correo", "email", "telefono", "rut")


def limpiar(texto):
    """minusculas, sin acentos, sin espacios extra — para comparar encabezados."""
    t = unicodedata.normalize("NFKD", str(texto or "")).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", t).strip().lower()


def buscar_columna(encabezados, *claves):
    """Devuelve el encabezado real que contenga alguna de las claves."""
    for clave in claves:
        for h in encabezados:
            if clave in limpiar(h):
                return h
    return None


def parsear_coords(texto):
    """Acepta '-38.7359, -72.5904' o '-38.7359 -72.5904'. Devuelve (lat, lon) o None."""
    nums = re.findall(r"-?\d+[.,]\d+", str(texto or ""))
    if len(nums) < 2:
        return None
    try:
        lat = float(nums[0].replace(",", "."))
        lon = float(nums[1].replace(",", "."))
    except ValueError:
        return None
    # Temuco esta ~ -38.7, -72.6. Validacion amplia pero razonable.
    if not (-56 < lat < -17 and -76 < lon < -66):
        return None
    return lat, lon


def normalizar_fecha(valor):
    """Devuelve YYYY-MM-DD si se puede reconocer; si no, el texto original."""
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


def descargar_csv(url):
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 (ObservatorioArbolado)"})
    with urlopen(req, timeout=90) as r:
        datos = r.read()
    return datos.decode("utf-8-sig", errors="replace")


def construir_geojson(texto_csv):
    filas = list(csv.DictReader(io.StringIO(texto_csv)))
    if not filas:
        return {"type": "FeatureCollection", "features": []}, 0, 0

    enc = list(filas[0].keys())
    col = {
        "estado": buscar_columna(enc, "estado", "publicar", "aprob"),
        "tipo": buscar_columna(enc, "tipo"),
        "especie": buscar_columna(enc, "especie"),
        "fecha": buscar_columna(enc, "fecha del hecho", "fecha"),
        "direccion": buscar_columna(enc, "direccion", "referencia", "calle"),
        "coords": buscar_columna(enc, "coordenada", "ubicacion", "gps", "lat"),
        "descripcion": buscar_columna(enc, "que paso", "descripcion", "detalle"),
        "foto": buscar_columna(enc, "foto", "imagen"),
        "marca": buscar_columna(enc, "marca temporal", "timestamp"),
    }
    if not col["estado"]:
        print("AVISO: no se encontro la columna ESTADO -> no se publica nada (moderacion).")
        return {"type": "FeatureCollection", "features": []}, len(filas), 0

    features, publicadas = [], 0
    for i, fila in enumerate(filas, start=2):  # fila 1 = encabezados
        estado = limpiar(fila.get(col["estado"], "")).upper().replace(" ", "")
        if estado not in {e.replace(" ", "") for e in ESTADOS_PUBLICABLES}:
            continue
        coords = parsear_coords(fila.get(col["coords"], "")) if col["coords"] else None
        if not coords:
            print(f"  fila {i}: VERIFICADA pero sin coordenadas validas -> se omite")
            continue
        lat, lon = coords
        props = {
            "tipo": (fila.get(col["tipo"]) or "Sin especificar").strip() if col["tipo"] else "Sin especificar",
            "especie": (fila.get(col["especie"]) or "").strip() if col["especie"] else "",
            "fecha": normalizar_fecha(fila.get(col["fecha"])) if col["fecha"] else "",
            "direccion": (fila.get(col["direccion"]) or "").strip() if col["direccion"] else "",
            "descripcion": (fila.get(col["descripcion"]) or "").strip() if col["descripcion"] else "",
            "foto": (fila.get(col["foto"]) or "").strip() if col["foto"] else "",
            "registrada": normalizar_fecha(fila.get(col["marca"])) if col["marca"] else "",
            "estado": "Verificada",
        }
        # blindaje de privacidad: jamas publicar datos de contacto
        for k in list(props):
            if any(p in limpiar(k) for p in PRIVADOS):
                props.pop(k)
        features.append({
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [round(lon, 6), round(lat, 6)]},
            "properties": props,
        })
        publicadas += 1

    gj = {
        "type": "FeatureCollection",
        "actualizado": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "features": features,
    }
    return gj, len(filas), publicadas


def main():
    url = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("SHEET_CSV_URL", "").strip()
    if not url:
        print("Sin SHEET_CSV_URL configurada todavia: no hay nada que sincronizar.")
        return 0
    print("Descargando respuestas de la planilla...")
    try:
        texto = descargar_csv(url)
    except Exception as e:
        print("ERROR al descargar la planilla:", e)
        return 1

    gj, total, publicadas = construir_geojson(texto)
    print(f"Filas en la planilla: {total} | publicadas (VERIFICADAS): {publicadas}")

    os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
    nuevo = json.dumps(gj, ensure_ascii=False, indent=1)
    anterior = ""
    if os.path.exists(SALIDA):
        with open(SALIDA, encoding="utf-8") as f:
            anterior = f.read()
    # comparar ignorando la marca de tiempo, para no commitear si no cambio nada
    def sin_fecha(t):
        return re.sub(r'"actualizado":\s*"[^"]*",?\s*', "", t)
    if sin_fecha(nuevo) == sin_fecha(anterior):
        print("Sin cambios en las denuncias publicadas.")
        return 0
    with open(SALIDA, "w", encoding="utf-8") as f:
        f.write(nuevo)
    print(f"Actualizado {SALIDA}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
