# Apprise-Microservice

[![Build Status](https://ci.strahlungsfrei.de/api/badges/djmaze/apprise-microservice/status.svg)](https://ci.strahlungsfrei.de/djmaze/apprise-microservice)
[![Docker Stars](https://img.shields.io/docker/stars/mazzolino/apprise-microservice.svg)](https://hub.docker.com/r/mazzolino/apprise-microservice/) [![Docker Pulls](https://img.shields.io/docker/pulls/mazzolino/apprise-microservice.svg)](https://hub.docker.com/r/mazzolino/apprise-microservice/)

A small JSON API server for delivering notifications using [Apprise](https://github.com/caronc/apprise).

* Notification services can be configured using an environment variable.
* The service listens for JSON-formatted notification messages on port 5000.

This service is suitable as a [sidecar service](https://docs.microsoft.com/en-us/azure/architecture/patterns/sidecar) to another service in a container-based cluster.


## Usage

These are quickstart instructions using Docker Compose.

1. Copy `app.env.example` to `app.env`
2. Set `NOTIFICATION_URLS` in `app.env` according to [the documentation](https://github.com/caronc/apprise/wiki). You can add multiple targets, separated by commas.
3. Start the container:
    ```bash
    docker-compose up
    ```
4. In another terminal, you should now be able to trigger a notification using curl:
    ```bash
    curl -X POST --data '{"title": "my notification title", "body": "what a great notification service!"}' localhost:5000
    ```

See the file [docker-compose.example.yml](docker-compose.example.yml) for a better example on how this supposed to work.

### Using secrets

If running on a docker swarm cluster [docker secrets](https://docs.docker.com/engine/swarm/secrets/) can be used to set the notification URLS to avoid leaking credentials through environment variables:

1. Set up the secret with the **same** content as you would with the regular environment variable
2. Attach the secret to the service
3. Set the `NOTIFICATION_URLS_FILE` to the path where the secret is mounted in the service
