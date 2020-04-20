def test_write(tmp_file):
    text = "Hello, World"
    written_bytes = tmp_file.write(text)
    assert written_bytes == len(text)

def test_possition(tmp_file):
    start_possition = tmp_file.tell()
    text = "Nobody is perfect"
    bytes_written = tmp_file.write(text)
    final_possition = tmp_file.tell()
    assert (final_possition-start_possition) == bytes_written

