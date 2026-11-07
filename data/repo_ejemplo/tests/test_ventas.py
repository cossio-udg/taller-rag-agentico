"""Pruebas de la capa de servicios del sistema de ventas."""

import pytest

from dominio.entidades import Cliente, EstadoPedido, LineaPedido, Producto
from servicios.ventas import ServicioVentas


def _cliente() -> Cliente:
    return Cliente(id=1, nombre="Cliente de prueba", email="cliente@example.com")


def _producto(stock: int = 10) -> Producto:
    return Producto(id=1, nombre="Producto de prueba", precio=50.0, stock=stock)


def test_crear_pedido_valida_stock():
    """R4: no se puede crear un pedido si no hay stock suficiente."""
    servicio = ServicioVentas()
    producto = _producto(stock=1)
    with pytest.raises(ValueError):
        servicio.crear_pedido(_cliente(), [LineaPedido(producto=producto, cantidad=2)])


def test_confirmar_descuenta_stock():
    """R7: al confirmar, el pedido pasa a CONFIRMADO y descuenta stock."""
    servicio = ServicioVentas()
    producto = _producto(stock=10)
    pedido = servicio.crear_pedido(_cliente(), [LineaPedido(producto=producto, cantidad=2)])

    servicio.confirmar(pedido.id)

    assert pedido.estado == EstadoPedido.CONFIRMADO
    assert producto.stock == 8


def test_cancelar_confirmado_repone_stock():
    """R8: cancelar un pedido confirmado repone el stock."""
    servicio = ServicioVentas()
    producto = _producto(stock=10)
    pedido = servicio.crear_pedido(_cliente(), [LineaPedido(producto=producto, cantidad=2)])

    servicio.confirmar(pedido.id)
    servicio.cancelar(pedido.id)

    assert pedido.estado == EstadoPedido.CANCELADO
    assert producto.stock == 10


def test_no_se_puede_cancelar_enviado():
    """R8: no se puede cancelar un pedido que ya fue enviado."""
    servicio = ServicioVentas()
    producto = _producto(stock=10)
    pedido = servicio.crear_pedido(_cliente(), [LineaPedido(producto=producto, cantidad=1)])

    servicio.confirmar(pedido.id)
    servicio.enviar(pedido.id)

    with pytest.raises(ValueError):
        servicio.cancelar(pedido.id)


def test_descuento_por_umbral():
    """R6: si el total supera 100, se aplica un 10 % de descuento."""
    servicio = ServicioVentas()
    producto = _producto(stock=10)  # precio 50
    pedido = servicio.crear_pedido(
        _cliente(), [LineaPedido(producto=producto, cantidad=3)]  # total 150
    )

    total = servicio.calcular_total_con_descuento(pedido)

    assert total == 135.0
