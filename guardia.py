"""Taller de terminal y análisis SOC. Ejecutar con Python 3 en Linux."""
import shlex
import subprocess
from pathlib import Path

BASE = Path(__file__).resolve().parent
MISIONES = [
    ("Reconocé tu terminal", [
        ("Averiguá con qué cuenta corre este proceso.", "whoami"),
        ("Ubicá la carpeta del taller.", "pwd"),
        ("Buscá tu UID y los grupos de tu cuenta.", "id"),
    ], "¿Qué UID efectivo identifica a root?", ["0", "uid=0"],
     "El UID es un número. Podés consultar solo el efectivo con id -u.",
     "Root tiene UID 0. En Kali probá id -u, sudo id -u e id -u en tu terminal. Si tu cuenta tiene permiso, solo la orden del medio corre como root."),
    ("Contá accesos SSH", [
        ("Listá los archivos de la primera guardia.", "ls evidencias/001"),
        ("Buscá fallos y mirá sus números de línea.", "grep -n 'Failed password' evidencias/001/auth.log.txt"),
        ("Hacé que grep cuente las líneas que coinciden.", "grep -c 'Failed password' evidencias/001/auth.log.txt"),
        ("Localizá el acceso exitoso.", "grep -n 'Accepted password' evidencias/001/auth.log.txt"),
    ], "¿Cuántos fallos hubo y qué cuenta entró después? Escribí número y cuenta.", ["5 ops"],
     "Contá eventos, incluso cuando se repite una cuenta. Leé el nombre después de Accepted password for.",
     "Cinco fallos y un acceso a ops desde la misma IP justifican revisar esa sesión."),
    ("Investigá el correo", [
        ("Leé el correo como texto y compará remitente y ruta de respuesta.", "cat evidencias/002/mensaje.eml"),
        ("Revisá qué observó el gateway.", "cat evidencias/002/alerta.txt"),
        ("Contrastá esa fuente con el relato de Marina.", "cat evidencias/002/declaracion.txt"),
    ], "¿Qué acción acredita el gateway? Escribí cuarentena, clic o entrega de credenciales.", ["cuarentena"],
     "Buscá la línea Acción observada dentro de alerta.txt.",
     "Se registró la cuarentena. El clic y la entrega de credenciales siguen sin verificar. Consultá soluciones/002.md después de escribir tu ticket."),
    ("Reconstruí la sesión 42", [
        ("Leé el alcance del cambio aprobado.", "cat evidencias/003/contexto.md"),
        ("Ubicá el principio y el fin de la sesión.", "cat evidencias/003/autenticacion.log.txt"),
        ("Identificá la cuenta destino de sudo.", "cat evidencias/003/sudo.log.txt"),
        ("Seguí la cadena PID y PPID hasta id.", "cat evidencias/003/procesos.csv"),
        ("Compará las dos observaciones TCP.", "cat evidencias/003/conexiones.csv"),
    ], "¿Qué estado registra la conexión saliente al puerto 443?", ["syn_sent"],
     "Mirá la columna state de la última fila.",
     "SYN_SENT documenta el intento. Para saber cómo terminó, pedirías más registros de red. Compará tu investigación con soluciones/003.md."),
    ("Cambiá tu primer programa", [
        ("Mirá cómo Python recorre el registro línea por línea.", "cat contar.py"),
        ("Ejecutá el contador con su patrón inicial.", "python3 contar.py"),
        ("Pasale otro texto al mismo programa.", "python3 contar.py 'Accepted password'"),
    ], "¿Cuántas líneas contienen Accepted password?", ["1", "una"],
     "Compará el último número con la salida del grep del caso 001.",
     "Ahora abrí contar.py en un editor, cambiá el patrón inicial por session opened y volvé a ejecutarlo sin argumentos. Esperá una coincidencia."),
]


def practicar(mision):
    titulo, pasos, pregunta, respuestas, pista, cierre = mision
    print(f"\n{titulo}\nEscribí cada comando. Usá :menu para volver.")
    for objetivo, ejemplo in pasos:
        print(f"\n{objetivo}\n  {ejemplo}")
        esperado = shlex.split(ejemplo)
        while True:
            entrada = input("$ ").strip()
            if entrada == ":menu":
                return
            try:
                argumentos = shlex.split(entrada)
            except ValueError:
                print("Revisá si cerraste las comillas.")
                continue
            if argumentos == esperado:
                resultado = subprocess.run(esperado, cwd=BASE, check=False)
                if resultado.returncode:
                    print("Revisá la salida de la herramienta y volvé a intentarlo.")
                    continue
                break
            print("Compará los espacios, las mayúsculas y las comillas con el ejemplo.")
    while True:
        respuesta = " ".join(input(f"\n{pregunta}\n> ").lower().split())
        if respuesta == ":menu":
            return
        if respuesta in respuestas:
            print(f"Correcto. {cierre}")
            return True
        print(pista)


def main():
    print("KALI EN GUARDIA · Taller de K47SUM070\nDatos simulados. Elegí una práctica por número.")
    completas = set()
    while True:
        for i, (titulo, *_) in enumerate(MISIONES, 1):
            marca = " ✓" if i in completas else ""
            print(f"  {i}. {titulo}{marca}")
        opcion = input("Número de práctica (0 para salir): ").strip()
        if opcion == "0":
            break
        if opcion not in {str(i) for i in range(1, len(MISIONES) + 1)}:
            print("Elegí un número de la lista.")
            continue
        if practicar(MISIONES[int(opcion) - 1]):
            completas.add(int(opcion))
        print(f"\nPrácticas completadas en esta sesión: {len(completas)}/{len(MISIONES)}")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nFin de la práctica.")
