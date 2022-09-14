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
It works with other IANA timezones in the similar fashion.

## For contributors

Skip if not dev.

### Dev suite install

1. Install `python3`.
2. Run `pip install pre-commit && pre-commit install`
3. Create a virtual environment using `python -m venv venv`
4. Run `venv/bin/pip install -r requirements-dev.txt` in project root.

### Testing

Run `make run_tests_local` to run tests. `pre-commit` will run it too, as well as some extra utils that will annoy you.

### Workflows

This repository has automagic GitHub actions.

[checks.yaml](.github/workflows/checks.yaml) is responsible for running linters and tests.
It basically does the same thing as `make run_linter` and `make run_test_local`

[build.yaml](.github/workflows/build.yaml) builds a docker image
and pushes it to `doctoractoantohich/make_your_time` on each pull request to `master` or `dev` branch.
In future, it's planned to publish specific tags, not only `:latest`.
