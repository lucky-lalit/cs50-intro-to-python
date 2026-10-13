from um import count


def test_correct():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("um, thanks for the album.") == 1


def test_tricky():
    assert count("yummy") == 0
    assert count("mum") == 0


def test_edge():
    assert count("Um, thanks for the album.") == 1
