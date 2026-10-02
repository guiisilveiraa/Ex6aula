import pytest

from src.frete import calcular_frete, calcular_total


def test_frete_padrao():
    assert calcular_frete(100) == pytest.approx(15)


def test_frete_gratis():
    assert calcular_frete(200) == pytest.approx(0)


def test_total_com_frete():
    assert calcular_total(100) == pytest.approx(115)


def test_total_sem_frete():
    assert calcular_total(200) == pytest.approx(200)