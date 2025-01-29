# Weiterentwicklungs-Möglichkeiten
<details><summary>Languages über locale-Ordner (de/en)</summary>

### Internationalization (I18n) / Translation (T9n)
The project uses django's internationalization mechanism for translation.

HTML Template files and dynamically generated content in python code refer to keys for each string literal that has to be translated using the `translate` and `blocktranslate`tags and the `gettext` methods. The translation for each specific language and each key can be found in `./src/{appdir}/locale/{lang}/LC_MESSAGES/django.po`.

After new keys for translation have been created using the html template tags `translate` and `blocktranslate` or the python `ugettext_lazy` method in code, the translation files need to be regenerated. This can be achieved my navigating to the app's directory and running the following commands:

```
cd ./src/{appdir}/
django-admin makemessages -l en
django-admin makemessages -l de
```

`django-admin` is installed alongside django if you are using the pip dependency manager. You might have to enable your virtual environment.

You should now have all the new message keys in your translation files. You can now manually edit their translations in the `django.po` files. Once you are satisfied, just run

```
django-admin compilemessages
```

in the same directory to compile them to `django.mo` files which will then be used by the actual application.
You also have to do this if you modify them later on.

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

<details><summary>Auswertungsskript für die Datenbank mit Lesezeiten</summary>
TODO

</details>

<details><summary>Browser Navigation ermöglichen</summary>
Möglicherweise über Javascript. Bis dahin ermöglicht eine interne Navigation über Vor- und Zurück-Buttons das Navigieren auf der Seite.

</details>

<details><summary>Responsivität ausbauen</summary>

</details>

<details><summary>API testen</summary>
TODO

</details>

<details><summary>Conditions für Artikel und Kommentare anlegen</summary>
Aktuell ist es nur möglich, Conditions für Newspapers anzulegen. Falls gewünscht, kann diese Logik auf Articles und Comments erweitert werden. Denkbar wären Extra Conditions pro Abschnitt - also Newspaper-Condition, Article-Condition, Comment-Condition. Jeder Versuchsperson werden dann Control oder Experimental tags <i>pro Condition</i> zugeordnet.

</details>
