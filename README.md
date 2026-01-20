Classic Donkey Kong Rebuild

Este es un videojuego retro desarrollado en Python utilizando la librería Pygame, inspirado en el clásico Donkey Kong de Nintendo NES.

El objetivo del juego es controlar al personaje, esquivar los barriles que lanza Donkey Kong y llegar hasta la princesa sin perder todas las vidas.

--------------------------------------------

Paradigma Utilizado

El videojuego fue desarrollado utilizando Programación Orientada a Objetos (POO), ya que este paradigma permite representar cada elemento del juego como un objeto independiente con sus propios atributos y comportamientos.

La clase Player controla el movimiento, salto, colisiones y animaciones del jugador.
La clase Barrel representa los barriles lanzados por Donkey Kong y su comportamiento.
La clase Hammer permite al jugador eliminar enemigos de forma temporal.
Las clases Bridge y Ladder representan la estructura del escenario.

--------------------------------------------

Controles del Juego

Flecha derecha: mover a la derecha
Flecha izquierda: mover a la izquierda
Flecha arriba: subir escaleras
Flecha abajo: bajar escaleras
Barra espaciadora: saltar

--------------------------------------------

Instrucciones de Instalación

1. Clona el repositorio desde GitHub:
git clone https://github.com/josealejandro-hub/Avance_donkey_kong.git

2. Instala la librería Pygame:
pip install pygame

3. Ejecuta el juego:
python main.py

--------------------------------------------

Explicación del Código

El proyecto está desarrollado principalmente en el archivo main.py.

Player controla el movimiento del personaje y las colisiones.
Barrel representa los barriles lanzados por Donkey Kong.
Hammer permite eliminar barriles por tiempo limitado.
Bridge y Ladder construyen las plataformas y escaleras.
La función reset reinicia el juego cuando se pierde una vida.
La función check_victory detecta la victoria.

--------------------------------------------

Estructura del Proyecto

assets/
images/

Aquí se encuentran todas las imágenes y recursos del juego.

--------------------------------------------

Autor

José Alejandro Calle Saltos
Desarrollo de Videojuego Retro con Python
Lenguaje: Python
Librería: Pygame
