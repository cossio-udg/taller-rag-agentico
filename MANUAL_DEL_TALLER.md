# Manual del taller (paso a paso) — RAG Agéntico aplicado a la Ingeniería de Software

Esta guía es para el participante. **No necesitas saber programar.** Solo sigue los
pasos en orden y verifica que veas lo que se indica en cada "✔ Qué deberías ver".

⏱ Duración: 2 horas · 💻 Necesitas: navegador, internet y cuenta de Google.

---

## Antes de empezar (10 min)

### Paso 0.1 — Consigue tu llave gratuita de Gemini
1. Entra a https://aistudio.google.com/app/apikey
2. Inicia sesión con tu cuenta de Google.
3. Pulsa **"Create API key"** y copia la llave **completa** (un texto largo; puede empezar con `AIza…` o `AQ…`).
4. Guárdala a mano. **No la compartas.**

✔ Qué deberías ver: un texto largo (tu llave).

### Paso 0.2 — Abre el notebook
1. Haz clic en el botón "Open in Colab" del README (o usa la URL que te dieron).
2. Arriba: **Archivo → Guardar una copia en Drive**.

✔ Qué deberías ver: un documento con celdas (cajitas) y un nombre tipo "Copia de taller_rag".

---

## Parte 1 · Preparar el entorno (25 min)

### Paso 1.1 — Instalar las herramientas
- Ejecuta la celda **"1.1 Instalar dependencias"** (clic en el ▶ a la izquierda, o `Shift + Enter`).

✔ Qué deberías ver: `✅ Dependencias instaladas.`

### Paso 1.2 — Pegar tu llave
- Ejecuta la celda **"1.2 Pega tu llave gratuita de Gemini"**.
- Cuando aparezca el cuadro de texto, pega tu llave y presiona **Enter**.

✔ Qué deberías ver: `✅ Llave configurada.`

### Paso 1.3 — Configurar el modelo
- Ejecuta la celda **"1.3 Configurar el modelo"**.

✔ Qué deberías ver: `✅ Listo. Modelo configurado con Gemini.`

---

## Parte 2 · Indexar el código (30 min)

### Paso 2.1 — Cargar el código de ejemplo
- Ejecuta la celda **"2.1 Cargar el código de ejemplo"**.

✔ Qué deberías ver: una lista de archivos del sistema de ventas (código en `dominio/`,
`servicios/`, `persistencia/`, `api/`; documentación, UML en `modelo/` y pruebas).

### Paso 2.2 — Indexar (leer y dividir)
- Ejecuta la celda **"2.2 Indexar"**.

✔ Qué deberías ver: tres líneas:
`📄 Documentos leídos: …`, `🧩 Bloques creados: …`, `✅ Índice listo.`

---

## Parte 3 · Hacer preguntas y ver citas (30 min)

### Paso 3.1 — Hacer tu primera pregunta
- Ejecuta la celda **"3.1 Preguntar al sistema"**.
- Aparecerá una **caja de texto** y un botón **"Preguntar"**.

✔ Qué deberías ver: una caja donde puedes escribir y un botón azul "Preguntar".

### Paso 3.2 — Preguntar
- Escribe: `¿Cómo se valida el stock al crear un pedido?` y pulsa **Preguntar**.

✔ Qué deberías ver:
- `📝 Respuesta:` con una explicación.
- `📎 Fuentes (trazabilidad):` con el archivo (ej. `persistencia.py`) y su relevancia.

### Paso 3.3 — Probar más preguntas (preguntas clave)
- Prueba: `¿Qué regla de descuento aplica el sistema?`
- Prueba: `¿Qué relación hay entre Cliente y Pedido?`
- Prueba: `Traza el requisito R8 desde su definición hasta su prueba.`

✔ Qué deberías ver: respuestas distintas, cada una con su fuente.

---

## Parte 4 · El agente decide dónde buscar (25 min)

> **¿RAG o agente?** El RAG busca en un solo lugar. El agente decide en cuál de
> varios lugares buscar (código, documentación, UML o pruebas). Cada fuente del
> agente es en realidad un RAG; lo "agéntico" es la capa que decide cuál usar.

**Las 4 especialidades del agente:**

| Fuente | Se especializa en | Pregunta típica |
|--------|-------------------|-----------------|
| Código | Funciones, clases, lógica | `¿Qué hace confirmar?` |
| Documentación | Requisitos, decisiones, arquitectura | `¿En qué capas se divide?` |
| UML | Clases, relaciones, estados | `¿Cuáles son los estados?` |
| Pruebas | Comportamiento esperado | `¿Qué prueba la cancelación?` |

### Paso 4.1 — Crear el agente
- Ejecuta la celda **"4.1 Crear el agente que decide dónde buscar"**.

✔ Qué deberías ver: `✅ Agente listo. Decide solo entre código, documentación, UML o pruebas.`

### Paso 4.2 — Preguntar al agente
- Ejecuta la celda **"4.2 Preguntar al agente"** y haz preguntas de distintos tipos:
  - De código: `¿Qué hace la función confirmar en ServicioVentas?`
  - De documentación: `¿En qué capas está dividido el proyecto y por qué?`
  - De UML: `¿Cuáles son los estados de un pedido?`
  - De pruebas: `¿Qué prueba que cancelar un pedido confirmado repone stock?`

✔ Qué deberías ver: el agente responde y, según la pregunta, busca en una fuente u otra.

> 💬 **Memoria:** el agente recuerda la conversación. Puedes preguntar de seguimiento,
> por ejemplo *«¿y cuál viene después de enviado?»*, y entenderá de qué hablas.

---

## Parte 5 · Cierre (10 min)

### Paso 5.1 — Guardar tu trabajo
- **Archivo → Guardar** (o `Ctrl/Cmd + S`).

✔ Qué deberías ver: el mensaje "Guardado" arriba.

---

## Siguiente paso (opcional)

Apunta el agente a **tu propio proyecto**.

### Si tu proyecto es similar (Python + Markdown + PlantUML, con carpetas de código/docs/UML/tests)

1. En la celda **2.1**, cambia `RUTA` por la ruta de tu proyecto (o `REPO_URL` si clonas de GitHub).
2. Vuelve a ejecutar desde la Parte 2.

### Si tu proyecto difiere, ajusta además

| Qué cambiar | Dónde |
|-------------|-------|
| Los nombres de tus carpetas de código | Celda **4.1** → `CARPETAS_CODIGO` |
| Las extensiones de tu lenguaje (ej. `.java`, `.ts`) | Celdas **2.2** y **4.1** → `required_exts` |
| Las fuentes del agente (ej. quitar UML si no lo tienes) | Celda **4.1** → herramientas |
