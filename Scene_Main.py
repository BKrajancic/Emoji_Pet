from Emoji import Emoji
from typing import List
import pygame
from pygame.locals import *
import sys
import math


class Scene_Main():
    def __init__(self, fps: int, ticks_per_frame: float):
        pygame.init()

        self.w = 600
        self.h = 600
        self.windowSurface = pygame.display.set_mode(
            (self.w, self.h))

        self.characters: List[Emoji] = []
        self.characters.append(Emoji())
        self.ms_per_frame: int = math.floor(1000.0 / fps)
        ticks: int = math.floor(fps * ticks_per_frame)
        self.ms_per_ticks: int = math.floor(1000.0 / ticks)

    def loop(self):
        while True:
            pygame.time.Clock().tick(60)
            self.update()
            self.render()
            self.act_on_input()
            pygame.display.update()

    def render(self):
        BLACK = (0, 0, 0)
        # self.windowSurface.fill(BLACK)

        for emoji in self.characters:
            emoji.draw(self.windowSurface)

    def update(self):
        for emoji in self.characters:
            emoji.update(self.w, self.h)

    def act_on_input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
