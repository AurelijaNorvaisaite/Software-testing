import tempfile
import pytest


@pytest.fixture()  # scope="function" is default
def tmp_file():
    f = tempfile.TemporaryFile("w+t")
    yield f
    if not f.closed:
        f.close()

def test_write(tmp_file):
    text = "Hello, World"
    written_bytes = tmp_file.write(text)
    assert written_bytes == len(text)
