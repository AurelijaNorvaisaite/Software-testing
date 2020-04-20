def test_write(tmp_file):
    text = "Hello, World"
    written_bytes = tmp_file.write(text)
    assert written_bytes == len(text)


def test_positions(tmp_file):
    start_pos = tmp_file.tell()
    text = "Nobody expects Spanish Inquisition!"
    written_bytes = tmp_file.write(text)
    assert tmp_file.tell() - len(text) == start_pos
