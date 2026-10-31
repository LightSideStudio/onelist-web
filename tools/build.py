#!/usr/bin/env python3
"""Genera la web de OneList en español e inglés: portada, privacidad y soporte.

    python3 tools/build.py

Los dos idiomas salen de la misma plantilla, así que dicen siempre lo mismo; el texto de
cada uno está en COPY, PRIVACY y SUPPORT. Escribe:
  index.html, privacidad.html, soporte.html          (español, raíz)
  en/index.html, en/privacy.html, en/support.html    (inglés)
"""
import html
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://lightsidestudio.github.io/onelist-web/"
EMAIL = "onelist@lightsidestudio.com"
# Cuando la app esté publicada, su enlace aquí: los botones se activan solos.
APPSTORE_URL = ""
UPDATED = {"es": "31 de octubre de 2026", "en": "October 31, 2026"}

COPY = {
    "es": {
        "lang": "es", "locale": "es_ES", "dir": "", "other": "en/", "other_label": "English",
        "pages": {"index": "index.html", "privacy": "privacidad.html", "support": "soporte.html"},
        "title": "OneList: tu backlog de ideas y tareas, y tu día",
        "description": "Todo lo que tienes pendiente, ordenado por temas en una sola lista. Cada día, un toque al sol y eliges lo que toca. Gratis, sin cuenta y sin recoger datos.",
        "appstore": "Descargar en el App Store", "soon": "Muy pronto en el App Store",
        "h1": "Todo tu backlog.<br><span class=\"g\">Y tu día, claro.</span>",
        "sub": "OneList guarda tus ideas, proyectos y tareas ordenados por temas. Sin agenda ni calendario que mantener: cada día eliges lo importante con un toque al sol.",
        "note": "Gratis · Sin cuenta · Sin anuncios · Para iPhone y iPad",
        "features": [
            ("Todo en su sitio", "Temas y subtemas para cada parte de tu vida, cada uno con su color."),
            ("Elige tu día", "Toca el sol de una tarea y entra en Mi día. Lo que estás haciendo, siempre arriba."),
            ("Con todo dentro", "Subtareas, etiquetas de colores, prioridad y notas. Sin pantallas de más."),
            ("Tuyo y privado", "Tus tareas se quedan en tu iPhone. Ni cuenta, ni seguimiento, ni datos recogidos."),
        ],
        "shots_title": "Así se ve.",
        "footer_support": "Soporte", "footer_privacy": "Privacidad",
        "footer_note": "OneList es una app de Light Side Studio. iPhone e iPad son marcas de Apple Inc.",
    },
    "en": {
        "lang": "en", "locale": "en_US", "dir": "en/", "other": "../", "other_label": "Español",
        "pages": {"index": "index.html", "privacy": "privacy.html", "support": "support.html"},
        "title": "OneList: your backlog of ideas and tasks, and your day",
        "description": "Everything on your plate, organized by topic in one list. Each day, tap the sun and pick what matters. Free, no account, no data collected.",
        "appstore": "Download on the App Store", "soon": "Coming soon to the App Store",
        "h1": "Your whole backlog.<br><span class=\"g\">And a clear day.</span>",
        "sub": "OneList keeps your ideas, projects and tasks organized by topic. No planner or calendar to keep up with: each day, pick what matters with a tap on the sun.",
        "note": "Free · No account · No ads · For iPhone and iPad",
        "features": [
            ("All in its place", "Topics and subtopics for every part of your life, each with its own color."),
            ("Pick your day", "Tap a task's sun and it's in My Day. What you're doing now, always on top."),
            ("Everything inside", "Subtasks, color tags, priority and notes. No extra screens."),
            ("Yours and private", "Your tasks stay on your iPhone. No account, no tracking, no data collected."),
        ],
        "shots_title": "Take a look.",
        "footer_support": "Support", "footer_privacy": "Privacy",
        "footer_note": "OneList is an app by Light Side Studio. iPhone and iPad are trademarks of Apple Inc.",
    },
}

PRIVACY = {
    "es": {
        "title": "Política de privacidad",
        "intro": "OneList no recoge ningún dato tuyo. Tus tareas se guardan solo en tu dispositivo y no salen de él salvo cuando tú decides compartirlas.",
        "sections": [
            ("Responsable", [f"Light Side Studio, estudio dirigido por Lucas Longueira. Contacto para cualquier cuestión de privacidad: <a href=\"mailto:{EMAIL}\">{EMAIL}</a>."]),
            ("Qué guarda la app y dónde", [
                "Tus temas, tareas, subtareas, etiquetas y notas, y tus ajustes, se guardan <strong>solo en tu iPhone o iPad</strong>. La app no tiene servidores, no tiene cuentas y no se conecta a internet.",
                "<strong>No recibimos ningún dato tuyo</strong>: ni el contenido de tus tareas, ni estadísticas de uso, ni identificadores.",
            ]),
            ("Notificaciones", ["Si las activas, el resumen diario y los avisos de tareas vencidas son notificaciones locales: las programa tu propio dispositivo y no pasan por ningún servidor nuestro."]),
            ("Lo que compartes tú", ["Si compartes tareas como texto, va a donde tú elijas (WhatsApp, Notas, Mail…) y se rige por la política de esa app."]),
            ("Publicidad y analítica", ["OneList no lleva publicidad ni herramientas de analítica o seguimiento de terceros."]),
            ("Tus derechos", ["Como no guardamos datos tuyos, no hay nada que pedirnos que borremos: para eliminar tus tareas basta con borrarlas en la app o desinstalarla. Para cualquier duda, escríbenos; si crees que algo no se ha atendido bien, puedes reclamar ante la Agencia Española de Protección de Datos (<a href=\"https://www.aepd.es\">www.aepd.es</a>)."]),
            ("Menores", ["OneList no recoge datos de nadie, tampoco de menores."]),
            ("Cambios", ["Si esta política cambia, se actualizará aquí con su fecha."]),
        ],
    },
    "en": {
        "title": "Privacy Policy",
        "intro": "OneList doesn't collect any of your data. Your tasks are stored only on your device and never leave it unless you choose to share them.",
        "sections": [
            ("Who we are", [f"Light Side Studio, a studio run by Lucas Longueira. Contact for any privacy matter: <a href=\"mailto:{EMAIL}\">{EMAIL}</a>."]),
            ("What the app stores and where", [
                "Your topics, tasks, subtasks, tags and notes, and your settings, are stored <strong>only on your iPhone or iPad</strong>. The app has no servers, no accounts and doesn't connect to the internet.",
                "<strong>We receive none of your data</strong>: not the content of your tasks, not usage statistics, not identifiers.",
            ]),
            ("Notifications", ["If you turn them on, the daily summary and overdue alerts are local notifications: your own device schedules them and they never go through any server of ours."]),
            ("What you share", ["If you share tasks as text, it goes wherever you choose (WhatsApp, Notes, Mail…) and is governed by that app's policy."]),
            ("Ads and analytics", ["OneList has no ads and no third-party analytics or tracking."]),
            ("Your rights", ["Since we don't store any of your data, there's nothing to ask us to delete: to remove your tasks, just delete them in the app or uninstall it. For any question, write to us; if you feel something wasn't handled properly, you can complain to the Spanish Data Protection Agency (<a href=\"https://www.aepd.es\">www.aepd.es</a>)."]),
            ("Children", ["OneList collects no one's data, children included."]),
            ("Changes", ["If this policy changes, it will be updated here with its date."]),
        ],
    },
}

SUPPORT = {
    "es": {
        "title": "Soporte",
        "intro": f"¿Algo no va como esperabas? Aquí tienes lo más habitual. Si no lo encuentras, escríbenos a <a href=\"mailto:{EMAIL}\">{EMAIL}</a> y te respondemos.",
        "faq": [
            ("¿Cómo añado una tarea a Mi día?", "En la pestaña Tareas, toca el sol de la tarea. Para quitarla, vuelve a tocarlo, o mantén pulsada la tarea en Mi día y elige «Quitar de Mi día»."),
            ("¿Qué es «En curso»?", "Lo que estás haciendo ahora mismo. Mantén pulsada una tarea de Mi día y elige «Marcar en curso»: sube arriba del todo. Al completarla, deja de estar en curso."),
            ("¿Por qué se vació Mi día?", "Porque está activado «Vaciar Mi día cada noche» en Ajustes. Las tareas sin terminar no se pierden: siguen en su tema. Si prefieres que se queden, desactívalo."),
            ("¿Cómo cambio el color de un tema?", "En Tareas, mantén pulsado el tema y elige editar. Los subtemas usan el color de su tema, más tenue."),
            ("¿Cómo comparto mis tareas?", "Entra en un tema, toca «Seleccionar», elige las tareas y toca Compartir: salen como texto con formato, listo para copiar."),
            ("¿Mis tareas se guardan en iCloud?", "Todavía no: se guardan solo en tu dispositivo. Si borras la app, se borran con ella."),
        ],
    },
    "en": {
        "title": "Support",
        "intro": f"Something not working as expected? Here are the most common questions. If yours isn't here, write to <a href=\"mailto:{EMAIL}\">{EMAIL}</a> and we'll get back to you.",
        "faq": [
            ("How do I add a task to My Day?", "In the Tasks tab, tap the task's sun. To remove it, tap it again, or touch and hold the task in My Day and choose “Remove from My Day”."),
            ("What does “In progress” mean?", "What you're doing right now. Touch and hold a task in My Day and choose “Mark in progress”: it moves to the very top. When you complete it, it's no longer in progress."),
            ("Why did My Day clear?", "Because “Clear My Day every night” is on in Settings. Unfinished tasks aren't lost: they stay in their topic. If you'd rather keep them, turn it off."),
            ("How do I change a topic's color?", "In Tasks, touch and hold the topic and choose edit. Subtopics use their topic's color, a little softer."),
            ("How do I share my tasks?", "Open a topic, tap “Select”, choose the tasks and tap Share: they come out as formatted text, ready to copy."),
            ("Are my tasks saved to iCloud?", "Not yet: they're stored only on your device. If you delete the app, they're deleted with it."),
        ],
    },
}

CSS = """
:root{--bg:#fff;--bg2:#f5f5f7;--ink:#1d1d1f;--sub:#6e6e73;--line:#d2d2d7;--btn:#1d1d1f;--btnt:#fff;--g1:#007aff;--g2:#af52de}
@media (prefers-color-scheme:dark){:root{--bg:#000;--bg2:#161617;--ink:#f5f5f7;--sub:#a1a1a6;--line:#38383a;--btn:#f5f5f7;--btnt:#000;--g1:#0a84ff;--g2:#bf5af2}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.47 -apple-system,BlinkMacSystemFont,"SF Pro Text","Helvetica Neue",Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--g1);text-decoration:none}a:hover{text-decoration:underline}
.wrap{max-width:1000px;margin:0 auto;padding:0 22px}
.nav{position:sticky;top:0;z-index:5;background:color-mix(in srgb,var(--bg) 80%,transparent);backdrop-filter:saturate(180%) blur(20px);-webkit-backdrop-filter:saturate(180%) blur(20px);border-bottom:1px solid color-mix(in srgb,var(--line) 60%,transparent)}
.nav .wrap{display:flex;align-items:center;justify-content:space-between;height:52px}
.marca{display:flex;align-items:center;gap:10px;color:var(--ink);font-weight:600}.marca:hover{text-decoration:none}
.marca img{width:28px;height:28px;border-radius:7px}
.nav nav{display:flex;gap:20px;font-size:14px}.nav nav a{color:var(--sub)}.nav nav a:hover{color:var(--ink);text-decoration:none}
.hero{text-align:center;padding:84px 0 40px}
.hero .icono{width:120px;height:120px;border-radius:27px;box-shadow:0 12px 40px rgba(0,0,40,.18)}
h1{font:700 clamp(44px,8vw,84px)/1.05 -apple-system,BlinkMacSystemFont,"SF Pro Display",sans-serif;letter-spacing:-.025em;margin:28px 0 22px}
.g{background:linear-gradient(90deg,var(--g1),var(--g2));-webkit-background-clip:text;background-clip:text;color:transparent}
.sub{font-size:clamp(19px,2.4vw,24px);line-height:1.38;color:var(--sub);max-width:720px;margin:0 auto 32px}
.btn{display:inline-block;background:var(--btn);color:var(--btnt);padding:14px 28px;border-radius:999px;font-weight:600}.btn:hover{text-decoration:none;opacity:.86}
.btn.off{opacity:.5;pointer-events:none}
.note{color:var(--sub);font-size:14px;margin-top:18px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:16px;margin:56px 0}
.card{background:var(--bg2);border-radius:22px;padding:26px}
.card h3{margin:0 0 8px;font-size:21px;letter-spacing:-.01em}.card p{margin:0;color:var(--sub)}
.tira{display:flex;gap:18px;overflow-x:auto;scroll-snap-type:x mandatory;padding:8px 22px 30px;max-width:1240px;margin:0 auto}
.tira img{width:270px;height:auto;border-radius:22px;scroll-snap-align:center;flex:none;background:var(--bg2)}
h2{font:700 clamp(32px,5vw,48px)/1.1 -apple-system,BlinkMacSystemFont,"SF Pro Display",sans-serif;letter-spacing:-.02em;text-align:center;margin:40px 0 24px}
.doc{max-width:720px;padding-top:56px;padding-bottom:40px}
.doc h1{font-size:clamp(36px,6vw,56px);margin:0 0 8px}.doc h2{text-align:left;font-size:24px;margin:36px 0 8px}
.doc .meta{color:var(--sub);font-size:14px;margin:0 0 24px}.doc .intro{font-size:21px;line-height:1.4}
details{border-bottom:1px solid var(--line);padding:18px 0}summary{cursor:pointer;font-weight:600;font-size:19px}
details p{color:var(--sub);margin:10px 0 0}
footer{border-top:1px solid var(--line);margin-top:64px;padding:28px 0 48px;font-size:13px;color:var(--sub)}
footer .wrap{display:flex;flex-wrap:wrap;gap:16px;justify-content:space-between}footer nav{display:flex;flex-wrap:wrap;gap:18px}
footer a{color:var(--sub)}
"""


def esc(s):
    return html.escape(s, quote=True)


def head(c, title, description, path, up):
    url = BASE + c["dir"] + path
    otro = "en" if c["lang"] == "es" else "es"
    alt = BASE + COPY[otro]["dir"] + COPY[otro]["pages"][next(k for k, v in c["pages"].items() if v == path)]
    return f"""<!doctype html>
<html lang="{c['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="color-scheme" content="light dark">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="{otro}" href="{alt}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="OneList">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}assets/{c['lang']}/og.jpg">
<meta property="og:locale" content="{c['locale']}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{up}assets/icon.png">
<link rel="apple-touch-icon" href="{up}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{up}assets/site.css">
</head>
<body>
<header class="nav"><div class="wrap">
  <a href="{c['pages']['index']}" class="marca"><img src="{up}assets/icon.png" alt="">OneList</a>
  <nav><a href="{c['pages']['support']}">{c['footer_support']}</a><a href="{c['other']}{COPY[otro]['pages'][next(k for k, v in c['pages'].items() if v == path)]}" lang="{otro}">{c['other_label']}</a></nav>
</div></header>
"""


def boton(c):
    if APPSTORE_URL:
        return f'<a class="btn" href="{APPSTORE_URL}">{c["appstore"]}</a>'
    return f'<span class="btn off">{c["soon"]}</span>'


def footer(c):
    p = c["pages"]
    return f"""<footer><div class="wrap">
  <span>{c['footer_note']} © 2026 Light Side Studio</span>
  <nav><a href="{p['support']}">{c['footer_support']}</a><a href="{p['privacy']}">{c['footer_privacy']}</a><a href="mailto:{EMAIL}">{EMAIL}</a></nav>
</div></footer>
</body></html>
"""


def index(c):
    up = "../" if c["dir"] else ""
    cards = "".join(f'<article class="card"><h3>{esc(t)}</h3><p>{esc(s)}</p></article>' for t, s in c["features"])
    shots = "".join(f'<img src="{up}assets/{c["lang"]}/{i}.jpg" alt="" loading="lazy" width="540" height="1168">' for i in range(1, 9))
    return head(c, c["title"], c["description"], c["pages"]["index"], up) + f"""
<main>
<section class="hero wrap">
  <img class="icono" src="{up}assets/icon.png" alt="OneList">
  <h1>{c['h1']}</h1>
  <p class="sub">{esc(c['sub'])}</p>
  {boton(c)}
  <p class="note">{esc(c['note'])}</p>
</section>
<section class="wrap"><div class="cards">{cards}</div></section>
<section><h2>{c['shots_title']}</h2><div class="tira">{shots}</div></section>
</main>
""" + footer(c)


def document(c, kind):
    up = "../" if c["dir"] else ""
    if kind == "privacy":
        t = PRIVACY[c["lang"]]
        updated = ("Última actualización: " if c["lang"] == "es" else "Last updated: ") + UPDATED[c["lang"]]
        body = "".join(f"<h2>{esc(h)}</h2>" + "".join(f"<p>{p}</p>" for p in ps) for h, ps in t["sections"])
        meta = f'<p class="meta">{updated}</p>'
    else:
        t = SUPPORT[c["lang"]]
        body = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in t["faq"])
        meta = ""
    return head(c, f"{t['title']} · OneList", t["intro"][:150], c["pages"][kind], up) + f"""
<main class="doc wrap">
  <h1>{t['title']}</h1>{meta}<p class="intro">{t['intro']}</p>
  {body}
</main>
""" + footer(c)


def main():
    open(os.path.join(ROOT, "assets", "site.css"), "w").write(CSS.lstrip())
    for c in COPY.values():
        carpeta = os.path.join(ROOT, c["dir"])
        os.makedirs(carpeta, exist_ok=True)
        open(os.path.join(carpeta, c["pages"]["index"]), "w").write(index(c))
        open(os.path.join(carpeta, c["pages"]["privacy"]), "w").write(document(c, "privacy"))
        open(os.path.join(carpeta, c["pages"]["support"]), "w").write(document(c, "support"))
    print("Listo")


if __name__ == "__main__":
    main()
