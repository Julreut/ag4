# base image
FROM python:3.8

# copy requirements file and install dependencies in the container
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy the (re)sources to the /ag4 directory in the container
COPY ./src /ag4/src
COPY ./static_cdn/static_root /ag4/static_cdn/static_root
COPY ./config /ag4/config

# Collect static files
RUN python /ag4/src/manage.py collectstatic --noinput

# set working directory for application inside the container
WORKDIR /ag4

# Create a startup script
COPY entrypoint.sh /ag4/entrypoint.sh
RUN chmod +x /ag4/entrypoint.sh

# run the entrypoint script on container run
ENTRYPOINT ["/ag4/entrypoint.sh"]

# start server, bind to all interfaces, port 8000
CMD ["runserver", "0.0.0.0:8000"]