# -*- coding: utf-8 -*-
"""Comprueba que las opciones de denuncia.html existan tal cual en el Google Form.

Por que hace falta: el <select> de "Tipo de situacion" manda su atributo value al
Google Form. Google RECHAZA cualquier valor que no este en su lista de opciones, y
como el envio va por fetch con mode:'no-cors', la pagina no se entera: le muestra
"Gracias" a quien denuncia y la denuncia no queda registrada en ninguna parte.

Paso el 28/07/2026 con "Propuesta de arbol patrimonial (Art. 9)" y
"Arbol danado (herido, quemado, con publicidad)".

Uso:
    python scripts/verificar_opciones.py

Devuelve 0 si todo calza, 1 si hay alguna opcion sin respaldo en el Form.
Conviene correrlo cada vez que se toque la lista de opciones, en cualquiera de los dos lados.
"""
import json
import os
import re
import sys
from urllib.request import Request, urlopen

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGINA = os.path.join(RAIZ, "docs", "denuncia.html")


def leer_valores_del_sitio():
    """Los value= del <select id="f_tipo"> de denuncia.html."""
    with open(PAGINA, encoding="utf-8") as f:
        html = f.read()
    m = re.search(r'<select[^>]*id="f_tipo".*?</select>', html, re.S)
    if not m:
        raise SystemExit("No se encontro el <select id=\"f_tipo\"> en docs/denuncia.html")
    valores = re.findall(r'<option value="([^"]*)"', m.group(0))
    return [v for v in valores if v.strip()]


def leer_url_del_form():
    """La URL del formResponse configurada en la pagina."""
    with open(PAGINA, encoding="utf-8") as f:
        html = f.read()
    m = re.search(r"action:\s*'([^']*formResponse)'", html)
    if not m:
        raise SystemExit("No se encontro la URL del Google Form en docs/denuncia.html")
    return m.group(1).replace("/formResponse", "/viewform")


def leer_preguntas_del_form(url):
    """Cada pregunta del formulario publico -> sus opciones, o None si es texto libre."""
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 (ObservatorioArbolado)"})
    with urlopen(req, timeout=60) as r:
        html = r.read().decode("utf-8", errors="replace")
    m = re.search(r"FB_PUBLIC_LOAD_DATA_ = (.*?);</script>", html, re.S)
    if not m:
        raise SystemExit("No se pudo leer la definicion del Google Form (¿cambio el formato?)")
    datos = json.loads(m.group(1))
    preguntas = {}
    for item in datos[1][1]:
        titulo = item[1]
        for campo in (item[4] or []):
            preguntas[titulo] = [o[0] for o in campo[1]] if campo[1] else None
    return preguntas


def bandera_del_sitio():
    """Como esta declarada en denuncia.html la constante TIPO_VALIDADO_POR_EL_FORM."""
    with open(PAGINA, encoding="utf-8") as f:
        m = re.search(r"const TIPO_VALIDADO_POR_EL_FORM\s*=\s*(true|false)", f.read())
    return None if not m else (m.group(1) == "true")


def main():
    valores = leer_valores_del_sitio()
    preguntas = leer_preguntas_del_form(leer_url_del_form())
    bandera = bandera_del_sitio()

    if not any("tipo" in t.lower() for t in preguntas):
        raise SystemExit("El Google Form no tiene ninguna pregunta llamada 'Tipo'")
    tipo = next(o for t, o in preguntas.items() if "tipo" in t.lower())

    # Caso bueno: la pregunta ya es de respuesta corta y el Form no puede rechazar nada.
    if tipo is None:
        print("La pregunta 'Tipo' del Google Form es de RESPUESTA CORTA:")
        print("acepta cualquier texto, asi que ninguna denuncia puede perderse por este motivo.")
        print("Opciones que ofrece el sitio:", valores)
        if bandera is not False:
            print("\nFALTA UN PASO: en docs/denuncia.html hay que dejar")
            print("  const TIPO_VALIDADO_POR_EL_FORM = false;")
            print("Mientras siga en true, un tipo fuera de la lista se degrada a 'Otro' sin necesidad.")
            return 1
        print("\nOK: el sitio ya esta configurado en concordancia (TIPO_VALIDADO_POR_EL_FORM = false).")
        return 0

    # Caso a vigilar: sigue siendo opcion multiple, el Form valida y puede rechazar.
    print("La pregunta 'Tipo' del Google Form es de OPCION MULTIPLE: el Form valida.")
    if bandera is False:
        print("\nPELIGRO: docs/denuncia.html declara TIPO_VALIDADO_POR_EL_FORM = false,")
        print("pero el Form SI valida. La red de seguridad esta desactivada de mas.")
        print("Dejarla en true, o convertir la pregunta a respuesta corta.")
        return 1

    print("Opciones en el sitio :", valores)
    print("Opciones en el Form  :", tipo)

    huerfanas = [v for v in valores if v not in tipo]
    sin_usar = [o for o in tipo if o not in valores]

    if sin_usar:
        print("\nAviso: el Form ofrece opciones que el sitio no muestra:", sin_usar)

    if huerfanas:
        print("\nERROR: estas opciones del sitio NO existen en el Google Form.")
        print("Google las rechaza y la denuncia se pierde sin aviso:")
        for v in huerfanas:
            print("  -", repr(v))
        print("\nArreglo: dejar el value identico al del Form (el texto visible puede diferir),")
        print("o agregar la opcion en el Google Form con ese mismo texto.")
        return 1

    print("\nOK: las", len(valores), "opciones del sitio existen en el Google Form.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
