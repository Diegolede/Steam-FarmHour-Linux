# Steam FarmHour Linux

Este proyecto es un simulador / idler para Steam en Linux (probado en Arch Linux). Te permite sumar horas de juego ("farmear") en múltiples juegos de Steam simultáneamente, sin necesidad de tenerlos instalados ni abiertos consumiendo recursos.

## ¿Cómo funciona?

El proyecto utiliza la API oficial de Steam (`libsteam_api.so`) para indicarle al cliente de Steam que los juegos se están ejecutando. 
El script principal (`start.py`) funciona como un administrador que lanza y mantiene múltiples instancias del script secundario (`steam-idle.py`) en segundo plano, una por cada juego que deseas farmear.

> **Nota:** El archivo `steam-idle.py` es **estrictamente necesario**, ya que es el encargado de comunicarse directamente con la API de Steam y generar la ventana gráfica para cada juego. `start.py` es solo el lanzador múltiple.

> [!IMPORTANT]
> **Aclaración de Seguridad:** Esta aplicación **NO recopila, ni lee, ni almacena** ningún tipo de información personal, contraseñas o datos de tu cliente de Steam. Tu cuenta está completamente segura. El script funciona única y exclusivamente comunicándose con la API oficial para "simular" que el juego está abierto y así sumar las horas.

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

## Apoyo

Si este proyecto te ha servido y te gusta, ¡me ayudarías un montón regalándome unos puntos de Steam (Steam Points) en mi perfil!
**Mi perfil de Steam:** [TRN1](https://steamcommunity.com/id/TRNONE/)

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles. Creado por Diego Ledesma (TRN1).
