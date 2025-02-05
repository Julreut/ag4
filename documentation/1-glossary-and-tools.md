# Übersicht über verwendete Tools

**Mirror Online** ist ein simuliertes, kontrollierbares Online-Forum, das auf dem Django-Webframework basiert. Es wurde auf Basis des [Fakebook Social Media Tools](https://github.com/jpfefferlab/Fakebook/tree/master/src) entwickelt.

Diese Dokumentation soll dir helfen, das Projekt zu verstehen, es lokal einzurichten, zu nutzen und weiterzuentwickeln, auch wenn du wenige Vorkenntnisse hast.

<details>
<summary>📂  <strong> Grundlagen Backend: Django & Python </strong></summary>

### **Was ist Django?**

Django ist ein Werkzeug, das dir hilft, Webseiten mit der Programmiersprache Python zu erstellen. Es hilft dir, eine Anwendung mit weniger Code schneller zu entwickeln. [Offizielle Django-Dokumentation](https://docs.djangoproject.com/de/3.2/)

### **Was ist das Admin Panel?**

Das Django Admin Panel ist eine automatisch erstellte Verwaltungsseite, die es dir (als Administrator) ermöglicht, Daten zu verwalten, ohne selbst programmieren zu müssen. Es bietet eine einfache Oberfläche zum Hinzufügen, Bearbeiten und Löschen von Daten.

### Installation von Python und Django

#### Download

Gehe zur offiziellen [Python-Website](https://www.python.org/downloads/) und lade die neueste Version herunter.

#### Installation Python

Folge den Installationsanweisungen für dein Betriebssystem.

**Wichtig:** Stelle sicher, dass du die Option „Add Python to PATH“ während der Installation aktivierst.

#### Überprüfung

Öffne dein Terminal oder die Eingabeaufforderung und führe folgenden Befehl aus:

```bash
python --version
```

#### Installation Django

```bash
pip install django
```

#### Überprüfung

```bash
django-admin --version
```

### Verzeichnis- und Dateistruktur eines Django-Projekts

```plaintext
Django-Projekt/
├── manage.py          # Ein Werkzeug zur Verwaltung des Django-Projekts.
├── project_name/      # Hauptverzeichnis des Projekts, enthält Einstellungen und Konfigurationen.
│   ├── settings.py    # Konfigurationsdatei für das Django-Projekt.
│   ├── urls.py        # Datei, die bestimmt, welche Webseiten aufgerufen werden können.
│   └── wsgi.py        # Datei für den Einsatz des Projekts auf einem Server.
├── app_name/          # Verzeichnis einer Django-App innerhalb des Projekts.
│   ├── models.py      # Datei, die die Struktur der Datenbank beschreibt.
│   └── views.py       # Datei, die bestimmt, wie Daten angezeigt werden.
├── templates/         # Verzeichnis für HTML-Dateien.
└── static/            # Verzeichnis für statische Dateien wie CSS, JS und Bilder.
```

</details>

---

<details>
<summary>🎨 <strong> Grundlagen Frontend: HTML & CSS </strong></summary>
<br>

**tl;dr** HTML ist die Baustruktur einer Webseite, CSS sorgt für das Design, und JavaScript fügt interaktive Elemente hinzu.
**HTML-Dateien** definieren die Struktur und Inhalte der Webseiten. In Django werden sie meist im `templates/`-Verzeichnis der jeweiligen App abgelegt.  
**Beispiel:** `src/comments/templates/article_comments.html`

Die Dateien enthalten oft spezielle Django-Template-Tags, um dynamische Inhalte einzubinden:

```html
{% extends "base.html" %} {% load static %}
```

Dies ermöglicht die Wiederverwendung einer Design-Basis und den Zugriff auf statische Ressourcen.

**CSS-Dateien** bestimmen das Aussehen und Layout der Webseiten. Diese befinden sich im static/css/ Verzeichnis.

**Beispiel:** `static/css/styles.css`

</details>

---

<details>
<summary>📜  <strong>Verwendung von JavaScript in Django Templates  </strong></summary>
<br>
JavaScript wird verwendet, um interaktive Funktionen auf deinen Webseiten bereitzustellen. In Django kannst du JavaScript-Dateien im `static/js/` Verzeichnis speichern und in deinen Templates einbinden.

### Einbindung von Skripten: Blocks und Static Files

Django lädt JavaScript-Dateien nicht automatisch. Du musst sie im Template einbinden. Dafür gibt es den scripts-Block. Um JavaScript in deinen Django-Templates effektiv zu verwalten, kannst du Template-Blöcke verwenden. Dies ermöglicht es dir, spezifische Skripte auf bestimmten Seiten zu laden.
In der base.html Datei `src/templates/base.html` findest du den Javascripts Block:

```html
<!-- JavaScript Block -->
{% block scripts %} {% endblock %}
```

Dieser Block dient als Platzhalter für JavaScript-Code, der in untergeordneten Templates eingebunden wird.

### Beispiel: JavaScript in einer Unterseite einfügen

In einem spezifischen Template, z. B. article_comments.html, kannst du den Block wie folgt nutzen:

```html
{% extends "base.html" %} {% block scripts %}
<script src="{% static 'js/article_comments.js' %}"></script>
{% endblock %}
```

#### Vorteile:

- Modularität: Skripte werden nur geladen, wenn sie tatsächlich benötigt werden.
- Performance: Weniger unnötige Skripte verbessern die Ladegeschwindigkeit.
- Wartbarkeit: Der Code bleibt übersichtlicher und einfacher zu verwalten.

</details>

---

<details>
<summary>🗄️<strong>Datenbank & Modelle</strong></summary>
<br>
Modelle definieren die Struktur deiner Datenbank. In Django werden sie im models.py einer App definiert.

**Beispiel:** src/articles/models.py

### Migrationen:

Wenn du einen Teil des Modells änderst, musst du die Migrationen neu generieren und anwenden, um die Datenbank zu migrieren.

```bash
python3 src/manage.py makemigrations
```

Erstellt eine neue Migrationsdatei mit den Änderungen an der Datenbankstruktur. `makemigrations` aktualisiert alle Migrationsskripte. Du kannst sie dann anwenden mit:

```bash
python3 src/manage.py migrate
```

</details>

<br>

# Glossar

| Begriff       | Beschreibung                                                                       |
| ------------- | ---------------------------------------------------------------------------------- |
| **User**      | Ein Benutzerkonto, das für die Anmeldung verwendet wird.                           |
| **Profile**   | Enthält zusätzliche Informationen über den Benutzer, wie Biografie und Profilbild. |
| **Superuser** | Ein Administrator, der vollen Zugriff auf das Admin-Panel hat.                     |
| **Session**   | Eine Möglichkeit, Benutzerdaten zwischen verschiedenen HTTP-Anfragen zu speichern. |

## Datenbank

| Begriff      | Beschreibung                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------- |
| **Model**    | Eine Klasse, die die Struktur der Datenbank beschreibt.                                                             |
| **QuerySet** | Eine Sammlung von Datenbankabfragen, die von einem Model zurückgegeben werden, die du filtern und bearbeiten kannst |
| **Fixture**  | Eine Datei, die initiale Daten für die Datenbank enthält.                                                           |

## Templates

| Begriff               | Beschreibung                                                                 |
| --------------------- | ---------------------------------------------------------------------------- |
| **Template**          | Eine HTML-Datei, die das Layout einer Seite definiert.                       |
| **Template Tag**      | Ein spezieller Befehl in einem Template, der dynamische Inhalte einfügt.     |
| **Template Filter**   | Eine Funktion, die den Wert einer Template-Variable verändert.               |
| **Context**           | Ein Wörterbuch von Variablen, die an ein Template übergeben werden.          |
| **Context Processor** | Eine Funktion, die zusätzliche Kontextdaten für alle Templates bereitstellt. |

## Views und URLs

| Begriff     | Beschreibung                                                                                     |
| ----------- | ------------------------------------------------------------------------------------------------ |
| **View**    | Eine Funktion oder Klasse, die eine HTTP-Anfrage entgegennimmt und eine HTTP-Antwort zurückgibt. |
| **URLconf** | Eine Datei, die URL-Muster und deren zugehörige Views definiert.                                 |

## Middleware und Caching

| Begriff          | Beschreibung                                                                      |
| ---------------- | --------------------------------------------------------------------------------- |
| **Middleware**   | Eine Klasse, die die Verarbeitung von HTTP-Anfragen und -Antworten beeinflusst.   |
| **Cache**        | Ein Mechanismus zur Zwischenspeicherung von Daten, um die Leistung zu verbessern. |
| **GET-Anfrage**  | Eine HTTP-Anfrage, die Daten vom Server anfordert.                                |
| **POST-Anfrage** | Eine HTTP-Anfrage, die Daten an den Server sendet, um sie zu verarbeiten.         |
| **HTTP**         | Ein Protokoll zur Übertragung von Daten im Web.                                   |

## Docker

| Begriff            | Beschreibung                                                                                                                                                                                                                                                                      |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Docker**         | Eine Plattform, die es ermöglicht, Anwendungen in sogenannten Containern zu verpacken und auszuführen. Diese Container enthalten alles, was die Anwendung zum Laufen braucht, und können leicht auf verschiedenen Systemen eingesetzt werden.                                     |
| **Container**      | Eine leichtgewichtige, eigenständige Einheit, die alle notwendigen Komponenten (Code, Laufzeit, System-Tools, Bibliotheken) enthält, um eine Anwendung auszuführen. Container sind isoliert voneinander und vom Host-System.                                                      |
| **Image**          | Eine schreibgeschützte Vorlage, die den Zustand eines Containers zu einem bestimmten Zeitpunkt beschreibt. Ein Image enthält alle Dateien und Einstellungen, die benötigt werden, um einen Container zu erstellen.                                                                |
| **Dockerfile**     | Eine Textdatei mit einer Reihe von Anweisungen, die Docker verwendet, um ein Image zu erstellen. In dieser Datei wird beschrieben, welche Software installiert und wie der Container konfiguriert werden soll.                                                                    |
| **Docker Compose** | Ein Werkzeug, das es ermöglicht, Multi-Container-Docker-Anwendungen zu definieren und auszuführen. Mit Docker Compose kannst du die Dienste, Netzwerke und Volumes, die deine Anwendung benötigt, in einer einzigen Datei beschreiben und dann mit einem einzigen Befehl starten. |
| **Volume**         | Ein Mechanismus zur Speicherung von Daten, die von Containern gemeinsam genutzt werden können. Volumes ermöglichen es, Daten auch dann zu speichern, wenn der Container gelöscht wird.                                                                                            |
| **Registry**       | Ein Speicherort für Docker-Images, wie z.B. Docker Hub. Eine Registry ermöglicht es, Images zu speichern, zu versionieren und zu teilen.                                                                                                                                          |
| **Orchestration**  | Die Verwaltung und Koordination von Containern in einer verteilten Umgebung. Orchestrierungstools wie Kubernetes helfen dabei, Container automatisch zu starten, zu stoppen und zu skalieren, um die Anforderungen der Anwendung zu erfüllen.                                     |

## Sonstiges

| Begriff                | Beschreibung                                                                            |
| ---------------------- | --------------------------------------------------------------------------------------- |
| **Form**               | Eine Klasse, die HTML-Formulare und deren Validierung verwaltet.                        |
| **Static Files**       | Dateien wie CSS, JavaScript und Bilder, die von der Webseite verwendet werden.          |
| **Signal**             | Ein Mechanismus, um bestimmte Aktionen auszulösen, wenn bestimmte Ereignisse eintreten. |
| **Management Command** | Ein benutzerdefiniertes Kommandozeilen-Tool für administrative Aufgaben.                |
