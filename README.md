PyChilddraw
=========
PyChildDraw is a gamine clone see http://gnunux.info/projets/gamine
This is a total re-implementation but now in python. All the sound assets are from gamine that is under GPL license. The pencils are drawn by Lisa Boman

## Background
My daughter liked Gamine but I was not able to install it under my Linux distribution. To solve this I ported Gamine Python using Pygame.

## To run the program

Start the program by executing the file pychilddraw/pychilddraw.py or install the program using:

    $ sudo python setup.py install
Now you can start the program in the terminal by just typing

    $ pychilddraw

If you want to uninstall the package use pip if you got it installed:

    $ sudo pip uninstall pychilddraw
If you don't have pip installed the process is little more complicated, see e.g. [stackoverflow suggestion](http://stackoverflow.com/questions/1550226/python-setup-py-uninstall)

    

## Controls
* Draw lines by moving the mouse
* Add symbols by clicking on a mouse button
* Save you drawing by pressing the **s** key
* Clear the screen by pressing the **space** key
* Change pens by pressing the **up** or **down** arrow key or use the mouse wheel
* Increase or decrease the sound volume by pressing **Right** and **Left** arrow key, respectively.
* To quit press the **Esc** key
* Get help by pressing the **h** key

## Dependence

The program is implemented in **Python 3** but should work with Python 2 as well (have tested 2.7). To run the program you need to install **pygame**
(http://www.pygame.org/news.html).

## Change log
###Version 0.5.3
* New pencils with different colors.
* The line color is now dependent on the color of the pencil
* New control: You can now also use the mouse wheel to change the pencil.
* Some minor bugs solved.

###Version 0.5.2
* The line color change at a minimum of 20 pixels length
* Pressing **Down** arrow key also change the pen
* Add volume control using **right** and **left** arrow key
* Add help screen by pressing **h** key

###Version 0.5.1
* setup.py and MANIFEST.in is introduced, this resulted in major rearrangement of the package.
* Save to folder pychilddraw in home is introduced
* Renamed from barnkladd to pychilddraw
###Version 0.5.0
* Initial released version.