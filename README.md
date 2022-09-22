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

You can also go to `127.0.0.1:8000/Asia/Krasnoyarsk` to see the current time in Krasnoyarsk.
It works with other IANA time zones in the similar fashion.

## For contributors

Refer to [Dev Notes](Dev%20Notes.md)
