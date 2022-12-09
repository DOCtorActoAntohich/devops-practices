# Make Your Time

## Overview

This web-application will quickly help you find out what time it is now in Moscow.
You can learn what time it is now in other places, too.

## How to Build and Run

Prerequisites:

- `Make`
- `Docker`
- `python3`

### Build locally

1. Clone this repository.
2. In its root folder, simply execute `make build_and_run_local`.

It will build an image locally and run a container with it.

### Run remote image

Execute `make run_from_remote`.

It will pull an already built image and run it.

### Stop the container

To stop and delete the container, execute `make stop_app` script.

## Usage

Go to `127.0.0.1:8000` in your browser to see the current Moscow Time.

If you update the page, the time will update too.

`/zone/<name>` path can show time in different timezones.
You can use any IANA time zone.
For example, `127.0.0.1:8000/zone/Asia/Krasnoyarsk` shows time in Krasnoyarsk.

`/metrics` path shows metrics powered by [Prometheus FastAPI Instrumentator](https://github.com/trallnag/prometheus-fastapi-instrumentator).

`/visits` path shows number of visits and last visit time since restart.
A visit means successfully fulfilled time request.

## For contributors

Refer to [Dev Notes](Dev%20Notes.md)
