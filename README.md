# Mirronline

Dies ist das Haupt-Repository des Mirror-Online-Projekts, einer Plattform, die eine Online-Forum-Umgebung ähnlich Spiegel Online für Forschungszwecke simuliert. Die Plattform ermöglicht es Forschenden, komplexe Interaktionen und Verhaltensmuster in einer kontrollierten und anpassbaren Umgebung zu analysieren.

## Nutzung des Tools

Mehr Informationen zu verwendeten Tools, Software-Aufbau, Deployment uvm. befinden sich im Ordner [Dokumentation](./Dokumentation) dieses Repositories.

### Requirements installieren

```bash
pip install -r requirements.txt
```

### Virtuelle Umgebung verwalten

Es wird empfohlen, eine virtuelle Umgebung zu verwenden, um Abhängigkeiten isoliert zu halten.

#### Virtuelle Umgebung erstellen

Erstelle eine virtuelle Umgebung namens `env`:

```bash
python3 -m venv env
```

#### Virtuelle Umgebung aktivieren

- **Windows:**

```
env\Scripts\activate
```

- **macOS/Linux:**

```
source env/bin/activate
```

#### Virtuelle Umgebung deaktivieren

Deaktiviere die virtuelle Umgebung mit:

```
deactivate
```

### Server starten:

```
python3 src/manage.py runserver
```

Öffne dann deinen Webbrowser und gehe zu `http://127.0.0.1:8000/`, um die Anwendung zu sehen.

The docker build process will not run database migrations. The application will repopulate its data folder using the template on startup if it detects its data to be missing. You will therefore have to **copy your migrated database file over to the** `data.template` folder when you migrate the database during development.
This also means that you will have to run them manually in case you want to update the database of a deployed instance to a new schema.

#### Database migration for deployed instance

The docker container and application do not migrate an existing DB automatically when upgraded. You will therefore have to manually migrate the database when updating the version / schema on a deployed instance.

This can be achieved by downloading the database and running migrations locally.
Another option is to run the migrations using the deployed instance in the docker container. This can be achieved by e.g. manipulating the start command of the deployed docker container to run the migration command. The application itself mustn't be running during the migration.

in the same directory to compile them to `django.mo` files which will then be used by the actual application.
You also have to do this if you modify them later on.
