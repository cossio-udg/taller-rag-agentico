# Sistema de Ventas

Proyecto de ejemplo usado en el taller de RAG Agéntico. Es un sistema de ventas
en capas: un cliente crea pedidos con productos, el pedido transita por un ciclo
de vida (pendiente → confirmado → enviado → entregado) y puede persistirse en JSON.

## Estructura por capas

- `dominio/` — entidades (`Cliente`, `Producto`, `LineaPedido`, `Pedido`) y estados.
- `servicios/` — lógica de negocio (`ServicioVentas`): stock, descuentos, transiciones.
- `persistencia/` — guardar y cargar pedidos en JSON.
- `api/` — capa de entrada (CLI de ejemplo).
- `modelo/` — diagramas UML (clases y máquina de estados) en PlantUML.
- `tests/` — pruebas automatizadas.

## Cómo se relaciona con el taller

El asistente de IA indexa este proyecto y responde preguntas sobre el código,
la documentación, el UML y las pruebas, citando el archivo de donde proviene
cada respuesta.

## Ejecutar (opcional)

Lo más fácil (menú): `./run.sh`

O manualmente:

```bash
python interactivo.py  # menú interactivo (tú manejas los pedidos)
python demo.py         # demo automática del ciclo de vida
python -m api.cli      # flujo mínimo por consola
pytest                 # correr las pruebas
```
