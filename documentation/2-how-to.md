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


 <details> <summary>Comments App</summary>
x</details> 


<details> <summary>Configuration App</summary>
x
</details>


<details> <summary> Fakebook App</summary>
x
</details>


</details> <details> <summary> Profiles App</summary>
x
</details>

<details> <summary> Questions App</summary>
x
</details>


<details> <summary> Static Project & Templates</summary>
x
</details>