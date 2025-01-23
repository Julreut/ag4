# Best Practices & Tipps zum Fehler beheben

Hier findest du eine strukturierte Übersicht über Best Practices und Tipps zur Fehlerbehebung in Django-Projekten.

---

<details>
<summary>Code-Organisation</summary>

- Halte deine Apps modular und übersichtlich.
- Verwende eine sinnvolle Ordnerstruktur, z. B. `/apps`, `/core`, `/utils`.
- Gruppiere verwandte Funktionen in Services, Serializern und Views.
- Verwende Funktionen wie `Prefetch` und `annotate` für optimierte Datenbankabfragen.

</details>

---

<details>
<summary>Versionskontrolle</summary>

- Nutze Git effektiv mit klaren Commit-Nachrichten (`feat:`, `fix:`, `refactor:`).
- Verwende Branch-Strategien wie Git Flow (`main`, `develop`, `feature/`).
- Füge `.gitignore` hinzu, um sensible Dateien wie `.env` und `*.sqlite3` auszuschließen.
- Stelle sicher, dass du vor dem Deployment alle Änderungen in der Produktion testest.

</details>

---

<details>
<summary>Sicherheit</summary>

- Schütze sensible Daten mit Umgebungsvariablen (z. B. über `python-decouple`).
- Halte Django und alle Abhängigkeiten aktuell (`pip list --outdated`).
- Nutze Django's `SECURE_*`-Einstellungen (z. B. `SECURE_SSL_REDIRECT`, `CSRF_COOKIE_SECURE`).
- Vermeide die Verwendung von `DEBUG=True` in Produktionsumgebungen.
- Sichere dein Admin-Panel, indem du es hinter einem VPN oder unter einem benutzerdefinierten Pfad (z. B. `/secret-admin`) versteckst.

</details>

---

<details>
<summary>Dokumentation</summary>
- Halte die Dokumentation aktuell und umfassend.
- Nutze Markdown-Dateien (`README.md`, `CHANGELOG.md`) für zentrale Informationen.
- Dokumentiere komplexe Logik mit Kommentaren im Code.
</details>


## Fehlerbehebung

Hier sind einige häufige Probleme und deren Lösungen:

---

<details>
<summary>Fehler beim Migration durchführen</summary>

**Problem:** `ModuleNotFoundError`  
**Lösung:**  
- Stelle sicher, dass alle Apps in `INSTALLED_APPS` aufgeführt sind.  
- Überprüfe, ob die virtuelle Umgebung aktiviert ist.  
- Führe die folgenden Befehle aus:  
  ```bash
  python manage.py makemigrations
  python manage.py migrate
</details>

---

<details> <summary>Statische Dateien werden nicht geladen</summary>

**Problem:** CSS oder JS wird nicht angezeigt.
**Lösung:**
- Führe python manage.py collectstatic aus.
- Stelle sicher, dass die Django-Einstellungen für STATICFILES_DIRS und STATIC_ROOT korrekt sind.
- Führe `python manage.py collectstatic` aus und überprüfe die Nginx/Apache Konfiguration.
</details>

---

<details> <summary>Admin Panel funktioniert nicht </summary>

**Problem:** Zugriff verweigert oder Seite nicht gefunden.  
**Lösung:** 
- Stelle sicher, dass du einen Superuser erstellt hast (`python manage.py createsuperuser`) und dass die URL-Konfiguration korrekt ist. ```path('admin/', admin.site.urls)```

</details>

---

<details> <summary>JavaScript-Probleme/ Logs werden nicht gespeichert</summary>

**Problem:** Javascript funktioniert nicht richtig / Log wird nicht korrekt gespeichert.  
**Lösung:** 
- Überprüfe in `analytics/views` die Funktion `log_user_action`, ob alle relevanten Actions korrekt verarbeitet werden.
- Debugge die Datenverarbeitung, indem du Folgendes hinzufügst:
```print("Empfangene Daten:", request.body)```

</details>
