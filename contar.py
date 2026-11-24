"""Cuenta las líneas de un registro que contienen un texto."""
import sys
from pathlib import Path

archivo = Path(__file__).parent / "evidencias/001/auth.log.txt"
patron = sys.argv[1] if len(sys.argv) > 1 else "Failed password"
cantidad = 0

with archivo.open(encoding="utf-8") as registro:
    for linea in registro:
        if patron in linea:
            cantidad += 1

print(f"{patron} → {cantidad}")
