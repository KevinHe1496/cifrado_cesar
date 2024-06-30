from funciones import creaCifrado

def test_cifrado():
    result = creaCifrado(2)

    result2 = result('Z')

    assert result2 == "B"