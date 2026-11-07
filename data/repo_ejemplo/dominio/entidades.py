"""Entidades del dominio del sistema de ventas.

Define los objetos principales —Cliente, Producto, LineaPedido y Pedido—
junto con el ciclo de vida (estados) por el que pasa un pedido.
"""

from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class EstadoPedido(str, Enum):
    """Ciclo de vida de un pedido.

    Orden normal: PENDIENTE -> CONFIRMADO -> ENVIADO -> ENTREGADO.
    Se puede CANCELAR solo desde PENDIENTE o CONFIRMADO.
    """

    PENDIENTE = "pendiente"
    CONFIRMADO = "confirmado"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"
    CANCELADO = "cancelado"


@dataclass
class Cliente:
    """Persona que realiza pedidos en el sistema."""

    id: int
    nombre: str
    email: str


@dataclass
class Producto:
    """Artículo a la venta. Tiene un precio y una cantidad en stock."""

    id: int
    nombre: str
    precio: float
    stock: int

    def reducir_stock(self, cantidad: int) -> None:
        """Descuenta `cantidad` unidades del stock.

        Lanza ``ValueError`` si no hay stock suficiente.
        """
        if cantidad > self.stock:
            raise ValueError(
                f"Stock insuficiente de '{self.nombre}' (disponible: {self.stock})"
            )
        self.stock -= cantidad

    def reponer_stock(self, cantidad: int) -> None:
        """Devuelve `cantidad` unidades al stock (p. ej. al cancelar)."""
        self.stock += cantidad


@dataclass
class LineaPedido:
    """Una línea dentro de un pedido: un producto y su cantidad."""

    producto: Producto
    cantidad: int

    @property
    def subtotal(self) -> float:
        """Importe de la línea = precio unitario x cantidad."""
        return self.producto.precio * self.cantidad


@dataclass
class Pedido:
    """Pedido realizado por un cliente.

    Agrupa una o varias líneas y transita por los estados de ``EstadoPedido``.
    """

    id: int
    cliente: Cliente
    fecha: date = field(default_factory=date.today)
    lineas: list[LineaPedido] = field(default_factory=list)
    estado: EstadoPedido = EstadoPedido.PENDIENTE

    @property
    def total(self) -> float:
        """Suma de los subtotales de todas las líneas (sin descuento)."""
        return sum(linea.subtotal for linea in self.lineas)
