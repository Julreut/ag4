# Einführung

**Mirror Online** ist ein Online-Forum, das auf dem Django-Webframework basiert. Diese Dokumentation soll dir helfen, das Projekt zu verstehen, es lokal einzurichten, zu nutzen und weiterzuentwickeln, auch wenn du keine Vorkenntnisse hast.


<details>
<summary>📂  <strong> Grundlagen Backend: Django & Python </strong></summary>

### **Was ist Django?**

Django ist ein leistungsstarkes, hochgradig konfigurierbares Webframework für Python. Es erleichtert die schnelle Entwicklung von sicheren und wartbaren Webseiten. [Offizielle Django-Dokumentation](https://docs.djangoproject.com/de/3.2/)

### **Was ist das Admin Panel?**

Das Django Admin Panel ist eine automatisch generierte Web-Oberfläche, die es Administratoren ermöglicht, Datenmodelle zu verwalten, ohne eigenen Code schreiben zu müssen. Es bietet eine benutzerfreundliche Oberfläche zum Hinzufügen, Bearbeiten und Löschen von Daten.

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

- **manage.py**: Ein Kommandozeilen-Tool zur Verwaltung des Django-Projekts.
- **project_name/**: Hauptverzeichnis des Projekts, enthält Einstellungen und Konfigurationen.
  - **settings.py**: Konfigurationsdatei für das Django-Projekt.
  - **urls.py**: URL-Routing für das Projekt.
  - **wsgi.py**: WSGI-Konfigurationsdatei für Deployment.
- **app_name/**: Verzeichnis einer Django-App innerhalb des Projekts.
  - **models.py**: Datenmodelle der jeweiligen App.
  - **views.py**: Logik für die Darstellung der Daten.
- **templates/**: HTML-Vorlagen.
- **static/**: Statische Dateien wie CSS, JS und Bilder.


</details>

<details>
<summary>🎨 <strong> Grundlagen Frontend: HTML & CSS </strong></summary>
<br>

**HTML-Dateien** definieren die Struktur und Inhalte der Webseiten. In Django werden sie meist im `templates/`-Verzeichnis der jeweiligen App abgelegt.  
**Beispiel:** `src/comments/templates/article_comments.html`  

Die Dateien enthalten oft spezielle Django-Template-Tags, um dynamische Inhalte einzubinden:  

```html
{% extends "base.html" %}
{% load static %}
```
Dies ermöglicht die Wiederverwendung einer Design-Basis und den Zugriff auf statische Ressourcen.

**CSS-Dateien** bestimmen das Aussehen und Layout der Webseiten. Diese befinden sich im static/css/ Verzeichnis.

**Beispiel:** `static/css/styles.css`

</details>

<details>
<summary>📜  <strong>Verwendung von JavaScript in Django Templates  </strong></summary>
<br>
JavaScript wird verwendet, um interaktive Funktionen auf deinen Webseiten bereitzustellen. In Django kannst du JavaScript-Dateien im `static/js/` Verzeichnis speichern und in deinen Templates einbinden.

### Einbindung von Skripten: Blocks und Static Files
Um JavaScript in deinen Django-Templates effektiv zu verwalten, kannst du Template-Blöcke verwenden. Dies ermöglicht es dir, spezifische Skripte auf bestimmten Seiten zu laden.
In der base.html Datei `src/templates/base.html` findest du den Javascripts Block: 
```html
<!-- JavaScript Block -->
    {% block scripts %}
    {% endblock %}
```
Dieser Block dient als Platzhalter für JavaScript-Code, der in untergeordneten Templates eingebunden wird.

### Beispiel: JavaScript in einer Unterseite einfügen

In einem spezifischen Template, z. B. article_comments.html, kannst du den Block wie folgt nutzen:

```html
{% extends "base.html" %}
{% block scripts %}
<script src="{% static 'js/article_comments.js' %}"></script>
{% endblock %}
```

#### Vorteile:
- Modularität: Skripte werden nur geladen, wenn sie tatsächlich benötigt werden.
- Performance: Weniger unnötige Skripte verbessern die Ladegeschwindigkeit.
- Wartbarkeit: Der Code bleibt übersichtlicher und einfacher zu verwalten.

</details>

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

Dies aktualisiert alle Migrationsskripte. Du kannst sie dann anwenden mit:

```bash
python3 src/manage.py migrate
```

</details>



details> <summary>📂 Projektstruktur</summary>
Projektstruktur
</details> <details> <summary> Frontend: HTML & CSS</summary>
Frontend: HTML & CSS
</details> <details> <summary> JavaScript Integration</summary>
JavaScript Integration
</details> <details> <summary>Datenbank & Modelle</summary>
Datenbank & Modelle
</details> <details> <summary>👥 Benutzerverwaltung</summary>
Benutzerverwaltung
</details> <details> <summary>🔗 API Endpunkte</summary>
API Endpunkte
</details> <details> <summary>🚀 Deployment</summary>
Deployment
</details> <details> <summary>✅ Best Practices & Tipps</summary>
Best Practices & Tipps
</details> <details> <summary>🛠️ Fehlerbehebung</summary>
Fehlerbehebung
</details> <details> <summary📚 Anhang </summary>
Anhang
</details>
