"""Pruebas de la capa de persistencia."""

from dominio.entidades import Cliente, LineaPedido, Producto
from persistencia.repositorio import cargar_pedidos, guardar_pedidos
from servicios.ventas import ServicioVentas


def test_guardar_y_cargar(tmp_path):
    """R9: un pedido guardado se recupera con las mismas líneas y cantidades."""
    servicio = ServicioVentas()
    producto = Producto(id=1, nombre="Producto", precio=50.0, stock=10)
    pedido = servicio.crear_pedido(
        Cliente(id=1, nombre="Cliente", email="c@example.com"),
        [LineaPedido(producto=producto, cantidad=2)],
    )

    ruta = tmp_path / "pedidos.json"
    guardar_pedidos([pedido], str(ruta))

    cargados = cargar_pedidos(str(ruta), {1: producto})

    assert len(cargados) == 1
    assert cargados[0].id == pedido.id
    assert cargados[0].lineas[0].cantidad == 2
    assert cargados[0].cliente.nombre == "Cliente"
