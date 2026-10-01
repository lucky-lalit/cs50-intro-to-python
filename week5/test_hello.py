from hello import hello

def test_hello():
    assert hello("Lalit") == "hello Lalit"
    assert hello() == "hello world"

