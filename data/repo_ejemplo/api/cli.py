"""Capa de entrada: interfaz de línea de comandos (CLI) del sistema de ventas.

Muestra un flujo mínimo de uso: crear un cliente y un producto, crear un
pedido, confirmarlo y calcular el total con descuento.
"""

from dominio.entidades import Cliente, LineaPedido, Producto
from servicios.ventas import ServicioVentas


def main() -> None:
    """Ejemplo de uso del sistema de ventas por consola."""
    servicio = ServicioVentas()

    cliente = Cliente(id=1, nombre="María López", email="maria@example.com")
    producto = Producto(id=1, nombre="Teclado mecánico", precio=80.0, stock=10)

    pedido = servicio.crear_pedido(
        cliente=cliente,
        lineas=[LineaPedido(producto=producto, cantidad=2)],
    )
    print(f"Pedido {pedido.id} creado en estado {pedido.estado.value}")

    servicio.confirmar(pedido.id)
    print(f"Pedido confirmado. Stock restante del producto: {producto.stock}")

    total = servicio.calcular_total_con_descuento(pedido)
    print(f"Total con descuento: {total}")


if __name__ == "__main__":
    main()
