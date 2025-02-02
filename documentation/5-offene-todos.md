# Weiterentwicklungs-Möglichkeiten

Du hast Lust, die Software weiterzuentwickeln? Super! Der folgende Befehl hilft dir, offene Aufgaben zu finden:

```bash
grep -r "TODO" ./src 
```
Damit werden alle TODO-Markierungen im Code aufgespürt, sodass du offene Punkte direkt findest. Einige mögliche Erweiterungen sind:

<details><summary>Mehrsprachigkeit über den locale-Ordner (de/en)</summary>

# Locale-Ordner und Sprachen in Django

Django verwaltet Übersetzungen über `locale`-Ordner, die sprachspezifische Übersetzungsdateien enthalten. Die wichtigsten Schritte:

## 1. Locale-Ordnerstruktur

Jeder `locale`-Ordner wird im Projekt oder in einer App erstellt und folgt dem Schema:
`<app_name>/locale/<language_code>/LC_MESSAGES/`
Beispiel für Deutsch und Englisch:
`myapp/locale/de/LC_MESSAGES/ myapp/locale/en/LC_MESSAGES/`

## 2. Übersetzungsdateien

Die Übersetzungsdateien heißen:

- `django.po`: Enthält die Übersetzungen.
- `django.mo`: Kompilierte Version der `.po`-Datei (wird automatisch generiert).

## 3. Erstellung der Übersetzungsdateien

Übersetzungsnachrichten werden mit dem Befehl gesammelt:

```bash
python manage.py makemessages -l <language_code>
```

## 4. Übersetzungen bearbeiten

Die `django.po`-Datei kann mit einem Texteditor oder speziellen Tools wie [Poedit](https://poedit.net/) bearbeitet werden. Beispiel:

```po
msgid "Welcome"
msgstr "Willkommen"
```

## 5. Übersetzungsdateien kompilieren

Nach dem Bearbeiten der .po-Dateien müssen sie in .mo-Dateien kompiliert werden:

```bash
python manage.py compilemessages
```

## 6. Aktivierung der Sprache

Django verwendet die aktive Sprache aus den Einstellungen oder der Benutzersitzung. Die Sprache kann über Middleware oder Views geändert werden:

Middleware
Stelle sicher, dass LocaleMiddleware in MIDDLEWARE aktiviert ist:

```bash
MIDDLEWARE = [
    ...
    'django.middleware.locale.LocaleMiddleware',
    ...
]
```
</details>

<details><summary>Auswertungsskript für die Datenbank</summary>
Offene Aufgabe (TODO): Es fehlt noch ein Skript zur automatischen Analyse der erfassten Daten wie Verweildauer, Klicks und weiteres Nutzerverhalten.
Aktuell können die Daten zwar exportiert, aber nicht direkt innerhalb des Systems ausgewertet werden. Die Analyse muss derzeit manuell in Python oder R erfolgen. Ein Skript, das diese Auswertung direkt übernimmt, wäre eine sinnvolle Erweiterung.</details>

<details><summary>Browser Navigation ermöglichen</summary>
Aktuell gibt es eine interne Navigation über einen JavaScript "Zurück"-Button. Allerdings funktioniert der "Vor"-Button nicht immer zuverlässig, da der "Zurück"-Button in manchen Fällen absichtlich doppelt springt (z. B. nach dem Schreiben eines Kommentars). Dies geschieht durch den session-pop-Befehl, der dann aber den "Vor"-Button durcheinanderbringt.
</details>

<details><summary>Responsivität ausbauen</summary>
Die Anwendung funktioniert bereits auf unterschiedlichen Bildschirmgrößen, benötigt aber noch einige Anpassungen für die mobile Nutzung.
</details>

<details><summary>API ausbauen</summary>

- Momentan können über die API Kommentare und Profile erstellt werden. Langfristig wäre es möglich, die gesamte Funktionalität über die API zugänglich zu machen.

- Aktuell erfolgen Admin-Tätigkeiten über das /admin-Panel, was für den Start ausreicht.
- Eine API ist bereits angelegt (im api-Ordner).
- Es gibt eine API-Dokumentation (.yaml-Datei), die im Swagger Editor geöffnet werden kann.
- Auch eine Postman-Anbindung ist vorhanden.

</details>

