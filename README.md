# Introducción al RAG Agéntico aplicado a la Ingeniería de Software

Taller introductorio y **100 % sin programar** donde construyes un asistente que responde
preguntas sobre un repositorio de código, citando la fuente exacta de cada respuesta.

El taller aborda problemas reales de **ingeniería de software**: el *onboarding* de personas
nuevas, el *código legado* difícil de entender y la *trazabilidad* entre requisitos, código,
documentación, UML y pruebas. Al final, el agente funciona como una **práctica de mejora de procesos
de software (SPI)**: centraliza el conocimiento del proyecto y reduce el tiempo para entenderlo.

| Dato | Detalle |
|------|---------|
| **Duración** | 2 horas |
| **Formato** | Hands-on guiado (Google Colab) |
| **Prerrequisitos** | Ninguno. No se requiere saber programar |
| **Pila técnica** | Google Colab · Gemini · LlamaIndex |
| **Costo** | Gratuito (llave de API de Gemini gratis) |

---

📖 **Guía paso a paso para participantes:** [MANUAL_DEL_TALLER.md](MANUAL_DEL_TALLER.md) — síguela durante el taller.

---

## Requisitos

- Laptop o computadora con navegador web moderno (Chrome, Firefox, Edge).
- Conexión a internet.
- **Cuenta de Google** (para Google Colab y para obtener la llave de Gemini).
- No se requiere saber programar.

---

## Cómo empezar (2 pasos)

### Paso 1 — Obtener tu llave gratuita de Gemini

1. Entra a [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Inicia sesión con tu cuenta de Google.
3. Haz clic en **"Create API key"** (o "Obtener clave de API").
4. Copia la llave generada (empieza con `AIza...`).

> 🔒 La llave es personal y secreta. **Nunca la compartas ni la subas a un repositorio.**

### Paso 2 — Abrir el notebook en Colab

Haz clic en el botón de abajo (o usa la URL de Colab):

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cossio-udg/taller-rag-agentico/blob/main/taller_rag.ipynb)

Una vez dentro:

1. **Archivo → Guardar una copia en Drive** (así tu progreso se guarda).
2. Pega tu llave de Gemini cuando el notebook te lo pida.
3. Ejecuta las celdas en orden con el botón ▶ (o `Shift + Enter`).

---

## Temario (2 horas)

1. **Bienvenida, entorno y qué es RAG** (25 min) — El problema de SE: entender un proyecto ajeno cuesta tiempo.
2. **Indexar el código** (30 min) — Convertir código y documentación en una base de conocimiento consultable.
3. **Hacer preguntas y ver citas** (30 min) — Respuestas con archivo y trazabilidad de origen.
4. **El agente decide dónde buscar** (25 min) — La IA elige entre código, documentación o pruebas.
5. **Cierre y siguiente paso** (10 min) — Guardar tu agente y conectarlo con la mejora de procesos.

---

## Estructura del repositorio

```
taller-rag-agentico/
├── README.md              ← este archivo
├── taller_rag.ipynb       ← notebook del taller (ábrelo en Colab)
├── requirements.txt       ← dependencias (por si ejecutas fuera de Colab)
└── data/
    └── repo_ejemplo/      ← sistema de ventas de ejemplo que se indexa
        ├── dominio/       ← entidades (Cliente, Producto, Pedido, LineaPedido)
        ├── servicios/     ← lógica de negocio (stock, descuentos, estados)
        ├── persistencia/  ← guardar/cargar pedidos en JSON
        ├── api/           ← capa de entrada (CLI)
        ├── modelo/        ← UML (clases.puml, estados.puml + PNG)
        ├── tests/         ← pruebas
        ├── README.md
        ├── ARCHITECTURE.md
        ├── DECISIONES.md
        └── REQUISITOS.md  ← R1–R10 con trazabilidad
```

---

## Casos de uso de ingeniería de software cubiertos

- **Onboarding**: responder "¿cómo funciona X?" sin leer miles de líneas.
- **Código legado**: entender sistemas viejos mal documentados.
- **Trazabilidad**: conectar requisitos → código → UML → pruebas.
- **Gestión del conocimiento**: no perder el "por qué" del código cuando cambia el equipo.

---

## Pila técnica (para quien prepara el taller)

- **LLM:** Google Gemini (`gemini-flash-lite-latest`). Gratuito y con cuota holgada (1,500 peticiones/día).
- **Embeddings:** `models/gemini-embedding-001`.
- **Framework RAG:** LlamaIndex.
- **Vector store:** en memoria (suficiente para 2 horas).
- **Entorno:** Google Colab.

Para cambiar a OpenAI o Claude, solo cambia la llave y el nombre del modelo en el
notebook; la lógica de RAG es la misma.
