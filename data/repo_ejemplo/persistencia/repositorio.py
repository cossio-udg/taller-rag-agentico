"""Capa de persistencia: guardar y recuperar pedidos en archivos JSON.

Permite conservar los pedidos entre sesiones, serializando las entidades
a un formato legible y reconstruyéndolas al cargar.
"""

import json

from dominio.entidades import Cliente, EstadoPedido, LineaPedido, Pedido, Producto


def guardar_pedidos(pedidos: list[Pedido], ruta: str) -> None:
    """Guarda una lista de pedidos en un archivo JSON.

    Args:
        pedidos: Lista de pedidos a serializar.
        ruta: Ruta del archivo de destino.
    """
    datos = []
    for pedido in pedidos:
        datos.append(
            {
                "id": pedido.id,
                "cliente": {
                    "id": pedido.cliente.id,
                    "nombre": pedido.cliente.nombre,
                    "email": pedido.cliente.email,
                },
                "fecha": str(pedido.fecha),
                "estado": pedido.estado.value,
                "lineas": [
                    {"producto_id": linea.producto.id, "cantidad": linea.cantidad}
                    for linea in pedido.lineas
                ],
            }
        )
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)


def cargar_pedidos(ruta: str, productos: dict[int, Producto]) -> list[Pedido]:
    """Recupera pedidos desde un archivo JSON.

    Args:
        ruta: Ruta del archivo JSON a leer.
        productos: Catálogo de productos indexados por id, para reconstruir las líneas.

    Returns:
        Lista de pedidos reconstruidos.
    """
    with open(ruta, encoding="utf-8") as archivo:
        datos = json.load(archivo)

    pedidos = []
    for item in datos:
        cliente = Cliente(**item["cliente"])
        lineas = [
            LineaPedido(
                producto=productos[linea["producto_id"]],
                cantidad=linea["cantidad"],
            )
            for linea in item["lineas"]
        ]
        pedido = Pedido(id=item["id"], cliente=cliente, lineas=lineas)
        pedido.estado = EstadoPedido(item["estado"])
        pedidos.append(pedido)
    return pedidos
