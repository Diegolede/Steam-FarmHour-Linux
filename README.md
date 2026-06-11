# Steam FarmHour Linux
🌎 [English](#english) | 🇪🇸 [Español](#español)

---

<a name="english"></a>
# 🌎 English

This project is a Steam simulator / idler for Linux (tested on Arch Linux). It allows you to idle ("farm") playtime hours in multiple Steam games simultaneously, without having them installed or open consuming system resources.

## How it works

The project uses the official Steam API (`libsteam_api.so`) to tell the Steam client that the games are running.
The main script (`start.py`) works as a manager that launches and keeps multiple instances of the secondary script (`steam-idle.py`) in the background, one for each game you want to farm.

> **Note:** The `steam-idle.py` file is **strictly necessary**, as it is responsible for communicating directly with the Steam API and generating the GUI window for each game. `start.py` is just the multiple launcher.

> [!IMPORTANT]
> **Security Notice:** This application **DOES NOT collect, read, or store** any personal information, passwords, or data from your Steam client. Your account is completely safe. The script works solely and exclusively by communicating with the official API to "simulate" that the game is open to farm hours.

> [!WARNING]
> **🌟 Support the Project:** This software is **100% free**! If it has been useful to you and you feel like supporting my work, any small gesture is more than welcome (whether it's some Steam Points on my profile, or even a game if you're feeling generous). It is truly appreciated from the bottom of my heart, but definitely not required!
> 👉 **[Visit TRN1's Steam profile](https://steamcommunity.com/id/TRNONE/)**

## Requirements

The script needs the following Python packages to work (particularly for the small GUI that displays the game image):

* requests
* beautifulsoup4
* pillow (with jpeg and tk support)
* tk (Tkinter)

**Installation example on Arch Linux (via pacman):**
```bash
sudo pacman -S python-beautifulsoup4 python-requests python-pillow tk
```

**Generic installation with pip (other distributions):**
```bash
pip install -r requirements.txt
# (Note: tkinter is usually installed separately from the system package manager, e.g.: sudo apt install python3-tk)
```

## Usage

1. Open the `start.py` file with your favorite text editor.
2. Find the `GAMES_TO_IDLE` list.
3. Modify the list by adding the **AppID** of the games you want to farm hours in. You can find a game's AppID in the URL of its Steam store page.
   * *Example:* For Counter-Strike 2, the AppID is `730`.
4. Save the changes.
5. Run the main script from the terminal:

```bash
python start.py
```
*(Or `python3 start.py` depending on your system).*

6. Leave the terminal open. When you want to stop farming, press `Ctrl + C` in the terminal and the script will close all instances safely.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. Created by Diego Ledesma (TRN1).

---

<a name="español"></a>
# 🇪🇸 Español

Este proyecto es un simulador / idler para Steam en Linux (probado en Arch Linux). Te permite sumar horas de juego ("farmear") en múltiples juegos de Steam simultáneamente, sin necesidad de tenerlos instalados ni abiertos consumiendo recursos.

## ¿Cómo funciona?

El proyecto utiliza la API oficial de Steam (`libsteam_api.so`) para indicarle al cliente de Steam que los juegos se están ejecutando. 
El script principal (`start.py`) funciona como un administrador que lanza y mantiene múltiples instancias del script secundario (`steam-idle.py`) en segundo plano, una por cada juego que deseas farmear.

> **Nota:** El archivo `steam-idle.py` es **estrictamente necesario**, ya que es el encargado de comunicarse directamente con la API de Steam y generar la ventana gráfica para cada juego. `start.py` es solo el lanzador múltiple.

> [!IMPORTANT]
> **Aclaración de Seguridad:** Esta aplicación **NO recopila, ni lee, ni almacena** ningún tipo de información personal, contraseñas o datos de tu cliente de Steam. Tu cuenta está completamente segura. El script funciona única y exclusivamente comunicándose con la API oficial para "simular" que el juego está abierto y así sumar las horas.

> [!WARNING]
> **🌟 Apoyo al Proyecto:** ¡Este software es **100% gratuito**! Si te ha sido de utilidad y nace de ti apoyar mi trabajo, cualquier pequeño detalle es más que bienvenido (ya sean unos puntitos de Steam en mi perfil, o hasta algún juego si te sientes generoso). ¡Se agradece de todo corazón, pero para nada es obligatorio!
> 👉 **[Visitar perfil de TRN1 en Steam](https://steamcommunity.com/id/TRNONE/)**

## Requisitos

El script necesita los siguientes paquetes de Python para funcionar (particularmente para la pequeña interfaz gráfica que muestra la imagen del juego):

* requests
* beautifulsoup4
* pillow (con soporte para jpeg y tk)
* tk (Tkinter)

**Ejemplo de instalación en Arch Linux (vía pacman):**  
```bash
sudo pacman -S python-beautifulsoup4 python-requests python-pillow tk
```

**Instalación genérica con pip (otras distribuciones):**
```bash
pip install -r requirements.txt
# (Nota: tkinter suele instalarse aparte desde el gestor de paquetes del sistema, ej: sudo apt install python3-tk)
```

## Uso

1. Abre el archivo `start.py` con tu editor de texto favorito.
2. Busca la lista `GAMES_TO_IDLE`.
3. Modifica la lista agregando los **AppID** de los juegos en los que quieres sumar horas. Puedes encontrar el AppID de un juego en la URL de su página en la tienda de Steam.
   * *Ejemplo:* Para Counter-Strike 2, el AppID es `730`.
4. Guarda los cambios.
5. Ejecuta el script principal desde la terminal:

```bash
python start.py
```
*(O `python3 start.py` dependiendo de tu sistema).*

6. Deja la terminal abierta. Cuando quieras dejar de farmear, presiona `Ctrl + C` en la terminal y el script cerrará todas las instancias de forma segura.

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles. Creado por Diego Ledesma (TRN1).
