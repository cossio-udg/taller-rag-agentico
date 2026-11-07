"""Capa de servicios: lógica de negocio del sistema de ventas.

Contiene las reglas para crear pedidos y para transitar su ciclo de vida
(confirmar, enviar, entregar, cancelar), incluyendo la validación de stock
y el cálculo de descuentos.
"""

from dominio.entidades import Cliente, EstadoPedido, LineaPedido, Pedido

# Regla de descuento: si el total supera el umbral, se aplica un porcentaje.
UMBRAL_DESCUENTO = 100.0
PORCENTAJE_DESCUENTO = 0.10  # 10 %


class ServicioVentas:
    """Orquesta las operaciones sobre pedidos.

    Guarda los pedidos en memoria y expone las transiciones de estado.
    """

    def __init__(self) -> None:
        self._pedidos: dict[int, Pedido] = {}
        self._siguiente_id = 1

    # --- Creación ---------------------------------------------------------
    def crear_pedido(self, cliente: Cliente, lineas: list[LineaPedido]) -> Pedido:
        """Crea un pedido en estado PENDIENTE, validando el stock disponible."""
        for linea in lineas:
            if linea.producto.stock < linea.cantidad:
                raise ValueError(
                    f"Stock insuficiente de '{linea.producto.nombre}' "
                    f"(disponible: {linea.producto.stock})"
                )
        pedido = Pedido(id=self._siguiente_id, cliente=cliente, lineas=lineas)
        self._siguiente_id += 1
        self._pedidos[pedido.id] = pedido
        return pedido

    # --- Transiciones del ciclo de vida -----------------------------------
    def confirmar(self, pedido_id: int) -> None:
        """Pasa el pedido a CONFIRMADO y descuenta el stock de sus productos."""
        pedido = self._obtener(pedido_id)
        if pedido.estado != EstadoPedido.PENDIENTE:
            raise ValueError("Solo se puede confirmar un pedido pendiente")
        for linea in pedido.lineas:
            linea.producto.reducir_stock(linea.cantidad)
        pedido.estado = EstadoPedido.CONFIRMADO

    def enviar(self, pedido_id: int) -> None:
        """Pasa el pedido a ENVIADO (requiere estar CONFIRMADO)."""
        pedido = self._obtener(pedido_id)
        if pedido.estado != EstadoPedido.CONFIRMADO:
            raise ValueError("Solo se puede enviar un pedido confirmado")
        pedido.estado = EstadoPedido.ENVIADO

    def entregar(self, pedido_id: int) -> None:
        """Pasa el pedido a ENTREGADO (estado final)."""
        pedido = self._obtener(pedido_id)
        if pedido.estado != EstadoPedido.ENVIADO:
            raise ValueError("Solo se puede entregar un pedido enviado")
        pedido.estado = EstadoPedido.ENTREGADO

    def cancelar(self, pedido_id: int) -> None:
        """Cancela el pedido. Si estaba CONFIRMADO, repone el stock."""
        pedido = self._obtener(pedido_id)
        if pedido.estado not in (EstadoPedido.PENDIENTE, EstadoPedido.CONFIRMADO):
            raise ValueError(
                "Solo se puede cancelar un pedido pendiente o confirmado"
            )
        if pedido.estado == EstadoPedido.CONFIRMADO:
            for linea in pedido.lineas:
                linea.producto.reponer_stock(linea.cantidad)
        pedido.estado = EstadoPedido.CANCELADO

    # --- Cálculos ---------------------------------------------------------
    def calcular_total_con_descuento(self, pedido: Pedido) -> float:
        """Devuelve el total aplicando el descuento si corresponde."""
        total = pedido.total
        if total > UMBRAL_DESCUENTO:
            total -= total * PORCENTAJE_DESCUENTO
        return round(total, 2)

    # --- Consulta ---------------------------------------------------------
    def listar_pedidos(self) -> list[Pedido]:
        """Devuelve los pedidos registrados en el sistema."""
        return list(self._pedidos.values())

    # --- Helpers ----------------------------------------------------------
    def _obtener(self, pedido_id: int) -> Pedido:
        if pedido_id not in self._pedidos:
            raise KeyError(f"No existe el pedido {pedido_id}")
        return self._pedidos[pedido_id]
