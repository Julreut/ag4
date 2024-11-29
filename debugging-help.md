# Debugging Help

## Inhaltsverzeichnis

1. [Problem: `django.contrib.sites` verwendet die falsche Standard-Domain](#problem-djangocontribsites-verwendet-die-falsche-standard-domain)
    - [Lösung: Standard-Domain in der `Site`-Datenbank aktualisieren](#lösung-standard-domain-in-der-site-datenbank-aktualisieren)

### Problem: `django.contrib.sites` verwendet die falsche Standard-Domain (bspw. example.com)

Wenn du das `sites`-Framework aktiviert hast (`django.contrib.sites`), könnte Django die falsche Domain wie `example.com` verwenden, was zu unerwartetem Verhalten führt, z. B. bei URL-Generierungen.

### Ursache
Die Standard-Domain in der `Site`-Datenbank ist falsch konfiguriert (z. B. `example.com` anstelle von `127.0.0.1:8000`).

---

## Lösung: Standard-Domain in der `Site`-Datenbank aktualisieren

### 1. Öffne die Django-Shell
```bash
python manage.py shell
```
### 2. Überprüfe die aktuell registrierten Sites
```bash
from django.contrib.sites.models import Site
print(Site.objects.all())  # Zeigt alle registrierten Sites an
```
### 3. Ändere die Domain
```bash
site = Site.objects.get(pk=1)
site.domain = '127.0.0.1:8000'
site.name = 'Localhost'
site.save()
```
Stelle sicher, dass deine aktuelle Entwicklungs-Domain (127.0.0.1:8000) in der Site-Datenbank korrekt eingetragen ist. Jetzt sollte Django URLs mit der richtigen Domain generieren.
