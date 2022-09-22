import asyncio

import pytest


# Fixed the "Event loop is closed" problem
# When running second file (any) with async tests.
@pytest.fixture(scope="session")
def event_loop():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
    yield loop
    loop.close()
