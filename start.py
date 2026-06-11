#!/usr/bin/env python
# =========================================================================
# Steam FarmHour Linux
# Creado por: Diego Ledesma (TRN1)
# Perfil de Steam: https://steamcommunity.com/id/TRNONE/
# (Si te gusta, ¡puedes premiar mi perfil con puntos!)
# =========================================================================
import subprocess
import sys
import os
import time

# Colores para la interfaz
colorGreen = "\033[32m"
colorRed = "\033[31m"
colorCyan = "\033[36m"
colorYellow = "\033[33m"
colorReset = "\033[39m"

# Forzar el directorio actual del script
os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))

print(colorGreen + "=== STEAM FARMHOUR LINUX ===" + colorReset)
print(colorCyan + "Creado por TRN1 - https://steamcommunity.com/id/TRNONE/" + colorReset)
print(colorYellow + "Si te gusta la app, ¡puedes premiar mi perfil con puntos!" + colorReset)

# =========================================================================
# CONFIGURACIÓN: Poné acá adentro los AppID de los juegos que querés farmear.
# Podés poner tantos como quieras separados por comas (Steam permite unos 30 a la vez).
# Ejemplo: [AppID_Juego1, AppID_Juego2]
# =========================================================================
GAMES_TO_IDLE = [
    304930, #Unturned
    730, #cs2
    2507950,#Delta Force
    582660,#Black desert
    714010,#Aimlabs
    578080,#PUBG
    2073620, #arena brekaut infinite
    1517290, #battlefield 2042
    227300, #Euro truck
    270880, #American truck
    3240220, #Gta V
    2456740, #InZoi
    1363080, #Manor Lords
    275850, #No mans sky
    1091500, #Cyberpunk
    1144200, #ready or not
    1404210, #rdr
    3321460,#crimson desert

    # Reemplazá este número por el AppID real del juego que quieras (fijate en su URL de la tienda)
    # 570,    # Podés desmarcar y agregar más IDs (ej: Dota 2)
    # 730,    # Ej: CS2
]
# =========================================================================

if not GAMES_TO_IDLE:
    print(colorRed + "Error: No agregaste ningún AppID en la lista GAMES_TO_IDLE." + colorReset)
    sys.exit()

# Detectar la versión correcta de Python
pyLink = "python3"
try:
    subprocess.call(["python3", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except:
    pyLink = "python"

processes = []

print(f"\nIniciando el farmeo simultáneo de {colorGreen}{len(GAMES_TO_IDLE)}{colorReset} juegos...\n")

try:
    # Lanzamos TODOS los juegos en paralelo (al mismo tiempo)
    for appID in GAMES_TO_IDLE:
        print(colorCyan + f"[+] Lanzando emulación para AppID: {appID}..." + colorReset)

        # Ejecuta tu sub-script steam-idle.py pasándole el ID
        p = subprocess.Popen([pyLink, "steam-idle.py", str(appID)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        processes.append((appID, p))

    print(colorGreen + "\n¡Todos los juegos seleccionados están corriendo en segundo plano!" + colorReset)
    print(colorYellow + "Dejá esta ventana abierta. Presioná Ctrl + C para CERRAR todos los juegos de golpe.\n" + colorReset)

    # Bucle infinito eficiente para mantener el script sumando horas
    while True:
        time.sleep(3600)  # Duerme 1 hora
        print(f"[{time.strftime('%H:%M:%S')}] Sincronizando con Steam... Horas acumulándose correctamente.")

except KeyboardInterrupt:
    print(colorYellow + "\n\n[-] Deteniendo el farmeo... Cerrando procesos de forma segura." + colorReset)

    # Matamos todos los subprocesos de los juegos abiertos antes de salir
    for appID, p in processes:
        try:
            p.terminate()
            print(f" -> Emulación de AppID {appID} finalizada.")
        except:
            pass

    print(colorGreen + "¡Listo! Todos los juegos se cerraron limpiamente." + colorReset)
    sys.exit()
