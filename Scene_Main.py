from Emoji import Emoji
from typing import List
import pygame
from pygame.locals import *
import sys
import math
from Accessory import *
from INTERACTION import *
from Hand import *
from sys import platform
from multiprocessing import Process
from threading import Thread, Lock

if platform == "linux" or platform == "linux2":
    from Arduino_Interaction_Handler import *
elif platform == "darwin":
    from Interaction_Handler import *


class Scene_Main():
    def __init__(self):
        pygame.init()

        self.w = 320
        self.h = 320
        self.windowSurface = pygame.display.set_mode(
            (self.w, self.h))

        self.emoji = Emoji(x=160, y=160, scene_width=128, scene_height=128)
        self.items: List[Accessory] = [
            Accessory(x=50, y=50, w=128, h=128)
        ]
        self.hand = Hand()
        self.mut = Lock()

        if platform == "linux" or platform == "linux2":
            self.interaction_handler = Arduino_Interaction_Handler()
            proc = Process(target=self.input_loop)
            proc.start()
        else:
            self.interaction_handler = Interaction_Handler()

        self.actions: List[Tuple[INTERACTION, int]] = []

    def input_loop(self):
        while True:
            copied = self.interaction_handler.get()
            if len(copied) > 0:
                self.mut.acquire()
                self.actions = copied.copy()
                self.mut.release()

    def loop(self):
        counter = 30
        max_counter = 30
        while True:
            pygame.time.Clock().tick(60)
            if (counter == 0):
                counter = max_counter
                # if platform != "linux" and platform != "linux2":
            else:
                counter -= 1

            self.actions = self.interaction_handler.get()
            self.mut.acquire()
            if len(self.actions) > 0:
                self.input(self.actions)
                self.actions = []
            self.mut.release()

            self.update()
            self.render()

    def update(self):
        self.emoji.update(self.w, self.h)
        self.emoji.update_position(self.w, self.h)

        for item in self.items:
            item.update(self.w, self.h, self.emoji, self)
            item.update_position(self.w, self.h)

    def render(self):
        BLACK = (0, 0, 0)
        self.windowSurface.fill(BLACK)
        self.emoji.draw(self.windowSurface)

        for item in self.items:
            item.draw(self.windowSurface)

        self.items = [i for i in self.items if i.dead == False]

        pygame.display.flip()

    def yeet_accessory(self):
        # add accessory into frame
        # yeet it
        # change emoji mood to neutral
        if(self.emoji.mood != "happy"):
            flying_hat = Accessory(
                x=self.emoji.get_pos()[0],
                y=self.emoji.get_pos()[1] - self.emoji.h,
                w=128,
                h=128,
                mood=self.emoji.mood
            )
            flying_hat.yeet()
            flying_hat.is_constrained = False
            flying_hat.lifeTime = 100
            flying_hat.noCollide(50)
            self.items.append(flying_hat)
            self.emoji.mood = "happy"
            print("yeet")

    def input(self, actions):
        for interaction, arg in actions:
            if interaction is INTERACTION.BUTTON_L:
                self.items.append(
                    Accessory(x=10, y=50, w=128, h=128, mood=self.emoji.mood))
            elif interaction is INTERACTION.BUTTON_R:
                self.emoji.bounce()
            elif interaction is INTERACTION.ROLL:
                self.emoji.roll(arg)
            elif interaction is INTERACTION.BUTTON_LESS_THAN:
                self.emoji.mood = "cowboy"
            elif interaction is INTERACTION.BUTTON_GREATER_THAN:
                self.emoji.mood = "sunglasses"
            elif interaction is INTERACTION.YEET:
                self.yeet_accessory()
            elif interaction is INTERACTION.DISTANCE:
                self.hand.on_input(arg)
            elif interaction is INTERACTION.EXIT:
                pygame.quit()
                sys.exit()
            else:
                raise NotImplementedError()
