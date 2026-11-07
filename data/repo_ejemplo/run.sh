#!/usr/bin/env bash
# Ejecuta el sistema de ventas con un menú. Uso: ./run.sh

cd "$(dirname "$0")"

PY="/Users/dr.cossio/Documents/MDPI-Metamorfico/CIMPS-taller-rag-agentico/.venv/bin/python"
[ -x "$PY" ] || PY="python3"

echo "=== Sistema de ventas ==="
echo "1. Interactivo (menú)"
echo "2. Demo (automática)"
echo "3. CLI (flujo mínimo)"
echo "4. Pruebas (pytest)"
echo "0. Salir"
read -r -p "Elige una opción: " op

case "$op" in
  1) exec "$PY" interactivo.py ;;
  2) exec "$PY" demo.py ;;
  3) exec "$PY" -m api.cli ;;
  4) exec "$PY" -m pytest ;;
  0) echo "Hasta luego" ;;
  *) echo "Opción no válida" ;;
esac
