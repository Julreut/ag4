## Using the software for a study

From Fakebook: Important:

- When using our tool for research purposes, please cite our paper: Voggenreiter, A; Brandt S; Putterer, F; Frings, A and Pfeffer J. The Role of Likes: How Online Feedback Impacts Users' Mental Health (2023).
  https://arxiv.org/abs/2312.11914

- Fakebook allows to setup a Social-Media-Environment, in which users can interact freely. Every interaction can be watched and controlled by the project maintainer (e.g. the researcher). The project maintainer is responsible for everything happening on his or her social media environment. The tool should be used in an ethical responsible manner. Study participants and other users of the social media environment have to be informed that all of their data can be inspected by the project maintainer. The project maintainers are responsible for clarifying the standards of acceptable and hatefree behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior. Project maintainers have the right and responsibility to remove, edit, or reject posts and comments, or to ban temporarily or permanently any user for other behaviors that they deem inappropriate, threatening, offensive, illegal or harmful.

### Deployment

Mirror Online is a web app and can be used with any modern Desktop or Mobile web browser.
All administration functionality is available via the user interface admin route (https://example.com/admin) or via an API (https://example.com/api).
It is installed on a server and functions as a standalone application, handling incoming HTTP requests itself. A separate web server is not required.

Fakebook can be set up behind a reverse proxy like nginx to allow for selective responses based on requested domain and route. This also allows using the application in conjunction with SSL/TLS over the HTTPS protocol, which is STRONGLY RECOMMENDED.

## Testing and Production purposes

### Docker

The easiest way to deploy the software for testing or production purposes is by using docker. Beforehand, you will have to install Docker on your system.

Start by cloning the repository:

```
git clone [https://the-git.server/mirroronline.git] mirroronline
cd mirroronline
```

The repository contains a Dockerfile. The image can be built based on this using docker:

```
docker build . -t fakebook
```

This should've built a runnable docker image, that can be used to create a container.

#### Running the container using docker-compose

The easiest way to scalably manage the containers is using docker compose.

Navigate to the directory you want your stack to be located in. Then create the docker-compose.yml file:

```
nano docker-compose.yml
```

and enter the following configuration:

```
version: "3.9"

services:

  demo:
    image: fakebook
    ports:
      - "8000:8000"
    volumes:
      - ./data/demo:/fakebook/data

  prod:
    image: fakebook
    ports:
      - "8001:8000"
    volumes:
      - ./data/prod:/fakebook/data
```

You can define more services, rename them, specify different ports for each service (first port is the external / host port) and change their data directory location.

You can then proceed to start services using:

```
docker compose up -d demo
```

This will create and start the demo instance and detach from it.

To see all running services, execute:

```
docker compose ps
```

Your instance should now be running on the desired address and port, e.g. `http://localhost:8000`.

To stop a service, run:

```
docker compose stop [service]
```

All instances will create a data directory in `./data/` on their first launch and copy their template database into there. The data files represent the entire instance and can be copied, replaced and backed up. They will survive destruction of the container itself.

#### Running the container manually

You can also run the container manually, although running using docker-compose is recommended.

```
docker run -d -p 8000:8000 -v [working-directory]/data/demo:/fakebook/data --name demo fakebook
```

REPLACE `[working-directory]` with the location you want the data of the container(s) to be stored in.

This will run the image in a new container named demo, on port 8000, map the `./data/demo` directory and detach the terminal.

To check if it's running, use:

```
docker ps
```

Your instance should now be running on the desired address and port, e.g. `http://localhost:8000`.

To stop the instance, use:

```
docker stop demo
```

The instance will copy it's data template into the data directory on its first launch. The data files represent the entire instance and can be copied, replaced and backed up. They will survive destruction of the container itself.

### Manual deployment

The dependencies can be installed and the software can be run directly. This is useful for development purposes.
This is achieved by creating a virtual environment, installing the required dependencies and running the web server as follows:

Install virtualenv and python 3. This depends on your operating system:

```shell
sudo apt install python3 python3-pip
sudo pip3 install virtualenv
```

Clone the repository:

```
git clone [https://the-git.server/fakebook.git] fakebook
cd fakebook
```

Create a virtual environment and activate it:

```shell
virtualenv .venv
source .venv/bin/activate
```

Install the required dependencies:

```shell
pip install -r requirements.txt
```

Collect the static files so they are shipped in a production environment:

```shell
python ./src/manage.py collectstatic
```

Run the server:

```shell
python ./src/manage.py runserver 0.0.0.0:8000
```

### First steps after deployment

Your instance should now be running on the desired address and port, e.g. `http://localhost:8000`. There you can login to the system and interact on the platform (publish posts,....). In the beginning, there are no user accounts in the system, except one admin account. The login details for the admin account are:
username: Admin
password: fb_apfel

Over the admin panel, e.g. accessible on `http://localhost:8000/admin`, new user accounts can be created. For more details on the platform and the admin panel, see the Fakebook Manual in the gitlab folder.
