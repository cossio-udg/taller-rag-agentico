# Introducción al RAG Agéntico aplicado a la Ingeniería de Software

Taller introductorio y **100 % sin programar**: construyes un asistente que responde
preguntas sobre un repositorio de código, citando la fuente exacta de cada respuesta.

Aborda problemas reales de **ingeniería de software** —*onboarding*, *código legado* y
*trazabilidad* entre requisitos, código, documentación, UML y pruebas— y termina con un
**agente** que es, en sí, una práctica de **mejora de procesos (SPI)**.

| Dato | Detalle |
|------|---------|
| Duración | 2 horas |
| Formato | Hands-on guiado (Google Colab) |
| Pila | Colab · Gemini · LlamaIndex |

## Para empezar

1. Abre el notebook en Colab:

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cossio-udg/taller-rag-agentico/blob/main/taller_rag.ipynb)

2. Sigue la guía paso a paso: **[MANUAL_DEL_TALLER.md](MANUAL_DEL_TALLER.md)**.

> Requisitos, llave de Gemini y las 5 partes del taller están en el manual.

## Estructura del repositorio

```
taller-rag-agentico/
├── README.md             ← este archivo
├── MANUAL_DEL_TALLER.md  ← guía paso a paso del taller
├── taller_rag.ipynb      ← notebook (ábrelo en Colab)
├── requirements.txt      ← dependencias
└── data/
    └── repo_ejemplo/     ← sistema de ventas de ejemplo (se indexa)
        ├── dominio/  servicios/  persistencia/  api/
        ├── modelo/       ← UML (clases.puml, estados.puml + PNG)
        ├── tests/
        └── README · ARCHITECTURE · DECISIONES · REQUISITOS (R1–R10)
```

## Pila técnica

- **LLM:** Google Gemini (`gemini-flash-lite-latest`) · **Embeddings:** `gemini-embedding-001`
- **Framework RAG:** LlamaIndex · **Vector store:** en memoria · **Entorno:** Google Colab

Para usar otro proveedor (OpenAI, Claude, DeepSeek o un modelo local), cambia la integración
en las celdas 1.1–1.3 (paquetes, clases, nombre de modelo y llave). La lógica del RAG y del
agente —indexación, recuperación y ruteo— se mantiene igual.
