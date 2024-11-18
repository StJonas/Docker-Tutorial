# Docker Demo

I created this small Docker demo project as part of my tutor job for the course _Information Management & Systems Engineering_. The goal is to show the basics of setting up and using Docker.

## Start app

First, the Docker Deamon needs to be started, then the app can be started using

```sh
docker-compose up
```

## Dockerfile & Docker Compose

The Dockerfile sets up a python & flask web app:

```yaml
FROM python:3.9
..
RUN pip install redis flask
```

The docker-compose file sets up the python frontend and the redis backend, as well as some additional configurations. The frontend is set up in the first part of the docker compose:

```yaml
services:
  app:
    build: .
    volumes:
      - ./data:/data
    ports:
      - "8000:8000"
    depends_on:
      - redis
    networks:
      - backend
```

The build command tells Docker to build the app in the current directory. Port 8000 is specified for the frontend and a depends_on attribute is added. This ensures that the backend service starts before the frontend service.
Lastly, the backend network is attached. The frontend uses the network to communicate with the redis database, this way, the backend does not have to be exposed to the public.

Moreover, the backend is set up using a redis:alpine image. A volume is attached to persist data and the network is added:

```yaml
redis:
  image: "redis:alpine"
  volumes:
    - redis_data:/data
  networks:
    - backend
```

## / Route & hello counter

The index route of the app counts and displays how often the page has been called.
This is implemented in the _hello()_ function in the app.py.
The route demonstrates the persistence of data across multiple starts of the app, this is made possible because a volume was attached to the backend.
The data can be reset using:

```sh
docker-compose down --rmi all
```

## Read-file route & Bind Mounts

A second route _/read-file_ has been set up to showcase bind mounts. During development, bind mounts allow live updates to files without restarting the stack, making developing much easier. In this demo app, the file `/data/message.txt` is mounted from the host machine by adding _./data:/data_ as a volume to the frontend in the docker compose.
By changing text in the message.txt and reloading the route, you can see the Docker container accessing the local file.
