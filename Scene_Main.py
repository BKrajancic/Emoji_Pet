from Emoji import Emoji
from typing import List
import pygame
from pygame.locals import *
import sys
import math
from Hat import *


class Scene_Main():
    def __init__(self, fps: int, ticks_per_frame: float):
        pygame.init()

        self.w = 320
        self.h = 320
        self.windowSurface = pygame.display.set_mode(
            (self.w, self.h))

        self.characters: List[Entity] = []
        self.characters.append(Emoji(x=160, y=160))
        self.characters.append(Hat(x=50, y=50))

        self.ms_per_frame: int = math.floor(1000.0 / fps)
        ticks: int = math.floor(fps * ticks_per_frame)
        self.ms_per_ticks: int = math.floor(1000.0 / ticks)

    def loop(self):
        while True:
            pygame.time.Clock().tick(60)
            self.update()
            self.render()
            self.act_on_input()
            pygame.display.flip()

    def render(self):
        BLACK = (0, 0, 0)
        self.windowSurface.fill(BLACK)

        for emoji in self.characters:
            emoji.draw(self.windowSurface)

    def update(self):
        for emoji in self.characters:
            emoji.update(self.w, self.h)
            emoji.update_position(self.w, self.h)

    def act_on_input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
