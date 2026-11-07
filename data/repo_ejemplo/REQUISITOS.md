# Requisitos del Sistema de Ventas

Lista de requisitos funcionales numerados con su **trazabilidad** al código y a
las pruebas. Se usa en el taller para mostrar cómo el asistente conecta un
requisito con su implementación y su prueba.

| ID | Requisito | Implementado en | Prueba |
|----|-----------|-----------------|--------|
| R1 | Registrar clientes con id, nombre y email. | `dominio/entidades.py` → `Cliente` | — |
| R2 | Registrar productos con precio y stock. | `dominio/entidades.py` → `Producto` | — |
| R3 | Crear un pedido con una o varias líneas de producto. | `servicios/ventas.py` → `crear_pedido` | `test_crear_pedido_valida_stock` |
| R4 | Validar stock suficiente al crear el pedido. | `servicios/ventas.py` → `crear_pedido` | `test_crear_pedido_valida_stock` |
| R5 | Calcular el total del pedido como suma de subtotales. | `dominio/entidades.py` → `Pedido.total` | `test_descuento_por_umbral` |
| R6 | Aplicar 10 % de descuento si el total supera 100. | `servicios/ventas.py` → `calcular_total_con_descuento` | `test_descuento_por_umbral` |
| R7 | Gestionar el ciclo de vida del pedido (pendiente → confirmado → enviado → entregado). | `servicios/ventas.py`, `dominio/entidades.py` → `EstadoPedido` | `test_confirmar_descuenta_stock` |
| R8 | Cancelar solo en pendiente/confirmado, reponiendo stock si estaba confirmado. | `servicios/ventas.py` → `cancelar` | `test_cancelar_confirmado_repone_stock`, `test_no_se_puede_cancelar_enviado` |
| R9 | Persistir y recuperar pedidos en JSON. | `persistencia/repositorio.py` | `test_guardar_y_cargar` |
| R10 | Exponer una interfaz de uso por consola. | `api/cli.py` → `main` | — |

## Reglas de negocio clave

- Un pedido nace en estado **pendiente**.
- Confirmar descuenta stock; cancelar un pedido confirmado lo repone.
- Un pedido enviado o entregado **no** se puede cancelar.
