# Notes for developers

Ignore this file if you are not a developer.
Read it if you want to contribute.

## Dev suite install

1. Install `python3`.
2. Run `pip install pre-commit && pre-commit install`
3. Create a virtual environment using `python -m venv venv`
4. Run `venv/bin/pip install -r requirements-dev.txt` in project root.

## Testing

Run `make run_tests_local` to run tests.
`pre-commit` will run it too, as well as some extra utilities that will annoy you.

## Workflows

This repository has automagic GitHub actions.

[evil.yaml](.github/workflows/evil.yaml) is a nice file that does the following:

- Runs app tests on each push.
- Builds (but doesn't push) a Docker container on each Pull Request to make sure it works.
- Builds and Pushes Docker container to the registry on each push to `dev` or `master` branch (i.e. when pull requests to these branches are merged).
