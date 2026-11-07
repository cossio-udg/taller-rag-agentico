"""Versión interactiva del sistema de ventas: menú por consola.

Uso (desde la carpeta repo_ejemplo):
    python interactivo.py
"""

from dominio.entidades import Cliente, Producto, LineaPedido
from servicios.ventas import ServicioVentas

CATALOGO = [
    Producto(1, "Teclado mecánico", 80.0, stock=10),
    Producto(2, 'Monitor 27"', 200.0, stock=5),
    Producto(3, "Mouse", 25.0, stock=8),
    Producto(4, "Auriculares", 45.0, stock=6),
]

MENU = """
=== Sistema de ventas (interactivo) ===
1. Ver catálogo
2. Crear pedido
3. Confirmar pedido
4. Enviar pedido
5. Entregar pedido
6. Cancelar pedido
7. Ver pedidos
0. Salir
"""


def mostrar_catalogo() -> None:
    print("\n--- Catálogo ---")
    for p in CATALOGO:
        print(f"  [{p.id}] {p.nombre} - ${p.precio:.2f} (stock: {p.stock})")


def mostrar_pedidos(servicio: ServicioVentas) -> None:
    pedidos = servicio.listar_pedidos()
    if not pedidos:
        print("\n  (no hay pedidos todavía)")
        return
    print("\n--- Pedidos ---")
    for p in pedidos:
        lineas = ", ".join(f"{l.producto.nombre} x{l.cantidad}" for l in p.lineas)
        print(f"  #{p.id} [{p.estado.value}] {p.cliente.nombre} | {lineas} | total ${p.total:.2f}")


def crear_pedido(servicio: ServicioVentas, cliente: Cliente) -> None:
    mostrar_catalogo()
    lineas = []
    while True:
        pid = input("  ID de producto (Enter para terminar): ").strip()
        if pid == "":
            break
        try:
            producto = next(p for p in CATALOGO if p.id == int(pid))
            cantidad = int(input(f"  Cantidad de '{producto.nombre}': ").strip())
            lineas.append(LineaPedido(producto, cantidad))
        except (StopIteration, ValueError):
            print("  ⚠️ Entrada inválida, intenta de nuevo.")
    if not lineas:
        print("  (pedido vacío, cancelado)")
        return
    try:
        pedido = servicio.crear_pedido(cliente, lineas)
        print(f"  ✅ Pedido #{pedido.id} creado (estado '{pedido.estado.value}')")
    except ValueError as e:
        print(f"  ❌ {e}")


def elegir_pedido(servicio: ServicioVentas, accion: str):
    if not servicio.listar_pedidos():
        print("\n  (no hay pedidos)")
        return None
    mostrar_pedidos(servicio)
    try:
        pid = int(input(f"  ID del pedido a {accion}: ").strip())
    except ValueError:
        print("  ⚠️ ID inválido")
        return None
    for p in servicio.listar_pedidos():
        if p.id == pid:
            return p
    print("  ⚠️ No existe ese pedido")
    return None


def main() -> None:
    servicio = ServicioVentas()
    cliente = Cliente(1, "María López", "maria@example.com")

    print("=== Sistema de ventas (interactivo) ===")
    print(f"Cliente: {cliente.nombre}")

    while True:
        print(MENU)
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            mostrar_catalogo()
        elif opcion == "2":
            crear_pedido(servicio, cliente)
        elif opcion in ("3", "4", "5", "6"):
            acciones = {"3": "confirmar", "4": "enviar", "5": "entregar", "6": "cancelar"}
            pedido = elegir_pedido(servicio, acciones[opcion])
            if pedido is None:
                continue
            try:
                getattr(servicio, acciones[opcion])(pedido.id)
                print(f"  ✅ Pedido #{pedido.id} -> estado '{pedido.estado.value}'")
            except (ValueError, KeyError) as e:
                print(f"  ❌ {e}")
        elif opcion == "7":
            mostrar_pedidos(servicio)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("  ⚠️ Opción no válida.")


if __name__ == "__main__":
    main()
