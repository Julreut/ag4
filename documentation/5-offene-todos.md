# Weiterentwicklungs-Möglichkeiten
<details><summary>Languages über locale-Ordner (de/en)</summary>

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

6. Aktivierung der Sprache

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

<details><summary>Auswertungsskript für die Datenbank mit Lesezeiten</summary>
TODO

</details>

<details><summary>Browser Navigation ermöglichen</summary>
TODO

</details>

<details><summary>Responsivität ausbauen</summary>
TODO

</details>

<details><summary>API testen</summary>
TODO

</details>

<details><summary>Conditions für Artikel und Kommentare anlegen</summary>
TODO

</details>
