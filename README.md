Childdraw
=========
PyChildDraw is a gamine clone see http://gnunux.info/projets/gamine
This is a total re-implementation but now in python. Most of the game assets are from gamine that is under GPL license.

## Background
My doter  liked Gamine but I was not able to install it under my Linux distribution. To solve this I ported Gamine to Python 3 and Pygame.

## To run the program

Start the program by executing the file pychilddraw.py or install the program using

    $ sudo python setup.py install
Now you can start the program in the terminal by just typing

    $ pychilddraw

## Controls
* Draw lines by moving the mouse
* Add symbols by clicking on a mouse button
* Save you drawing by pressing the "s key"
* Clear the screen by pressing the "space key"
* Change pens by pressing the "up arrow key"
* To quit press the "Esc-key"

## Dependence

The program is implemented in Python 3 but should work in Python
2 as well. To run the program you need to install pygame
(http://www.pygame.org/news.html).

## Change log

###Release 0.5.1
* setup.py and MANIFEST.in is introduced, this resulted in major rearrangement of the package.
* Save to folder pychilddraw in home is introduced
* Renamed from barnkladd to pychilddraw