# Mirronline

## Verwendung des Tools

### Anforderungen installieren

```
pip install -r requirements.txt
```

### Virtuelle Umgebung verwalten

Es wird empfohlen, eine virtuelle Umgebung zu verwenden, um Abhängigkeiten isoliert zu halten.

#### Virtuelle Umgebung erstellen

Erstelle eine virtuelle Umgebung namens `env`:
```
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

### Änderungen in Anweisungsdateien .po (Schritte zur Aktualisierung der Übersetzungen)

**Übersetzungen kompilieren:**

Führe den folgenden Befehl aus, um die `.po`-Dateien in `.mo`-Dateien zu kompilieren:

```
python3 src/manage.py compilemessages
```

Dieser Befehl erstellt die .mo-Dateien, die von Django zur Laufzeit verwendet werden. Die .mo-Dateien müssen nach jeder Änderung in den .po-Dateien neu erstellt werden.


## Management API

The fakebook application contains an API that can be used to automate certain tasks. It can be used to automatically set up testing environments for development and studies on large scales without having to manually create lots of accounts and posts. This can be achieved by creating a program that automatically calls the API and therefore creates all of the content.

### Making a request

The API can be found at the `/api` route.

#### Authorization

All requests to this route have to contain a `Token` Header for authorization. The value of the token can be seen and set in the django administration panel in the configuration section.

#### Request format

The API doesn't support retrieving information, only creating new information. It therefore only uses the POST and DELETE methods. All parameters (apart from images) have to be sent as url-encoded.

Dates/Times are encoded as Unix epoch timestamps in seconds.

#### Binary content

In case an image is being submitted, insert it into the body of type `form-data` as the value of a key named `avatar`/`image`.

#### Response

The result is of `application/json` type. It usually indicates the ID of the created object.

The response code will be 200, 400, 401, 404 or 405.

### Route specification

There is an interactive up to date documentation avaiable at [/docs/api.html](/docs/api.html). It does not contain any response information, for this, see the image below.

You will need to serve the file using a webserver. You will also require an internet connection.
Alternatively, you can preview it using the [Swagger Editor](https://editor.swagger.io/) by just pasting the [OpenAPI specification](/docs/api-openapi.yaml). GitHub and GitLab may also be capable of [rendering it](/docs/api-openapi.yaml) for you.

### Route documentation

The following image shows all routes available in the API except for the `/api/advertisement` route, including their parameters and response:

![API documentation](docs/images/fakebook-api.jpg)

Some of those parameter names may be outdated, for an up to date documentation of the actual parameter names and all routes, see the OpenAPI and postman collections.

### OpenAPI documentation

An up to date OpenApi documentation can be found [here](/docs/api-openapi.yaml).

The documentation can be interactively visualized using [Swagger](https://editor.swagger.io/).

### Postman collection

An up to date postman collection documenting the API can be found [here](/docs/api-postman.json).

### Python implementation template

A small library that can be used for accessing the API using Python can be found at [docs/api-access-template/api.py](docs/api-access-template/api.py).

Using it you can easily send requests to a Fakebook instance in the following way:

```python
from api import ApiAccessor
api = ApiAccessor(base_url="http://localhost:8000/api", token="yourtoken")

api.create_user(…)
api.create_relationship(…)
api.…
```

Change the base url to point at your Fakebook instance and obtain (or set) the management token from the admin panel's [configuration section](http://localhost:8000/admin/configuration/configuration/1/change/).

The implementation <span style="text-decoration: underline">**isn't complete**</span> though and you might have to add additional parameters and routes, in case you need them.
Notably, it is missing support for images on the (create) `/user` route and missing an implementation of the entire `/advertisement` route.

Please also take note that the template does not URL-encode the parameters. If you are using special characters, you need to encode them yourself or adapt the code.

## Development

### Structure

The application is structured into multiple django apps:

- Fakebook: the main app, linking all other apps together and containing utility
- Posts: handles posts, comments and reactions, responsible for rendering the main page
- Profiles: handles profiles and relationships, responsible for profile list, invite system and profile pages
- Advertisements: handles advertisements, displayed on the main page
- Analytics: monitors the users behavior, including session time and post view time
- Chat: handles the chat system, drawer and windows, is embedded as an iframe on every page
- Configuration: handles the configuration model

#### Interface generation / Networking

In most cases, all dynamic information gets rendered into django templates on the backend and then shipped as a static page. The only two exceptions are the chat and analytics systems.
The entire chat system is handled dynamically on the frontend using JavaScript and communicates with the backend using WebSockets.
The analytics module also uses WebSockets for communication.

#### Database template

If the application detects its `data` folder (including database file and image resources) to be missing during startup, it will look for the `data.template` folder and copy its contents. The template folder should therefore always be kept up to date during the development process and be updated to a (preferably clean) new version after each database migration.

### Debug mode / Static Files

The application will serve static files using the WhiteNoise middleware in production mode. For this to work, the static files have to be collected beforehand.

For development purposes, using `DEBUG_MODE` is recommended. This will automatically serve all static files without prior collection, allowing them to be modified and updated immediately during development. Additionally, a detailed error description page will be shown in case of an error.
`DEBUG_MODE` can be enabled by setting the environment variable `DEBUG_MODE=1`.

Alternatively, production mode can be used. This will require you to run

```
python3 src/manage.py collectstatic
```

beforehand and each time you update a file.

The docker build runs this command automatically.

**Always use production mode in production environments.**

### Model change / Database migration

When changing any part of the model you need to regenerate the migrations and apply them to migrate the database.

```
python3 src/manage.py makemigrations
```

This will update all migration scripts. You can then apply them using:

```
python3 src/manage.py migrate
```

This will migrate your database.

The docker build process will not run database migrations. The application will repopulate its data folder using the template on startup if it detects its data to be missing. You will therefore have to **copy your migrated database file over to the** `data.template` folder when you migrate the database during development.
This also means that you will have to run them manually in case you want to update the database of a deployed instance to a new schema.

#### Database migration for deployed instance

The docker container and application do not migrate an existing DB automatically when upgraded. You will therefore have to manually migrate the database when updating the version / schema on a deployed instance.

This can be achieved by downloading the database and running migrations locally.
Another option is to run the migrations using the deployed instance in the docker container. This can be achieved by e.g. manipulating the start command of the deployed docker container to run the migration command. The application itself mustn't be running during the migration.

Further details of implementing this are left to the reader.

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

### Miscellaneous

Some other noteworthy information:

#### User-Profile Duality:

Fakebook uses a framework for user authentication which brings its own `User` class. Additionally, on user creation, it creates and links its own `Profile` object to the new user. The <span style="text-decoration: underline">**user is used for authentication**</span> (loginname, password, email), the <span style="text-decoration: underline">**profile for everything else**</span> Fakebook related (firstname, lastname, bio, ...).

There are some duplicate fields on them, `firstname` and `lastname` on the `User` are ignored, and `email` on the `profile` is ignored.

The variable naming in code is quite inconsistent. In most cases relating to business logic profiles are used but are called users (which leads to the beautiful `user.user` statement). So make sure to check which one it is in either case.

#### Displaynames

If you set a firstname on a user's profile, it will be displayed instead of the username.
