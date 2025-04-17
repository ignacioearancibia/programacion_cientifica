import pytest
from unittest.mock import Mock, patch
from src.pagos import procesar_pago

def test_procesar_pago_saldo_suficiente():
    mock_verificador = Mock(return_value=100.0)
    resultado = procesar_pago("usuario_test", 50.0, mock_verificador)
    assert resultado is True
    mock_verificador.assert_called_once_with("usuario_test")

def test_procesar_pago_saldo_insuficiente():
    mock_verificador = Mock(return_value=30.0)
    resultado = procesar_pago("usuario_test", 50.0, mock_verificador)
    assert resultado is False
    mock_verificador.assert_called_once_with("usuario_test")

def test_procesar_pago_saldo_exacto():
    mock_verificador = Mock(return_value=50.0)
    resultado = procesar_pago("usuario_test", 50.0, mock_verificador)

    assert resultado is True
    mock_verificador.assert_called_once_with("usuario_test")

@patch('src.pagos.verificar_saldo_en_banco')
def test_procesar_pago_con_patch(mock_verificador):

    mock_verificador.return_value = 75.0

    resultado = procesar_pago("usuario_test", 50.0, mock_verificador)

    assert resultado is True
    mock_verificador.assert_called_once_with("usuario_test")
