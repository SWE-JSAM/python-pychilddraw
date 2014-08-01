#!/usr/bin/env python3
"""
# Authors: Joergen Samuelsson <samuelssonjorgen@gmail.com>
# PyChildDraw is a gamine clone (Small drawing program for children)
# see http://gnunux.info/projets/gamine/
# This is a total re-implementation but now in python.
# Most of the game assets are from gamine, see license
# The application is reimplemented by JSAM-SWE
#
# PyChildDraw is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyChildDraw is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyChildDraw. If not, see <http://www.gnu.org/licenses/gpl.html>.
"""
import sys
import os
import pygame
import itertools
import math
from pygame.locals import *
from random import (randint, choice)
from time import (gmtime, strftime)
__version__ = "0.5.2"


# if not pygame.font:
#     print('Warning, fonts disabled in pygame')

if not pygame.mixer:
    print('Warning, sound disable in pygame')

# Sounds that are played if any mouse bottom is pressed
Sounds = ['bleep.wav', 'bonus.wav', 'brick.wav', 'bubble.wav', 'crash.wav',
          'darken.wav', 'drip.wav', 'eat.wav', 'eraser1.wav', 'eraser2.wav',
          'flip.wav', 'gobble.wav', 'grow.wav', 'level.wav', 'line_end.wav',
          'paint1.wav', 'plick.ogg', 'prompt.wav', 'receive.wav', 'tri.ogg',
          'tuxok.wav', 'youcannot.wav']

shapes = ['rectangle', 'circle']
get_pen = itertools.cycle(['pencil2.png', 'pencil3.png'])
BackgroundColor = (255, 255, 255)
Rect = pygame.Rect(0, 0, 23, 23)
base_dir = os.path.dirname(os.path.abspath(__file__))


def loadImage(figfile):
    figfile_name = os.path.join(base_dir, 'data', 'img', figfile)
    try:
        image = pygame.image.load(figfile_name).convert_alpha()
    except pygame.error as message:
        print('Missing file ', figfile)
        print('error ', message)
        terminate()
    return image


def sound_path(soundfile):
    return os.path.join(base_dir, 'data', 'sounds', soundfile)


def get_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


def terminate():
    pygame.quit()
    sys.exit()


class Pen:
    def __init__(self):
        self.image = loadImage(next(get_pen))
        self.mouseCurserHeight = self.image.get_height()

    def change_pen(self):
        self.image = loadImage(next(get_pen))
        self.mouseCurserHeight = self.image.get_height()

    def draw(self, screen, pos):
        screen.blit(self.image, pos)


class BarnLine:
    def __init__(self, color):
        self.start = (0, 0)
        self.stop = (0, 0)
        self.color = color

    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.start, self.stop, 4)


class BarnSymbol:
    def __init__(self):
        self.color = get_color()
        self.symbol = choice(shapes)
        self.pos = (0, 0)

    def draw(self, screen):
        if self.symbol == "rectangle":
            Rect.center = self.pos
            pygame.draw.rect(screen, self.color, Rect)
        elif self.symbol == "circle":
            pygame.draw.circle(screen, self.color, self.pos, 14)


class ChildDraw:
    def __init__(self):
        # initiate mixer and pygame
        if pygame.mixer:
            pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()

        # set up screen by selecting the largest (sizes[0])
        sizes = pygame.display.list_modes()
        set_display = pygame.HWSURFACE | pygame.FULLSCREEN | pygame.DOUBLEBUF
        self.screen = pygame.display.set_mode(sizes[0], set_display)
        # set up game speed fps (frames per second)
        self.clock = pygame.time.Clock()
        self.fps = 40
        user_dir = os.path.expanduser('~')
        self.save_dir = os.path.join(user_dir, 'pychilddraw')
        self.line_len = 20
        self.line_color = get_color()
        self.sound_level = 0.5
        # Get a pen
        self.pen = Pen()
        pygame.mouse.set_visible(False)

        # background music
        if pygame.mixer:
            musicfile = 'BachJSBrandenburgConcertNo2.ogg'
            try:
                pygame.mixer.music.load(sound_path(musicfile))
            except pygame.error as message:
                print('Missing file ', musicfile)
                print('error ', message)
                terminate()

            pygame.mixer.music.play(-1)  # -1 to get infinite loop
            self.sound_level = pygame.mixer.music.get_volume()

        self.lines = []
        self.symbols = []
        self.first = True  # to remove artifact at first mouse move

        self.screen.fill(BackgroundColor)
        pygame.display.flip()

    def game_loop(self):
        # this is th updates in all
        while True:
            self.clock.tick(self.fps)
            self.game_events()
            self.draw()

    def game_events(self):
        # Handles users input
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                terminate()

            elif event.type == KEYDOWN:
                self.keydown(event.key)

            elif event.type == MOUSEBUTTONUP:
                self.mouseup(event.button, event.pos)

            elif event.type == MOUSEMOTION:
                self.mousemotion(event.buttons, event.pos, event.rel)

    def mouseup(self, button, pos):
        symbol = BarnSymbol()
        symbol.pos = pos
        self.symbols.append(symbol)

        if pygame.mixer:
            try:
                sound_file = sound_path(choice(Sounds))
                SoundToPlay = pygame.mixer.Sound(sound_file)
                SoundToPlay.set_volume(self.sound_level)
                SoundToPlay.play()
            except pygame.error as message:
                print("Can't find sound file ", sound_file.split("/")[-1])
                print("Error ", message)

    def mousemotion(self, buttons, pos, rel):
        # A ugly hack to remove the first strange line
        if self.first:
            rel = (0, 0)
            self.first = False
        # Set color change at minimum line length of 20 pixels
        if self.line_len < 20:
            self.line_len += math.sqrt(rel[0] ** 2 + rel[1] ** 2)
        else:
            self.color = get_color()
            self.line_len = 0

        line = BarnLine(self.color)
        line.start = (pos[0] - rel[0], pos[1] - rel[1])
        line.stop = pos
        self.lines.append(line)
        self.mouse = (pos[0], pos[1] - self.pen.mouseCurserHeight)

    def keydown(self, key):
        """
        Space (clear screen) remove all objects in self.{lines,symbols}
        s to take screen shoot
        arrow UP change pen
        """
        if key == K_SPACE:
            self.lines = []
            self.symbols = []

        elif key == K_s:
            savefigfileName = strftime("%Y-%m-%d-%H:%M:%S", gmtime()) + '.png'
            savefig_name_path = os.path.join(self.save_dir, savefigfileName)
            pygame.image.save(self.screen, savefig_name_path)
            # to get a flash as the file is saved
            self.screen.fill((0, 0, 0))
            pygame.display.flip()
            pygame.time.wait(100)
            pygame.event.clear()  # Clear event queue
            self.draw()

        elif key == K_UP:
            self.pen.change_pen()
            # to avoid jumping pen first frame
            pos = pygame.mouse.get_pos()
            self.mouse = (pos[0], pos[1] - self.pen.mouseCurserHeight)

        elif key == K_DOWN:
            self.pen.change_pen()
            # to avoid jumping pen first frame
            pos = pygame.mouse.get_pos()
            self.mouse = (pos[0], pos[1] - self.pen.mouseCurserHeight)

        elif key == K_RIGHT:
            # increase sound level
            if pygame.mixer:
                self.sound_level += 0.1
                if self.sound_level > 1:
                    self.sound_level = 1
                pygame.mixer.music.set_volume(self.sound_level)

        elif key == K_LEFT:
            # decrease sound level
            if pygame.mixer:
                self.sound_level -= 0.1
                if self.sound_level < 0:
                    self.sound_level = 0
                pygame.mixer.music.set_volume(self.sound_level)

        elif key == K_h:
            # print help screen
            help_image = loadImage('help_screen.png')
            self.screen.blit(help_image, (100, 100))
            pygame.display.flip()
            pygame.time.wait(3000)
            pygame.event.clear()  # Clear event queue

    def draw(self):
        self.screen.fill(BackgroundColor)

        for symbol in self.symbols:
            symbol.draw(self.screen)

        for lines in self.lines:
            lines.draw(self.screen)

        self.pen.draw(self.screen, self.mouse)
        pygame.display.flip()


def check_config():
    # check if save directory is present else make it
    user_dir = os.path.expanduser('~')
    save_dir = os.path.join(user_dir, 'pychilddraw')
    if not os.path.isdir(save_dir):
        os.mkdir(save_dir)


def main():
    check_config()
    game = ChildDraw()
    game.game_loop()

# Start the game
if __name__ == "__main__":
    main()
