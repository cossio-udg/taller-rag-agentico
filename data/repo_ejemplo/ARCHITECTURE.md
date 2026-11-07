# Arquitectura del Sistema de Ventas

## Visión general

El sistema sigue una **arquitectura en capas** para separar responsabilidades:

```
api/ ──► servicios/ ──► dominio/
             │
             ▼
       persistencia/
```

## Capas y responsabilidades

| Capa | Carpeta | Responsabilidad | Depende de |
|------|---------|-----------------|------------|
| Entrada | `api/` | Exponer la interfaz de uso (CLI) | `servicios` |
| Lógica de negocio | `servicios/` | Reglas de ventas, stock, descuentos, transiciones | `dominio` |
| Dominio | `dominio/` | Entidades y estados (sin lógica de infraestructura) | — |
| Persistencia | `persistencia/` | Guardar y cargar pedidos en JSON | `dominio` |

## Regla de dependencia

Las dependencias apuntan **hacia el dominio**: `api` → `servicios` → `dominio`.
El dominio no importa a `servicios` ni a `persistencia`; así la lógica central
queda aislada de la infraestructura (JSON, CLI).

## Ciclo de vida del pedido

El estado de un pedido avanza por:

```
pendiente → confirmado → enviado → entregado
     └──────────┴────► cancelado
```

Las transiciones están gobernadas por `ServicioVentas` (`servicios/ventas.py`).
