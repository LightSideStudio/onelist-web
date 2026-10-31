# OneList · web pública

La web de OneList, la app de backlog de tareas de Light Side Studio:
<https://lightsidestudio.github.io/onelist-web/>

- `/` en español y `/en/` en inglés: portada, privacidad y soporte. Son las URL que van en
  App Store Connect (privacidad: `privacidad.html` / `en/privacy.html`; soporte:
  `soporte.html` / `en/support.html`).

## Se genera, no se edita a mano

Las seis páginas y `assets/site.css` salen de `tools/build.py`, con el texto de los dos
idiomas en el mismo archivo para que digan siempre lo mismo:

```bash
python3 tools/build.py
```

El enlace de la App Store está en una línea, `APPSTORE_URL`. Mientras esté vacío, el botón
dice «Muy pronto en el App Store».
