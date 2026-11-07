"""Demo del sistema de ventas: muestra el ciclo de vida de un pedido en acción.

Uso (desde la carpeta repo_ejemplo):
    python demo.py
"""

from dominio.entidades import Cliente, Producto, LineaPedido
from servicios.ventas import ServicioVentas


def main() -> None:
    servicio = ServicioVentas()

    # Catálogo y cliente
    cliente = Cliente(1, "María López", "maria@example.com")
    teclado = Producto(1, "Teclado mecánico", 80.0, stock=10)
    monitor = Producto(2, 'Monitor 27"', 200.0, stock=5)
    mouse = Producto(3, "Mouse", 25.0, stock=4)

    print("=== Sistema de ventas: demo ===\n")

    # 1) Crear un pedido
    pedido = servicio.crear_pedido(
        cliente,
        [LineaPedido(teclado, 2), LineaPedido(monitor, 1)],
    )
    print(f"[1] Pedido #{pedido.id} creado")
    print(f"    Estado: {pedido.estado.value} | Total: ${pedido.total:.2f}")
    print(f"    Stock: teclado={teclado.stock}, monitor={monitor.stock}\n")

    # 2) Ciclo de vida (máquina de estados)
    servicio.confirmar(pedido.id)
    print(f"[2] Confirmado -> estado '{pedido.estado.value}'")
    print(f"    Stock descontado: teclado={teclado.stock}, monitor={monitor.stock}\n")

    servicio.enviar(pedido.id)
    print(f"[3] Enviado -> estado '{pedido.estado.value}'\n")

    servicio.entregar(pedido.id)
    print(f"[4] Entregado -> estado '{pedido.estado.value}'\n")

    # 3) Descuento por umbral
    con_descuento = servicio.calcular_total_con_descuento(pedido)
    print(f"[5] Total: ${pedido.total:.2f} -> con descuento: ${con_descuento:.2f}")
    print("    (10 % de descuento por superar $100)\n")

    # 4) Cancelación y reposición de stock
    pedido2 = servicio.crear_pedido(cliente, [LineaPedido(mouse, 4)])
    print(f"[6] Pedido #{pedido2.id} creado (estado '{pedido2.estado.value}') | stock mouse={mouse.stock}")
    servicio.confirmar(pedido2.id)
    print(f"    Confirmado | stock mouse={mouse.stock}")
    servicio.cancelar(pedido2.id)
    print(f"    Cancelado -> estado '{pedido2.estado.value}' | stock repuesto mouse={mouse.stock}\n")

    print("=== Fin de la demo ===")


if __name__ == "__main__":
    main()
