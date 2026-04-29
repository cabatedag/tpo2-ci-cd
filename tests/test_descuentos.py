import pytest
from app.descuentos import calcular_precio_final


def test_descuento_correcto():
    assert calcular_precio_final(100, 10) == 90

def test_precio_negativo():
    with pytest.raises(ValueError):
        calcular_precio_final(-50, 10)

def test_descuento_cero():
    assert calcular_precio_final(200, 0) == 200

