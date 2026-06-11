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
        p = subprocess.Popen([pyLink, "steam-idle.py", str(appID), "nogui"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        processes.append((appID, p))

    print(colorGreen + "\n¡Todos los juegos seleccionados están corriendo en segundo plano!" + colorReset)
    print(colorYellow + "Cerrá la ventana de carátulas o presioná Ctrl + C en esta terminal para DETENER todos los juegos.\n" + colorReset)

    import tkinter as tk
    from PIL import Image, ImageTk
    import io
    from urllib.request import urlopen

    gui = tk.Tk()
    gui.title("Steam FarmHour Linux - Farmeando")
    gui.configure(bg="#1e1e24")

    def on_closing():
        print(colorYellow + "\n\n[-] Deteniendo el farmeo (Ventana cerrada)..." + colorReset)
        for aID, proc in processes:
            try:
                proc.terminate()
                print(f" -> Emulación de AppID {aID} finalizada.")
            except:
                pass
        print(colorGreen + "¡Listo! Todos los juegos se cerraron limpiamente." + colorReset)
        gui.destroy()
        sys.exit()

    gui.protocol("WM_DELETE_WINDOW", on_closing)

    gui.geometry("950x500") # Tamaño inicial razonable

    import webbrowser
    def open_profile():
        webbrowser.open("https://steamcommunity.com/id/TRNONE/")

    # Frame para los botones en la parte inferior
    bottom_frame = tk.Frame(gui, bg="#1e1e24")
    bottom_frame.pack(side="bottom", fill="x", padx=15, pady=15)

    # Nota: Tkinter estándar no tiene "border-radius". 
    # Usamos un estilo 'flat' sin bordes para darle un look moderno similar a botones redondeados/planos.
    btn_profile = tk.Button(bottom_frame, text="⭐ Creator Steam Profile", font=("Arial", 12, "bold"), bg="#2a475e", fg="#66c0f4", activebackground="#171a21", activeforeground="white", command=open_profile, pady=10, cursor="hand2", relief="flat", bd=0)
    btn_profile.pack(side="left", fill="both", expand=True, padx=(0, 5))

    btn_stop = tk.Button(bottom_frame, text="🛑 STOP FARM", font=("Arial", 12, "bold"), bg="#d9534f", fg="white", activebackground="#c9302c", activeforeground="white", command=on_closing, pady=10, cursor="hand2", relief="flat", bd=0)
    btn_stop.pack(side="right", fill="both", expand=True, padx=(5, 0))

    # Frame para el contenedor de carátulas y su barra de desplazamiento (Scrollbar)
    container_frame = tk.Frame(gui, bg="#1e1e24")
    container_frame.pack(side="top", fill="both", expand=True, padx=15, pady=(15, 0))

    # Scrollbar vertical
    scrollbar = tk.Scrollbar(container_frame, bg="#1e1e24", troughcolor="#1e1e24")
    scrollbar.pack(side="right", fill="y")

    # Usamos un widget Text como contenedor para lograr un efecto "flexbox" responsivo
    container = tk.Text(container_frame, bg="#1e1e24", bd=0, highlightthickness=0, wrap="char", yscrollcommand=scrollbar.set)
    container.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=container.yview)

    images = []

    for appID in GAMES_TO_IDLE:
        try:
            url = f"http://cdn.akamai.steamstatic.com/steam/apps/{appID}/header_292x136.jpg"
            image_bytes = urlopen(url).read()
            data_stream = io.BytesIO(image_bytes)
            pil_image = Image.open(data_stream)
            # Mantenemos el tamaño original 292x136 para que no queden cortas
            tk_image = ImageTk.PhotoImage(pil_image)
            images.append(tk_image)

            lbl = tk.Label(container, image=tk_image, bg="#1e1e24", bd=0)
            container.window_create("end", window=lbl, padx=5, pady=5)
        except Exception:
            lbl = tk.Label(container, text=f"AppID {appID}\nSin Imagen", fg="white", bg="#333333", width=35, height=8)
            container.window_create("end", window=lbl, padx=5, pady=5)

    container.configure(state="disabled")

    gui.mainloop()

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
