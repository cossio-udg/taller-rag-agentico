# Decisiones de diseño (ADR)

Registro de decisiones relevantes tomadas en el diseño del sistema.

## ADR-1: Arquitectura en capas

**Contexto:** el sistema mezcla reglas de negocio, entrada y persistencia.

**Decisión:** separar en capas (`api`, `servicios`, `dominio`, `persistencia`).

**Justificación:** aislar la lógica de negocio de la infraestructura facilita
probar y cambiar el mecanismo de persistencia (p. ej. de JSON a una base de datos)
sin tocar las reglas de venta.

## ADR-2: Estados como `enum`

**Contexto:** el pedido atraviesa un número finito y conocido de estados.

**Decisión:** modelar los estados con la enumeración `EstadoPedido`.

**Justificación:** evita cadenas sueltas y errores de tipeo; centraliza los
estados válidos y facilita validar las transiciones permitidas.

## ADR-3: Persistencia en JSON

**Contexto:** se necesita conservar los pedidos entre sesiones.

**Decisión:** serializar a JSON en `persistencia/repositorio.py`.

**Justificación:** formato legible y sin dependencias externas, suficiente para
un sistema de ejemplo. Una base de datos sería sobredimensionada aquí.

## ADR-4: Descuento configurable por umbral

**Contexto:** se desea incentivar pedidos grandes.

**Decisión:** aplicar un 10 % de descuento cuando el total supera 100, mediante
las constantes `UMBRAL_DESCUENTO` y `PORCENTAJE_DESCUENTO`.

**Justificación:** valores como constantes (no "mágicos") para que sean fáciles
de encontrar y ajustar sin tocar la lógica.
