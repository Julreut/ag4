# Deployment-Anleitung

Diese Anleitung beschreibt, wie du das Projekt auf deinem Rechner startest. 

## Voraussetzungen

- **Git** muss installiert sein.
- **Docker** muss installiert sein.

Falls Docker noch nicht installiert ist, lade es hier herunter und installiere es:  
[https://www.docker.com/get-started](https://www.docker.com/get-started)

---

### 1. Repository klonen

Öffne ein Terminal und gib folgenden Befehl ein, um das Repo zu klonen und ins Projektverzeichnis wechseln

```sh
git clone [https://the-git.server/mirroronline.git] mirroronline
cd mirroronline
```

### 2. Docker-Compose verwenden:

   - Starte die Anwendung mit Docker-Compose:
     ```bash
     docker-compose up --build
     ```
   - Dieser Befehl baut die Docker-Images und startet die Container. Das kann einige Minuten dauern, da alle benötigten Abhängigkeiten installiert werden.


### 3. Anwendung im Browser aufrufen:*
   - Öffne einen Browser und gehe zu:
     ```
     http://127.0.0.1:8001/
     ```
   - Die Anwendung sollte nun erreichbar sein.

#### Alternative: Docker-Images ohne Docker-Compose starten

- Du kannst die Docker-Images auch ohne Docker-Compose starten. Kopiere dazu den folgenden Befehl ins Terminal:
  ```bash
  docker run -d \
    --name mirroronline \
    -p 8001:8000 \
    -v $(pwd)/data/:/ag4/data \
    mirroronline:latest

    Erklärung der Parameter:
	•	-d: Startet den Container im Hintergrund.
	•	--name mirroronline: Gibt dem Container den Namen „mirroronline“.
	•	-p 8001:8000: Leitet den internen Port 8000 auf Port 8001 auf deinem Rechner um.
	•	-v $(pwd)/data/:/ag4/data: Verbindet das lokale data/-Verzeichnis mit dem Verzeichnis /ag4/data im Container.
	•	mirroronline:latest: Verwendet das aktuellste Docker-Image „mirroronline“.


Info: Alle Instanzen erstellen beim ersten Start ein Datenverzeichnis unter ./data/ und kopieren ihre Vorlagen-Datenbank dorthin. Die Daten-Dateien repräsentieren die gesamte Instanz und können kopiert, ersetzt und gesichert werden. Sie bleiben auch bei der Zerstörung des Containers selbst erhalten.


Fertig! 🎉 Dein Projekt läuft jetzt lokal mit Docker. Falls Probleme auftreten, überprüfe die Fehlermeldungen im Terminal und stelle sicher, dass Docker korrekt installiert ist.

---

# Erste Schritte nach dem Deployment

<details><summary> Erster Schritt </summary>
Deine Instanz sollte nun unter der gewünschten Adresse und dem gewünschten Port laufen, z. B. `http://localhost:8001`. Bevor du nun loslegen kannst und Zeitungen und Artikel anlegen, benötigen wir einen Admin-Account. Anfangs gibt es noch keine Benutzerkonten im System, daher ist der **erste Schritt**, einen sogenannten **Superuser** zu erstellen:

Folge diesen Schritten:

### **Schritt 1: Shell im Docker-Container öffnen**
- Identifiziere zunächst den Namen des Django-Containers, der deine Anwendung ausführt:
```bash
  docker ps
```
- Öffne eine Shell im Container:
``` bash
docker exec -it <container_name> bash
```
Ersetze <container_name> durch den Namen deines Django-Containers.

### **Schritt 2: Superuser erstellen**
Führe den folgenden Befehl aus, um einen neuen Superuser zu erstellen:
```bash
python manage.py createsuperuser
```

Du wirst aufgefordert, die folgenden Details einzugeben:
**Benutzername:** Wähle einen Admin-Benutzernamen (z. B. admin).
**E-Mail:** Gib eine E-Mail-Adresse ein (optional).
**Passwort:** Setze ein sicheres Passwort und bestätige es.

### **Schritt 3: Mit dem neuen Superuser anmelden**

Sobald der Superuser erstellt wurde, kannst du dich mit den neuen Anmeldedaten im Admin-Panel anmelden:
- Das Admin-Panel ist unter `http://localhost:8001/admin` erreichbar.
- Verwende die oben angegebenen Admin-Anmeldedaten, um dich einzuloggen.
- Über das Admin-Panel kannst du Benutzer, Artikel, Kommentare und andere Daten verwalten.

</details>


---

<details><summary>Reguläre Benutzerkonten erstellen </summary>

Reguläre Benutzerkonten können direkt über das Admin-Panel erstellt werden:

- Gehe zu `http://localhost:8000/admin`.
- Navigiere zum Abschnitt Users.
- Klicke auf Add User.
- Fülle die erforderlichen Details aus (Benutzername, Passwort usw.).
- Speichere den Benutzer.

</details>

### Weitere Dokumentation

Weitere Details zur Nutzung der Plattform und des Admin-Panels findest du im [HOW TO](./2-how-to.md)-Dokument.
Dort findest du Schritt-für-Schritt-Anleitungen und Details zum Aufbau der Software

.

Mirror Online is a web app and can be used with any modern Desktop or Mobile web browser.
All administration functionality is available via the user interface admin route (https://example.com/admin) or via an API (https://example.com/api).


## Using the software for a study

From Fakebook: Important:

- When using our tool for research purposes, please cite our paper: Voggenreiter, A; Brandt S; Putterer, F; Frings, A and Pfeffer J. The Role of Likes: How Online Feedback Impacts Users' Mental Health (2023).
  https://arxiv.org/abs/2312.11914

- Fakebook allows to setup a Social-Media-Environment, in which users can interact freely. Every interaction can be watched and controlled by the project maintainer (e.g. the researcher). The project maintainer is responsible for everything happening on his or her social media environment. The tool should be used in an ethical responsible manner. Study participants and other users of the social media environment have to be informed that all of their data can be inspected by the project maintainer. The project maintainers are responsible for clarifying the standards of acceptable and hatefree behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior. Project maintainers have the right and responsibility to remove, edit, or reject posts and comments, or to ban temporarily or permanently any user for other behaviors that they deem inappropriate, threatening, offensive, illegal or harmful.


## Manuelles Deployment

Die Abhängigkeiten können installiert und die Software direkt ausgeführt werden. Dies ist nützlich für Entwicklungszwecke. Dies wird erreicht, indem eine virtuelle Umgebung erstellt, die erforderlichen Abhängigkeiten installiert und der Webserver wie folgt gestartet wird:

#### 1. **Virtualenv und Python 3 installieren**
Die Installation hängt von deinem Betriebssystem ab. Unter Linux (z. B. Ubuntu) kannst du folgende Befehle verwenden:

```shell
sudo apt install python3 python3-pip
sudo pip3 install virtualenv
```

#### 2. Repository klonen

Öffne ein Terminal und gib folgenden Befehl ein, um das Repo zu klonen und ins Projektverzeichnis wechseln

```sh
git clone [https://the-git.server/mirroronline.git] mirroronline
cd mirroronline
```

#### 3. Virtuelle Umgebung erstellen und aktivieren

Erstelle eine virtuelle Umgebung und aktiviere sie:

```sh
virtualenv .venv
source .venv/bin/activate
```

#### 4. Virtuelle Umgebung erstellen und aktivieren

Installiere die erforderlichen Abhängigkeiten:

```sh
pip install -r requirements.txt
```

#### 5. Static Files einsammeln

Sammle die statischen Dateien, damit sie in einer Produktionsumgebung bereitgestellt werden können:

```sh
python ./src/manage.py collectstatic
```

#### 5. Server starten

Entwicklungsserver starten.
```sh
python ./src/manage.py runserver 0.0.0.0:8000
```

Mit diesen Schritten kannst du die Software manuell auf deinem lokalen System bereitstellen. Dies ist besonders nützlich für Entwicklungs- und Testzwecke. Stelle sicher, dass Python 3 und Virtualenv installiert sind, bevor du beginnst. Falls du Fragen hast oder auf Probleme stößt, konsultiere die Dokumentation oder wende dich an deinen Entwickler. 😊
