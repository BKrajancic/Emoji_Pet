from pygame.locals import *
import pygame
from INTERACTION import *
from typing import List, Tuple
import time
import grovepi


class Interaction_Handler():
    def __init__(self):
        self.button_l = 1
        self.button_r = 2
        grovepi.pinMode(self.button_l, "INPUT")
        grovepi.pinMode(self.button_r, "INPUT")
        self.rac_max = 300
        self.grove_vcc = 5
        self.adc_ref = 5

        self.rac_1 = 3
        self.rac_1_prev = self.get_rotation(grovepi.analogRead(self.rac_1))
        grovepi.pinMode(self.rac_1, "INPUT")

        self.rac_2 = 4
        self.rac_2_prev = self.get_rotation(grovepi.analogRead(self.rac_2))
        grovepi.pinMode(self.rac_2, "INPUT")

    def get(self) -> List[Tuple[INTERACTION, int]]:
        events = pygame.event.get()
        interactions: List[Tuple[INTERACTION, int]] = []

        if grovepi.digitalRead(self.button_l) == 1:
            interactions.append((INTERACTION.BUTTON_L, 0))
        if grovepi.digitalRead(self.button_r) == 1:
            interactions.append((INTERACTION.BUTTON_R, 0))

        rac_1_rot = self.get_rotation(grovepi.analogRead(self.rac_1))
        if (rac_1_rot != self.rac_1_prev):
            p = (INTERACTION.ROLL, int(abs(self.rac_1_prev - rac_1_rot)))
            interactions.append(p)
        self.rac_1_prev = rac_1_rot

        rac_2_rot = self.get_rotation(grovepi.analogRead(self.rac_2))
        if (rac_2_rot != self.rac_2_prev):
            p = (INTERACTION.ROLL, int(abs(self.rac_2_prev - rac_2_rot)))
            interactions.append(p)
        self.rac_2_prev = rac_2_rot

        return interactions

    def get_rotation(self, rac_read):
        voltage = round((float)(rac_read) * self.adc_ref / 1023, 2)
        rac_deg = round((voltage * self.rac_max) / self.grove_vcc, 2)
        return rac_deg
