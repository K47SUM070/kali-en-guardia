# Kali en guardia
Taller de K47SUM070 para tu primera guardia en un centro de operaciones de seguridad (SOC). Vas a escribir comandos, investigar un correo y seguir una sesión SSH. Al final cambiás un programa de Python para que cuente eventos por vos.

## Empezá acá
Descomprimí el paquete. En Kali, abrí la carpeta `kali-en-guardia` en el gestor de archivos, hacé clic derecho sobre el fondo y elegí **Abrir terminal aquí**. Ejecutá:

```sh
python3 guardia.py
```

Elegí **1** y escribí la orden que aparece después de la consigna. El símbolo `$` indica dónde escribir. Pulsá Enter para ver qué devuelve la herramienta en tu máquina. Al final de cada práctica, respondé la pregunta. Si te equivocás, recibís una pista. Podés repetir cualquier misión. La marca de progreso dura mientras el programa está abierto. Escribí `:menu` durante una práctica para volver. En el menú, 0 termina el taller.

Necesitás Python 3 y las herramientas habituales de Kali (whoami, pwd, id, ls, grep y cat). Funciona sin conexión con una cuenta común. Los datos son simulados.

| Misión | Qué vas a producir |
|---|---|
| 1 · Terminal | Un parte con tu usuario, UID y carpeta de trabajo. |
| 2 · SSH | Un recuento de fallos y la cuenta que consiguió entrar. |
| 3 · Correo | Un ticket con los indicios, la acción del gateway y los datos faltantes. |
| 4 · Sesión 42 | Una cronología que une procesos, privilegios y conexiones. |
| 5 · Python | Un contador de eventos que podés adaptar cambiando una línea. |

## Probalo en la terminal de Kali
Abrí otra terminal en la misma carpeta. Acá podés variar las órdenes libremente.

1. Escribí `whoam`, pulsá **Tab** y luego **Enter**. Recuperá la orden con **↑**. **Ctrl+C** descarta la línea o interrumpe un programa en primer plano.
2. Ejecutá `id -u`. Si tu cuenta tiene permiso de sudo, anticipá qué devolverá `sudo id -u`, probalo y volvé a ejecutar `id -u`. El valor 0 identifica a root. Cuando sudo pide tu contraseña, la terminal oculta los caracteres.
3. Abrí `less evidencias/001/auth.log.txt`. Escribí `/Failed password`, pulsá Enter y usá **n** para la coincidencia siguiente. Con **q** volvés a la terminal.
4. Probá `grep 'Failed password' evidencias/001/auth.log.txt | wc -l`. La barra vertical lleva las líneas que seleccionó grep a wc, que las cuenta. Contrastá el resultado con la misión 2.
5. Antes de leer cada solución, guardá un ticket propio. En la carpeta del taller ejecutá `cp ticket-modelo.md mi-ticket-002.md` y abrilo con `nano mi-ticket-002.md`. Guardá con **Ctrl+O**, Enter, y salí con **Ctrl+X**. Para el caso SSH usá el número 003. Compará luego tu evidencia y decisión con la carpeta soluciones.
6. Para modificar tu primer programa, ejecutá `cp contar.py mi-contador.py` y `nano mi-contador.py`. Cambiá el texto inicial Failed password por Accepted password. Antes de ejecutar `python3 mi-contador.py`, anotá cuántos eventos esperás. El bucle for visita cada línea, if comprueba el texto y += 1 suma una coincidencia.

## Integración con soc-l1-lab
El ZIP se extrae en la raíz del repositorio y agrega la carpeta kali-en-guardia. Para que los visitantes la encuentren, agregá al README principal el enlace `[Empezá el taller de Kali](kali-en-guardia/README.md)`. El taller corre localmente. Las evidencias incluidas son transcripciones del material de consulta del proyecto. Los registros llevan la extensión .log.txt para facilitar su lectura y seguimiento en Git. Para calcular huellas de los originales, usá los archivos del repositorio.

[Repositorio y fuentes originales](https://github.com/K47SUM070/soc-l1-lab) · [Mesa de trabajo en el navegador](https://soc-l1-lab.vercel.app/mesa-de-trabajo/index.html)
