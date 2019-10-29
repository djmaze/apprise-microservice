# Apprise-Microservice

A small JSON API server for delivering notifications using [Apprise](https://github.com/caronc/apprise).

* Notification services can be configured using an environment variable.
* The service listens for JSON-formatted notification messages on port 5000.

This service is suitable as a [sidecar service](https://docs.microsoft.com/en-us/azure/architecture/patterns/sidecar) to another service in a container-based cluster.


## Usage

These are quickstart instructions using Docker Compose.

1. Copy `app.env.example` to `app.env`
2. Set `NOTIFICATION_URLS` in `app.env` according to [the documentation](https://github.com/caronc/apprise/wiki). You can add multiple targets, separated by whitespace.
3. Start the container:
    ```bash
    docker-compose up
    ```
4. In another terminal, you should now be able to trigger a notification using curl:
    ```bash
    curl -X POST --data '{"title": "my notification title", "body": "what a great notification service!"}' localhost:5000
    ```
