import pytest
import tempfile


# This file is always included by pytest, provided it is found.
# Before using this solution, change this file's name to 'conftest.py'
# If you are experiencing any issues with it, move it to project root.
@pytest.fixture(scope="session")
def tmp_file():
    f = tempfile.TemporaryFile("w+t")
    yield f
    if not f.closed:
        f.close()
