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

<details> <summary>🚀 Articles App (Zeitungen und Artikel)
</summary>

Artikel:
Alle Artikel werden in der Admin-Ansicht unter Artikel gelistet.
Forscher können neue Artikel hinzufügen oder bestehende bearbeiten.

Felder zur Bearbeitung eines Artikels:
Titel: Titel des Artikels.
Inhalt: Text des Artikels.
Autor: Kann ein Nutzer oder ein künstlicher Nutzer sein.
Kommentare:
Kommentare zu Artikeln werden unter Kommentare verwaltet.
Felder zur Bearbeitung eines Kommentars:
Artikel: Artikel, zu dem der Kommentar gehört.
Inhalt: Text des Kommentars.
Autor: Der Nutzer, der den Kommentar verfasst hat.

</details>

 <details> <summary>✅ xx</summary>
x</details> <details> <summary>🛠️ xx</summary>
x
</details> <details> <summary>📚 xx </summary>
x
</details>