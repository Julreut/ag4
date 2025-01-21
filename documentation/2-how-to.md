# Aufbau der Software


# Hinweise für Versuchsleiter

<details> <summary>Feature-Überblick</summary>

User:
- Artikel lesen: Zugriff auf veröffentlichte Zeitungsartikel.
- Kommentare schreiben: Artikel können kommentiert werden.
- Reaktionen: Kommentare können geliked und kommentiert werden.
- Benutzerprofile bearbeiten (Bio ändern).
- Andere Benutzerprofile und deren Bio ansehen.

Forschende:
- Hosting der Website: Anleitung dazu in Datei: ```deployment.md```.
- Nutzerinformationen einsehen: Name, User ID etc. (Passwörter sind nicht einsehbar).
- Nutzerverwaltung: Nutzer hinzufügen, entfernen und bearbeiten.
- Inhalte einsehen und bearbeiten: Zugriff auf Artikel, Kommentare, Likes und alle Interaktionen (über das Admin-Panel).
- Tracking-Daten einsehen: Verweildauer und Klickverhalten der Nutzer.
- Datenexport: Export der Daten als .xlsx-Datei (ausgewählte Tabellen oder gesamte Datenbank).
</details>

<details> <summary>Nutzerverwaltung für Forscher </summary>
Registrierung:

- Jede/r Nutzende kann sich direkt über die Registrierungsseite anmelden.
Nach dem Login haben Nutzende Zugriff auf die oben beschriebenen Features.

Admin-Zugriff:
- Forscher können über <URL>/admin auf die Administrationsseite zugreifen. 
- Login erfolgt mit Superuser-Zugangsdaten, die während der Einrichtung festgelegt wurden. Über die Admin-Seite können alle Module eingesehen und bearbeitet werden.
</details>

<details> <summary>🚀 Analytics App
</summary>

<br> TL;DR: Hier werden Nutzerdaten getrackt (User Event Log, Content Position) und Experimentalbedingung festgelegt.

- Admin Panel: 
    - Experiment Conditions: Hier werden die Experiment-Conditions festgelegt (falls vorhanden). Bisher werden nur die Zeitungen nach den Conditions gefiltert.

- Dateien: 
    - ```admin.py``` legt fest, wie die Conditions bearbeitet werden können.
    - ```models.py``` definiert Datenbanktabellen fuer 1. allgemeinen User Event Log, 2. Content Position (Anzeigeposition Artikel, Zeitung etc.) fuer jeweiligen User, 3. ExperimentCondition
    - ```urls.py``` enthaelt URL fuer Javascript User Event Logging
    - ```utils.py``` create_event_log erstellt einen UserEventLog-Eintrag mit validierten JSON-Daten
    - ```views.py``` log_user_action loggt Javascript User Actions
</details>


<details> <summary>Articles App (Zeitungen und Artikel)
</summary>
<br> TL;DR: Hier passiert die Verwaltung und Darstellung von Zeitungen und Artikeln. Das Admin-Panel ermöglicht die dynamische Anpassung und CSV-Exporte. Die Models definieren die Struktur von Zeitungen und Artikeln, und die Templates sorgen für die Anzeige von Listen und Details.

## Admin Panel:
- **Zeitungen und Artikel verwalten**: Hier können Zeitungen und Artikel bearbeitet und verwaltet werden. Zusätzlich können Experiment-Conditions für Tags dynamisch aus einer separaten Tabelle (`ExperimentCondition`) geladen werden.
- **CSV-Export**: Es ist möglich, Daten zu Zeitungen und Artikeln als CSV-Datei herunterzuladen.

## Dateien:
- ```admin.py```: 
  - Legt fest, wie Zeitungen und Artikel im Admin-Panel bearbeitet werden können.
  - Ermöglicht den CSV-Export von Artikeln und Zeitungen.
  - Dynamische Dropdown-Menüs für Tags basierend auf den `ExperimentCondition`-Daten.

- ```models.py```:
  - Definiert die Datenbanktabellen für:
    1. **NewsPaper**: Enthält Informationen zu Zeitungen wie Name, Bild und Tag.
    2. **Article**: Enthält Informationen zu Artikeln wie Titel, Inhalt, Slug, Bild und zugehörige Zeitung.
  - Beide Modelle bieten Methoden zur Generierung von `absolute_url`-Links und zur automatischen Erstellung von Slugs.

- ```urls.py```:
  - Enthält die URLs für:
    1. **Alle Zeitungen anzeigen** (`/`).
    2. **Artikel einer Zeitung auflisten** (`/article_list/<int:news_paper_id>/`).
    3. **Detailansicht eines Artikels** (`/<int:news_paper_id>/<slug:slug>/`).

- ```apps.py```:
  - Registriert die App unter dem Namen `'articles'`.

## Templates:
- **`all_articles.html`**: Listet alle Artikel einer spezifischen Zeitung.
- **`detailed_article.html`**: Zeigt die Detailansicht eines Artikels.
- **`news_papers.html`**: Zeigt eine Übersicht aller Zeitungen.

</details>


<details> <summary>💬 Comments App</summary>

<br> **TL;DR:** Die Comments App ermöglicht es Benutzern, Kommentare zu Artikeln zu verfassen, zu liken/disliken, und in einer strukturierten Ansicht darzustellen. Es werden sowohl Haupt- als auch Sekundärkommentare (Antworten) unterstützt.

- **Admin Panel:**
    - Kommentare verwalten:
        - Kommentare können als öffentlich oder privat markiert werden. Öffentliche Kommentare sind sichtbar für alle Nutzer. Private Kommentare sind nur für den jeweiligen Autor selbst sichtbar.
        - Experimentelle Bedingungen (`tag`) können dynamisch zugewiesen werden. (Still TODO das in den views zu hinterlegen)
        - Likes und Dislikes werden detailliert angezeigt und gefiltert.

- **Dateien:**
    - **`article_comments.html`**: Template für die Haupt-Kommentarseite eines Artikels. 
        - Zeigt Hauptkommentare und deren Antworten an.
        - Ermöglicht das Liken/Disliken und Hinzufügen neuer Kommentare.
    - **`detailed_comment.html`**: Template für die Detailansicht eines Kommentars.
        - Zeigt einen spezifischen Kommentar und seine Antworten.
        - Ermöglicht das Hinzufügen von Sekundärkommentaren.
    - **`admin.py`**: 
        - Registriert Modelle (`Comment`, `Like`, `Dislike`) im Admin-Bereich.
        - Ermöglicht schnelles Erstellen von Kommentaren.
    - **`forms.py`**:
        - Stellt Formulare für Haupt- und Sekundärkommentare bereit, inklusive dynamischer Felder.
    - **`models.py`**:
        - `Comment`: Hauptmodell für Kommentare, unterstützt hierarchische Strukturen (Antworten).
        - `PlannedReaction`: Ermöglicht geplante Reaktionen auf Kommentare.
        - `Like` & `Dislike`: Modelle zur Verwaltung von Reaktionen.
    - **`urls.py`**:
        - Definiert Routen für:
            - Kommentarseiten eines Artikels.
            - Detailansicht eines spezifischen Kommentars.
            - Like/Dislike-Aktionen.
    - **`views.py`**:
        - `article_comments_view`: 
            - Lädt Hauptkommentare in zufälliger, aber stabiler Reihenfolge.
            - Unterstützt das Hinzufügen von Haupt- und Sekundärkommentaren.
        - `detailed_comment_view`: 
            - Zeigt Details eines einzelnen Kommentars und seiner Antworten an.
            - Ermöglicht das Antworten auf Kommentare.
        - `like_unlike_comment` & `dislike_undislike_comment`:
            - Verarbeiten Like/Dislike-Aktionen und loggen Änderungen.
</details>

<details> <summary>Configuration App</summary>
x
</details>


<details> 
<summary>📘 Fakebook App</summary>

<br> **TL;DR:** **TL;DR:** Kernstück der Anwendung im Backend src-folder zur Verwaltung von Benutzerdaten, Interaktionen und Experimentbedingungen.

---

### **Funktionalitäten**

- **Benutzerverwaltung**:
  - Registrierung und Anmeldung mit optionaler Anpassung von Benutzerprofilen.
  - Benutzer können über das Admin-Panel manuell erstellt werden.

- **Interaktionen**:
  - Beiträge (Posts), Kommentare, Likes und Dislikes sind zentrale Funktionen.
  - Aktivitäten wie das Betrachten von Beiträgen und Interaktionen werden für Analysen geloggt.

- **Datenexport**:
  - Ermöglicht den Export der Datenbank (CSV, XLSX, SQLite).
  - Exportiert auch hochgeladene Bilder oder andere Mediendateien.

- **Zeiterfassung**:
  - Ein Middleware-basierter Timer erfasst die Verweildauer der Benutzer auf spezifischen Seiten und leitet bei Überschreiten der Zeit zur nächsten Experimentphase weiter.

---

### **Admin Panel:**
- **Nutzererstellung**:
  - Admins können Benutzer und Profile direkt über ein spezielles Interface erstellen.
- **Datenexport**:
  - Tools zum Herunterladen der Datenbank und spezifischer Tabellen.
- **Sitzungskonfiguration**:
  - Anpassung der maximalen Sitzungsdauer und Aktivierung/Deaktivierung des Timers.

---

### **Dateien**

#### **`urls.py`**
Definiert Routen für verschiedene Funktionen:
- **Benutzererstellung**:
  - `/admin/user_creation_view` – Formular für die Benutzererstellung.
- **Datenexport**:
  - `/admin/download_xlsx` – Export von Datenbanktabellen als XLSX.
  - `/admin/download_database` – Download der gesamten SQLite-Datenbank.
  - `/admin/download_pictures` – Herunterladen von Mediendateien (z. B. Profilbilder).
- **Allgemeine Navigation**:
  - Verlinkung der Apps `profiles`, `questions`, `comments`, etc.

#### **`views.py`**
- **`home_view`**:
  - Startpunkt der App, leitet Benutzer basierend auf ihrem Status (z. B. Admin oder Teilnehmer) weiter.
- **`user_creation_view`**:
  - Ansicht zur Benutzererstellung durch Admins.
- **`download_xlsx`**:
  - Generiert eine XLSX-Datei mit ausgewählten Datenbanktabellen.
- **`download_database`**:
  - Stellt die SQLite-Datenbank als Download bereit.
- **`download_pictures`**:
  - Komprimiert Mediendateien (z. B. Bilder) in ein ZIP-Archiv und stellt sie zum Download bereit.

#### **`middleware.py`**
- **NewspaperTimerMiddleware**:
  - Verfolgt die Verweildauer von Benutzern auf bestimmten Seiten.
  - Automatische Weiterleitung nach Ablauf der maximalen Sitzungszeit.

#### **`settings.py`**
- Definiert globale Einstellungen der Fakebook App:
  - **Datenbank**: SQLite als Standard.
  - **Statische Dateien**:
    - Statische Inhalte (CSS, JS) und Mediendateien sind konfigurierbar.
  - **Zeitzonen und Sprache**:
    - Standardmäßig `en` als Sprache und UTC als Zeitzone.
  - **Externe Authentifizierung**:
    - Integration von `django-allauth` für Benutzerverwaltung.

---

### **Datenexport**

#### **`downloads.py`**
- Enthält Tools zum Erstellen von Download-Dateien:
  - **CSV-Export**:
    - Erstellt CSV-Dateien basierend auf Datenbanktabellen.
  - **XLSX-Export**:
    - Generiert Excel-Dateien mit ausgewählten Tabellen.
  - **Datenbank-Download**:
    - Stellt die gesamte SQLite-Datenbank als Datei bereit.
  - **Mediendateien**:
    - Komprimiert ausgewählte Mediendateien (z. B. Bilder) in ein ZIP-Archiv.

---

### **Wichtige Features für Versuchsleiter**

1. **Timer und Weiterleitung**:
   - Überwachung der Sitzungszeit mit automatischer Weiterleitung zu spezifischen Seiten.
   - Anpassbar über das `SessionConfig` Modell im Admin-Panel.

2. **Profilverwaltung**:
   - Automatisches Anlegen von Benutzerprofilen bei der Registrierung.
   - Verwaltung der Profilbilder und anderer Benutzerdaten.

3. **Export-Tools**:
   - Datenbanktabellen, Mediendateien und andere Daten können direkt heruntergeladen werden.

---

</details>


<details> <summary>👤 Profiles App</summary>

<br> **TL;DR:** Die Profiles App ermöglicht die Verwaltung von Benutzerprofilen, einschließlich Biografie, Profilbild und experimentellen Bedingungen. Sie bietet Funktionen zur Ansicht und Bearbeitung des eigenen Profils, zur Anzeige anderer Profile sowie zur automatischen Zuweisung von experimentellen Bedingungen bei der Anmeldung.

- **Admin Panel:**
    - **Profile Management:** 
        - Benutzerprofile können angezeigt, bearbeitet und als CSV exportiert werden.
        - Anzeigen von Details wie Benutzername, Biografie, Slug und experimentelle Bedingung.

- **Dateien:**
    - **`urls.py`**:
        - Definiert Routen für:
            - Eigenes Profil (`my_profile_view`)
            - Detailansicht einzelner Profile (`ProfileDetailView`).
    - **`views.py`**:
        - **`my_profile_view`**:
            - Ermöglicht die Ansicht und Bearbeitung des eigenen Profils.
            - Zeigt alle Kommentare des Nutzers an (nur explizit öffentliche für andere Benutzer).
        - **`ProfileDetailView`**:
            - Detailansicht eines Profils, inklusive Biografie und Kommentare.
    - **`models.py`**:
        - **`Profile`**:
            - Modell für Benutzerprofile mit Feldern wie `bio`, `avatar`, `slug` und `condition`.
            - Automatische Slug-Generierung für eindeutige Profil-URLs.
    - **`forms.py`**:
        - **`ProfileModelForm`**:
            - Formular zur Bearbeitung von Biografie und Profilbild.
    - **`signals.py`**:
        - **Benutzererstellung**:
            - Automatische Erstellung eines Profils und einer Zustimmungserklärung (`Consent`) bei Registrierung.
        - **Experimentbedingungen**:
            - Zuweisung einer zufälligen experimentellen Bedingung bei Login, falls noch nicht zugewiesen.
        - **Logging**:
            - Ereignisprotokollierung bei Benutzeranmeldung und -abmeldung, einschließlich IP-Tracking.
    - **`utils.py`**:
        - **`get_random_string`**:
            - Generiert zufällige Zeichenfolgen zur Sicherstellung eindeutiger Slugs.
    - **`admin.py`**:
        - Registrierung des `Profile`-Modells im Admin-Bereich mit CSV-Exportfunktion.

</details>


<details> <summary>❓ Questions App</summary>

<br> **TL;DR:** Die Questions App ist unser SoSciSurvey-Nachbau. Sie ermöglicht es, Fragebögen zu erstellen und zu verwalten, die vor und nach dem Experiment ausgefüllt werden. Sie unterstützt verschiedene Fragetypen, Einverständniserklärungen und benutzerdefinierte Endnachrichten. 

- **Admin Panel:**
    - **Question Management**:
        - Fragetypen (z. B. Dropdown, Likert-Skala, Slider) und Eigenschaften (z. B. Pflichtfrage, Min-/Max-Werte) können hier konfiguriert werden.
        - `choices`, `sub_questions` und `sub_choices` definieren Antwortmöglichkeiten für spezifische Fragetypen.
        - Fragetyp-spezifische Validierungen werden automatisch ausgeführt.
    - **Text Management**:
        - Texte für Einverständniserklärung, Endnachrichten und Teilnehmerinformationen werden über `Text` verwaltet. Diese sollten im HTML Format eingefuegt werden, um gute Lesbarkeit zu garantieren. Sichtbarkeit (`visibility`) der Texte steuert deren Anzeige im Frontend.
    - **Session Configuration**:
        - Maximale Sitzungsdauer und Timer (an/aus) können im `SessionConfig` Modell konfiguriert werden.

- **Dateien:**
    - **`urls.py`**:
        - Definiert Routen für verschiedene Phasen des Experiments:
            - Teilnehmerinformationen (`participant_info`)
            - Einverständniserklärung (`consent_form`)
            - Fragebögen vor/nach dem Experiment (`questions_before`/`questions_after`)
            - Abschlussseite (`experiment_end`).
    - **`models.py`**:
        - **`Question`**:
            - Ermöglicht die Definition von Fragen mit unterschiedlichen Typen und Antwortmöglichkeiten.
            - Fragetypen: `dropdown`, `slider`, `multiple_choice`, `single_choice`, u. a.
            - Validierungen: z. B. Pflichtfelder, Min-/Max-Werte.
        - **`Answer`**:
            - Speichert Antworten, einschließlich Sub-Fragen (z. B. bei Likert-Skalen).
        - **`Text`**:
            - Verwalten von statischen Texten für Consent-Formulare, Endseiten und Teilnehmerinformationen.
        - **`SessionConfig`**:
            - Timer- und Sitzungsdauer-Management.
    - **`views.py`**:
        - **`experiment_start`**:
            - Begrüßungsseite mit Optionen für Erst- und Wiederholungsteilnehmer.
        - **`participant_info`**:
            - Zeigt konfigurierbare Teilnehmerinformationen an (`Text` Modell).
        - **`consent_form`**:
            - Zeigt die Einverständniserklärung an und verarbeitet die Auswahl.
            - Redirect bei Zustimmung oder Ablehnung.
        - **`question_list`**:
            - Dynamische Anzeige von Fragebögen basierend auf Labels (`before`, `after`).
            - Unterstützung für verschiedene Fragetypen (Dropdown, Likert, Slider).
            - Beantwortungspflicht wird validiert.
        - **`experiment_end`**:
            - Abschlussnachricht mit Logout-Option.
        - **`not_eligible`**:
            - Zeigt eine Nachricht für nicht teilnahmebereite Personen an.
    - **`templates/`**:
        - **`consent_form.html`**: Einverständniserklärung mit Auswahlmöglichkeit (Ja/Nein).
        - **`question_list.html`**: Dynamischer Fragebogen mit Fortschrittsanzeige.
        - **`end.html`**: Abschlussseite des Experiments.
        - **`participant_info.html`**: Informationen für Teilnehmer.
        - **`start.html`**: Begrüßungsseite für die Studie.
        - **`not_eligible.html`**: Nachricht für Teilnehmer, die die Einverständniserklärung verweigern.
    - **`utils.py`**:
        - **`calculate_questionnaire_duration`**:
            - Berechnet die Dauer für das Ausfüllen eines Fragebogens basierend auf Event-Logs. (Still TODO)

## Wichtig für den Versuchsleiter:

#### Anpassbare Texte:
- Texte für Consent-Formulare, Endnachrichten und Teilnehmerinformationen können im Admin-Bereich (Modell `Text`) bearbeitet werden.
- Die Sichtbarkeit (`visibility`) steuert, welche Texte im Frontend angezeigt werden.

#### Fragebögen erstellen:
- Fragen können im Admin-Bereich unter `Question` hinzugefügt werden.
- Fragetypen sind flexibel (z. B. Dropdown, Slider, Likert).
- `choices` und `sub_questions` müssen bei entsprechenden Fragetypen definiert werden.

#### Validierungen und Pflichtfelder:
- Pflichtfragen und spezifische Validierungen (z. B. Min-/Max-Werte) sind automatisiert.

#### Einverständniserklärung:
- Bei Ablehnung wird automatisch eine "Nicht teilnahmefähig"-Seite angezeigt.
- Consent-Status wird im Modell `Consent` gespeichert.

#### Timer und Sitzungskonfiguration:
- Sitzungsdauer (`max_duration`) und Timer können über das Modell `SessionConfig` angepasst werden.

#### Debugging und Logs:
- Änderungen an Fragen werden im Admin-Bereich geloggt.
- Event-Logs (z. B. `questions_started`, `questions_completed`) sind verfügbar für Analysen.

#### Vollständiger Ablauf:
1. Start: Begrüßung und Teilnehmerinfo.
2. Login (Start des Trackings)
3. Vor-Experiment-Fragen → Experiment → Nach-Experiment-Fragen
4. Abschlussseite.
</details>

<details> <summary>🗂️ Static Project & Templates</summary>

### **Static Project**
Das Verzeichnis `static_project` enthält alle statischen Dateien, die für das Frontend benötigt werden, einschließlich CSS, JavaScript und Bilder. Statische Dateien werden genutzt, um Styles, Interaktivität und visuelle Assets bereitzustellen, die für die Benutzererfahrung relevant sind.

#### **Unterverzeichnisse:**
1. **`css/`**:
    - Enthält Stylesheets für verschiedene Bereiche und Funktionen der Anwendung:
        - **`articles.css`**: Styling für Artikelansichten.
        - **`base.css`**: Basis-Styling für die gesamte Anwendung.
        - **`comments.css`**: Styling für die Kommentaransichten.
        - **`experiment.css`**: Spezielle Styles für Experiment-bezogene Seiten.
        - **`login-signup-custom-style.css`**: Anpassungen für die Login- und Registrierungsseiten.
        - **`newspaper.css`**: Styling für Zeitungsansichten.
        - **`questions.css`**: Styles für Fragebögen.
        - **`style.css`**: Generelle Styles.
        - **`grid.css`**: Grid-Layout-Styles für die Anordnung von Elementen.
    - **Favicons**:
        - `favicon.ico` und `favicon2.ico` dienen als kleine Icons für den Browser-Tab der Website.

2. **`js/`**:
    - **`log.js`**: JavaScript-Datei für Logging-Funktionen (z. B. Nutzerinteraktionen).
    - **`main.js`**: Haupt-JavaScript-Datei für allgemeine Interaktivität und Logik.

---

### **Templates**
Das `templates`-Verzeichnis enthält HTML-Dateien, die das Frontend der Anwendung definieren. Es ist in verschiedene Unterverzeichnisse organisiert:
- **`account/`**: Templates für Login, Registrierung und Konto-Verwaltung.
- **`admin/`**: Templates für den Admin-Bereich.
- **`main/`**: Generelle Templates für Hauptseiten der Anwendung.
- **`base.html`**: Basis-Template, das von anderen Templates erweitert wird.
- **`lib-jquery.html`**: Einbindung von jQuery-Bibliotheken.
- **`ui-template-stylesheets.html`**: Template für die Einbindung von CSS-Dateien.

---

### **Django und `collectstatic`**
- **Statische Dateien in Django**:
    - Alle statischen Ressourcen, wie CSS, JavaScript und Bilder, werden im Entwicklungsmodus direkt aus dem `static_project`-Verzeichnis geladen.
    - Im Produktionsmodus werden alle statischen Dateien an einem zentralen Speicherort gesammelt.

- **Befehl `collectstatic`**:
    - Mit dem Befehl `python manage.py collectstatic` werden alle Dateien aus den `static`-Verzeichnissen in den in der `settings.py` definierten `STATIC_ROOT`-Ordner kopiert.
    - Dieser zentrale Speicherort ermöglicht die effiziente Bereitstellung der statischen Ressourcen durch einen Webserver (z. B. Nginx).

- **Wichtig für den Versuchsleiter:**
    - Änderungen an den CSS- oder JavaScript-Dateien im `static_project`-Verzeichnis erfordern einen erneuten Aufruf von `collectstatic`, damit die aktualisierten Dateien auf dem Produktionsserver verfügbar sind.
    - Der Speicherort für die statischen Dateien wird in den Django-Einstellungen mit `STATIC_ROOT` festgelegt.

---

### **Zusammenfassung**
Das `static_project`-Verzeichnis ist für die Bereitstellung und Verwaltung von Styles und Interaktivität verantwortlich. Durch das `templates`-Verzeichnis wird sichergestellt, dass die Benutzeroberfläche modular und erweiterbar bleibt. Der `collectstatic`-Prozess spielt eine entscheidende Rolle, um alle statischen Dateien für die Produktion zentral bereitzustellen.

</details>

<details> <summary>🔧 Base Template und Navbar</summary>

<br> TL;DR: Das Base Template `base.html` dient als **Grundgerüst für alle HTML-Dateien** der Anwendung. Es enthält allgemeine Layout- und Design-Elemente, die in anderen Templates wiederverwendet werden. Alle spezifischen Seiten basieren auf diesem Template und ergänzen oder überschreiben dessen Inhalte mithilfe von **`{% block ... %}` und `{% endblock %}`**. Die Navigationsleiste `navbar.html` bietet Zugriff auf zentrale Funktionen und wird ebenfalls auf allen Seiten eingebunden.


#### **Was passiert in `base.html`?**
1. **Grundstruktur**:
    - `<!doctype html>` definiert das Dokument als HTML5.
    - Das Template bindet wichtige **Meta-Tags** (z. B. für die mobile Ansicht) und Basis-Ressourcen ein.

2. **Statische Dateien**:
    - **CSS**: Mehrere Stylesheets für unterschiedliche Komponenten der Anwendung werden über `{% static %}` eingebunden:
        - z. B. `style.css`, `articles.css`, `comments.css`.
    - **JavaScript**: Funktionen für Logging (`log.js`) und Interaktivität (`main.js`) werden ebenfalls eingebunden.

3. **Blöcke für Erweiterungen**:
    - **`{% block title %}`**: Ermöglicht das Setzen eines individuellen Titels für jede Seite.
    - **`{% block content %}`**: Hauptinhalt der Seite, der von spezifischen Templates überschrieben wird.
    - **`{% block scripts %}`**: Ermöglicht das Einfügen von seitenabhängigen JavaScript-Funktionen.

4. **Navbar**:
    - Das Template bindet die Navigationsleiste (`navbar.html`) ein, die auf jeder Seite angezeigt wird.

5. **CSRF und URLs**:
    - Die **CSRF-Token** und wichtige URLs (z. B. `analytics:log_user_action`) werden als JavaScript-Variablen definiert, damit sie für Frontend-Skripte verfügbar sind.

#### **Warum ist `base.html` wichtig?**
- **Wiederverwendbarkeit**: Alle Templates bauen auf `base.html` auf. Änderungen an der Struktur oder dem Design müssen nur hier vorgenommen werden.
- **Erweiterbarkeit**: Mithilfe von **`{% block ... %}`** können Inhalte leicht angepasst werden, ohne die Grundstruktur zu verändern.

---

### **Navbar (`navbar.html`)**

#### **Funktionalität der Navbar:**
1. **Benutzerstatus**:
    - Wenn der Benutzer **nicht eingeloggt** ist, zeigt die Navbar nur eine Login-Option an.
    - Wenn der Benutzer **eingeloggt** ist:
        - Zeigt Links zu wichtigen Bereichen, wie **News-Papers**, **Profil** und **Experiment-Ende**.
        - Das Profilbild des Benutzers wird angezeigt.
        - Links zum Logout und zum Abbruch des Experiments stehen zur Verfügung.

2. **Timer-Funktion**:
    - Zeigt die verbleibende Zeit des Experiments an.
    - Wenn die Zeit abgelaufen ist, wird der Benutzer automatisch auf die Seite für **Nach-Experiment-Fragen** umgeleitet.

3. **Flexibilität**:
    - Die Navbar passt sich dynamisch basierend auf dem Benutzerstatus und der Sitzungskonfiguration (`MAX_SESSION_DURATION`) an.

---

### **Blöcke in Templates verwenden**
Templates, die auf `base.html` basieren, verwenden folgende Syntax, um Inhalte hinzuzufügen oder anzupassen:
- **`{% block title %}`**: Setzt den Titel der Seite, z. B. "News-Papers".
- **`{% block content %}`**: Fügt den Hauptinhalt der spezifischen Seite ein.
- **`{% block scripts %}`**: Fügt zusätzliche JavaScript-Funktionen ein.

Beispiel:
```html
{% extends "base.html" %}

{% block title %} Meine Seite {% endblock title %}

{% block content %}
<div>
  <h1>Willkommen!</h1>
  <p>Das ist eine spezifische Seite.</p>
</div>
{% endblock content %}
{% block scripts %}
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('clickMeButton');
    button.addEventListener('click', function() {
      document.getElementById('greeting').textContent = "Danke für deinen Klick!";
      button.disabled = true;
    });
  });
</script>
{% endblock scripts %}
```
</details>

<details> <summary> manage.py in Django</summary>
<br> TL;DR:Die Datei `manage.py` ist ein zentraler Bestandteil jeder Django-Anwendung. Sie dient als **Schnittstelle für administrative Aufgaben** und wird verwendet, um verschiedene Befehle auszuführen.

---

#### **Hauptfunktionen:**
1. **Starten des Servers:**
```bash
python src/manage.py runserver
```
2. **Migrationen:**
```bash
python src/manage.py makemigrations
python src/manage.py migrate
```

3. **Statische Dateien sammeln:**
```bash
python src/manage.py collectstatic
```

4. **Interaktive Shell:**
```bash
python src/manage.py shell
```

5. **Alle Befehle anzeigen/ Hilfe:**
```bash
python src/manage.py help
```
</details>


<details> 
<summary>🛠 Kleine Änderungen vornehmen</summary>

### Beispielhafte Schritte, um den "Cancel Experiment"-Button zu entfernen:

1. **Datei öffnen**:
   Öffne die Datei `navbar.html` in deinem Code-Editor.

2. **Button entfernen**:
   Finde den folgenden Codeabschnitt in der Datei:

   ```html
   <a href="{% url 'account_logout' %}" class="ui item">
     <i class="fas fa-sign-out-alt"></i>&nbsp;
     Cancel (Quit Experiment) 
   </a>

3. **Zeilen Auskommentieren über cmd+shift+7 (Mac)**
4. **Änderungen speichern**
5. **Server neu starten**

</details>